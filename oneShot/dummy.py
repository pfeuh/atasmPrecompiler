#!/usr/bin/python
# -*- coding: utf-8 -*-

import sys
import os

def write(text):
    sys.stdout.write(str(text))
    
def writeln(text):
    write(text)
    write("\n")

prog = ['', 'lda', '#', '3']

writeln(prog)
del prog[2]
writeln(prog)
