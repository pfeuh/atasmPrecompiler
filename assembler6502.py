#!/usr/bin/python
# -*- coding: utf-8 -*-

import sys
import os

from tables6502 import *

DEBUG = "-debug" in sys.argv
SILENT = "-silent" in sys.argv

if 1:
    VERSION = "0.99"
    COMMENT_TAG = ";"
    EMPTY_STR = ""
    KEYWORD_INCLUDE = ".include"
    CHAR_SPACE =' '
    CHAR_EOL = chr(0)
    CHAR_SINGLE_QUOTE = "'"
    CHAR_QUOTE = '"'
    CHAR_ANTISLASH = "\\"
    CHAR_UNDERSCORE = "_"
    CHAR_DOLLAR = '$'
    CHAR_TILD = '~'
    CHAR_LF = '\n'
    CHAR_EQUAL = '='
    CHAR_COMMA = ','
    
    DEFAULT_PC_VALUE = 0x200

    APP_NAME = os.path.splitext(os.path.basename(sys.argv[0]))[0]

    KEYWORD_STRING = ".string"
    KEYWORD_CH_ARRAY = ".ch_array"
    PRECOMP_KEYWORDS = (KEYWORD_STRING, KEYWORD_CH_ARRAY)
    KEYWORD_SOURCE_START = "source_start"
    KEYWORD_MAIN = "main"
    KEYWORD_IRQ = "irq"
    KEYWORD_NMI = "nmi"
    KEYWORD_SOURCE_END = "source_end"
    REQUIRED_LABELS = (KEYWORD_SOURCE_START, KEYWORD_MAIN, KEYWORD_IRQ, KEYWORD_NMI,KEYWORD_SOURCE_END)

    SIZEOF_BYTE = 1
    SIZEOF_WORD = 2

    FIRST_CHAR = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz_"
    OTHER_CHAR = FIRST_CHAR + "0123456789"
    NO_LABEL_FIRST_CHAR = " ;"

    TYPE_VOID = 0
    TYPE_VARIABLE = 1
    TYPE_DIRECTIVE = 2
    TYPE_OPCODE = 3
    TYPE_KEYWORD = 4
    TYPE_PONCTUATION = 5
    TYPE_STRING = 6
    TYPE_CONSTANT = 7
    WORD_TYPES = (None, TYPE_VOID, TYPE_VARIABLE, TYPE_DIRECTIVE, TYPE_OPCODE, TYPE_KEYWORD, TYPE_PONCTUATION, TYPE_STRING, TYPE_CONSTANT)
    TYPE_NAME = {None:"None", TYPE_VOID:'void', TYPE_VARIABLE:'variable', TYPE_DIRECTIVE:'directive', TYPE_OPCODE:'opcode', TYPE_KEYWORD:'keyword', TYPE_PONCTUATION:'ponct',TYPE_STRING:'string', TYPE_CONSTANT:"const"}

    PONCTUATION = ('(', ')', ',', '#', '+', '-', '/', '*', CHAR_EQUAL, '<', '>', '&', '!', '|', '^')
    
    CMD_BYTE = '.byte'
    CMD_WORD = '.word'
    CMD_DBYTE = '.dbyte'
    CMD_STRING = '.string'
    CMD_CH_ARRAY = '.ch_array'
    CMD_DBS = '.dbs'
    CMD_DWS = '.dws'
    CMD_ORG = '*'
    DIRECTIVES = (CMD_BYTE, CMD_WORD, CMD_DBYTE, CMD_STRING, CMD_CH_ARRAY, CMD_DBS, CMD_DWS, CMD_ORG)

    REGISTERS = ('x', 'y', 'X', 'Y', 'a', 'A')
    KEYWORDS = DIRECTIVES + PONCTUATION + REGISTERS

def write(text, fp=sys.stdout):
    if fp != None:
        fp.write(str(text))
    
def writeln(text, fp=sys.stdout):
    write(text, fp)
    write("\n", fp)

def printLink(message=EMPTY_STR, line=None):
    if not SILENT:
        if line != None:
            writeln('File "%s", line %d, %s'%(line.getFname(), line.getNum(), message))
            writeln(line.getText())
    
def printWarning(message, line=None):
    if not SILENT:
        if line != None:
            writeln('File "%s", line %d, warning : %s'%(line.getFname(), line.getNum(), message))
            writeln(line.getText())
        else:
            writeln('Warning : %s'%(message))
    
def printError(message, line=None):
    if DEBUG:
        # the goal is to trig an error, then, it's possible to follow the white rabbit
        1/0
    else:
        if not SILENT:
            if line != None:
                writeln('File "%s", line %d, error : %s'%(line.getFname(), line.getNum(), message))
                writeln(line.getText())
            else:
                writeln('Error : %s'%(message))

def buildName(old_name, new_name):
    fname = os.path.splitext(os.path.basename(old_name))[0]
    return "%s.%s"%(fname, new_name)
    
def getFileLines(fp):
    return [line.rstrip() for line in fp.readlines()]
    
def labelIsOk(label):
    if not len(label):
        return False
    if not label[0] in FIRST_CHAR:
        return False
    if label == CHAR_UNDERSCORE:
        return False
    for car in label[1:]:
        if not car in OTHER_CHAR:
            return False
    if label.lower() in OPCODES or label in PONCTUATION or label in KEYWORDS:
        return False
    if label.lower() in ('x', 'y'): # 6502 registers, appear in some instructions
        return False
    return True

def removeComment(text, line=None):
    otext = EMPTY_STR
    mode_normal = 1
    mode_string = 2
    mode = mode_normal
    current_quote = None
    
    for position, car in enumerate(text):
        if mode == mode_normal:
            if car == COMMENT_TAG:
                return otext.rstrip()
            #~ elif (car == CHAR_SINGLE_QUOTE) or (car == CHAR_QUOTE):
            elif car == CHAR_QUOTE:
                otext += car
                current_quote = car
                mode = mode_string
            else:
                otext += car
        elif mode == mode_string:
            otext += car
            if car == current_quote:
                if text[position -1] != CHAR_ANTISLASH:
                    mode = mode_normal
                    current_quote = None
                    
    # whole line is parsed, last check:
    if mode != mode_normal:
        printError("string not closed!", line)
    return otext.rstrip()
    
def extractLabelsFromLine(text, line=None):
    mode_normal = 1
    mode_string = 2
    mode = mode_normal
    current_quote = None
    words = []
    
    word = EMPTY_STR
    
    if not len(text):
        return []
    
    if text[0] == CHAR_SPACE:
        words.append(EMPTY_STR)
        
    for position, car in enumerate(text):
        if mode == mode_normal:
            if car == COMMENT_TAG:
                if len(word):
                    words.append(word)
                    break
            elif car == CHAR_SPACE:
                    if len(word):
                        words.append(word)
                        word = EMPTY_STR
            #~ elif (car == CHAR_SINGLE_QUOTE) or (car == CHAR_QUOTE):
            elif car == CHAR_QUOTE:
                word += car
                current_quote = car
                mode = mode_string
            elif car in PONCTUATION:
                if len(word):
                    words.append(word)
                words.append(car)
                word = EMPTY_STR
            else:
                word += car
        elif mode == mode_string:
            word += car
            if car == current_quote:
                if text[position -1] != CHAR_ANTISLASH:
                    mode = mode_normal
                    current_quote = None
    if word != EMPTY_STR:
                    words.append(word)
                    
    # whole line is parsed, last check:
    if mode != mode_normal:
        printError("string not closed!", line)
    return words
    
def commentLine(text, line):
    otext = EMPTY_STR
    if text.startswith(COMMENT_TAG):
        # no labelo, no problemo!
        return text
    elif text.startswith(CHAR_SPACE):
        # no labelo, no problemo!
        return "%s%s"%(COMMENT_TAG, text)
    else:
        # there is a label :(
        space_found = False
        for car in text:
            if not space_found:
                if car == CHAR_SPACE:
                    otext += " %s "%COMMENT_TAG
                    space_found = True
                else:
                    otext += car
            else:
                otext += car
    return otext

def getOpcodeValue(mnemo, mode, line, strict=True):
    for value, item in enumerate(OPCODE_VALUES):
        if item == mnemo:
            if MODES[value] == mode:
                return value
    # no opcode with this mode
    if strict:
        printError("illegal mnemonic %s %s"%(mnemo, mode), line)
    else:
        return None

def isString(label):
    if label.startswith(CHAR_QUOTE) and label.endswith(CHAR_QUOTE):
        return True
    else:
        return False

def placebo():
    pass

def diskSave(fname=None, hook=placebo, mode = "wb"):
    if fname:
        with open(fname, mode) as fp:
            if hook:
                fp.write(hook)

def getInstructionSize(opcode):
    return CODE_SIZES[opcode]

def xx__formatData(items, datatype, word, pc, info):
    ret_lst = []
    
    if datatype in (CMD_DBS, CMD_DWS):
        if type(items) == int:
            items = [0] * items
        else:
            printError("%s command accepts only 1 parameter"%datatype, info)
    if datatype in ('<', '>'):
        if type(items) == int:
            items = (items,)
        else:
            printError("%s command accepts only 1 parameter"%datatype, info)
    else:
        if type(items) == int:
            items = (items,)
        elif type(items) == str:
            items = [ord(car) for car in items]
        
    if datatype in ('<', '>'):
        if datatype == '>':
            ret_lst = (items[0] & 0xff,)
        else:
            ret_lst = (items[0] / 0x100,)
    else:
        for item in items:
            if datatype == CMD_BYTE:
                if item & 0xff != item:
                    printError("byte $%02x out of range"%item, info)
                ret_lst.append(item)
            elif datatype in (CMD_WORD, CMD_DBYTE):
                if item & 0xffff != item:
                    printError("word $%02x out of range"%item, info)
                if datatype == CMD_WORD:
                    ret_lst.append(item & 255)
                    ret_lst.append(item / 256)
                else:
                    ret_lst.append(item / 256)
                    ret_lst.append(item & 255)
            elif datatype in (CMD_STRING, CMD_CH_ARRAY):
                ret_lst.append(item)
            elif datatype == CMD_DBS:
                ret_lst.append(0)
            
    if datatype == CMD_STRING:
        ret_lst.append(0) # eol (end of line)

    result = tuple(ret_lst)
    word.set(result)
    if pc.isOK():
        pc.add(len(result))
    return result

def countItems(words, item, line):
    count = 0
    for word in words:
        if word.getLabel() == item:
            count += 1
    return count
    
class PROGRAM_COUNTER():
    def __init__(self, value=DEFAULT_PC_VALUE):
        self.__PC = value

    def get(self):
        return self.__PC
        
    def add(self, size):
        self.__PC += size
        
    def kill(self):
        self.__PC = None
        
    def isOK(self):
        return self.__PC != None

class WORD():
    def __init__(self, label, wtype=None, value=None):
        assert type(label) == str
        self.__text = label
        self.__wtype = wtype
        self.__value = value

    def isSolved(self):
        if self.__wtype in (TYPE_VARIABLE, TYPE_OPCODE):
            return self.__value != None
        elif self.__wtype in (TYPE_VOID,):
            return True
        return False

    def isByte(self):
        if self.__wtype in (TYPE_VARIABLE):
            return self.__value <= 0xff

    def getLabel(self):
        return self.__text

    def getType(self):
        return self.__wtype

    def setType(self, wtype):
        if self.__wtype == None:
            self.__wtype = wtype
        else:
            raise Exception("type %s already set (%s) for word %s"%(TYPE_VARIABLE[wtype], TYPE_NAME[self.__wtype], self.getLabel()))

    def get(self):
        return self.__value

    def set(self, value):
        self.__value = value

    def isVariable(self):
        return self.__wtype == TYPE_VARIABLE

    def isOpcode(self):
        if self.__wtype == TYPE_OPCODE:
            return True
        return False

    def isKeyWord(self):
        if self.__wtype == TYPE_KEYWORD:
            return True
        return False

    def isPonctuation(self):
        if self.__wtype == TYPE_PONCTUATION:
            return True
        return False

    def isVoid(self):
        if self.__wtype == TYPE_VOID:
            return True
        return False

    def __str__(self):
        if self.getType() == TYPE_VOID:
            otext = "  --------"
        else:
            otext  = "%s "%{False:".", True:"X", None:" "}[self.isSolved()]
            otext += "(%s) "%TYPE_NAME[self.getType()]
            otext += "%s "%self.getLabel()
        return otext + CHAR_LF

    def debugStr(self):
        if self.__wtype == TYPE_VOID:
            return "-------- "
        wtype = TYPE_NAME[self.__wtype]
        value = self.__value
        
        if value == None:
            value = "None"
        elif type(value) == int:
            value = "0x%04x"%value
        else:
            value = str(value)
        return "(%s)%s=%s"%(wtype, self.__text, value)

class SOURCE_LINE():
    def __init__(self, fname, text, num):
        self.__num = num
        self.__text = text
        self.__fname = os.path.basename(fname)

    def getFname(self):
        return self.__fname

    def getText(self):
        return self.__text

    def setText(self, text):
        self.__text = text

    def getNum(self):
        return self.__num
        
    def __str__(self):
        return "%-40s %s\n"%("%s#%d"%(self.__fname, self.__num), self.__text)

class ASM_LINE():
    def __init__(self, text, line):
        self.__line = line
        self.__text = text
        self.__solved = False
        self.__bytes = []
        self.__address = None
        self.__words = []

    def hasLabel(self):
        if len(self.__words):
            return self.__words[0].getType() == TYPE_VARIABLE
        else:
            return False

    def isMnemonicLine(self):
        if len(self.__words) >= 2:
            return self.__words[1].getType() == TYPE_OPCODE
        else:
            return False
    
    def isDirectiveLine(self):
        if len(self.__words) >= 2:
            return self.__words[1].getType() == TYPE_DIRECTIVE
        else:
            return False
    
    def isAffectationLine(self):
        if len(self.__words) >= 4:
            return self.__words[2].getLabel() == CHAR_EQUAL
        else:
            return False
    
    def setAddress(self, prog_count):
        self.__address= prog_count

    def getAddress(self):
        return self.__address

    def addWord(self, word):
        if word in (None, str):
            printLink("", self.getLine())
            raise Exception("attempt to add a bad word '%s'!"%str(word))
            
        self.__words.append(word)
    
    def getWord(self, label):
        if label in self.__words.keys():
            return self.__words[label]
    
    def getWords(self):
        return self.__words

    def setWords(self, words):
        self.__words = words

    def getText(self):
        return self.__text

    def appendByte(self, byte):
        self.__bytes.append(byte)
    
    def getBytes(self):
        return self.__bytes
    
    def setBytes(self, bytes):
        self.__bytes = bytes
    
    def getLine(self):
        return self.__line

    def isSolved(self):
        for word in self.__words:
            if not word.isSolved():
                return False
        # all words are checked, finaly line is solved
        return True
            
    def setSolved(self):
        self.__solved = True
            
    def clrSolved(self):
        self.__solved = False
            
    def getCode(self):
        otext = "%06d "%self.getLine().getNum()
        for word_num, word in enumerate(self.__words):
            label = word.getLabel()
            if word_num:
                otext += "%s "%label
            else:
                if word.getType() == TYPE_VOID:
                    otext += "   "
                else:
                    otext += label
        return otext + CHAR_LF

    def __str__(self):
        line = self.getLine()
        solved_text = "."
        if self.isSolved():
            solved_text = "X"
        otext = '%s %06d %s\n'%(solved_text, line.getNum(), line.getText())
        for word in self.__words:
            otext += "%s"%str(word)
        otext += "-" * 20
        for word in self.__words:
            otext += " %s:%s"%(word.getLabel(), word.isSolved())
        
        
        
        
        return otext + CHAR_LF

class ASSEMBLER():
    const_num = 0
    
    def __init__(self, params, solver_fp=None):
        # arguments stuff
        self.__params = params
        self.__fname = self.getArgument('-ifname')
        self.__nb_cols = self.__params.get('-nb_cols')
        self.__org = self.getArgument('-org')
        if not os.path.isfile(self.__fname):
            printError("file \"%s\" not found"%self.__fname, SOURCE_LINE(self.__fname, CHAR_SPACE.join(sys.argv), 0))

        # assembler stuff
        self.__source_lines = []
        self.__asm_lines = []
        self.__words = {}
        self.setSolveExpressionFp(solver_fp)

        # let's go!
        self.createAsmLines(self.__fname)
    
    def getNewConstantName(self):
        ASSEMBLER.const_num += 1
        return "const_%04x"%ASSEMBLER.const_num
        
    def getSourceLines(self):
        return self.__source_lines
        
    def getAsmLines(self):
        return self.__asm_lines
        
    def getAsmLine(self, line_num):
        if line_num < len(self.__asm_lines):
            return self.__asm_lines[line_num]
        
    def debugStr(self):
        otext = EMPTY_STR
        otext += self.getStatText() + CHAR_SPACE
        return otext

    def getWord(self, label, strict=False):
        if label in self.__words.keys():
            return self.__words[label]
        if strict:
            raise Exception("global word '%s' not found!"%label)
            
    def getWords(self):
        return self.__words
        
    def decodeValue(self, chars, info):
        if chars.startswith(CHAR_DOLLAR):
            # vintage assemblers use $ instead of 0x for hex values
            chars = "0x" + chars[1:]
        elif chars.startswith(CHAR_TILD):
            # vintage assemblers use ~ to prefix a binary value
            chars = "0b" + chars[1:]
        elif chars.startswith(CHAR_SINGLE_QUOTE):
            # vintage assemblers use ' to prefix a single character
            if len(chars) != 2:
                printError("syntax on word '%s'"%chars, info)
            else:
                chars = "0x%04x"%ord(chars[1])
        elif chars[0] in "0123456789-":
            # nothing to adjust
            pass
        else:
            # it is not a value
            return None
    
        # let's test numerical values
        success = False
        try:
            return eval(chars)
            success = True
        except:
            return None
        
    def addWord(self, word, strict=False):
        # each variable has to be global,
        # so if it's solved somewhere, it's solved evereywhere
        if word.getType() == TYPE_VARIABLE:
            label = word.getLabel()
            wtype = word.getType()
            value = word.get()
            if label in self.__words.keys():
                global_word = self.__words[label]
                if value != None:
                    global_word.set(value)
            else:
                self.__words[label] = word
            return self.__words[label]
        else:
            if strict:
                raise Exception("type mismatch! attempting to add word '%s' with type %s!"%(word.getLabel(), TYPE_NAME[word.getType()]))
            else:
                return None

    def getArgument(self, pname):
        #getting an argument from commandline
        if pname in self.__params.keys():
            return self.__params.get(pname)
        else:
            printError("mandatory parameter '%s' missing"%pname)
    
    def createAsmLines(self, fname):
        # let's slice the line in a list of words
        with open(fname, "r") as fp:
            lines = getFileLines(fp)
        # building minimal source file (empty lines and comments are removed)
        for num, text in enumerate(lines):
            line = SOURCE_LINE(fname, text, num + 1)
            self.__source_lines.append(line)
            text = removeComment(text, line)
            if len(text):
                asm_line = ASM_LINE(text, line)
                self.__asm_lines.append(asm_line)
            else:
                # line is empty, no need to store it
                continue
            self.splitLine(asm_line)

    def splitLine(self, line):

            # line is created, let's add its words
            labels = [label for label in extractLabelsFromLine(line.getText(), line)]
            info = line.getLine()
            
            for position, label in enumerate(labels):
                if not position:
                    if label.endswith(":"):
                        label = label[:-1]

                word = self.InitializeWord(label, position, info)
                if label in self.__words.keys():
                    # let's check a little list...
                    global_word = self.__words[label]
                    if word.getType() != global_word.getType():
                        raise Exception("datatype mismatch!\nnew word:%s\nold_word:%s"%(str(word), str(global_word)))
                    if global_word.isSolved():
                        word = global_word
                    else:
                        if word.isSolved():
                            self.__words[label] = word
                        else:
                            word = global_word
                else:
                    if word.getType() == TYPE_VARIABLE:
                        self.__words[label] = word
                line.addWord(word)

            if line.getWords()[-1].getLabel() == CHAR_COMMA:
                del line.getWords()[-1]

            if len(line.getWords()) >= 3:
                if line.getWords()[2].getLabel() == CHAR_COMMA:
                    printError("unexpected comma", info)
                
    def assemble(self):
        # this is only one pass, all may not be solved with it
        pc = PROGRAM_COUNTER(self.__org)

        for line in self.__asm_lines:
            if not line.isSolved():
                self.parseLine(line, pc)

    def parseLine(self, line, pc):
        line.setAddress, pc.get()
        info = line.getLine()
        
        if line.hasLabel():
            self.computeLabel(line, pc)
        
        if line.isMnemonicLine():
            self.computeOpcode(line, pc)
        elif line.isDirectiveLine():
            self.computeDirective(line, pc)
        elif line.isAffectationLine():
            self.computeAffectation(line, pc)
        else:
            if not line.hasLabel():
                printError("syntax error", info)
        
    def computeLabel(self, line, pc):
        words = line.getWords()
        word = words[0]
        old_value = word.get()
        new_value = line.getAddress()
        if old_value != None:
            if new_value != None:
                word.set(new_value)
            else:
                printError("program counter mismatch! already set at $%04X attempt to write $%04X"%(old_value, new_value), line.getLine())
        else:
            return
            
    def computeOpcode(self, line, pc):
        words = line.getWords()
        nb_words = len(words)
        info = line.getLine()
        
        word = words[1]
        if word.isSolved():
            return
            
        mnemonic = word.getLabel().lower()
        
        if nb_words >= 3 and mnemonic in RELATIVE_OPCODES:
            self.computeRelative(line, pc)
        elif nb_words == 2 and mnemonic in IMPLIED_OPCODES:
            self.computeImplied(line, pc)
        elif nb_words == 3 and words[2].getLabel().lower() == "a":
            self.computeAccumulator(line, pc)
        elif nb_words >= 4 and words[2].getLabel() == "#":
            self.computeImmediate(line, pc)
        elif nb_words >= 7 and words[-1].getLabel() == ")" and words[-2].getLabel().lower() == "x" and words[-3].getLabel() == "," and words[2].getLabel() == "(":
            self.computeIndirectx(line, pc)
        elif nb_words >= 7 and words[-1].getLabel().lower() == "y" and words[-2].getLabel() == "," and words[-3].getLabel() == ")" and words[2].getLabel() == "(":
            self.computeIndirecty(line, pc)
        elif nb_words >= 5 and words[-1].getLabel() == ")" and words[2].getLabel() == "(":
            self.computeIndirect(line, pc)
        elif nb_words >= 5 and words[-1].getLabel().lower() == "x" and words[-2].getLabel() == ",":
            self.computeAbsolutex(line, pc)
        elif nb_words >= 5 and words[-1].getLabel().lower() == "y" and words[-2].getLabel() == ",":
            self.computeAbsolutey(line, pc)
        elif nb_words >= 3:
            self.computeAbsolute(line, pc)
        else:
            printError('illegal addressing mode', info)

    def computeRelative(self, line, pc):
        words = line.getWords()
        info = line.getLine()
        
        mnenonic = words[1].getLabel().lower()
        mode = RELATIVE
        opcode = getOpcodeValue(mnenonic, mode, info, strict=True)
        if opcode != None:
            line_size = getInstructionSize(opcode)
            value = self.solveExpression(words[2:], info)
            if value != None and pc.isOK():
                # all prerequisites are good, let's solve
                move = value - (pc.get() + 2) 
                if move < -128 or move > 127:
                    printError("relative value out of range pc=$%04x target=$%04X move:$%04X"%(pc.get(), value, move), info)
                else:
                    move = move & 0xff
                    words[1].set(opcode)
                    words[2] = WORD(self.getNewConstantName(), TYPE_CONSTANT, move)
                    line.setBytes((opcode, move))
                    while len(words) > 3:
                        del words[-1]
        # event if it's not solved, let's compute pc for the next lines
        else:
            line_size = 0
        line.setAddress(pc.get())
        pc.add(line_size)

    def computeImplied(self, line, pc):
        words = line.getWords()
        info = line.getLine()
        
        mnenonic = words[1].getLabel().lower()
        mode = IMPLIED
        opcode = getOpcodeValue(mnenonic, mode, info, strict=True)
        if opcode != None:
            line_size = getInstructionSize(opcode)
            # all prerequisites are good, let's solve
            words[1].set(opcode)
            line.setBytes((opcode,))
        # event if it's not solved, let's compute pc for the next lines
        else:
            line_size = 0
        line.setAddress(pc.get())
        pc.add(line_size)

    def computeAccumulator(self, line, pc):
        words = line.getWords()
        info = line.getLine()
        
        mnenonic = words[1].getLabel().lower()
        mode = ACCUMULATOR
        opcode = getOpcodeValue(mnenonic, mode, info, strict=True)
        if opcode != None:
            line_size = getInstructionSize(opcode)
            # all prerequisites are good, let's solve
            words[1].set(opcode)
            del words[2]
            line.setBytes((opcode,))
        # event if it's not solved, let's compute pc for the next lines
        else:
            line_size = 0
        line.setAddress(pc.get())
        pc.add(line_size)

    def computeImmediate(self, line, pc):
        words = line.getWords()
        info = line.getLine()
        
        mnenonic = words[1].getLabel().lower()
        mode = IMMEDIATE
        opcode = getOpcodeValue(mnenonic, mode, info, strict=True)
        if opcode != None:
            line_size = getInstructionSize(opcode)
            value = self.solveExpression(words[3:], info)
            if value != None and pc.isOK():
                # all prerequisites are good, let's solve
                if value < 0 or value > 255:
                    printError("immediate value $%04x out of range"%(value), info)
                else:
                    words[1].set(opcode)
                    words[2] = WORD(self.getNewConstantName(), TYPE_CONSTANT, value)
                    line.setBytes((opcode, value))
                    while len(words) > 3:
                        del words[-1]
        # event if it's not solved, let's compute pc for the next lines
        else:
            line_size = 0
        line.setAddress(pc.get())
        pc.add(line_size)

    def computeIndirectx(self, line, pc):
        words = line.getWords()
        info = line.getLine()
        
        mnenonic = words[1].getLabel().lower()
        mode = INDIRECTX
        opcode = getOpcodeValue(mnenonic, mode, info, strict=True)
        if opcode != None:
            line_size = getInstructionSize(opcode)
            value = self.solveExpression(words[3:-3], info)
            if value != None and pc.isOK():
                # all prerequisites are good, let's solve
                if value < 0 or value > 255:
                    printError("zero page value $%04x out of range"%(value), info)
                else:
                    words[1].set(opcode)
                    words[2] = WORD(self.getNewConstantName(), TYPE_CONSTANT, value)
                    line.setBytes((opcode, value))
                    while len(words) > 3:
                        del words[-1]
        # event if it's not solved, let's compute pc for the next lines
        else:
            line_size = 0
        line.setAddress(pc.get())
        pc.add(line_size)

    def computeIndirecty(self, line, pc):
        words = line.getWords()
        info = line.getLine()
        
        mnenonic = words[1].getLabel().lower()
        mode = INDIRECTY
        opcode = getOpcodeValue(mnenonic, mode, info, strict=True)
        if opcode != None:
            line_size = getInstructionSize(opcode)
            value = self.solveExpression(words[3:-3], info)
            if value != None and pc.isOK():
                # all prerequisites are good, let's solve
                if value < 0 or value > 255:
                    printError("zero page value $%04x out of range"%(value), info)
                else:
                    words[1].set(opcode)
                    words[2] = WORD(self.getNewConstantName(), TYPE_CONSTANT, value)
                    line.setBytes((opcode, value))
                    while len(words) > 3:
                        del words[-1]
        # event if it's not solved, let's compute pc for the next lines
        else:
            line_size = 0
        line.setAddress(pc.get())
        pc.add(line_size)

    def computeIndirect(self, line, pc):
        words = line.getWords()
        info = line.getLine()
        
        mnenonic = words[1].getLabel().lower()
        mode = INDIRECT
        opcode = getOpcodeValue(mnenonic, mode, info, strict=True)
        if opcode != None:
            line_size = getInstructionSize(opcode)
            value = self.solveExpression(words[3:-1], info)
            if value != None and pc.isOK():
                # all prerequisites are good, let's solve
                if value < 0 or value > 65535:
                    printError("absolute value $%04x out of range"%(value), info)
                else:
                    words[1].set(opcode)
                    words[2] = WORD(self.getNewConstantName(), TYPE_CONSTANT, value)
                    line.setBytes((opcode, value & 255, value / 256))
                    while len(words) > 3:
                        del words[-1]
        # event if it's not solved, let's compute pc for the next lines
        else:
            line_size = 0
        line.setAddress(pc.get())
        pc.add(line_size)

    def computeAbsolute(self, line, pc):
        words = line.getWords()
        info = line.getLine()
        
        mnenonic = words[1].getLabel().lower()
        mode = ABSOLUTE
        opcode = getOpcodeValue(mnenonic, mode, info, strict=True)
        if opcode != None:
            line_size = getInstructionSize(opcode)
            value = self.solveExpression(words[2:], info)
            if value != None and pc.isOK():
                # all prerequisites are good, let's solve
                if value < 0 or value > 65535:
                    printError("absolute value $%04x out of range"%(value), info)
                else:
                    words[1].set(opcode)
                    words[2] = WORD(self.getNewConstantName(), TYPE_CONSTANT, value)
                    line.setBytes((opcode, value & 255, value / 256))
                    while len(words) > 3:
                        del words[-1]
        # event if it's not solved, let's compute pc for the next lines
        else:
            line_size = 0
        line.setAddress(pc.get())
        pc.add(line_size)

    def computeAbsolutex(self, line, pc):
        words = line.getWords()
        info = line.getLine()
        
        mnenonic = words[1].getLabel().lower()
        mode = ABSOLUTEX
        opcode = getOpcodeValue(mnenonic, mode, info, strict=True)
        if opcode != None:
            line_size = getInstructionSize(opcode)
            value = self.solveExpression(words[2:-2], info)
            if value != None and pc.isOK():
                # all prerequisites are good, let's solve
                if value < 0 or value > 65535:
                    printError("absolute value $%04x out of range"%(value), info)
                else:
                    words[1].set(opcode)
                    words[2] = WORD(self.getNewConstantName(), TYPE_CONSTANT, value)
                    line.setBytes((opcode, value & 255, value / 256))
                    while len(words) > 3:
                        del words[-1]
        # event if it's not solved, let's compute pc for the next lines
        else:
            line_size = 0
        line.setAddress(pc.get())
        pc.add(line_size)

    def computeAbsolutey(self, line, pc):
        words = line.getWords()
        info = line.getLine()
        
        mnenonic = words[1].getLabel().lower()
        mode = ABSOLUTEY
        opcode = getOpcodeValue(mnenonic, mode, info, strict=True)
        if opcode != None:
            line_size = getInstructionSize(opcode)
            value = self.solveExpression(words[2:-2], info)
            if value != None and pc.isOK():
                # all prerequisites are good, let's solve
                if value < 0 or value > 65535:
                    printError("absolute value $%04x out of range"%(value), info)
                else:
                    words[1].set(opcode)
                    words[2] = WORD(self.getNewConstantName(), TYPE_CONSTANT, value)
                    line.setBytes((opcode, value & 255, value / 256))
                    while len(words) > 3:
                        del words[-1]
        # event if it's not solved, let's compute pc for the next lines
        else:
            line_size = 0
        line.setAddress(pc.get())
        pc.add(line_size)

    def computeAffectation(self, line, pc):
        words = line.getWords()
        info = line.getLine()
        
        value = self.solveExpression(words[3:], info)
        if value != None:
            words[1].set(value)
            while len(words) > 2:
                del words[-1]

    def xx__computeWordSplitter(self, line, pc):
        # '<' means use most significant byte
        # '>' means use least significant byte
        info = line.getLine()
        words = line.getWords()
        nb_words = len(words)
        for index, word in enumerate(words):
            label = word.getLabel()
            if label in ('<', '>'):
                if index == nb_words - 1:
                    printError("no value after '%s'"%label, info)
                else:
                    result = self.solveExpression([words[index+1]], info)
                    if result != None:
                        result = formatData(result, label, word, pc, info)
                        writeln("-> %s"%str(result), fp=self.__solver_fp)
                        line.setWords(words[index+1:] + words[:index+2])
                    else:
                        writeln("-> None", fp=self.__solver_fp)
                    writeln("-"*40, fp=self.__solver_fp)
        
    def InitializeWord(self, label, word_num, info):
        word = WORD(label)
        test_value = False

        if word_num == 0:
            # first word of a line can only be a label
            
            if labelIsOk(label):
                return self.addWord(WORD(label, TYPE_VARIABLE))
            else:
                if label != EMPTY_STR:
                    printError("Unexpected word '%s'"%label, info)
                else:
                    word.setType(TYPE_VOID)
                    word.set("---")

        elif word_num == 1:
            # 2nd word of a line can be a mnemonic, a variable or a command
            if labelIsOk(label):
                return self.addWord(WORD(label, TYPE_VARIABLE))
            elif label.lower() in OPCODES:
                # insensitive case allowed
                return WORD(label, TYPE_OPCODE)
            elif label in DIRECTIVES:
                return WORD(label, TYPE_DIRECTIVE)
            else:
                printError("Unexpected word '%s'"%label, info)
                
        elif word_num >= 2:
            # from 3rd position, words can be everything except opcode or command
            if labelIsOk(word.getLabel()):
                return self.addWord(WORD(label, TYPE_VARIABLE))
            elif label in PONCTUATION:
                return WORD(label, TYPE_PONCTUATION)
            elif label in REGISTERS:
                return WORD(label, REGISTERS)
            elif self.decodeValue(label, info) != None:
                return self.addWord(WORD(label, TYPE_VARIABLE, self.decodeValue(label, info)))
            elif isString(label):
                return WORD(label, TYPE_STRING, label)

        return word

    def computeAffectations(self, line):
        # solve some affectations
        words = line.getWords()
        if len(words) >= 4:
            if words[2].getLabel() == CHAR_EQUAL:
                if words[3].isVariable():
                    if words[3].isSolved():
                        words[1].set(words[3].get())
                        del words[-1]
                        del words[-1]

    def computeDirective(self, line, pc):
        words = line.getWords()
        nb_words = len(words)
        info = line.getLine()
        
        word = words[1]
        if word.isSolved():
            return
            
        label = word.getLabel()
        
        if label == CMD_BYTE:
            self.computeByte(line, pc)
        elif label == CMD_WORD:
            self.computeWord(line, pc)
        elif label == CMD_DBYTE:
            self.computeDbyte(line, pc)
        elif label == CMD_STRING:
            self.computeString(line, pc)
        elif label == CMD_CH_ARRAY:
            self.computeChArray(line, pc)
        elif label == CMD_DBS:
            self.computeDbs(line, pc)
        elif label == CMD_DWS:
            self.computeDws(line, pc)
        elif label == CMD_ORG:
            self.computeOrg(line, pc)
        return
        
    def computeByte(self, line, pc):
        words = line.getWords()
        info = line.getLine()
        
        bytes = self.solveExpression(words[2:], info)
        if bytes != None and pc.isOK():
            # all prerequisites are good, let's solve
            if type(bytes) == int:
                bytes = (bytes,)
            for index, byte in enumerate(bytes):
                if byte < 0 or byte > 255:
                    printError("byte #%d value $%04x out of range"%(index+1, byte), info)
            else:
                words[2] = WORD(self.getNewConstantName(), TYPE_CONSTANT, bytes)
                line.setBytes(bytes)
                nb_items = len(bytes)
                while len(words) > 3:
                    del words[-1]
        # event if it's not solved, let's compute pc for the next lines
        else:
            nb_items = countItems(words[2:], CHAR_COMMA, line) + 1
        line.setAddress(pc.get())
        pc.add(nb_items * SIZEOF_BYTE)

    def computeWord(self, line, pc):
        words = line.getWords()
        info = line.getLine()
        
        integers = self.solveExpression(words[2:], info)
        if integers != None and pc.isOK():
            # all prerequisites are good, let's solve
            if type(integers) == int:
                integers = (integers,)
            for index, integer in enumerate(integers):
                if integer < 0 or integer > 65535:
                    printError("word #%d value $%04x out of range"%(index+1, integer), info)
            else:
                bytes = []
                for integer in integers:
                    bytes.append(integer & 255)
                    bytes.append(integer / 256)
                words[2] = WORD(self.getNewConstantName(), TYPE_CONSTANT, bytes)
                line.setBytes(tuple(bytes))
                nb_items = len(integers)
                while len(words) > 3:
                    del words[-1]
        # event if it's not solved, let's compute pc for the next lines
        else:
            nb_items = countItems(words[2:], CHAR_COMMA, line) + 1
        line.setAddress(pc.get())
        pc.add(nb_items * SIZEOF_WORD)

    def computeDbyte(self, line, pc):
        words = line.getWords()
        info = line.getLine()
        
        integers = self.solveExpression(words[2:], info)
        if integers != None and pc.isOK():
            # all prerequisites are good, let's solve
            if type(integers) == int:
                integers = (integers,)
            for index, integer in enumerate(integers):
                if integer < 0 or integer > 65535:
                    printError("word #%d value $%04x out of range"%(index+1, integer), info)
            else:
                bytes = []
                for integer in integers:
                    bytes.append(integer / 256)
                    bytes.append(integer & 255)
                words[2] = WORD(self.getNewConstantName(), TYPE_CONSTANT, bytes)
                line.setBytes(tuple(bytes))
                nb_items = len(integers)
                while len(words) > 3:
                    del words[-1]
        # event if it's not solved, let's compute pc for the next lines
        else:
            nb_items = countItems(words[2:], CHAR_COMMA, line) + 1
        line.setAddress(pc.get())
        pc.add(nb_items * SIZEOF_WORD)

    def computeString(self, line, pc):
        words = line.getWords()
        info = line.getLine()
        
        bytes = self.solveString(words[2], info)
        
        if bytes != None and pc.isOK():
            # all prerequisites are good, let's solve
            bytes = list(bytes)
            bytes.append(0)
            bytes = tuple(bytes)
            if len(bytes):
                for byte in bytes[:-1]:
                    printWarning('unexpected zero byte in string', info)
            words[2] = WORD(self.getNewConstantName(), TYPE_CONSTANT, bytes)
            line.setBytes(tuple(bytes))
            nb_items = len(bytes)
            while len(words) > 3:
                del words[-1]
        # event if it's not solved, let's compute pc for the next lines
        else:
            nb_items = countItems(words[2:], CHAR_COMMA, line) + 1
        line.setAddress(pc.get())
        pc.add(nb_items * SIZEOF_BYTE)

    def computeChArray(self, line, pc):
        words = line.getWords()
        info = line.getLine()
        
        bytes = self.solveString(words[2], info)
        
        if bytes != None and pc.isOK():
            # all prerequisites are good, let's solve
            words[2] = WORD(self.getNewConstantName(), TYPE_CONSTANT, bytes)
            line.setBytes(tuple(bytes))
            nb_items = len(bytes)
            while len(words) > 3:
                del words[-1]
        # event if it's not solved, let's compute pc for the next lines
        else:
            nb_items = countItems(words[2:], CHAR_COMMA, line) + 1
        line.setAddress(pc.get())
        pc.add(nb_items * SIZEOF_BYTE)

    def computeDbs(self, line, pc):
        words = line.getWords()
        info = line.getLine()
        
        nb_bytes = self.solveExpression(words[2:], info)
        if nb_bytes != None and pc.isOK():
            # all prerequisites are good, let's solve
            if type(nb_bytes) != int:
                printError("syntax error"%(), info)
                nb_bytes = 0
            elif nb_bytes < 1 or nb_bytes > 65535:
                printError("value $%04x out of range"%nb_bytes, info)
                nb_bytes = 0
            else:
                bytes = [0] * nb_bytes
                bytes = tuple(bytes)
                words[2] = WORD(self.getNewConstantName(), TYPE_CONSTANT, bytes)
                line.setBytes(tuple(bytes))
                while len(words) > 3:
                    del words[-1]
        # event if it's not solved, let's compute pc for the next lines
        else:
            nb_bytes = 0
        line.setAddress(pc.get())
        pc.add(nb_bytes * SIZEOF_BYTE)

    def computeDws(self, line, pc):
        words = line.getWords()
        info = line.getLine()
        
        nb_words = self.solveExpression(words[2:], info)
        if nb_words != None and pc.isOK():
            # all prerequisites are good, let's solve
            if type(nb_words) != int:
                printError("syntax error"%(), info)
                nb_words = 0
            elif nb_words < 1 or nb_words > 32767:
                printError("value $%04x out of range"%nb_words, info)
                nb_words = 0
            else:
                bytes = [0] * nb_words * SIZEOF_WORD
                bytes = tuple(bytes)
                words[2] = WORD(self.getNewConstantName(), TYPE_CONSTANT, bytes)
                line.setBytes(tuple(bytes))
                while len(words) > 3:
                    del words[-1]
        # event if it's not solved, let's compute pc for the next lines
        else:
            nb_words = 0
        line.setAddress(pc.get())
        pc.add(nb_words * SIZEOF_WORD)

    def computeOrg(self, line, pc):
        pass

    def solveExpression(self, words, info, log=False):
        labels = []
        for word in words:
            if word.isSolved():
                labels.append(str(word.get()))
            else:
                labels.append(str(word.getLabel()))
        if log:
            write("%05d %s >>> "%(info.getNum(), info.getText()))
        expression = CHAR_SPACE.join(labels)
        if log:
            write("%s >>> "%expression)

        try:
            result = eval(expression)
        except:
            result = None
        
        if log:
            writeln(result)
        return result

    def solveString(self, word, info):
        try:
            text = eval(word.get())
            if type(text) == int:
                printWarning("syntax error (perhaps an unexpected value instead of a string)", info)
                return (text & 0xff, )
            elif type(text) != str:
                printError("syntax error (perhaps an unexpected non-ascii byte)", info)
                return None
            else:
                return tuple([ord(car) for car in text])
        except:
            printError("syntax error", info)
            return None

    def setSolveExpressionFp(self, fp):
        self.__solver_fp = fp
        
    def getCodeText(self):
        otext = EMPTY_STR
        for line in self.__asm_lines:
            otext += line.getCode()# + CHAR_LF
        return otext

    def getStatText(self):
        items = 0
        solved = 0
        lines = self.__asm_lines

        for line in lines:
                items += 1
                if line.isSolved():
                    solved += 1
        if items == 0:
            return "nothing solved!"
        else:
            percent = (float(solved) / float(items)) * 100.0
            return "%6.2f%% assembled (%d/%d)"%(percent, solved, items)

    def getLabelsText(self):
        otext = EMPTY_STR
        labels = []
        keys = self.__words.keys()
        keys.sort()
        for key in keys:
            item = self.__words[key]
            if item.isVariable():
                otext += "%-20 %s"%(key, str(item.get())) + CHAR_LF
        return otext

    #~ def desass(self):
        #~ pc = PROGRAM_COUNTER(self.__org)

        #~ for line in self.__asm_lines:
            #~ label = ""
            #~ pointer = "????"
            #~ word1 = "???"
            
            #~ words = line.__words()
            #~ nb_words = len(words)
            #~ if nb_words:
                #~ if words[0].getType() == TYPE_VARIABLE:
                    #~ label = words[0]. getLabel()
                    #~ if word[0].isSolved():
                        #~ pointer = pc.get()
            #~ if nb_words >= 2:
                #~ if words[1].getType() == TYPE_OPCODE:
                    #~ if words[2].getType() == TYPE_VARIABLE:
                        #~ if words[2].isSolved() == TYPE_VARIABLE:
                            #~ instruction = desass(words[1].getValue(), words[2].getValue()
                            #~ writeln(instruction)
        
    def getLineReport(self, line_num):
        lines = self.getAsmLines()
        if line_num < len(lines):
            line = lines[line_num]
            words = []
            bytes = " ".join(["%02X"%byte for byte in line.getBytes()])
            for word in line.getWords():
                if not word.isSolved():
                    words.append(word.getLabel())
                else:
                    value = word.get()
                    if value == None:
                        words.append('None')
                    elif type(value) == int:
                        words.append("%04X"%value)
                    elif type(value) == tuple:
                        words.append(" ".join(("%02X"%byte for byte in value)))
                    elif value == "---":
                        words.append("    ")
                    else:
                        raise Exception("unknown type %s"%value)
            pc = line.getAddress()
            if pc == None:
                pc = "----"
            else:
                pc = "%04X"%pc
                
            return "#%05d %-30s #%05d %-30s %-30s %s %s\n"%(line_num+1, line.getText(), line.getLine().getNum(), line.getLine().getText(), " ".join(words), pc, bytes)

    def getReport(self):
        otext = EMPTY_STR
        for line_num in range(len(self.__asm_lines)):
            otext += self.getLineReport(line_num)
        return otext

    def __str__(self):
        otext = EMPTY_STR
        for asm_line in self.__asm_lines:
            otext += str(asm_line)
        return otext

class ARGUMENT():
    def __init__(self, aname, atype=bool, check_minus=False, check_file=False, family=None):
        self.__aname = aname
        if not atype in (int, bool, str):
            raise Exception("not implemented argument type %s !"%type(atype))
        self.__atype = atype
        self.__avalue = False
        self.__check_minus = check_minus != False
        self.__check_file = check_file != False
        self.__labelType = {int:"int", bool:"bool", str:"str", }
        if family != None:
            for member in family:
                count = 0
                for member2 in family:
                    if member == member2:
                        count += 1
                if count != 1:
                    raise Exception("member '%s' already declared in family '%s' !"%(member, str(family)))
            if not aname in family:
                raise Exception("argument '%s' not declared in family '%s' !"%(aname, str(family)))
            self.__family = family
        else:
            self.__family = []

    def getFamily(self):
        return self.__family

    def reset(self):
        self.__avalue = False

    def __str__(self):
        otext = "%-4s %-20s %-20s"%(self.__labelType[self.__atype], self.__aname, self.__avalue)
        if self.__check_minus:
            otext += " checkMinus"
        if self.__check_file:
            otext += " checkFile"
        return otext + "\n"

    def mustTestFile(self):
        return self.__check_file
        
    def mustTestMinus(self):
        return self.__check_minus
        
    def getName(self):
        return self.__aname
        
    def set(self, value):
        if self.__atype == bool and type(value) == int:
            self.__avalue = value != False
        elif type(value) != self.__atype:
            raise Exception("bad type %s for setting argument '%s' : type %s required"%(type(value), self.__aname, self.__atype))
        else:
            self.__avalue = value

    def get(self):
        return self.__avalue
        
    def getType(self):
        return self.__atype

class ARGUMENTS():
    def __init__(self, warning_all=False, offset=1):
        self.__args = {}
        self.__rejected = []
        self.__processed = []
        self.__warning_all = warning_all
        self.__offset = offset
        self.__index = None
        self.__words_to_parse = None
    
    def __str__(self):
        otext = ""
        keys = self.__args.keys()
        keys.sort()
        for key in keys:
            otext += str(self.__args[key])
        return otext

    def raiseError(self, message):
        printError(message)

    def addArgument(self, argument):
        if not argument.getName() in self.__args.keys():
            self.__args[argument.getName()] = argument
        else:
            raise Exception("argument '%s' already processed!"%argument.getName())

    def getArgument(self, aname, strict=False):
        if aname in self.__args.keys():
            return self.__args[aname]
        if strict:
            raise Exception("argument '%s' not found!"%aname)

    def getNextArgument(self, aname):
        if self.__index < (len(self.__words_to_parse) - 1):
            word = self.__words_to_parse[self.__index + 1]
            self.__index += 1
            return word            
        else:
            self.raiseError("bad or missing argument for %s !"%aname)
        
    def parse(self, words_to_parse):
        self.reset()
        self.__words_to_parse = words_to_parse        
        self.__index = self.__offset # let's skip the first argument(s) (program name, ...)
        self.__rejected = []
        self.__processed = []

        if len(self.__words_to_parse) > self.__index:
            while 1:
                aname = self.__words_to_parse[self.__index]
                
                arg = self.getArgument(aname)
                if arg == None:
                    self.__rejected.append(aname)
                else:

                    # checking if already processed
                    if aname in self.__processed:
                        raise Exception("argument '%s' already processed!\n"%aname)
                        
                    family = arg.getFamily()
                    for member in family:
                        if member in self.__processed:
                            raise Exception("argument '%s' & '%s' processed together!\n"%(aname, member))
                        
                    atype = arg.getType()

                    if atype == str:
                        value_word = self.getNextArgument(aname)
                        if value_word.startswith('"'):
                            value = eval(value_word)
                            arg.set(value)
                        else:
                            value = value_word
                            arg.set(value)
                        if arg.mustTestFile():
                            # don't want to include os.path just for isfile() method
                            try:
                                with open(value) as fp:
                                    pass
                            except:
                                self.raiseError("file \"%s\" not found!"%value) 
                        if arg.mustTestMinus():
                            if arg.get().startswith('-'):
                                self.raiseError("in %s:'-' forbidden as first parameter's character!"%value) 
                    elif atype == int:
                        value_word = self.getNextArgument(aname)
                        if value_word.startswith('-'):
                            self.raiseError("in %s:'-' forbidden as first parameter's character!"%value) 
                        value = eval(value_word)
                        arg.set(value)
                    else:
                        arg.set(True)
                    self.__processed.append(aname)
    
                self.__index += 1
                if self.__index >= len(self.__words_to_parse):
                    break
        else:
            # nothing to parse
            return
        
        # if an args name starts with '-W', it has to be set
        # only if '-Wall' is set and 'warning_all' is set
        if self.__warning_all:
            if not "-Wall" in self.__args.keys():
                self.raiseError("no argument '-Wall' declared but 'warning_all' is True!" )
            elif self.getArgument("-Wall").get():
                # do something only if -Wall is active (True)
                for warning in self.__args.values():
                    if warning.getName().startswith("-W"):
                        warning.set(True)

    def getRejected(self):
        return self.__rejected
        
    def getProcessed(self):
        return self.__processed
        
    def getArgsDictionary(self):
        kwds = {}
        for key in self.__args.keys():
            kwds[key] = self.getArgument(key).get()
        return kwds

    def getArgNames(self):
        return self.__args.keys()

    def reset(self):
        for aname in self.__args.keys():
            self.getArgument(aname, strict=True).reset()
            
    def set(self, aname, value):
        arg = self.getArgument(aname, strict=True)
        if not len(arg.getFamily()):
            arg.set(value)
        else:
            self.raiseError("internal error")
        
    def get(self, aname):
        arg = self.getArgument(aname, strict=True)
        return arg.get()

if __name__ == "__main__":
    
    #####################################
    #                                   #
    # COMMAND LINE PARAMETERS COMPUTING #
    #                                   #
    #####################################

    ap = ARGUMENTS(warning_all=True)
    ap.addArgument(ARGUMENT('-verbose')) # blablabla...
    ap.addArgument(ARGUMENT('-debug'))   # useful for programer only
    ap.addArgument(ARGUMENT('-Wall'))    # set all warnings
    ap.addArgument(ARGUMENT('-Winc'))    # include already done
    ap.addArgument(ARGUMENT('-Wstr'))    # \x00 in a string
    ap.addArgument(ARGUMENT('-Wlbl'))    # a label is missing
    ap.addArgument(ARGUMENT('-ifname', str, check_minus=True, check_file=True))  # input file to assemble
    ap.addArgument(ARGUMENT('-ofname', str, check_minus=True))  # output file name (all files merged)
    ap.addArgument(ARGUMENT('-dfname', str, check_minus=True))  # debug (verbose listing) filename
    ap.addArgument(ARGUMENT('-lfname', str, check_minus=True))  # labels list filename
    ap.addArgument(ARGUMENT('-nb_cols', int))  # number of columns of the bytes generator
    media = ('-ram', '-rom', '-cartridge', )
    ap.addArgument(ARGUMENT('-ram', family=media))  # type of output file RAM
    ap.addArgument(ARGUMENT('-rom', family=media))  # type of output file ROM, means add vectors in fffa-ffff
    ap.addArgument(ARGUMENT('-cartridge', family=media))  # type of output file, means just under OS's ROM
    ap.addArgument(ARGUMENT('-org', int, check_minus=True))  # start address of code segment
    
    ap.parse(sys.argv)

    if ap.get('-org') == False:
        ap.set('-org', 0x200)
    if ap.get('-nb_cols') == False:
        ap.set('-nb_cols', 16)
    if ap.get('-ifname') == False:
        printError("'-ifname' is mandatory")

    ##################
    #                #
    # ASSEMBLER PART #
    #                #
    ##################

    # let's parse source file and clean it
    #~ source = ASSEMBLER(ap.getArgsDictionary(), solver_fp=open(buildName(ap.get('-ifname'), "solver.asm"), "w") )
    
    #~ source = ASSEMBLER(ap.getArgsDictionary())
    #~ source.assemble()
    #~ diskSave(buildName(ap.get('-ifname'), "debug.asm"), source.debugStr())

    #~ diskSave(buildName(ap.get('-ifname'), "asm_lines.asm"), source.getCodeText())
    #~ diskSave(buildName(ap.get('-ifname'), "asm_words.asm"), str(source))
    #~ diskSave(buildName(ap.get('-ifname'), "labels.asm"), source.getLabelsText())
