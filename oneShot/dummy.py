#!/usr/bin/python
# -*- coding: utf-8 -*-

import sys
import os

def write(text):
    sys.stdout.write(str(text))
    
def writeln(text):
    write(text)
    write("\n")

writeln(eval("0x0a"))
cmp("toto", "titi")