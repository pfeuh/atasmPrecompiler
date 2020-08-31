#!/usr/bin/python
# -*- coding: utf-8 -*-

import sys
import os

def write(text, fp=sys.stdout):
    if fp != None:
        fp.write(str(text))
    
def writeln(text, fp=sys.stdout):
    write(text, fp)
    write("\n", fp)

with open("TEST_OPCODES_ATASM.BIN", "r") as fp:
    while 1:
        byte = fp.read(1)
        writeln("%02x"%ord(byte))
        if byte == "":
            break
        