#!/usr/bin/python
# -*- coding: utf-8 -*-

import sys
import os

# arguments
VERBOSE = False
DEBUG = False
WARN_ALL = False
WARN_EQU = False # include already done
WARN_STR = False # \x00 in a string
WARN_LAB = False # a label is missing
IFNAME = None
OFNAME = None
TFNAME = None
NB_COLS = 16

VERSION = "0.99"
COMMENT_TAG = ";"
EMPTY_STR = ""
INCLUDE_KEYWORD = ".include"
CHAR_SPACE =' '
CHAR_EOS = chr(0)
CHAR_QUOTE = '"'
CHAR_ANTISLASH = "\\"
CHAR_UNDERSCORE = "_"

APP_NAME = os.path.splitext(os.path.basename(sys.argv[0]))[0]

KEYWORD_STRING = ".string"
KEYWORD_CH_ARRAY = ".ch_array"
PRECOMP_KEYWORDS = (KEYWORD_STRING, KEYWORD_CH_ARRAY)
KEYWORD_MAIN = "main"
KEYWORD_IRQ = "irq"
KEYWORD_NMI = "nmi"
KEYWORD_SOURCE_END = "source_end"
REQUIRED_LABELS = (KEYWORD_MAIN, KEYWORD_IRQ, KEYWORD_NMI,KEYWORD_SOURCE_END)

FIRST_CHAR = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz_"
OTHER_CHAR = FIRST_CHAR + "0123456789"
NO_LABEL_FIRST_CHAR = " ;"

def write(text):
    sys.stdout.write(str(text))
    
def writeln(text):
    write(text)
    write("\n")

def printWarning(message, line=None):
    if line != None:
        writeln('File "%s", line %d, warning : %s'%(line.getFname(), line.getNum(), message))
        writeln(line.getText())
    
def printError(message, line=None):
    if DEBUG:
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

def removeComment(text):
    otext = EMPTY_STR
    out_str = 1
    in_str = 2
    mode = out_str
    for position, car in enumerate(text):
        if mode == out_str:
            if car == CHAR_QUOTE:
                otext += car
                mode = in_str
            elif car == COMMENT_TAG:
                return otext.rstrip()
            else:
                otext += car
        elif mode == in_str:
            if car == CHAR_QUOTE:
                otext += car
                mode = out_str
            else:
                otext += car
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
    if text.startswith(COMMENT_TAG):
        return text
    elif text.startswith(CHAR_SPACE):
        return "%s%s"%(COMMENT_TAG, text)
    else:
        # don't comment all the line if it begins with a label
        found = False
        ret_text = EMPTY_STR
        for car in text:
            if found:
                ret_text += car
            else:
                if not car in (CHAR_SPACE, COMMENT_TAG):
                    ret_text += car
                else:
                    if car == COMMENT_TAG:
                        ret_text +=" %s "%COMMENT_TAG
                        found = True
        return ret_text

class SOURCE_LINE():
    def __init__(self, fname, text, num):
        assert type(fname) == str
        assert type(text) == str
        assert type(num) == int
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

class SOURCE_FILE():
    lines = []
    fnames = []
    line_num = 1
    __labels = {}
    
    def __init__(self, fname=None):
        self.parseFile(fname)
    
    def parseFile(self, fname):
        if not os.path.isfile(fname):
            raise Exception("file \"%s\" not found"%fname)
        self.__fname = fname
        SOURCE_FILE.fnames.append(fname)
        with open(fname, "r") as fp:
            print fname
            lines = getFileLines(fp)
            print lines
            for num, text in enumerate(lines):
                self.parseLine(fname, text, num)
                
        # some labels are mandatory to build a ROM
        #~ for label in REQUIRED_LABELS:
            #~ if not label in SOURCE_FILE.__labels:
                #~ writeln("label %s not found"%label)
                #~ if WARN_LAB:
                    #~ printWarning("label %s not found"%label)

    def parseLine(self, fname, text, num):
        word = extractWord(text, 1)
        print word
        if word == INCLUDE_KEYWORD :
            
            self.includeFname(line, extractWord(text, 2, lower=False))
        
        
        
        
        
    def includeFname(self, line, fname):
        writeln("include now file %s"%fname)
        

    def getLabels(self):
        labels = SOURCE_FILE.__labels.keys()
        labels.sort()
        return labels
        
    def printLabels(self):
        keys = SOURCE_FILE.__labels.keys()
        keys.sort()
        for key in keys:
            line = SOURCE_FILE.__labels[key]
            writeln("%-16s %-16s %3d %s"%(key, line.getFname(), line.getNum(), line.getText()))

    def getOutputSource(self):
        text = EMPTY_STR
        for line in SOURCE_FILE.lines:
            text += line.getText() + "\n"
        return text
                        
    def saveOutputSource(self, fname):
        open(fname, "w").write(self.getOutputSource())
                        
    def __str__(self):
        text= EMPTY_STR
        for line in SOURCE_FILE.lines:
            text += line.__str__()
        return text
        
    def saveTrace(self, fname):
        fp = open(fname, "w")
        fp.write(self.__str__())
        fp.close()

def checkNextParameter(index, label):
    if index < len(sys.argv) -1:
        arg = sys.argv[index + 1]
        if not arg.startswith("-"):
            return arg
    raise Exception("bad or missing argument for %s !"%label)

def checkNextValue(index, label):
    text = checkNextParameter(index, label)
    try:
        value = int(text)
    except:
        raise Exception("bad or missing hex value for %s !"%label)
    return value
    
def chekFile(fname):
    if not os.path.isfile(fname):
        raise Exception("file \"%s\" not found"%fname)

def parseArguments():
    global VERBOSE
    global DEBUG
    global WARN_ALL
    global WARN_EQU
    global MODEL
    global IFNAME
    global OFNAME
    global TFNAME
    global NB_COLS
    global WARN_STR
    global WARN_LAB
    
    index = 1
    ignored_paremeters = []
    processed = []
    
    while 1:
        arg = sys.argv[index]
        if arg in processed:
            raise Exception("argument \"%s\" already processed!\n"%arg)
        else:
            processed.append(arg)
            
        if arg == "-ifname":
            IFNAME = checkNextParameter(index, arg)
            chekFile(IFNAME)
            index += 1
        elif arg == "-ofname":
            OFNAME = checkNextParameter(index, arg)
            chekFile(OFNAME)
            index += 1
        elif arg == "-tfname":
            TFNAME = checkNextParameter(index, arg)
            index += 1
        elif arg == "-nb_cols":
            NB_COLS = checkNextValue(index, arg)
            index += 1
        elif arg == "-version":
            writeln("%s - version %s"%(APP_NAME, VERSION))
            # if there is a calling script, it should stop, no precompilation done,
            # only display version ant then stop, so let's return an error 
            sys.exit(1)
        elif arg == "-verbose":
            VERBOSE = True
        elif arg == "-debug":
            DEBUG = True
        elif arg == "-Wall":
            WARN_ALL = True
        elif arg == "-Wequ":
            WARN_EQU = True
        elif arg == "-Wstr":
            WARN_STR = True
        elif arg == "-Wlab":
            WARN_LAB = True
        else:
            ignored_paremeters.append(arg)
        index+=1
        if index >= len(sys.argv):
            break
    
    if WARN_ALL:
        WARN_EQU = True
        WARN_STR = True
        WARN_LAB = True

    if VERBOSE:
        writeln("-version %s"%(VERSION))
        writeln("-verbose %s"%(VERBOSE))
        writeln("-debug   %s"%(DEBUG))
        writeln("-Wall    %s"%(WARN_ALL))
        writeln("-Wequ    %s"%(WARN_EQU))
        writeln("-Wstr    %s"%(WARN_STR))
        writeln("-Wlab    %s"%(WARN_LAB))
        writeln("-ifname  %s"%(IFNAME))
        writeln("-ofname  %s"%(OFNAME))
        writeln("-tfname  %s"%(TFNAME))
        writeln("-nb_cols %s"%(NB_COLS))
        for arg in ignored_paremeters:
            writeln("ignored parameter \"%s\""%arg)
        writeln("--------------------------")

if __name__ == "__main__":

    sys.argv = ('precompile.py', '-Wlab', '-ifname',\
    'monitor.asm', '-ofname', 'precompiled.asm','-tfname', 'full_prec.asm', '-nb_cols', '13') 

    parseArguments()
    
    source = SOURCE_FILE(IFNAME)
    
    #~ labels = source.getLabels()
    #~ labels.sort()
    #~ for label in labels:
        #~ writeln(label)
    #~ source.printLabels()
    
    if OFNAME != None:
        source.saveOutputSource(OFNAME)

    if TFNAME != None:
        source.saveTrace(TFNAME)

