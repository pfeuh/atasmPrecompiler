#!/usr/bin/python
# -*- coding: utf-8 -*-

import sys
import os

TYPE_VOID = 0
TYPE_VARIABLE = 1
TYPE_COMMAND = 2
TYPE_MNEMO = 3
TYPE_KEYWORD = 4
TYPE_PONCTUATION = 5
TYPE_STRING = 6
TYPE_NAME = {None:"None", TYPE_VOID:'void', TYPE_VARIABLE:'variable', TYPE_COMMAND:'command', TYPE_MNEMO:'mnemo', TYPE_KEYWORD:'keyword', TYPE_PONCTUATION:'ponct',TYPE_STRING:'string'}

def write(text):
    sys.stdout.write(str(text))
    
def writeln(text):
    write(text)
    write("\n")

class WORD():
    def __init__(self, label, wtype, value=None):
        assert type(label) == str
        self.__text = label
        self.__wtype = None
        if value != None and wtype != TYPE_VARIABLE:
            raise Exception("unexpected value '%s' for type %s"%(value, TYPE_NAME[wtype]))
        self.__value = value

    def isSolved(self):
        if self.__wtype == TYPE_VARIABLE:
            return self.__value != None

    def getLabel(self):
        return self.__text

    def getType(self):
        return self.__wtype

    def setType(self, wtype):
        self.__wtype = wtype

    def get(self):
        return self.__value

    def set(self, value):
        self.__value = value

    def isVariable(self):
        return self.__wtype == TYPE_VARIABLE

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
        pass

def buildLine(words):
    text = ""
    for word in words:
        if word.isVariable():
            if word.isSolved():
                text += word.getValue()
        else:
            text += word.getLabel()
        text += " "
    return text

def solveLines(lines):
    error = True
    nb_loops = 0
    while error:
        error = False
        for line in lines:
            expression = buildLine(line)
            write("%-20s"%expression)
            try:
                exec(expression)
                writeln('+')
            except:
                writeln('-')
                error= True
            if not error:
                value = eval(line[0].getLabel())
                writeln("setting %s to %d"%(line[0].getLabel(), value))
                line[0].set(value)
        nb_loops += 1
        if nb_loops > 6:
            break
    #all variables should be solved. Let's display them
    if not error:
        writeln("---*** Done! ***---")
    else:
        writeln("---*** Failed! ***---")
    
    for line in lines:
        if len(line):
            if line[0].getType() == TYPE_VARIABLE:
                print "%s = %s"%(line[0].getLabel(), line[0].get())

if __name__ == "__main__":
        
    # testing this:
    #     op1 = 0
    #     op2 = op1 + 2
    #     op3 = op2 + 2
    #     zp  = op3 + 2

    w_0    = WORD("0", TYPE_VARIABLE   , 0)
    w_2    = WORD("2",TYPE_VARIABLE   , 0)
    w_op1  = WORD("op1", TYPE_VARIABLE   , 'op1')
    w_op2  = WORD("op2", TYPE_VARIABLE   , 'op2')
    w_op3  = WORD("op3", TYPE_VARIABLE   , 'op3')
    w_zp   = WORD("zp", TYPE_VARIABLE   , 'zp')
    w_plus = WORD("+", TYPE_PONCTUATION)
    w_equ  = WORD("=", TYPE_PONCTUATION)

    lines = (
        (w_op1, w_equ, w_0),
        (w_op3, w_equ, w_op2, w_plus, w_2),
        (w_op2, w_equ, w_op1, w_plus, w_2),
        (w_zp , w_equ, w_op3, w_plus, w_2))

    #~ for line in lines:
        #~ expression = buildLine(line)
        #~ print expression
        
    #~ sys.exit()

    solveLines(lines)
