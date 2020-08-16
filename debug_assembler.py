#!/usr/bin/python
# -*- coding: utf-8 -*-

import sys
import os

from assembler6502 import *

class GNAGNA():
    def __init__(self):
        pass
    def get(self, gnagna):
        return True

line = SOURCE_LINE("----", "", 0)

words = getWords("azerty", line)
words = getWords('"az\'erty"', line)
words = getWords("'az\"erty'", line)
words = getWords("'a", line)
writeln(words)

writeln("A L L   T E S T S   P A S S E D !")
