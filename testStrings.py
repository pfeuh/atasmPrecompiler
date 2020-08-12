#!/usr/bin/python
# -*- coding: utf-8 -*-

import sys
import os

def write(text):
    sys.stdout.write(str(text))
    
def writeln(text):
    write(text)
    write("\n")

text = """
    .byte $22, $56, $4f, $53, $43, $36, $35, $30, $32, $22, $20, $28, $56
    .byte $69, $72, $74, $75, $61, $6c, $20, $4f, $6c, $64, $20, $53, $63
    .byte $68, $6f, $6f, $6c, $20, $43, $6f, $6d, $70, $75, $74, $65, $72
    .byte $20, $77, $69, $74, $68, $20, $61, $20, $36, $35, $30, $32, $20
    .byte $70, $72, $6f, $63, $65, $73, $73, $6f, $72, $29, $0a, $00
"""

def convert(text):
    text = text.replace("    .byte", "")
    text = text.replace("$", "")
    text = text.replace("\n", "")
    text = text.replace(",", "")
    words = text.split()
    for word in words:
        write(chr(int(word, 16)))

convert(text)