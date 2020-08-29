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

def addSign(value):
    if value > 127:
        return (value ^ 255) + 1
    else:
        return value

for x in range(256):
    write("%4d->%4d "%(x, addSign(x)))
    if x % 8 == 7:
        writeln("")
