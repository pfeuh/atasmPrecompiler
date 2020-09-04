#!/usr/bin/python
# -*- coding: utf-8 -*-

import sys

def dumpFile (fname, nb_cols=16, fp=sys.stdout):
    glyphes = ['.'] * 32 + [chr(x) for x in range(32,128)] + ['.'] * 128
    
    with open(fname, "r") as fpi:
        count = 0
        while 1:
            if not (count % nb_cols):
                fp.write("%04X "%count)
                ascii = ""
                
            car = fpi.read(1)
            if car == "":
                break
            byte = ord(car)
            
            fp.write("%02X "%byte)
            ascii += glyphes[byte]
            count += 1
            
            if not (count % 16):
                fp.write("%s\n"%ascii)
                
        if count % nb_cols:
            while count % nb_cols:
                fp.write("-- ")
                count += 1
            fp.write("%s"%ascii)
        fp.write("\n")

if __name__ == "__main__":
    
    dumpFile(sys.argv[0])
    dumpFile("TEST_OPCODES_CC65_1536.BIN", fp=open("test.log", "w"))
