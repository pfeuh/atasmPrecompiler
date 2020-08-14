#!/usr/bin/python
# -*- coding: utf-8 -*-

import sys
import os

VERSION = "0.99"
MEMORY_SIZE = 0x10000
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
    if line != None:
        writeln('File "%s", line %d, error : %s'%(line.getFname(), line.getNum(), message))
        writeln(line.getText())
    else:
        writeln('error : %s'%(message))
    sys.exit(1)

class ARGUMENT():
    
    def raiseError(self, message):
        sys.stdout.write("Error - %s!\n", message)
        sys.exit(1)

    def raiseWarning(self, message):
        sys.stdout.write("Warning - %s!\n", message)

    def __init__(self, aname, atype=bool, check_minus=False, check_file=False, family=None, mandatory=False):
        self.__aname = aname
        if not atype in (int, bool, str):
            raise Exception("not implemented argument type %s !"%type(atype))
        self.__atype = atype
        self.__avalue = False
        self.__check_minus = check_minus != False
        self.__check_file = check_file != False
        self.__mandatory = mandatory
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
        
    def isMandatory(self):
        return self.__mandatory
        
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
    
    def raiseError(self, message):
        sys.stdout.write("Error - %s!\n", message)
        sys.exit(1)

    def raiseWarning(self, message):
        sys.stdout.write("Warning - %s!\n", message)

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
        
        # if argument is mandatory, it must in the parsed list
        not_found_list = []
        for aname in self.__args.keys():
            if self.getArgument(aname).isMandatory():
                if not aname in self.__processed:
                    not_found_list.append(aname)
        if len(not_found_list):
            printError("mandatory argument(s) missing : %s"%" ".join(not_found_list))
        
        # if an args name starts with '-W', it has to be set
        # only if '-Wall' is set and 'warning_all' is set
        if self.__warning_all:
            if not "-Wall" in self.__args.keys():
                self.raiseError("no argument '-Wall' declared but 'warning_all' is True!" )
            if self.getArgument("-Wall").get():
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

def readLabels(fname, verbose=False, check_lbl=False):
    dictionary = {}
    fp = open(fname, "r")
    for line in fp.readlines():
        words = line.split()
        dictionary[words[1].lower()] = int(words[0], 16)
    if verbose:
        writeln("%s $%04x labels read"%(fname, len(dictionary)))
    return dictionary

def readWord(fp):
    lo = fp.read(1)
    hi = fp.read(1)
    if hi == "" or lo == "":
        return None
    else:
        return ord(lo) + ord(hi) * 256

def readAtariBinFile(fname, verbose=False, check_eof=False):
    fp = open(fname, 'rb')
    magic_word = readWord(fp)
    if magic_word == None:
        raise Exception("unexpected end of file '%s'!'"%fname)
    if magic_word != 0xffff:
        raise Exception("file '%s' is not an Atari file!"%fname)
    first = readWord(fp)
    last = readWord(fp)
    if first != None and last != None:
        if verbose:
            writeln("%s <$%04x:$%04x> $%d bytes"%(fname, first, last, 1 - first + last))
        binary_code = [ord(car) for car in fp.read(last - first + 1)]
    else:
        raise Exception("unexpected end of file '%s'!'"%fname)
    dummy = fp.read(1)
    if dummy != EMPTY_STR:
        if check_eof:
            printWarning("there are some other bytes in file '%s'!'"%fname)
            
    return binary_code, first, last

def makeROM(ap):
    verbose=ap.get('-verbose')
    ifname = ap.get('-ifname')
    lfname = ap.get('-lfname')
    check_lbl = ap.get('-Wlbl')
    fill_byte = ap.get('-fb')
    rname = ap.get('-rfname')
    
    # collecting data
    body, start, last = readAtariBinFile (ifname, verbose=verbose)
    labels = readLabels(lfname, verbose=verbose, check_lbl=check_lbl)
    
    for item in REQUIRED_LABELS:
        if not item in labels:
            writeln("label '%s' not found"%item)
    
    fill_byte = ap.get('-fb')
    for addr in range(last+1, MEMORY_SIZE):
        body.append(fill_byte)
    if verbose:
        writeln("$%04x free bytes filled with $%02x"%(MEMORY_SIZE - len(body) - 6, fill_byte))
        
    if verbose:
        writeln("ROM at $%04x - size $%04x used bytes"%(labels['source_start'], len(body)))
    
    vectors = (("nmi", -6, 'main'), ("run", -4, 'main'), ("irq", -6, 'irq'))
    for vector in vectors:
        label = vector[2]
        value = labels[label]
        addr =  vector[1]
        vector_name = vector[0]
        if verbose:
            writeln("setting vector %s ($%04x) with address of %s ($%04x)"%(vector_name, MEMORY_SIZE - addr, label, value))
        body[addr] = value & 0xff
        body[addr + 1] = value / 0x100
        
    
    with open(rname, "wb") as fp:
        for byte in body:
            fp.write(chr(byte))
    
    if verbose:
        writeln("ROM written as %s"%(rname))
    
    for index, byte in enumerate(body):
        if not (index % 16):
            write("%04x"%(0xf000 + index))
        write(" %02x"%body[index])
        if (index % 16) == 15:
            write("\n")
        
        
        
        
        
        
        
#~ * = $fffa ; nmi vector
#~ .word nmi_in

#~ * = $fffc ; run vector
#~ .word main

#~ * = $fffe ; irq vector
#~ .word irq_in
 
    

if __name__ == "__main__":


    ap = ARGUMENTS(warning_all=True)
    ap.addArgument(ARGUMENT('-verbose')) # blablabla...
    ap.addArgument(ARGUMENT('-Wall'))    # set all warnings
    ap.addArgument(ARGUMENT('-W eof'))    # warning end of file expected, but there are still some bytes
    ap.addArgument(ARGUMENT('-Wlbl'))    # a label is missing
    ap.addArgument(ARGUMENT('-ifname', str, check_minus=True, check_file=True, mandatory=True))  # input file to assemble
    ap.addArgument(ARGUMENT('-lfname', str, check_minus=True, check_file=True, mandatory=True))  # input label file
    ap.addArgument(ARGUMENT('-rfname', str, check_minus=True, mandatory=True))  # output ROM file
    ap.addArgument(ARGUMENT('-fb', int, ))  # value for filling unused bytes of ROM

    sys.argv = (sys.argv[0], '-ifname', 'monitor.bin', '-verbose', '-rfname', 'MONITOR', '-lfname', 'monitor.lbl', '-Wall', '-fb', '0xff')

    ap.parse(sys.argv)
    
    makeROM(ap)