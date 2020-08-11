#!/usr/bin/python
# -*- coding: utf-8 -*-

import sys
import os

# if ROM
#       zp begins at zp
#       code begins at code start
#       rodata begins at code end
#       bss begins at ram start
#       data begins at bss end
# 
# if RAM
#       zp begins at zp
#       code begins at code start
#       rodata begins at code end
#       bss begins at rocode end
#       data begins at bss end

VERBOSE = False

VERSION = "0.99"
COMMENT_TAG = ";"
EMPTY_STR = ""
INCLUDE_KEYWORD = ".include"
CHAR_SPACE =' '
APP_NAME = os.path.splitext(os.path.basename(sys.argv[0]))[0]

ZP_KEYWORD = "zp"
CODE_KEYWORD = "code"
RODATA_KEYWORD = "rodata"
DATA_KEYWORD = "data"
BSS_KEYWORD = "bss"
SEGMENTS_NAMES = (ZP_KEYWORD, CODE_KEYWORD, RODATA_KEYWORD, DATA_KEYWORD, BSS_KEYWORD)

BYTE_KEYWORD = "byte"
WORD_KEYWORD = "word"
FLOAT_KEYWORD = "float"
LONG_KEYWORD = "long"
DATATYPES = (BYTE_KEYWORD, WORD_KEYWORD, FLOAT_KEYWORD, LONG_KEYWORD)

BYTE_SIZE = 1
WORD_SIZE = 2
FLOAT_SIZE = 6
LONG_SIZE = 4
DATASIZES = {BYTE_KEYWORD:BYTE_SIZE, WORD_KEYWORD:WORD_SIZE, FLOAT_KEYWORD:FLOAT_SIZE, LONG_KEYWORD:LONG_SIZE}

ROM = 1
RAM = 2

FIRST_CHAR = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"
OTHER_CHAR = FIRST_CHAR + "_0123456789"

def write(text):
    sys.stdout.write(str(text))
    
def writeln(text):
    write(text)
    write("\n")

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
    return "%s %s"%(COMMENT_TAG, text)

class SEGMENT():
    def __init__(self, name, start=0):
        self.__name = name
        self.__start = start
        self.__cursor = start
        
    def getName(self):
        return self.__name
        
    def addData(self, datatype):
        ret_val = self.__cursor
        self.__cursor += DATASIZES[datatype]
        return ret_val

    def getStart(self):
        return self.__start

    def setStart(self, value):
        self.__start = value

    def getCursor(self):
        return self.__cursor

    def setCursor(self, value):
        self.__cursor = value
        
    def __str__(self):
        return "<%s start=%d cursor=%d>\n"%(self.__name, self.__start, self.__cursor)

class SEGMENTS():
    def __init__(self):
        self.__segments = {}
        
    def addSegment(self, segment):
        self.__segments[segment.getName()] = segment
        
    def getSegment(self, name):
        if name in self.__segments.keys():
            return self.__segments[name]
        raise Exception('\nsegment "%s" not found!\n'%name)
            
    def __str__(self):
        text = EMPTY_STR
        keys = self.__segments.keys()
        keys.sort()
        for key in keys:
            text += self.__segments[key].__str__()
        return text

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
    labels = {}
    line_num = 1
    
    def __init__(self, fname=None, segments=None):
        if not os.path.isfile(fname):
            raise Exception("file \"%s\" not found"%fname)
        self.__fname = fname
        if segments == None:
            segments = SEGMENTS()
        self.__segments = segments
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
                            raise Exception("\n%sfile %s not found!\n"%(str(line), inc_fname))
                        SOURCE_FILE.lines.append(line)
                        # recursivity, seriously? :)
                        SOURCE_FILE(inc_fname, segments=segments)
                    else:
                        if VERBOSE:
                            writeln('Warning:file "%s" already included!'%inc_fname)

                elif word1 in (ZP_KEYWORD, CODE_KEYWORD, RODATA_KEYWORD, DATA_KEYWORD, BSS_KEYWORD):
                    # a variable declaration is detected, let's add some lines
                    line = SOURCE_LINE(fname, commentLine(text), num + 1)
                    segment_name = word1
                    datatype = word2
                    label = word3
                    if not datatype in (BYTE_KEYWORD, WORD_KEYWORD):
                        raise Exception('\n%sunknown datatype "%s"!\n'%(str(line), datatype))
                    if not labelIsOk(label):
                        raise Exception('\n%sbad label "%s"!\n'%(str(line), label))
                    if label in SOURCE_FILE.labels:
                        raise Exception('\n%slabel "%s" already defined!\n'%(str(line), label))
                    SOURCE_FILE.lines.append(line)
                    self.declareVariable(line, segment_name, datatype, label)
                    
                else:
                    # nothing special, let's add this "regular" line
                    SOURCE_FILE.lines.append(SOURCE_LINE(fname, text, num + 1))

    def declareVariable(self, old_line, segment_name, datatype, label):
        if not self.isLabelFree(label):
            raise Exception("\n%s\nlabel \"%s\" already declared!\n"%(str(old_line), label))
        value = self.getSegments().getSegment(segment_name).addData(datatype)
        fname = "<precompiler>"
        text = "    %s = %d"%(label, value)
        line = SOURCE_LINE(fname, text, self.getNextPrecompLineNum())
        SOURCE_FILE.lines.append(line)
        self.addLabel(label, value)

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
            text +=line.__str__()
        return text

def parse(fname, zp=0, code=0xc00, rodata=0, data=0x200, bss=0, model=ROM):
    if 1:
        writeln("fname  = %s"%fname)
        writeln("model  = %s"%["WTF", "ROM", "RAM"][model])
        writeln("zp     = %02x"%zp)
        writeln("code   = %04x"%code)
        writeln("rodata = %04x"%rodata)
        writeln("data   = %04x"%data)
        writeln("bss    = %04x"%bss)
        #~ sys.exit(12345)
    
    segments = SEGMENTS()
    for segment_name in SEGMENTS_NAMES:
        segments.addSegment(SEGMENT(segment_name))
    # PASS ONE
    source = SOURCE_FILE(fname, segments=segments)
    
    #~ # editing results
    #~ segments = source.getSegments()
    
    #~ seg = segments.getSegment(ZP_KEYWORD)
    #~ seg.setStart(zp)
    #~ seg.setCursor(0)
    
    #~ seg = segments.getSegment(ZP_KEYWORD)
    #~ seg.setStart(zp)
    #~ seg.setCursor(0)
    
    
    
    
    #~ # PASS TWO
    #~ source = SOURCE_FILE(fname, segments=segments)
    return source

    
if __name__ == "__main__":

    ifname = None
    ofname = None
    model = ROM
    for num, arg in enumerate(sys.argv):
        if arg == "-ifname" or arg == "-ofname":
            if (num + 1) < len(sys.argv):
                fname = sys.argv[num+1]
                if arg == "-ifname":
                    if not os.path.isfile(fname):
                        raise Exception("file \"%s\" not found"%fname)
                    ifname = fname
                elif arg == "-ofname":
                    ofname = fname
                continue
            else:
                raise Exception("bad argument(s)!")
        if arg == "-version":
            writeln("%s - version %s"%(APP_NAME, VERSION))
            sys.exit(0)
        if arg == "-verbose":
            VERBOSE = True
        if arg == "-ram":
            model = ram
    
    if ifname == None or ofname == None:
        raise Exception ("\n missing argument(s)!\n")
   
    source = parse(ifname, model=model)
    
    segments = source.getSegments()
    for segment_name in SEGMENTS_NAMES:
        write(segments.getSegment(segment_name))
    write(source.listLabels())

    #~ write(source.getOutputSource())
    #~ write(source.getSegments())
    #~ write(source)
    source.saveOutputSource(ofname)

