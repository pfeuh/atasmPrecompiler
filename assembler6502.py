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

    FIRST_CHAR = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz_"
    OTHER_CHAR = FIRST_CHAR + "0123456789"
    NO_LABEL_FIRST_CHAR = " ;"

    TYPE_VOID = 0
    TYPE_VARIABLE = 1
    TYPE_COMMAND = 2
    TYPE_MNEMO = 3
    TYPE_KEYWORD = 4
    TYPE_PONCTUATION = 5
    TYPE_STRING = 6
    WORD_TYPES = (None, TYPE_VOID, TYPE_VARIABLE, TYPE_COMMAND, TYPE_MNEMO, TYPE_KEYWORD, TYPE_PONCTUATION, TYPE_STRING)
    TYPE_NAME = {None:"None", TYPE_VOID:'void', TYPE_VARIABLE:'variable', TYPE_COMMAND:'command', TYPE_MNEMO:'mnemo', TYPE_KEYWORD:'keyword', TYPE_PONCTUATION:'ponct',TYPE_STRING:'string'}

    PONCTUATION = ('(', ')', ',', '#', '+', '-', '/', '*', '=', '<', '>', '&', '!', '|', '^')
    
    COMMANDS = ('.byte', '.word', '.long', '.string', '.ch_array', '.ds', '*')
    REGISTERS = ('x', 'y', 'X', 'Y')
    KEYWORDS = COMMANDS + PONCTUATION + REGISTERS

def write(text):
    sys.stdout.write(str(text))
    
def writeln(text):
    write(text)
    write("\n")

def printLink(message=EMPTY_STR, line=None):
    if line != None:
        writeln('File "%s", line %d, %s'%(line.getFname(), line.getNum(), message))
        writeln(line.getText())
    
def printWarning(message, line=None):
    if line != None:
        writeln('File "%s", line %d, warning : %s'%(line.getFname(), line.getNum(), message))
        writeln(line.getText())
    else:
        writeln('Warning : %s'%(message))
    
def printError(message, line=None):
    if ap.get('-debug'):
        # the goal is to trig an error, then, it's possible to follow the white rabbit
        1/0
    elif line != None:
        writeln('File "%s", line %d, error : %s - %s'%(line.getFname(), line.getNum(), message, line.getText()))
    else:
        writeln('Error : %s'%(message))
    sys.exit(1)
    #~ if ap.get('-debug'):
        #~ # the goal is to trig an error, then, it's possible to follow the white rabbit
        #~ 1/0
    #~ elif line != None:
        #~ writeln('File "%s", line %d, error : %s - %s'%(line.getFname(), line.getNum(), message, line.getText()))
    #~ else:
        #~ writeln('Error : %s'%(message))
    #~ sys.exit(1)

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
    
def extractWordsFromLine(text, line=None):
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

def getOpcodeValue(opcode, mode, line):
    for value, item in enumerate(MNEMOS):
        if item == opcode:
            if MODES[value] == mode:
                return value
    # no opcode with this mode
    printError("illegal opcode '%s' (%s)"%(opcode, mode), line)
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

class ASM_VARIABLE():
    def __init__(self, vname):
        self.__vname = vname
        self.__value = None
        
    def getLabel(self):
        return self.__vname

    def set(self, value):
        if type(value) != int:
            printError("integer expected for %s. got %s"%(self.__name, str(value)))
            
        if value < 0 or value > 0xffff:
            printError("variable %s out of range (%)"%(self.__name, value))
        else:
            self.__value = value
        
    def get(self):
        return self.__value
        
    def isSolved(self):
        return self.__value != None
        
    def isByte(self):
        return self.__value < 0x100
    
    def __str__(self):
        if self.__value != None:
            value_text = "0x%04x"%self.__value
        else:
            value_text = "------"
        return "%-016s %s"%(self.__vname, value_text) 

class ASM_WORD():
    def __init__(self, label, line, num):
        self.__text = label
        self.__wtype = None
        self.__value = None
        self.__position = num
        self.__solved = False
        self.__variable = None
        self.__line = line

    def getLine(self):
        return self.__line

    def hasVariable(self):
        return self.__variable != None

    def getVariable(self):
        return self.__variable

    def setVariable(self, value):
        if self.__variable != None:
            self.__variable.set(value)
        else:
            raise Exception("no variable binded to %s!"%self.getLabel())

    def solve(self):
        self.__solved = True
        
    def isSolved(self):
        if self.__wtype == TYPE_VARIABLE:
            return self.__variable.isSolved()
        return self.__solved

    def getLabel(self):
        return self.__text

    def setLabel(self, label):
        self.__text = label

    def getType(self):
        return self.__wtype

    def setType(self, wtype, source=None):
        self.__wtype = wtype
        if wtype == TYPE_VARIABLE:
            if source == None:
                raise Exception("for type TYPE_VARIABLE, source is a mandatory parameter")
            variable = source.addVariable(self.getLabel())
            self.__variable = variable

    def get(self):
        if self.__wtype == TYPE_VARIABLE:
            return self.__variable.get()
        return self.__value

    def set(self, value):
        if self.__wtype == TYPE_VARIABLE:
            self.__variable.set(value)
        else:
            self.__value = value
            self.__solved = True

    def isVariable(self):
        if self.__wtype == TYPE_VARIABLE:
            return True
        return False

    def isMmemo(self):
        if self.__wtype == TYPE_MNEMO:
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
            otext  = "%s "%{False:".", True:"X"}[self.isSolved()]
            otext += "(%s) "%TYPE_NAME[self.getType()]
            otext += "%s "%self.getLabel()
        while len(otext) < 40:
            otext += CHAR_SPACE
        if self.hasVariable():
            otext += str(self.getVariable())
        return otext + CHAR_LF

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
        self.__words = []

    def addWord(self, word):
        if word in (None, str):
            printLink("", self.getLine())
            raise Exception("attempt to add a bad word '%s'!"%str(word))
            
        self.__words.append(word)
    
    def getText(self):
        return self.__text

    def appendByte(self, byte):
        self.__bytes.append(byte)
    
    def getBytes(self):
        return self.__bytes
    
    def getLine(self):
        return self.__line

    def isSolved(self):
        for word in self.__words:
            if not word.isSolved():
                return False
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

    def getWords(self):
        return self.__words

    def __str__(self):
        line = self.getLine()
        solved_text = "."
        if self.isSolved():
            solved_text = "X"
        otext = '%s %06d %s\n'%(solved_text, line.getNum(), line.getText())
        for word in self.__words:
            otext += "%s"%str(word)
        otext += "-" * 40
        return otext + CHAR_LF

class ASM_FILE():
    def __init__(self, params):
        # arguments stuff
        self.__params = params
        self.__fname = self.getArgument('-ifname')
        self.__nb_cols = self.__params.get('-nb_cols')
        self.__org = self.getArgument('-org')
        self.__PC = None
        if not os.path.isfile(self.__fname):
            printError("file \"%s\" not found"%self.__fname, SOURCE_LINE(fname, CHAR_SPACE.join(sys.argv), 0))

        # assembler stuff
        self.__source_lines = []
        self.__asm_lines = []
        self.__variables = {}
        self.percent = 0.0

        # let's go!
        self.createAsmLines(self.__fname)
        self.computeOpcodes()
        #~ self.computeAffectations()

    def initPC(self):
        self.__PC = self.__org
        return self.__PC
        
    def getPC(self):
        return self.__PC
        
    def adjustPC(self, size):
        self.__PC += size
        return self.__PC
        
    def addVariable(self, label):
        if not label in self.__variables.keys():
            variable = ASM_VARIABLE(label)
            self.__variables[label] = variable
        return self.__variables[label]
            
    def getArgument(self, pname):
        #getting an argument from commandline
        if pname in self.__params.keys():
            return self.__params.get(pname)
        else:
            printError("mandatory parameter '%s' missing"%pname)
    
    def createAsmLines(self, fname):
        with open(fname, "r") as fp:
            lines = getFileLines(fp)
        # building minimal source file (comments are removed)
        for num, text in enumerate(lines):
            line = SOURCE_LINE(fname, text, num + 1)
            self.__source_lines.append(line)
            text = removeComment(text, line)
            if len(text):
                asm_line = ASM_LINE(text, line)
                self.__asm_lines.append(asm_line)
            else:
                continue

            # line is created, let's add its words
            words = [word for word in extractWordsFromLine(asm_line.getText(), line)]
            for position, label in enumerate(words):
                asm_line.addWord(self.InitializeWord(label, position, line))

    def InitializeWord(self, label, word_num, line):
        word = ASM_WORD(label, line, word_num)
        label = word.getLabel()
        test_value = False

        if not word_num:
            # managing variables, 1rst word can only be label
            if labelIsOk(word.getLabel()):
                word.setType(TYPE_VARIABLE, self)
            else:
                word.setType(TYPE_VOID)
                word.set("---")
        elif word_num == 1:
            #managing variable
            if labelIsOk(word.getLabel()):
                word.setType(TYPE_VARIABLE, self)
            # managing opcodes
            elif label.lower() in OPCODES:
                # insensitive case allowed
                word.setType(TYPE_MNEMO)
            #managing commands
            elif label in COMMANDS:
                word.setType(TYPE_KEYWORD)
            elif label in REGISTERS:
                word.setType(TYPE_KEYWORD)
            else:
                printError("Unexpected word '%s'"%label, line)
        elif word_num >= 2:
            #managing variables
            if labelIsOk(word.getLabel()):
                word.setType(TYPE_VARIABLE, self)
            #managing commands
            elif label in COMMANDS:
                word.setType(TYPE_KEYWORD)
            elif label in COMMANDS:
                word.setType(TYPE_COMMAND)
            elif label in KEYWORDS:
                word.setType(TYPE_KEYWORD)
            elif label in PONCTUATION:
                word.setType(TYPE_PONCTUATION)
            #managing values
            elif label.startswith(CHAR_DOLLAR):
                # vintage assemblers use $ instead of 0x for hex values
                label = "0x" + label[1:]
                test_value = True
            elif label.startswith(CHAR_TILD):
                # vintage assemblers use ~ to prefix a binary value
                label = "0b" + label[1:]
                test_value = True
            elif label.startswith(CHAR_SINGLE_QUOTE):
                # vintage assemblers use ' to prefix a single character
                if len(label) != 2:
                    printError("syntax on word '%s'"%label, line)
                else:
                    label = "0x%04x"%ord(label[1])
                    test_value = True
                    #~ word.set(value)
            elif label[0] in "0123456789-":
                # decimal value
                test_value = True
            elif isString(label):
                word.setType(TYPE_VARIABLE, self)
                # no setting, it will come later
            if test_value:
                # let's test numerical values
                success = False
                try:
                    value = eval(label)
                    success = True
                except:
                    pass
                if success:
                    if type(value) == int:
                        word.setType(TYPE_VARIABLE, self)
                        #~ word.set(value)
                        word.setVariable(value)
                    else:
                        printError("unknown type for '%s'"%word, line)
                else:
                    printError("syntax on word '%s'"%word, line)
            
        # did we missed something?
        if word.getType() == None:
            printError("Unexpected word '%s'"%label, line)
            
        return word

    def computeOpcodes(self):
        pc = self.initPC()
        
        for asm_line in self.__asm_lines:
            solved = False
            line = asm_line.getLine()
            words = asm_line.getWords()
            nb_words = len(words)
            
            if len(words):
                if words[0].getType() == TYPE_VARIABLE:
                    words[0].setVariable(pc)
            
            if nb_words >= 2:
                opcode = words[1].getLabel().lower()
                if words[1].getType() == TYPE_MNEMO:
# mode Relative
                    if opcode in RELATIVE_OPCODES:
                        value = getOpcodeValue(opcode, RELATIVE, line)
                        words[1].set(value)
                        pc = self.adjustPC(getInstructionSize(value))
                        solved = True
# mode Implied
                    if not solved:
                        if opcode in IMPLIED_OPCODES:
                            value = getOpcodeValue(opcode, IMPLIED, line)
                            words[1].set(value)
                            pc = self.adjustPC(getInstructionSize(value))
                            solved = True
                    
                    if not solved:
                        # all opcodes without operand are done, it's a bad one 
                        if len(words) == 2:
                            printError("illegal opcode '%s'"%(opcode), line)
                            
# mode Accumulator
                    if not solved:
                        if nb_words == 3:
                            if words[2].getLabel().lower() == "a":
                                value = getOpcodeValue(opcode, ACCUMULATOR, line)
                                words[1].set(value)
                                pc = self.adjustPC(getInstructionSize(value))
                                solved = True
                                del words[2]
# mode Immediate
                    if not solved:
                        if nb_words >= 4:
                            if words[2].getLabel() == "#":
                                value = getOpcodeValue(opcode, IMMEDIATE, line)
                                words[1].set(value)
                                del words[2]
                                pc = self.adjustPC(getInstructionSize(value))
                                solved = True
# mode Indirect,X
                    if not solved:
                        if nb_words >= 7:
                            if words[-1].getLabel() == ")":
                                if words[-2].getLabel().lower() == "x":
                                    if words[-3].getLabel() == ",":
                                        if words[2].getLabel() == "(":
                                            value = getOpcodeValue(opcode, INDIRECTX, line)
                                            words[1].set(value)
                                            del words[2]
                                            del words[-1]
                                            del words[-1]
                                            del words[-1]
                                            pc = self.adjustPC(getInstructionSize(value))
                                            solved = True
# mode Indirect,Y
                    if not solved:
                        if nb_words >= 7:
                            if words[-1].getLabel().lower() == "y":
                                if words[-2].getLabel() == ",":
                                    if words[-3].getLabel() == ")":
                                        if words[2].getLabel() == "(":
                                            value = getOpcodeValue(opcode, INDIRECTY, line)
                                            words[1].set(value)
                                            del words[2]
                                            del words[-1]
                                            del words[-1]
                                            del words[-1]
                                            pc = self.adjustPC(getInstructionSize(value))
                                            solved = True
# mode Absolute,X & Zero Page,X - choice done when size of operand will be known
                    if not solved:
                        if nb_words >= 7:
                            if words[-1].getLabel().lower() == "x":
                                if words[-2].getLabel().lower() == ",":
                                        if words[2].getLabel() != "(":
                                            value = getOpcodeValue(opcode, ABSOLUTEX, line)
                                            words[1].set(value)
                                            del words[2]
                                            del words[-1]
                                            del words[-2]
                                            pc = self.adjustPC(getInstructionSize(value))
                                            solved = True
# mode Absolute,Y  & Zero Page,Y - choice done when size of operand will be known
                    if not solved:
                        if nb_words >= 7:
                            if words[-1].getLabel().lower() == "y":
                                if words[-2].getLabel().lower() == ",":
                                        if words[2].getLabel() != "(":
                                            value = getOpcodeValue(opcode, ABSOLUTEY, line)
                                            words[1].set(value)
                                            del words[2]
                                            del words[-1]
                                            del words[-2]
                                            pc = self.adjustPC(getInstructionSize(value))
                                            solved = True
# mode Indirect
                    if not solved:
                        if nb_words >= 5:
                            if words[-1].getLabel() == ")":
                                if words[2].getLabel() == "(":
                                    value = getOpcodeValue(opcode, INDIRECT, line)
                                    words[1].set(value)
                                    del words[2]
                                    del words[-1]
                                    pc = self.adjustPC(getInstructionSize(value))
                                    solved = True
# mode Absolute & Zero Page - choice done when size of operand will be known
                    if not solved:
                        if nb_words >= 2:
                            found_bad = False
                            for unknown_word in words[2:]:
                                if unknown_word.getLabel().lower in (',', 'x', 'y', 'a'):
                                    found_bad = True
                                    break
                            if not found_bad:
                                value = getOpcodeValue(opcode, ABSOLUTE, line)
                                words[1].set(value)
                                pc = self.adjustPC(getInstructionSize(value))
                                solved = True
                    if not solved:
                        printWarning("unsolved opcode %s"%opcode, line)

    def computeAffectations(self):
        # solve some affectations
        lines_to_solve = []
        for asm_line in self.__asm_lines:
            line = asm_line.getLine()
            words = asm_line.getWords()
            if len(words) == 4:
                if words[2].getLabel() == "=":
                    if words[3].isVariable():
                        variable = words[3].getVariable()
                        if words[3].isSolved():
                            words[1].setVariable(variable.get())
                            asm_line.setSolved()
                            del words[2]

                            


    def getCodeText(self):
        otext = EMPTY_STR
        for line in self.__asm_lines:
            otext += line.getCode()# + CHAR_LF
        return otext

    def getStatText(self):
        items = 0
        solved = 0
        for line in self.__asm_lines:
            for item in line.getWords():
                if item.getType() != TYPE_VOID:
                    items += 1
                    if item.isSolved():
                        solved += 1
        self.__percent = (float(solved) / float(items)) * 100.0
        return "%6.2f%% assembled (%d/%d)"%(self.__percent, solved, items)

    def getVariablesText(self):
        otext = EMPTY_STR
        keys = self.__variables.keys()
        keys.sort()
        for key in keys:
            otext += str(self.__variables[key]) + CHAR_LF
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
                    #~ print count, family
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

    ##################
    #                #
    # ASSEMBLER PART #
    #                #
    ##################

    # let's parse source file and clean it
    source = ASM_FILE(ap.getArgsDictionary())

    #~ source.assemble()
    writeln(source.getStatText())

    diskSave(buildName(ap.get('-ifname'), "asm_lines.asm"), source.getCodeText())
    diskSave(buildName(ap.get('-ifname'), "asm_words.asm"), str(source))
    diskSave(buildName(ap.get('-ifname'), "variables.asm"), source.getVariablesText())
