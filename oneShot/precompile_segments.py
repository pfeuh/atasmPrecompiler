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

ROM = 1
RAM = 2

# arguments
VERBOSE = False
WARNING = False
MODEL = ROM
IFNAME = None
OFNAME = None
TFNAME = None
CODE_START = 0xf000
RAM_START = 0x0200
ZP_START = 0x0000

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

FIRST_CHAR = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz_"
OTHER_CHAR = FIRST_CHAR + "0123456789"

def write(text):
    sys.stdout.write(str(text))
    
def writeln(text):
    write(text)
    write("\n")

def printWarning(message, line):
    writeln(line)
    writeln("Warning:%s - %s"%message, str(line))
    
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

    def getSize(self):
        return self.__cursor - self.__start

    def setCursor(self, value):
        self.__cursor = value
        
    def reset(self, value):
        self.__cursor = value
        self.__start = value
        
    def __str__(self):
        return "<%-08s start=$%04x size=$%x bytes>\n"%(self.__name, self.__start, self.__cursor - self.__start)

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
    
    def reset(self):
        SOURCE_FILE.lines = []
        SOURCE_FILE.fnames = []
        SOURCE_FILE.labels = {}
        SOURCE_FILE.line_num = 1
    
    def __init__(self, fname=None, segments=None, reset=False):
        if reset:
            self.reset()
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
                        if WARNING:
                            printWarning('file "%s" already included'%inc_fname)

                elif word1 in SEGMENTS_NAMES:
                    # a variable declaration is detected, let's add some lines
                    line = SOURCE_LINE(fname, commentLine(text), num + 1)
                    segment_name = word1
                    datatype = word2
                    label = word3
                    if not datatype in DATATYPES:
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
        fname = "---*** precompiler ***---"
        if segment_name == RODATA_KEYWORD:
            text = "%s * = * + %d"%(label, value)
        else:
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
            text += line.__str__()
        return text
        
    def saveTrace(self, fname):
        fp = open(fname, "w")
        fp.write(self.__str__())
        fp.close()

def getNewSegments():
    segments = SEGMENTS()
    for segment_name in SEGMENTS_NAMES:
        segments.addSegment(SEGMENT(segment_name))
    return segments

def parse(fname, zp_start=0, code_start=0xc00, ram_start=0x200, rom_start=0xf000, model=ROM):
    if VERBOSE:
        writeln("parse(...) parameters:")
        writeln("    fname      = %s"%fname)
        writeln("    model      = %s"%["WTF", "ROM", "RAM"][model])
        writeln("    zp_start   =   %02x"%zp_start)
        writeln("    code_start = %04x"%code_start)
        writeln("    ram_start  = %04x"%ram_start)
        writeln("    rom_start  = %04x"%rom_start)
        #~ sys.exit(12345)
    
    segments = getNewSegments()

    # PASS ONE
    if VERBOSE:
        writeln("pass ONE started")
    source = SOURCE_FILE(fname, segments=segments)
    if VERBOSE:
        writeln(segments)

    # computing segments stuff
    segments2 = getNewSegments()
    segments2.getSegment(ZP_KEYWORD).reset(zp_start)    
    #~ if model == ROM:
        #~ cursor = 
        #~ size = segments.getSegment(CODE_KEYWORD).getSize()
        #~ segments.getSegment(CODE_KEYWORD).getAndReset(code_start)
        
        #~ cursor = segments.getSegment(RODATA_KEYWORD).getAndReset(cursor)
        #~ cursor = segments.getSegment(BSS_KEYWORD).getAndReset(ram_start)
        #~ cursor = segments.getSegment(DATA_KEYWORD).getAndReset(cursor)
    #~ if model == RAM:
        #~ cursor = segments.getSegment(CODE_KEYWORD).getAndReset(code_start)
        #~ cursor = segments.getSegment(BSS_KEYWORD).getAndReset(cursor)
        #~ cursor = segments.getSegment(RODATA_KEYWORD).getAndReset(cursor)
        #~ cursor = segments.getSegment(DATA_KEYWORD).getAndReset(cursor)
    
    source = None
    segments = None
    
    # PASS TWO
    if VERBOSE:
        writeln("pass TWO started")
    source2 = SOURCE_FILE(fname, segments=segments2, reset=True)
    if VERBOSE:
        writeln(segments2)
    return source2

def checkNextParameter(index, label):
    if index < len(sys.argv) -1:
        arg = sys.argv[index + 1]
        if not arg.startswith("-"):
            return arg
    raise Exception("bad or missing argument for %s !"%label)

def checkNextValue(index, label):
    text = checkNextParameter(index, label)
    try:
        value = int(text, 16)
    except:
        raise Exception("bad or missing hex value for %s !"%label)
    return value
    
def chekFile(fname):
    if not os.path.isfile(fname):
        raise Exception("file \"%s\" not found"%fname)

def parseArguments():
    global VERBOSE
    global WARNINGS
    global MODEL
    global IFNAME
    global OFNAME
    global TFNAME
    global CODE_START
    global RAM_START
    global ZP_START
    
    index = 1
    ignored_paremeters = []
    processed = []
    
    while 1:
        arg = sys.argv[index]
        if arg in processed:
            raise Exception("argument \"%s\" alread processed!\n"%arg)
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
        elif arg == "-version":
            writeln("%s - version %s"%(APP_NAME, VERSION))
            # if there is a calling script, it should stop, no precompilation done
            # so let's return an error 
            sys.exit(1)
        elif arg == "-verbose":
            VERBOSE = True
        elif arg == "-ram":
            if "-rom" in processed:
                raise Exception("argument \"-rom/ram\" alread processed!\n")
            MODEL = RAM
        elif arg == "-rom":
            if "-ram" in processed:
                raise Exception("argument \"-rom/ram\" alread processed!\n")
            MODEL = ROM
        elif arg == "-Wall":
            WARNINGS = True
        elif arg == "-zp":
            ZP_START = checkNextValue(index, arg)
            index += 1
        elif arg == "-code":
            CODE_START = checkNextValue(index, arg)
            index += 1
        else:
            ignored_paremeters.append(arg)
        index+=1
        if index >= len(sys.argv):
            break
            
    if VERBOSE:
        writeln("%-16s %s"%("VERBOSE", VERBOSE))
        writeln("%-16s %s"%("VERSION", VERSION))
        writeln("%-16s %s"%("WARNINGS", WARNINGS))
        writeln("%-16s %s"%("MODEL", ["WTF", "ROM", "RAM"][MODEL]))
        writeln("%-16s %s"%("IFNAME", IFNAME))
        writeln("%-16s %s"%("OFNAME", OFNAME))
        writeln("%-16s %s"%("TFNAME", TFNAME))
        writeln("%-16s %04x"%("CODE_START", CODE_START))
        writeln("%-16s %04x"%("RAM_START", RAM_START))
        writeln("%-16s %04x"%("ZP_START", ZP_START))
        for arg in ignored_paremeters:
            writeln("ignored parameter \"%s\""%arg)

if __name__ == "__main__":

    sys.argv = ('precompile.py','-rom', '-zp', '26', '-code', 'f000', '-Wall', '-ifname',\
    'monitor.asm', '-ofname', 'precompiled.asm', '-verbose','-tfname', 'debug.txt') 
    #~ writeln(sys.argv)
    parseArguments()
    #~ sys.exit()
    
    source = parse(IFNAME, model=MODEL, zp_start=ZP_START, code_start=CODE_START, ram_start=RAM_START)
    
    if OFNAME != None:
        source.saveOutputSource(OFNAME)

    if TFNAME != None:
        source.saveTrace(TFNAME)

