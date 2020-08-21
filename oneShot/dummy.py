#!/usr/bin/python
# -*- coding: utf-8 -*-

import sys
import os

def write(text):
    sys.stdout.write(str(text))
    
def writeln(text):
    write(text)
    write("\n")

result = (0x1234, 0x2345, 0x3456)

tmp_lst = []
for value in result:
    tmp_lst.append(value & 255)
    tmp_lst.append(value /256)

print tmp_lst
for byte in tmp_lst:
    print "%02x"%byte

print tuple(tmp_lst)
print tuple([-1])
    