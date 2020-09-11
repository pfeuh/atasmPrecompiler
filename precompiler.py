#!/usr/bin/python
# -*- coding: utf-8 -*-

import sys
import os

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

def write(text):
    sys.stdout.write(str(text))
    
def writeln(text):
    write(text)
    write("\n")

def printLink(message, line=None):
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
        # the goal is to trig an error, then it's possible to follow the white rabbit
        1/0
    writeln('File "%s", line %d, error : %s'%(line.getFname(), line.getNum(), message))
    writeln(line.getText())
    sys.exit(1)

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
            elif (car == CHAR_SINGLE_QUOTE) or (car == CHAR_QUOTE):
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
                    
    # whole line is parser, last check:
    if mode != mode_normal:
        if line == None:
            raise Exception("string not closed!")
        else:
            printError("string not closed!")
    return otext
    
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

class PRECOMPILED_FILE():
    def __init__(self, fname=None, nb_cols=16, w_equ=False, w_str=False, w_lbl=False):
        self.__fname = fname
        self.__nb_cols = nb_cols
        self.__w_equ = w_equ
        self.__w_str = w_str
        self.__w_lbl = w_lbl
        self.__lines = []
        self.__fnames = []
        self.__line_num = 1
        self.__labels = {}
        if type(fname) != str:
            printError("no source file is defined!", SOURCE_LINE("", CHAR_SPACE.join(sys.argv), 0))
        if not os.path.isfile(fname):
            printError("file \"%s\" not found"%inc_fname, SOURCE_LINE(fname, CHAR_SPACE.join(sys.argv), 0))
        self.parseFile(fname)
    
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
        #~ text = self.getOutputSource()
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
                    print count, family
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
        raise Exception(message)

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

    #~ sys.argv = ('precompile.py', '-ifname',\
    #~ 'monitor.asm', '-ofname', 'precompiled.asm',\
    #~ '-dfname', 'full_prec.asm', '-nb_cols', '7',\
    #~ '-lfname', 'prelabels.txt', '-Wall') 

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
    ap.set('-nb_cols', 16)
    media = ('-ram', '-rom', '-cartridge', )
    ap.addArgument(ARGUMENT('-ram', family=media))  # number of columns of the bytes generator
    ap.addArgument(ARGUMENT('-rom', family=media))  # number of columns of the bytes generator
    ap.addArgument(ARGUMENT('-cartridge', family=media))  # number of columns of the bytes generator

    ap.parse(sys.argv)
    
    source = PRECOMPILED_FILE(ap.get('-ifname'), nb_cols=ap.get('-nb_cols'), w_equ=ap.get('-Winc'), w_str=ap.get('-Wstr'), w_lbl=ap.get('-Wlbl'))
    
    ofname = ap.get('-ofname')
    if ofname != None:
        # saving the precompiled source file (all source files merged)
        source.saveOutputSource(ofname)

    dfname = ap.get('-dfname')
    if dfname != None:
        # saving the debug file (same as precompiled but with more info)
        source.saveDebug(dfname)
        
    lfname = ap.get('-lfname')
    if lfname != None:
        # saving the labels file
        source.saveLabels(lfname)
        
