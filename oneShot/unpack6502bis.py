#!/usr/bin/python
# -*- coding: utf-8 -*-

import sys
import os

def write(text):
    sys.stdout.write(str(text))
    
def writeln(text):
    write(text)
    write("\n")

table = []
table.append(('BRK','inherent'))
table.append(('ORA','indzerox'))
table.append(('???','inherent'))
table.append(('???','inherent'))
table.append(('???','inherent'))
table.append(('ORA','zeropage'))
table.append(('ASL','zeropage'))
table.append(('???','inherent'))
table.append(('PHP','inherent'))
table.append(('ORA','immediate'))
table.append(('ASL','inherent'))
table.append(('???','inherent'))
table.append(('???','inherent'))
table.append(('ORA','absolute'))
table.append(('ASL','absolute'))
table.append(('???','inherent'))
table.append(('BPL','relative'))
table.append(('ORA','indzeroy'))
table.append(('???','inherent'))
table.append(('???','inherent'))
table.append(('???','inherent'))
table.append(('ORA','zeropagex'))
table.append(('ASL','zeropagex'))
table.append(('???','inherent'))
table.append(('CLC','inherent'))
table.append(('ORA','absoly'))
table.append(('???','inherent'))
table.append(('???','inherent'))
table.append(('???','inherent'))
table.append(('ORA','absolx'))
table.append(('ASL','absolx'))
table.append(('???','inherent'))
table.append(('JSR','absolute'))
table.append(('AND','indzerox'))
table.append(('???','inherent'))
table.append(('???','inherent'))
table.append(('BIT','zeropage'))
table.append(('AND','zeropage'))
table.append(('ROL','zeropage'))
table.append(('???','inherent'))
table.append(('PLP','inherent'))
table.append(('AND','immediate'))
table.append(('ROL','inherent'))
table.append(('???','inherent'))
table.append(('BIT','absolute'))
table.append(('AND','absolute'))
table.append(('ROL','absolute'))
table.append(('???','inherent'))
table.append(('BMI','relative'))
table.append(('AND','indzeroy'))
table.append(('???','inherent'))
table.append(('???','inherent'))
table.append(('???','inherent'))
table.append(('AND','zeropagex'))
table.append(('ROL','zeropagex'))
table.append(('???','inherent'))
table.append(('SEC','inherent'))
table.append(('AND','absoly'))
table.append(('???','inherent'))
table.append(('???','inherent'))
table.append(('???','inherent'))
table.append(('ORA','absolx'))
table.append(('ASL','absolx'))
table.append(('???','inherent'))
table.append(('RTI','inherent'))
table.append(('EOR','indzerox'))
table.append(('???','inherent'))
table.append(('???','inherent'))
table.append(('???','inherent'))
table.append(('EOR','zeropage'))
table.append(('LSR','zeropage'))
table.append(('???','inherent'))
table.append(('PHA','inherent'))
table.append(('EOR','immediate'))
table.append(('LSR','inherent'))
table.append(('???','inherent'))
table.append(('JMP','absolute'))
table.append(('EOR','absolute'))
table.append(('LSR','absolute'))
table.append(('???','inherent'))
table.append(('BVC','relative'))
table.append(('EOR','indzeroy'))
table.append(('???','inherent'))
table.append(('???','inherent'))
table.append(('???','inherent'))
table.append(('EOR','zeropagex'))
table.append(('LSR','zeropagex'))
table.append(('???','inherent'))
table.append(('CLI','inherent'))
table.append(('EOR','absoly'))
table.append(('???','inherent'))
table.append(('???','inherent'))
table.append(('???','inherent'))
table.append(('EOR','absolx'))
table.append(('LSR','absolx'))
table.append(('???','inherent'))
table.append(('RTS','inherent'))
table.append(('ADC','indzerox'))
table.append(('???','inherent'))
table.append(('???','inherent'))
table.append(('???','inherent'))
table.append(('ADC','zeropage'))
table.append(('ROR','zeropage'))
table.append(('???','inherent'))
table.append(('PLA','inherent'))
table.append(('ADC','immediate'))
table.append(('ROR','inherent'))
table.append(('???','inherent'))
table.append(('JMP','indirect'))
table.append(('ADC','absolute'))
table.append(('ROR','absolute'))
table.append(('???','inherent'))
table.append(('BCS','relative'))
table.append(('ADC','indzeroy'))
table.append(('???','inherent'))
table.append(('???','inherent'))
table.append(('???','inherent'))
table.append(('ADC','zeropagex'))
table.append(('ROR','zeropagex'))
table.append(('???','inherent'))
table.append(('SEI','inherent'))
table.append(('ADC','absoly'))
table.append(('???','inherent'))
table.append(('???','inherent'))
table.append(('???','inherent'))
table.append(('ADC','absolx'))
table.append(('ROR','absolx'))
table.append(('???','inherent'))
table.append(('???','inherent'))
table.append(('STA','indzerox'))
table.append(('???','inherent'))
table.append(('???','inherent'))
table.append(('STY','zeropage'))
table.append(('STA','zeropage'))
table.append(('STX','zeropage'))
table.append(('???','inherent'))
table.append(('DEY','inherent'))
table.append(('???','inherent'))
table.append(('TXA','inherent'))
table.append(('???','inherent'))
table.append(('STY','absolute'))
table.append(('STA','absolute'))
table.append(('STX','absolute'))
table.append(('???','inherent'))
table.append(('BCC','relative'))
table.append(('STA','indzeroy'))
table.append(('???','inherent'))
table.append(('???','inherent'))
table.append(('STY','inherent'))
table.append(('STA','zeropagex'))
table.append(('STX','zeropagey'))
table.append(('???','inherent'))
table.append(('TYA','inherent'))
table.append(('STA','absoly'))
table.append(('TXS','inherent'))
table.append(('???','inherent'))
table.append(('???','inherent'))
table.append(('STA','absolx'))
table.append(('???','inherent'))
table.append(('???','inherent'))
table.append(('LDY','immediate'))
table.append(('LDA','indzerox'))
table.append(('LDX','immediate'))
table.append(('???','inherent'))
table.append(('LDY','zeropage'))
table.append(('LDA','zeropage'))
table.append(('LDX','zeropage'))
table.append(('???','inherent'))
table.append(('TAY','inherent'))
table.append(('LDA','immediate'))
table.append(('TAX','inherent'))
table.append(('???','inherent'))
table.append(('LDY','absolute'))
table.append(('LDA','absolute'))
table.append(('LDX','absolute'))
table.append(('???','inherent'))
table.append(('BCS','relative'))
table.append(('LDA','indzeroy'))
table.append(('???','inherent'))
table.append(('???','inherent'))
table.append(('LDY','zeropagex'))
table.append(('LDA','zeropagex'))
table.append(('LDX','zeropagey'))
table.append(('???','inherent'))
table.append(('CLV','inherent'))
table.append(('LDA','absoly'))
table.append(('TSX','inherent'))
table.append(('???','inherent'))
table.append(('LDY','inherent'))
table.append(('LDA','absolx'))
table.append(('LDX','absoly'))
table.append(('???','inherent'))
table.append(('CPY','immediate'))
table.append(('CMP','indzerox'))
table.append(('???','inherent'))
table.append(('???','inherent'))
table.append(('CPY','zeropage'))
table.append(('CMP','zeropage'))
table.append(('DEC','zeropage'))
table.append(('???','inherent'))
table.append(('INY','inherent'))
table.append(('CMP','immediate'))
table.append(('DEX','inherent'))
table.append(('???','inherent'))
table.append(('CPY','absolute'))
table.append(('CMP','absolute'))
table.append(('DEC','absolute'))
table.append(('???','inherent'))
table.append(('BNE','relative'))
table.append(('CMP','indzeroy'))
table.append(('???','inherent'))
table.append(('???','inherent'))
table.append(('???','inherent'))
table.append(('CMP','zeropagex'))
table.append(('DEC','zeropagex'))
table.append(('???','inherent'))
table.append(('CLD','inherent'))
table.append(('CMP','absoly'))
table.append(('???','inherent'))
table.append(('???','inherent'))
table.append(('???','inherent'))
table.append(('CMP','absolx'))
table.append(('DEC','absolx'))
table.append(('???','inherent'))
table.append(('CPX','immediate'))
table.append(('SBC','indzerox'))
table.append(('???','inherent'))
table.append(('???','inherent'))
table.append(('CPX','zeropage'))
table.append(('SBC','zeropage'))
table.append(('INC','zeropage'))
table.append(('???','inherent'))
table.append(('INX','inherent'))
table.append(('SBC','immediate'))
table.append(('NOP','inherent'))
table.append(('SBC','inherent'))
table.append(('CPX','absolute'))
table.append(('SBC','absolute'))
table.append(('INC','absolute'))
table.append(('???','inherent'))
table.append(('BEQ','relative'))
table.append(('SBC','indzeroy'))
table.append(('???','inherent'))
table.append(('???','inherent'))
table.append(('???','inherent'))
table.append(('SBC','zeropagex'))
table.append(('INC','zeropagex'))
table.append(('???','inherent'))
table.append(('SED','inherent'))
table.append(('SBC','absoly'))
table.append(('???','inherent'))
table.append(('???','inherent'))
table.append(('???','inherent'))
table.append(('SBC','absolx'))
table.append(('INC','absolx'))
table.append(('???','inherent'))

def format_sub(items, table_name, nb_cols=8, width=5):
    writeln("%s = {"%table_name)
    for num, label in enumerate(items):
        if not (num % nb_cols):
            line = "    "

        if label != None:
            label = "'%s'"%label
        else:
            label = "None"
        while len(label) < width:
            label += " "
        line += "%s, "%label

        if (num % nb_cols) == nb_cols - 1:
            writeln(line)
            line = ""
    if line != "":
            writeln(line)
    writeln("    }\n")

def format(labels):
    opcodes = []
    mnemos = []
    modes = []

    for num, item in enumerate(table):
        mnemo = item[0].lower()
        mode = item[1].lower()

        if mnemo == "???":
            mode = None
            mnemo = None
        if mnemo != None:
            if not mnemo in opcodes:
                opcodes.append(mnemo)
        mnemos.append(mnemo)
        modes.append(mode)
                    
    format_sub(opcodes, "OPCODES")
    format_sub(mnemos, "MNEMOS")
    format_sub(modes, "MODES", nb_cols=4, width=11)
                    
format(table)
