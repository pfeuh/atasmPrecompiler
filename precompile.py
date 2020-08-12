#!/usr/bin/python
# -*- coding: utf-8 -*-

import sys
import os

# arguments
VERBOSE = False
WARN_ALL = False
WARN_EQU = False # include already done
WARN_STR = False # \x00 in a string
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
APP_NAME = os.path.splitext(os.path.basename(sys.argv[0]))[0]

KEYWORD_STRING = ".string"
KEYWORD_CH_ARRAY = ".ch_array"
PRECOMP_KEYWORDS = (KEYWORD_STRING, KEYWORD_CH_ARRAY)

FIRST_CHAR = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz_"
OTHER_CHAR = FIRST_CHAR + "0123456789"

def write(text):
    sys.stdout.write(str(text))
    
def writeln(text):
    write(text)
    write("\n")

def printWarning(message, line):
    writeln('File "%s", line %d, warning : %s'%(line.getFname(), line.getNum(), message))
    writeln(line.getText())
    
def printError(message, line=None):
    writeln('File "%s", line %d, error : %s'%(line.getFname(), line.getNum(), message))
    writeln(line.getText())
    sys.exit(1)

def getvalidText(text):
    line = EMPTY_STR
    for car in text:
        if car == COMMENT_TAG:
            break
        else:
            line += car
    return line

def getFileLines(fp):
    return [line.rstrip() for line in fp.readlines()]
    
def hasPattern(line, pattern):
    if " %s "%pattern in text.lower():
        return True
    else:
        return False

def labelIsOk(label):
    if not len(label):
        return False
    if not label[0] in FIRST_CHAR:
        return False
    for car in label[1:]:
        if not car in OTHER_CHAR:
            return False
    return True

def extractWord(text, word_number, lower=True):
    if text.startswith(CHAR_SPACE):
        text = ".%s"%text
    words = text.split()
    if word_number < len(words):
        word = words[word_number]
        if lower:
            word = word.lower()
        return word

def commentLine(text):
    if text.startswith(CHAR_SPACE):
        return "%s %s"%(COMMENT_TAG, text)
    else:
        # don't comment all the line if it begins with a label
        found = False
        ret_text = EMPTY_STR
        for car in text:
            if found:
                ret_text += car
            else:
                if car != CHAR_SPACE:
                    ret_text += car
                else:
                    ret_text +=" ; "
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

    def getNum(self):
        return self.__num
        
    def __str__(self):
        return "%-40s %s\n"%("%s#%d"%(self.__fname, self.__num), self.__text)

class SOURCE_FILE():
    lines = []
    fnames = []
    line_num = 1
    
    def __init__(self, fname=None):
        if not os.path.isfile(fname):
            raise Exception("file \"%s\" not found"%fname)
            
        self.__fname = fname
        SOURCE_FILE.fnames.append(fname)
        with open(fname, "r") as fp:
            lines = getFileLines(fp)
            for num, text in enumerate(lines):
                word1 = extractWord(text, 1)
                word2 = extractWord(text, 2)
                word3 = extractWord(text, 3)
                if word1 == INCLUDE_KEYWORD :
                    # keyword ".include" is detected, let's include the new file
                    line = SOURCE_LINE(fname, commentLine(text), num + 1)
                    inc_fname = extractWord(text, 2, lower=False)
                    if not inc_fname in SOURCE_FILE.fnames:
                        if not os.path.isfile(inc_fname):
                            printError("file \"%s\" not found"%inc_fname, SOURCE_LINE(fname, text, num + 1))
                        SOURCE_FILE.lines.append(line)
                        # recursivity, seriously? :)
                        SOURCE_FILE(inc_fname)
                    else:
                        if WARN_EQU:
                            printWarning('file "%s" already included'%inc_fname, SOURCE_LINE(fname, text, num + 1))

                elif word1 in PRECOMP_KEYWORDS:
                    #a precompiler's keyword is detected, let's add some code
                    line = SOURCE_LINE(fname, commentLine(text), num + 1)                    
                    SOURCE_FILE.lines.append(line)
                    
                    if word1 == KEYWORD_STRING:
                        self.addString(text, word1, SOURCE_LINE(fname, text, num + 1), oes=True)
                    elif word1 == KEYWORD_CH_ARRAY:
                        self.addString(text, word1, SOURCE_LINE(fname, text, num + 1), oes=False)
                    
                else:
                    # nothing special, let's add this "regular" line
                    SOURCE_FILE.lines.append(SOURCE_LINE(fname, text, num + 1))

    def addString(self, text, key_word, line, oes=True):
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
        
        # setting difference between string and ch_array (no end of string)
        if oes:
            if chr(0) in btext:
                if WARN_STR:
                    printWarning("there is a \\x00 (enf of string) in this line:", line)
            btext += CHAR_EOS
        
        self.buildMatrix( btext)

    def buildMatrix(self, text):

        # lets build the matrix
        position = 0
        last = len(text) - 1

        words = []
        for position, car in enumerate(text):
            byte = ord(text[position])
            if position % NB_COLS == 0:
                string_txt = "    .byte "
                
            words.append("$%02x"%byte)
            
            if (position % NB_COLS) == (NB_COLS - 1):
                string_txt += ", ".join(words)
                self.addPrecompilerLine(string_txt)
                words = []
                
        if len(words):
            string_txt += ", ".join(words)
            self.addPrecompilerLine(string_txt)

    def addPrecompilerLine(self, text):
        line = SOURCE_LINE("<precompiler>", text, self.getNextPrecompLineNum())
        SOURCE_FILE.lines.append(line)

    def isLabelFree(self, label):
        return not label in SOURCE_FILE.labels.values()

    def addLabel(self, label, value):
        SOURCE_FILE.labels[value] = label

    def listLabels(self):
        keys = SOURCE_FILE.labels.keys()
        keys.sort()
        text = EMPTY_STR
        for key in keys:
            text += "%04x %s\n"%(key, SOURCE_FILE.labels[key])
        return text

    def getSegments(self):
        return self.__segments

    def getNextPrecompLineNum(self):
        ret_val = SOURCE_FILE.line_num
        SOURCE_FILE.line_num += 1
        return ret_val

    def getOutputSource(self):
        text = EMPTY_STR
        for line in SOURCE_FILE.lines:
            text += line.getText() + "\n"
        return text
                        
    def saveOutputSource(self, fname):
        text = self.getOutputSource()
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

def parse(fname):
    if VERBOSE:
        writeln("parse(...) parameters:")
        writeln("    fname      = %s"%fname)
        
    source = SOURCE_FILE(fname)
    
    return source

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
    global WARN_ALL
    global WARN_EQU
    global MODEL
    global IFNAME
    global OFNAME
    global TFNAME
    global NB_COLS
    global WARN_STR
    
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
        elif arg == "-Wall":
            WARN_ALL = True
        elif arg == "-Wequ":
            WARN_EQU = True
        elif arg == "-Wstr":
            WARN_STR = True
        else:
            ignored_paremeters.append(arg)
        index+=1
        if index >= len(sys.argv):
            break
    
    if WARN_ALL:
        WARN_EQU = True
        WARN_STR = True
    
    
    if VERBOSE:
        writeln("-verbose %s"%(VERBOSE))
        writeln("-version %s"%(VERSION))
        writeln("-Wall    %s"%(WARN_ALL))
        writeln("-Wequ    %s"%(WARN_EQU))
        writeln("-Wstr    %s"%(WARN_STR))
        writeln("-ifname  %s"%(IFNAME))
        writeln("-ofname  %s"%(OFNAME))
        writeln("-tfname  %s"%(TFNAME))
        writeln("-nb_cols %s"%(NB_COLS))
        for arg in ignored_paremeters:
            writeln("ignored parameter \"%s\""%arg)

if __name__ == "__main__":

    #~ sys.argv = ('precompile.py', 'chachacha', '-ifname',\
    #~ 'monitor.asm', '-ofname', 'precompiled.asm','-tfname', 'full_prec.asm', '-nb_cols', '13') 

    parseArguments()
    
    source = parse(IFNAME)
    
    if OFNAME != None:
        source.saveOutputSource(OFNAME)

    if TFNAME != None:
        source.saveTrace(TFNAME)

