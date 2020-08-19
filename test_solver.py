#!/usr/bin/python
# -*- coding: utf-8 -*-

import sys
import os

def solve(lines):
    error = True
    while error:
        error = False
        for line in lines:
            try:
                exec(line)
            except:
                error= True
    #all variables are solved. Lets display them
    print "a = %d"%a
    print "b = %d"%b
    print "c = %d"%c
        
solve(lines = ("a = b + 7 * 3 + 14 * c", "c = 12", "b = 33"))
