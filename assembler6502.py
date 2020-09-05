#!/usr/bin/python
# -*- coding: utf-8 -*-

import sys
import os

from tables6502 import *

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
    DIGITS = "123456789"
    
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

    VAR_NUM = 0
    
    ARG_VERBOSE = '-verbose'
    ARG_DEBUG = '-debug'
    ARG_WALL = '-Wall'
    ARG_WEQU = '-Wequ'
    ARG_WLBL = '-Wlbl'
    ARG_WSTR = '-Wstr'
    ARG_IFNAME = '-ifname'
    ARG_OFNAME = '-ofname'
    ARG_DFNAME = '-dfname'
    ARG_LFNAME = '-lfname'
    ARG_NB_COLS = '-nb_cols'
    ARG_NB_CART = '-cartridge'
    ARG_NB_RAM = '-ram'
    ARG_NB_ROM = '-rom'
    ARG_ORG = '-org'

def write(text, fp=sys.stdout):
    if fp != None:
        fp.write(str(text))
    
def writeln(text, fp=sys.stdout):
    write(text, fp)
    write("\n", fp)

def printLink(message=EMPTY_STR, line=None):
    if not "-debug" in sys.argv:
        if line != None:
            writeln('File "%s", line %d, %s'%(line.getFname(), line.getNum(), message))
            writeln(line.getText())
    
def printWarning(message, line=None):
    if not "-silent" in sys.argv:
        if line != None:
            writeln('File "%s", line %d, warning : %s'%(line.getFname(), line.getNum(), message))
            writeln(line.getText())
        else:
            writeln('Warning : %s'%(message))
    
def printError(message, line=None):
    if "-debug" in sys.argv:
        # the goal is to trig an error, then, it's possible to follow the white rabbit
        1/0
    else:
        if not "-silent" in sys.argv:
            if line != None:
                writeln('File "%s", line %d, error : %s'%(line.getFname(), line.getNum(), message))
                writeln(line.getText())
            else:
                writeln('Error : %s'%(message))

def getLabel(line, lower=True):
    text = removeComment(line.getText())
    if text != None:
        if len(text):
            if text[0] not in NO_LABEL_FIRST_CHAR:
                word = text.split()[0]
                if lower:
                    word = word.lower()
                if not labelIsOk(word):
                    printError("label \"%s\" incorrect"%word, line)
                return word
    return None

def extractWord(text, word_number, lower=True):
    if text.startswith(CHAR_SPACE):
        text = ".%s"%text
        if not word_number:
            return None
    text = removeComment(text)
    words = text.split()
    if word_number < len(words):
        word = words[word_number]
        if lower:
            word = word.lower()
        return word

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
    if label.lower() in ('x', 'y', 'a'): # 6502 registers, appear in some instructions
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
            # elif (car == CHAR_SINGLE_QUOTE) or (car == CHAR_QUOTE):
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
    
    line_num = EMPTY_STR
    for index, car in enumerate(text):
        if car in DIGITS:
            line_num += car
        elif car == CHAR_SPACE:
            if len(line_num):
                text = text[index+1:]
                break
            else:
                break
        else:
            if len(line_num):
                printError("bad syntax", line.getLine())
            else:
                break

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
    
def commentLine(text):
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

def countItems(words, item, line):
    count = 0
    
    if words[-1].getLabel() == CHAR_COMMA:
        for word in words[:-1]:
            if word.getLabel() == item:
                count += 1
    else:
        for word in words:
            if word.getLabel() == item:
                count += 1
    return count
    
def getModesByMnemonic(mnemonic):
    if mnemonic in MODES_BY_MNEMONIC.keys():
        return MODES_BY_MNEMONIC[mnemonic]
    else:
        return None

def isByte(value):
    if value != None:
        if value >= 0 and value < 256:
            return True
    return None
    
def isWord(value):
    if value != None:
        if value >= 0 and value < 65536:
            return True
    return None

def isRelative(value):
    return value >= -128 and value <= 127

def asmLinePrologue(line, mode, words, log=False):
    info = line.getLine()
    
    mnenonic = line.getWords()[1].getLabel().lower()
    opcode = getOpcodeValue(mnenonic, mode, info, strict=True)
    
    value = solveExpression(words, info, log=log)
    if opcode != None:
        size = getInstructionSize(opcode)
    else:
        size = 0
    
    return opcode, value, size
    
def asmLineEpilogue(line, pc, opcode, value, bytes, size):
    words = line.getWords()

    if bytes != None:
        words[1].set(opcode)
        if len(words) > 2:
            #mode relative has nothing to memorize
            words[2] = WORD(getNewConstantName(), TYPE_CONSTANT, value)
        line_bytes = [opcode]
        for byte in bytes:
            line_bytes.append(byte)
        line.setBytes(tuple(line_bytes))
        while len(words) > 3:
            del words[-1]
    
    # event if it's not solved, let's compute pc for the next lines
    line.setAddress(pc.get())
    pc.add(size)    

def getNewConstantName():
    global VAR_NUM
    VAR_NUM += 1
    return "const_%04x"%VAR_NUM

def solveArray(words, info, log=False):
    labels = []
    
    items_array = []
    
    item = []
    for word in words:
        if word.getLabel() != CHAR_COMMA:
            item.append(word)
        else:
            result = solveExpression(item, info)
            if result != None:
                items_array.append(result)
                item = []
            else:
                return None
    if item != []:
            result = solveExpression(item, info)
            if result != None:
                items_array.append(result)
                item = []
            else:
                return None
            
    return tuple(items_array)

def solveExpression(words, info, log=False):
    labels = []
    
    truncator = None
    
    if len(words):
        label = words[0].getLabel()
        if label in ('<', '>'):
            truncator = label
            words = words[1:]
    
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
        if truncator == '>':
            result = result / 256
        elif truncator == '<':
            result = result & 255
    except:
        result = None
    
    if log:
        writeln(result)
    return result

def solveString(word, info):
    try:
        text = eval(word.get())
        if type(text) == int:
            printError("syntax error (perhaps an unexpected value instead of a string)", info)
            return None
        elif type(text) != str:
            printError("syntax error (perhaps an unexpected non-ascii byte)", info)
            return None
        else:
            return tuple([ord(car) for car in text])
    except:
        printError("syntax error", info)
        return None

def addSign(value):
    if value > 127:
        return (value ^ 255) + 1
    else:
        return value

class PRECOMPILER_FILE():
    def __init__(self, arguments):
        if ARG_IFNAME in arguments.keys():
            self.__fname = arguments[ARG_IFNAME]
        else:
            printError("input filename is mandatory")
            sys.exit(1)
        if type(self.__fname) != str or self.__fname == None:
            printError("no source file is defined!", SOURCE_LINE("", CHAR_SPACE.join(sys.argv), 0))
            sys.exit(1)
        if not os.path.isfile(self.__fname):
            printError("file \"%s\" not found"%inc_fname, SOURCE_LINE(self.__fname, CHAR_SPACE.join(sys.argv), 0))
            sys.exit(1)
        
        if ARG_NB_COLS in arguments.keys():
            self.__nb_cols = arguments[ARG_NB_COLS]
        else:
            self.__nb_cols = 16
        
        if ARG_WALL in arguments.keys():
            self.__w_equ = True
            self.__w_str = True
            self.__w_lbl = True
        else:
            self.__w_equ = ARG_WEQU in arguments.keys()
            self.__w_str = ARG_WSTR in arguments.keys()
            self.__w_lbl = ARG_WLBL in arguments.keys()
        
        self.__lines = []
        self.__fnames = []
        self.__line_num = 1
        self.__labels = {}
        self.parseFile(self.__fname)
    
        # some labels are mandatory to build a ROM
        for label in REQUIRED_LABELS:
            if not label in self.__labels:
                if self.__w_lbl:
                    printWarning("label %s not found"%label)

    def parseFile(self, fname):
        self.__fnames.append(fname)
        with open(fname, "r") as fp:
            lines = getFileLines(fp)
            for num, text in enumerate(lines):
                self.parseLine(fname, text, num)
                
    def parseLine(self, fname, text, num):
        word1 = extractWord(text, 1)
        if word1 == KEYWORD_INCLUDE :
            # keyword ".include" is detected, let's include the new file
            self.addLabel(SOURCE_LINE(fname, text, num + 1))
            line = SOURCE_LINE(fname, commentLine(text), num + 1)
            inc_fname = extractWord(text, 2, lower=False)
            if not self.isFileAlreadyIncluded(inc_fname):
                if not os.path.isfile(inc_fname):
                    printError("file \"%s\" not found"%inc_fname, SOURCE_LINE(fname, text, num + 1))
                self.__lines.append(line)
                # recursivity, seriously? :)
                self.parseFile(inc_fname)
                self.addPrecompilerLine("%s   End of inclusion of file %s"%(COMMENT_TAG, inc_fname))
            else:
                if self.__w_equ:
                    printWarning('file "%s" already included'%inc_fname, SOURCE_LINE(fname, text, num + 1))

        elif word1 in PRECOMP_KEYWORDS:
            self.addLabel(SOURCE_LINE(fname, text, num + 1))
            #a precompiler's keyword is detected, let's add some code
            line = SOURCE_LINE(fname, commentLine(text), num + 1)                    
            self.__lines.append(line)
            
            if word1 == KEYWORD_STRING:
                self.addString(text, word1, SOURCE_LINE(fname, text, num + 1), eol=True)
            elif word1 == KEYWORD_CH_ARRAY:
                self.addString(text, word1, SOURCE_LINE(fname, text, num + 1), eol=False)
            
        else:
            self.addLabel(SOURCE_LINE(fname, text, num + 1))
            # nothing special, let's add this "regular" line
            self.__lines.append(SOURCE_LINE(fname, text, num + 1))


    def addString(self, text, key_word, line, eol=True):
        position = text.lower().find(key_word)
        start = position + len(key_word) + 1
        # checking if keyword is not in the label's location
        try:
            while text[start] == CHAR_SPACE:
                start += 1
        except:
            printError("missing data", line)
        # extracting & evaluating the string
        try:
            btext = eval(text[start:])
        except:
            printError("data mismatch, perhaps a comment (not allowed on %s line)"%key_word, line)
        
        # setting difference between string and ch_array (no end of line)
        if eol:
            if chr(0) in btext:
                if self.__w_str:
                    printWarning("there is a \\x00 (enf of string) in this line:", line)
            btext += CHAR_EOL
        
        self.buildMatrix( btext)

    def buildMatrix(self, text):
        position = 0
        last = len(text) - 1

        words = []
        for position, car in enumerate(text):
            byte = ord(text[position])
            
            if position % self.__nb_cols == 0:
                string_txt = "    .byte "
                
            words.append("$%02x"%byte)
            
            if (position % self.__nb_cols) == (self.__nb_cols - 1):
                string_txt += ", ".join(words)
                self.addPrecompilerLine(string_txt)
                words = []
                
        if len(words):
            string_txt += ", ".join(words)
            self.addPrecompilerLine(string_txt)

    def getNextPrecompLineNum(self):
        ret_val = self.__line_num
        self.__line_num += 1
        return ret_val

    def addPrecompilerLine(self, text):
        line = SOURCE_LINE("<precompiler>", text, self.getNextPrecompLineNum())
        self.__lines.append(line)

    def isFileAlreadyIncluded(self, fname):
        return fname in self.__fnames

    def isLabelFree(self, label):
        return not label in self.__labels.keys()

    def addLabel(self, line):
        label = getLabel(line)
        if label != None:
            if not self.isLabelFree(label):
                printLink("label previous declaration :", self.getLabelLine(label))
                printError("label %s already defined!"%label, line)
            else:
                self.__labels[label] = line

    def getLabelLine(self, label):
        return self.__labels[label]

    def getLabels(self):
        labels = self.__labels.keys()
        labels.sort()
        return labels
        
    def saveLabels(self, fname):
        keys = self.__labels.keys()
        keys.sort()
        with open(fname, "w") as fp:
            for key in keys:
                fp.write("%s\n"%key)

    def saveLabelsOrigin(self, fname):
        keys = self.__labels.keys()
        keys.sort()
        with open(fname, "w") as fp:
            for key in keys:
                line = self.__labels[key]
                fp.write("%-16s %-16s %3d %s\n"%(key, line.getFname(), line.getNum(), line.getText()))

    def getOutputSource(self):
        text = EMPTY_STR
        for line in self.__lines:
            text += line.getText() + "\n"
        return text
                        
    def saveOutputSource(self, fname):
        open(fname, "w").write(self.getOutputSource())
                        
    def __str__(self):
        text= EMPTY_STR
        for line in self.__lines:
            text += line.__str__()
        return text
        
    def saveDebug(self, fname):
        fp = open(fname, "w")
        fp.write(self.__str__())
        fp.close()

class PROGRAM_COUNTER():
    def __init__(self, value=DEFAULT_PC_VALUE):
        self.__PC = value

    def get(self):
        return self.__PC
        
    def set(self, value):
        self.__PC = value
        
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
        if self.__wtype in (TYPE_VARIABLE, TYPE_OPCODE, TYPE_CONSTANT):
            return self.__value != None
        elif self.__wtype in (TYPE_VOID,):
            return True
        return False

    def isByte(self):
        if self.__wtype  == TYPE_VARIABLE:
            return isByte(self.get())
        return False

    def isWord(self):
        if self.__wtype  == TYPE_VARIABLE:
            return isWord(self.get())
        return False

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
            #~ otext += "(%s) "%self.getType()
            otext += "%s = "%self.getLabel()
            otext += "%s"%self.get()
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
        self.__fname = fname
        #~ self.__fname = os.path.basename(fname)

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
        self.__bytes = None
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

    def isImplied(self):
        words = self.__words
        mnemonic = words[1].getLabel().lower()
        return len(self.__words) == 2 and mnemonic in IMPLIED_OPCODES

    def isRelative(self):
        words = self.__words
        mnemonic = words[1].getLabel().lower()
        return len(self.__words) >= 3 and mnemonic in RELATIVE_OPCODES

    def isAccumulator(self):
        words = self.__words
        mnemonic = words[1].getLabel().lower()
        return len(self.__words) == 3 and words[2].getLabel().lower() == "a"
        
    def isImmediate(self):
        words = self.__words
        mnemonic = words[1].getLabel().lower()
        return len(self.__words) >= 4 and words[2].getLabel() == "#"
        
    def isZeroPage(self):
        words = self.__words
        mnemonic = words[1].getLabel().lower()
        value = words[2].get()
        if self.isSolved():
            if self.isAbsolute():
                if ZEROPAGE in getModesByMnemonic(mnemonic):
                    if value != None:
                        if isByte(value):
                            return True                        
        return False
        
    def isZeroPageX(self):
        words = self.__words
        mnemonic = words[1].getLabel().lower()
        value = words[2].get()
        if self.isSolved():
            if self.isAbsoluteX():
                if ZEROPAGEX in getModesByMnemonic(mnemonic):
                    if value != None:
                        if isByte(value):
                            return True                        
        return False
        
    def isZeroPageY(self):
        words = self.__words
        mnemonic = words[1].getLabel().lower()
        value = words[2].get()
        if self.isSolved():
            if self.isAbsoluteY():
                if ZEROPAGEY in getModesByMnemonic(mnemonic):
                    if value != None:
                        if isByte(value):
                            return True                        
        return False
        
    def isAbsolute(self):
        words = self.__words
        mnemonic = words[1].getLabel().lower()
        if self.__bytes == None:
            return len(self.__words) >= 3
        else:
            return getOpcodeValue(mnemonic, ABSOLUTE, self.getLine(), strict=False) == words[1].get()
        
    def isAbsoluteX(self):
        words = self.__words
        mnemonic = words[1].getLabel().lower()
        result = True
        if self.__bytes == None:
            result &= len(self.__words) >= 5
            result &= words[-1].getLabel().lower() == "x"
            result &= words[-2].getLabel() == ","
        else:
            result &= getOpcodeValue(mnemonic, ABSOLUTEX, self.getLine(), strict=False) == words[1].get()
        return result
        
    def isAbsoluteY(self):
        words = self.__words
        mnemonic = words[1].getLabel().lower()
        result = True
        if self.__bytes == None:
            result &= len(self.__words) >= 5
            result &= words[-1].getLabel().lower() == "y"
            result &= words[-2].getLabel() == ","
        else:
            result &= getOpcodeValue(mnemonic, ABSOLUTEY, self.getLine(), strict=False) == words[1].get()
        return result
        
    def isIndirect(self):
        words = self.__words
        mnemonic = words[1].getLabel().lower()
        return len(self.__words) >= 5 and words[-1].getLabel() == ")" and words[2].getLabel() == "("
        
    def isIndirectX(self):
        words = self.__words
        mnemonic = words[1].getLabel().lower()
        return len(self.__words) >= 7 and words[-1].getLabel() == ")" and words[-2].getLabel().lower() == "x" and words[-3].getLabel() == "," and words[2].getLabel() == "("
        
    def isIndirectY(self):
        words = self.__words
        mnemonic = words[1].getLabel().lower()
        return len(self.__words) >= 7 and words[-1].getLabel().lower() == "y" and words[-2].getLabel() == "," and words[-3].getLabel() == ")" and words[2].getLabel() == "("

    def isDirectiveLine(self):
        if len(self.__words) >= 2:
            return self.__words[1].getType() == TYPE_DIRECTIVE
        else:
            return False
    
    def isAffectationLine(self):
        if len(self.__words) >= 4:
            if self.__words[1].getLabel() != "*":            
                return self.__words[2].getLabel() == CHAR_EQUAL
            else:
                return False
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
        words = self.__words
        if len(words) > 1:
            word = words[1]
            if word.getType() in (TYPE_OPCODE, TYPE_DIRECTIVE):
                return self.getBytes() != None
            elif word.getLabel() == CMD_ORG:
                return word.get() != None
        elif len(words) == 1:
            return words[0].getType() == TYPE_CONSTANT
        

    def xx__isSolved(self):
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
    def __init__(self, params):
        # arguments stuff
        self.__params = params
        self.__fname = self.getArgument('-ifname')
        self.__nb_cols = self.getArgument('-nb_cols')
        self.__org = self.getArgument('-org')
        if self.__fname == None:
            printError("input filename is mandatory")
            sys.exit(1)
        if not os.path.isfile(self.__fname):
            printError("file \"%s\" not found"%self.__fname)
            sys.exit(1)

        # assembler stuff
        self.__source_lines = []
        self.__asm_lines = []
        self.__words = {}
        self.__labels = {}
        self.__short_opcodes_line_nums = {}

        # let's go!
        self.createAsmLines(self.__fname)
    
    def getArgument(self, pname):
        #getting an argument from commandline
        if pname in self.__params.keys():
            return self.__params.get(pname)
        else:
            return None
    
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
        
    def checkStartAddress(self):
        too_late = False
        for line in self.getAsmLines():
            if line.isDirectiveLine():
                if line.getWords()[1].getLabel() == '*':
                    if too_late:
                        printError("start address set too late", line.getLine())
                        sys.exit(1)
                    elif self.__org:
                        printError("start address already set", line.getLine())
                        sys.exit(1)
                    else:
                        result = solveExpression(line.getWords()[3:], line.getLine())
                        if result != None:
                            self.__org = result
                            line.setAddress(result)
                            return
                else:
                    too_late = True
            elif line.isMnemonicLine() or line.isDirectiveLine():
                if line.getWords()[1].getLabel() != '*':
                    too_late == True
        if not self.__org:
            printError("start address is missing")
            sys.exit(1)

    def createAsmLines(self, fname):
        # let's slice the line in a list of words
        with open(fname, "r") as fp:
            lines = getFileLines(fp)

        for num, text in enumerate(lines):
            # building original source lines with filename and line number
            # information in order to display them in case of warning/error
            line = SOURCE_LINE(fname, text, num + 1)
            self.__source_lines.append(line)
            text = removeComment(text, line)
            if len(text):
                # building minimal assembler lines (empty lines and comments are removed)
                asm_line = ASM_LINE(text, line)
                self.__asm_lines.append(asm_line)
            else:
                # line is empty, no need to store it
                continue
            self.splitLine(asm_line)
            
        # must have a start address to begin assembling
        self.checkStartAddress()

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

            if position == 0 and word.getType() == TYPE_VARIABLE:
                label = word.getLabel()
                if label in self.__labels.keys():
                    printError("label '%s' already declared"%label, line.getLine())
                else:
                    self.__labels[label] = word

        if len(line.getWords()) >= 3:
            if line.getWords()[2].getLabel() == CHAR_COMMA:
                printError("unexpected comma", info)
            
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

    def reset(self):
        # when all is solved must restart with identified zero page opcodes 
        temp_dict = {}
        for key in self.__short_opcodes_line_nums.keys():
            temp_dict[key] = self.__short_opcodes_line_nums[key]
        self.__init__(self.__params)
        self.__short_opcodes_line_nums = temp_dict

    def assemble(self):
        # this is only one pass, all may not be solved with it
        pc = PROGRAM_COUNTER(self.__org)

        for line_num, line in enumerate(self.__asm_lines):
            if not line.isSolved():
                self.parseLine(line_num, line, pc)
        
        # classical 6502 trap, page zero modes are shorter than absolute ones
        self.correctShortOpcodes();

    def parseLine(self, line_num, line, pc):
        line.setAddress, pc.get()
        info = line.getLine()
        
        words = line.getWords()
        if len(words) >= 2:
            if words[1].getLabel() == "*":
                pass
        
        if line.hasLabel():
            self.computeLabel(line, pc)
        
        if line.isMnemonicLine():
            self.computeOpcode(line_num, line, pc)

        elif line.isDirectiveLine():
            self.computeDirective(line, pc)

        elif line.isAffectationLine():
            self.computeAffectation(line, pc)

        else:
            #~ if not line.hasLabel():
            if len(line.getWords()) > 1:
                if not line.getWords()[1].isSolved():
                    printError("syntax error", info)
        
    def computeLabel(self, line, pc):
        words = line.getWords()
        word = words[0]
        word.set(pc.get())
        line.setAddress(pc.get())
        return
            
    def computeOpcode(self, line_num, line, pc):
        words = line.getWords()
        nb_words = len(words)
        info = line.getLine()
        
        word = words[1]
        if word.isSolved():
            return
            
        mnemonic = word.getLabel().lower()
        modes = getModesByMnemonic(mnemonic)
        
        if line.isRelative():
            self.computeRelative(line, pc)

        elif line.isImplied():
            self.computeImplied(line, pc)

        elif line.isAccumulator():
            self.computeAccumulator(line, pc)

        elif line.isImmediate():
            self.computeImmediate(line, pc)

        elif line.isIndirectX():
            self.computeIndirectX(line, pc)

        elif line.isIndirectY():
            self.computeIndirectY(line, pc)

        elif line.isIndirect():
            self.computeIndirect(line, pc)

        elif line.isAbsoluteX():
            if not line_num in self.__short_opcodes_line_nums.keys():
                if ABSOLUTEX in modes:
                    self.computeAbsoluteX(line, pc)
                elif ZEROPAGEX in modes:
                    self.computeZeroPageX(line, pc)
                else:
                    printError('illegal addressing mode', info)
            else:
                self.computeZeroPageX(line, pc)

        elif line.isAbsoluteY():
            if not line_num in self.__short_opcodes_line_nums.keys():
                if ABSOLUTEY in modes:
                    self.computeAbsoluteY(line, pc)
                elif ZEROPAGEY in modes:
                    self.computeZeroPageY(line, pc)
                else:
                    printError('illegal addressing mode', info)
            else:
                self.computeZeroPageY(line, pc)

        elif line.isAbsolute():
            if not line_num in self.__short_opcodes_line_nums.keys():
                self.computeAbsolute(line, pc)
            else:
                self.computeZeroPage(line, pc)

        else:
            printError('illegal addressing mode', info)

    def computeRelative(self, line, pc):
        words = line.getWords()
        opcode, value, size = asmLinePrologue(line, RELATIVE, words[2:])
        bytes = None
        
        if opcode != None:
            # all prerequisites are good, let's solve
            if value == None:
                pass
            else:
                move = value - (pc.get() + 2) 
                if not isRelative(move):
                    printError("relative value out of range pc=$%04x target=$%04X move:$%04X"%(pc.get(), value, move), line.getLine())
                else:
                    bytes = (move & 0xff,)

        asmLineEpilogue(line, pc, opcode, value, bytes, size)

    def computeImplied(self, line, pc):
        words = line.getWords()
        opcode, value, size = asmLinePrologue(line, IMPLIED, [])
        bytes = None
        
        if opcode != None:
            # all prerequisites are good, let's solve
            bytes = tuple([])

        asmLineEpilogue(line, pc, opcode, value, bytes, size)

    def computeAccumulator(self, line, pc):
        words = line.getWords()
        opcode, value, size = asmLinePrologue(line, ACCUMULATOR, [])
        bytes = None
        
        if opcode != None:
            # all prerequisites are good, let's solve
            bytes = tuple([])

        asmLineEpilogue(line, pc, opcode, value, bytes, size)

    def computeImmediate(self, line, pc):
        words = line.getWords()
        opcode, value, size = asmLinePrologue(line, IMMEDIATE, words[3:])
        bytes = None
        
        if opcode != None:
            # all prerequisites are good, let's solve
            if value == None:
                pass
            elif not isByte(value):
                printError("bad byte $%02x"%(value), line.getLine())
            else:
                bytes = (value,)

        asmLineEpilogue(line, pc, opcode, value, bytes, size)

    def computeIndirectX(self, line, pc):
        words = line.getWords()
        opcode, value, size = asmLinePrologue(line, INDIRECTX, words[3:-3])
        bytes = None
        
        if opcode != None:
            # all prerequisites are good, let's solve
            if value == None:
                pass
            elif not isByte(value):
                printError("bad byte $%02x"%(value), line.getLine())
            else:
                bytes = (value,)

        asmLineEpilogue(line, pc, opcode, value, bytes, size)
        
    def computeIndirectY(self, line, pc):
        words = line.getWords()
        opcode, value, size = asmLinePrologue(line, INDIRECTY, words[3:-3])
        bytes = None
        
        if opcode != None:
            # all prerequisites are good, let's solve
            if value == None:
                pass
            elif not isByte(value):
                printError("bad byte $%02x out of range"%(value), line.getLine())
            else:
                bytes = (value,)

        asmLineEpilogue(line, pc, opcode, value, bytes, size)

    def computeIndirect(self, line, pc):
        words = line.getWords()
        opcode, value, size = asmLinePrologue(line, INDIRECT, words[3:-1])
        bytes = None
        
        if opcode != None:
            # all prerequisites are good, let's solve
            if value == None:
                pass
            elif not isWord(value):
                printError("bad word $%04x"%(value), line.getLine())
            else:
                bytes = (value & 255, value / 256)

        asmLineEpilogue(line, pc, opcode, value, bytes, size)

    def computeAbsolute(self, line, pc):
        words = line.getWords()
        opcode, value, size = asmLinePrologue(line, ABSOLUTE, words[2:])
        bytes = None
        
        if opcode != None:
            # all prerequisites are good, let's solve
            if value == None:
                pass
            elif not isWord(value):
                printError("bad word $%04x"%(value), line.getLine())
            else:
                bytes = (value & 255, value / 256)

        asmLineEpilogue(line, pc, opcode, value, bytes, size)

    def computeAbsoluteX(self, line, pc):
        words = line.getWords()
        opcode, value, size = asmLinePrologue(line, ABSOLUTEX, words[2:-2])
        bytes = None
        
        if opcode != None:
            # all prerequisites are good, let's solve
            if value == None:
                pass
            elif not isWord(value):
                printError("bad word $%04x"%(value), line.getLine())
            else:
                bytes = (value & 255, value / 256)

        asmLineEpilogue(line, pc, opcode, value, bytes, size)

    def computeAbsoluteY(self, line, pc):
        words = line.getWords()
        opcode, value, size = asmLinePrologue(line, ABSOLUTEY, words[2:-2])
        bytes = None
        
        if opcode != None:
            # all prerequisites are good, let's solve
            if value == None:
                pass
            elif not isWord(value):
                printError("bad word $%04x"%(value), line.getLine())
            else:
                bytes = (value & 255, value / 256)

        asmLineEpilogue(line, pc, opcode, value, bytes, size)

    def computeZeroPage(self, line, pc):
        words = line.getWords()
        opcode, value, size = asmLinePrologue(line, ZEROPAGE, words[2:])
        bytes = None
        
        if opcode != None:
            # all prerequisites are good, let's solve
            if value == None:
                pass
            elif not isByte(value):
                printError("bad word $%04x"%(value), line.getLine())
            else:
                bytes = (value,)

        asmLineEpilogue(line, pc, opcode, value, bytes, size)

    def computeZeroPageX(self, line, pc):
        words = line.getWords()
        opcode, value, size = asmLinePrologue(line, ZEROPAGEX, words[2:-2])
        bytes = None
        
        if opcode != None:
            # all prerequisites are good, let's solve
            if value == None:
                pass
            elif not isByte(value):
                printError("bad word $%04x"%(value), line.getLine())
            else:
                bytes = (value,)

        asmLineEpilogue(line, pc, opcode, value, bytes, size)

    def computeZeroPageY(self, line, pc):
        words = line.getWords()
        opcode, value, size = asmLinePrologue(line, ZEROPAGEY, words[2:-2])
        bytes = None
        
        if opcode != None:
            # all prerequisites are good, let's solve
            if value == None:
                pass
            elif not isByte(value):
                printError("bad word $%04x"%(value), line.getLine())
            else:
                bytes = (value,)

        asmLineEpilogue(line, pc, opcode, value, bytes, size)

    def computeAffectation(self, line, pc):
        words = line.getWords()
        info = line.getLine()
        
        value = solveExpression(words[3:], info)
        if value != None:
            words[1].set(value)
            while len(words) > 2:
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
        
        #~ bytes = solveExpression(words[2:], info)
        bytes = solveArray(words[2:], info)
        if bytes != None and pc.isOK():
            # all prerequisites are good, let's solve
            if type(bytes) == int:
                bytes = (bytes,)
            for index, byte in enumerate(bytes):
                if byte < 0 or byte > 255:
                    printError("byte #%d value $%04x out of range"%(index+1, byte), info)
            else:
                words[2] = WORD(getNewConstantName(), TYPE_CONSTANT, bytes)
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
        
        integers = solveArray(words[2:], info)
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
                words[2] = WORD(getNewConstantName(), TYPE_CONSTANT, bytes)
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
        
        integers = solveArray(words[2:], info)
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
                words[2] = WORD(getNewConstantName(), TYPE_CONSTANT, bytes)
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
        
        bytes = solveString(words[2], info)
        
        if bytes != None and pc.isOK():
            # all prerequisites are good, let's solve
            bytes = list(bytes)
            if len(bytes):
                for byte in bytes[:-1]:
                    if not byte:
                        printWarning('unexpected zero byte in string', info)
            bytes.append(0)
            bytes = tuple(bytes)
            words[2] = WORD(getNewConstantName(), TYPE_CONSTANT, bytes)
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
        
        bytes = solveString(words[2], info)
        
        if bytes != None and pc.isOK():
            # all prerequisites are good, let's solve
            words[2] = WORD(getNewConstantName(), TYPE_CONSTANT, bytes)
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
        
        nb_bytes = solveExpression(words[2:], info)
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
                words[2] = WORD(getNewConstantName(), TYPE_CONSTANT, bytes)
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
        
        nb_words = solveExpression(words[2:], info)
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
                words[2] = WORD(getNewConstantName(), TYPE_CONSTANT, bytes)
                line.setBytes(tuple(bytes))
                while len(words) > 3:
                    del words[-1]
        # event if it's not solved, let's compute pc for the next lines
        else:
            nb_words = 0
        line.setAddress(pc.get())
        pc.add(nb_words * SIZEOF_WORD)

    def computeOrg(self, line, pc):
        words = line.getWords()
        info = line.getLine()
        
        result = solveExpression(words[3:], info)
        if result != None:
            self.__org = result
            words[1].set(result)
            pc.set(result)

    def correctShortOpcodes(self):
        for line_num, line in enumerate(self.getAsmLines()):
            if line.isMnemonicLine():
                if line.isSolved():
                    word = line.getWords()[1]
                    label = word.getLabel()
                    opcode = word.get()
                    mnemonic = OPCODE_VALUES[opcode]
                    mode = MODES[opcode]
                    size =  CODE_SIZES[opcode]
                    modes = getModesByMnemonic(mnemonic)
                    new_opcode = None
                    bytes = line.getBytes()
                    if size == 3:
                        if not bytes[2]:
                            # if third byte is null, address is a page zero one
                            if mode == ABSOLUTE:
                                if ZEROPAGE in modes:
                                    new_opcode = getOpcodeValue(mnemonic, ZEROPAGE, line.getLine(), strict=True)
                                    new_mode = ZEROPAGE
                            elif mode == ABSOLUTEX:
                                if ZEROPAGEX in modes:
                                    new_opcode = getOpcodeValue(mnemonic, ZEROPAGEX, line.getLine(), strict=True)
                                    new_mode = ZEROPAGEX
                            elif mode == ABSOLUTEY:
                                if ZEROPAGEY in modes:
                                    new_opcode = getOpcodeValue(mnemonic, ZEROPAGEY, line.getLine(), strict=True)
                                    new_mode = ZEROPAGEY
                    if new_opcode != None:
                        self.__short_opcodes_line_nums[line_num] = new_opcode
                        #~ printWarning("%02X -> %02X (%s %s -> %s)"%(opcode, new_opcode, mnemonic, mode, new_mode), line.getLine())

    def getShortOpcodes(self):
        pass

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

    def getLabels(self):
        ret_dic = {}
        keys = self.__labels.keys()
        keys.sort()
        for key in keys:
            ret_dic[key] = self.__labels[key].get()
        return ret_dic

    def getLabelsText(self):
        keys = self.__labels.keys()
        keys.sort()
        otext = EMPTY_STR
        
        for key in keys:
            value = self.__labels[key]
            otext += "%s 0x%x"%(key, value.get()) + CHAR_LF
        return otext

    def getBytes(self):
        bytes = []
        for line in self.__asm_lines:
            if line.isMnemonicLine() or line.isDirectiveLine():
                if line.isSolved():
                    for byte in line.getBytes():
                        bytes.append(byte)
                else:
                    printWarning('not solved', line.getLine())
        return bytes

    def getDesassembled(self):
        otext = EMPTY_STR
        for line in self.__asm_lines:
            if line.hasLabel():
                address = line.getAddress()
                label = line.getWords()[0].getLabel()
                otext += "%04X: %s\n"%(address, label)
                
            if line.isMnemonicLine():
                if line.isSolved():
                    opcode = line.getWords()[1].get()
                    address = line.getAddress()
                    mnemonic = OPCODE_VALUES[opcode].upper()
                    mode = MODES[opcode]
                    bytes = line.getBytes()
                    
                    otext += "%04X "%address
                    otext += "%-8s "%CHAR_SPACE.join(["%02X"%byte for byte in bytes])
                    
                    if mode == IMPLIED:
                        otext += "%s"%(mnemonic)
                    elif mode == INDIRECTX:
                        otext += "%s ($%02X,X)"%(mnemonic, bytes[1])
                    elif mode == ZEROPAGE:
                        otext += "%s $%02X"%(mnemonic, bytes[1])
                    elif mode == IMMEDIATE:
                        otext += "%s #$%02X"%(mnemonic, bytes[1])
                    elif mode == ACCUMULATOR:
                        otext += "%s A"%(mnemonic)
                    elif mode == ABSOLUTE:
                        otext += "%s $%04X"%(mnemonic, bytes[1] + bytes[2] * 256)
                    elif mode == RELATIVE:
                        otext += "%s $%04X"%(mnemonic, address + 2 + addSign(bytes[1]))
                    elif mode == INDIRECTY:
                        otext += "%s ($%02X),Y"%(mnemonic, bytes[1])
                    elif mode == ZEROPAGEX:
                        otext += "%s $%02X,X"%(mnemonic, bytes[1])
                    elif mode == ABSOLUTEY:
                        otext += "%s $%04X,Y"%(mnemonic, bytes[1] + bytes[2] * 256)
                    elif mode == ABSOLUTEX:
                        otext += "%s $%04X,X"%(mnemonic, bytes[1] + bytes[2] * 256)
                    elif mode == INDIRECT:
                        otext += "%s ($%04X)"%(mnemonic, bytes[1])
                    elif mode == ZEROPAGEY:
                        otext += "%s $%02X"%(mnemonic, bytes[1])
                    else:
                        raise Exception("WTF???")
                    otext += CHAR_LF
                else:
                    info = line.getLine()
                    otext += "NOT SOLVED:%s #%d %s\n"%(info.getFname(), info.getNum(), info.getText())
            elif line.isDirectiveLine():
                if line.isSolved():
                    bytes = line.getBytes()
                    address = line.getAddress()
                    cols = self.__nb_cols
                    
                    #~ text = EMPTY_STR
                    for index, byte in enumerate(bytes):
                        if (index % cols) == 0:
                            text = "%04X "%(address + index)
                            
                        text += "%02X "%byte
                        
                        if (index % cols) == (cols - 1):
                            text += "\n"
                            otext += text
                            text = EMPTY_STR

                    if text != EMPTY_STR:
                        text += "\n"
                        otext += text
                    
                else:
                    info = line.getLine()
                    word = line.getWords()[1]
                    if word.getLabel() != "*" or word.get() == None:
                        otext += "NOT SOLVED:%s #%d %s\n"%(info.getFname(), info.getNum(), info.getText())
                    
        return otext

    def getPercent(self):
        tot = 0.0
        done = 0.0
        
        for line in self.getAsmLines():
            if line.isMnemonicLine() or line.isDirectiveLine():
                tot += 1.0
                if line.getBytes() != None:
                    done += 1.0
                elif line.getWords()[1].getLabel() == "*":
                    if line.getWords()[1].get() != None:
                        done += 1.0
            elif line.isAffectationLine():
                tot += 1.0
                if line.isSolved():
                    done += 1.0
        return (done / tot) * 100.0
        
    def getUnsolvedText(self):
        otext = EMPTY_STR
        found = 0
        for index, key in enumerate(self.getWords()):
            word = self.getWord(key)
            if word.get() == None:
                found += 1
                otext += "%s "%key
                if index %16 == 15:
                    otext += "\n"
        if index %16 != 15:
            otext += "\n"
        
        if found:
            return "Can't solve these %d values:\n"%found + otext
        else:
            return EMPTY_STR

    def __str__(self):
        otext = EMPTY_STR
        for asm_line in self.__asm_lines:
            otext += str(asm_line)
        return otext

def getArguments(arguments, pairs=[], offset=1):
    index = offset
    kwds = {}
    nb_args = len(arguments)
    while index < nb_args:
        arg = arguments[index]
        if arg in pairs:
            if index < (nb_args - 1):
                param = arguments[index + 1]
                if param.startswith('"'):
                    value = eval(param)
                else:
                    try:
                        value = eval(param)
                    except:
                        value = param
                kwds[arg] = value
                index += 1
            else:
                printError("unexpected end of command line arguments")
                sys.exit(1)
        else:
            kwds[arg] = True
        index += 1
    return kwds
    
if __name__ == "__main__":
    
    #####################################
    #                                   #
    # COMMAND LINE PARAMETERS COMPUTING #
    #                                   #
    #####################################

    arguments = getArguments(sys.argv, (ARG_IFNAME, ARG_OFNAME, ARG_DFNAME, ARG_LFNAME, ARG_ORG, ARG_NB_COLS))
    if not ARG_NB_COLS in arguments.keys():arguments[ARG_NB_COLS] = 16
    
    #####################
    #                   #
    # PREASSEMBLER PART #
    #                   #
    #####################

    precompiler = PRECOMPILER_FILE(arguments)
    # change ifname for assembler
    arguments[ARG_IFNAME] = buildName(arguments[ARG_IFNAME], "precompiled.asm")
    precompiler.saveOutputSource(arguments[ARG_IFNAME])
    writeln('precompilation done')

    ##################
    #                #
    # ASSEMBLER PART #
    #                #
    ##################

    # let's parse source file and clean it
    assembler = ASSEMBLER(arguments)
    
    old_percent = 0.0
    pass_num = 0
    while 1:
        assembler.assemble()
        percent = assembler.getPercent()
        write("pass %d - done:%.02f%%\n"%(pass_num+1, percent))
        if percent == 100.0:
            break
        elif percent == old_percent:
            writeln(assembler.getUnsolvedText())
            sys.exit(1)
        else:
            old_percent = percent
        pass_num += 1

    #~ write(assembler.getDesassembled())

    #~ diskSave(buildName(ap.get('-ifname'), "debug.asm"), assembler.debugStr())

    #~ diskSave(buildName(ap.get('-ifname'), "asm_lines.asm"), assembler.getCodeText())
    #~ diskSave(buildName(ap.get('-ifname'), "asm_words.asm"), str(assembler))
    #~ diskSave(buildName(ap.get('-ifname'), "labels.asm"), assembler.getLabelsText())
