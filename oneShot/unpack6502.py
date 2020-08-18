#!/usr/bin/python
# -*- coding: utf-8 -*-

import sys
import os
import random

def write(text, fp=sys.stdout):
    fp.write(str(text))
    
def writeln(text, fp=sys.stdout):
    write(text, fp)
    write("\n", fp)

if 1:
    table = []
    table.append(['BRK','inherent'])    # opcode $00
    table.append(['ORA','indzerox'])    # opcode $01
    table.append(['???','inherent'])    # opcode $02
    table.append(['???','inherent'])    # opcode $03
    table.append(['???','inherent'])    # opcode $04
    table.append(['ORA','zeropage'])    # opcode $05
    table.append(['ASL','zeropage'])    # opcode $06
    table.append(['???','inherent'])    # opcode $07
    table.append(['PHP','inherent'])    # opcode $08
    table.append(['ORA','immediate'])   # opcode $09
    table.append(['ASL','accumulator']) # opcode $0A
    table.append(['???','inherent'])    # opcode $0B
    table.append(['???','inherent'])    # opcode $0C
    table.append(['ORA','absolute'])    # opcode $0D
    table.append(['ASL','absolute'])    # opcode $0E
    table.append(['???','inherent'])    # opcode $0F
    table.append(['BPL','relative'])    # opcode $10
    table.append(['ORA','indzeroy'])    # opcode $11
    table.append(['???','inherent'])    # opcode $12
    table.append(['???','inherent'])    # opcode $13
    table.append(['???','inherent'])    # opcode $14
    table.append(['ORA','zeropagex'])   # opcode $15
    table.append(['ASL','zeropagex'])   # opcode $16
    table.append(['???','inherent'])    # opcode $17
    table.append(['CLC','inherent'])    # opcode $18
    table.append(['ORA','absoly'])      # opcode $19
    table.append(['???','inherent'])    # opcode $1A
    table.append(['???','inherent'])    # opcode $1B
    table.append(['???','inherent'])    # opcode $1C
    table.append(['ORA','absolx'])      # opcode $1D
    table.append(['ASL','absolx'])      # opcode $1E
    table.append(['???','inherent'])    # opcode $1F
    table.append(['JSR','absolute'])    # opcode $20
    table.append(['AND','indzerox'])    # opcode $21
    table.append(['???','inherent'])    # opcode $22
    table.append(['???','inherent'])    # opcode $23
    table.append(['BIT','zeropage'])    # opcode $24
    table.append(['AND','zeropage'])    # opcode $25
    table.append(['ROL','zeropage'])    # opcode $26
    table.append(['???','inherent'])    # opcode $27
    table.append(['PLP','inherent'])    # opcode $28
    table.append(['AND','immediate'])   # opcode $29
    table.append(['ROL','accumulator']) # opcode $2A
    table.append(['???','inherent'])    # opcode $2B
    table.append(['BIT','absolute'])    # opcode $2C
    table.append(['AND','absolute'])    # opcode $2D
    table.append(['ROL','absolute'])    # opcode $2E
    table.append(['???','inherent'])    # opcode $2F
    table.append(['BMI','relative'])    # opcode $30
    table.append(['AND','indzeroy'])    # opcode $31
    table.append(['???','inherent'])    # opcode $32
    table.append(['???','inherent'])    # opcode $33
    table.append(['???','inherent'])    # opcode $34
    table.append(['AND','zeropagex'])   # opcode $35
    table.append(['ROL','zeropagex'])   # opcode $36
    table.append(['???','inherent'])    # opcode $37
    table.append(['SEC','inherent'])    # opcode $38
    table.append(['AND','absoly'])      # opcode $39
    table.append(['???','inherent'])    # opcode $3A
    table.append(['???','inherent'])    # opcode $3B
    table.append(['???','inherent'])    # opcode $3C
    table.append(['ORA','absolx'])      # opcode $3D
    table.append(['ASL','absolx'])      # opcode $3E
    table.append(['???','inherent'])    # opcode $3F
    table.append(['RTI','inherent'])    # opcode $40
    table.append(['EOR','indzerox'])    # opcode $41
    table.append(['???','inherent'])    # opcode $42
    table.append(['???','inherent'])    # opcode $43
    table.append(['???','inherent'])    # opcode $44
    table.append(['EOR','zeropage'])    # opcode $45
    table.append(['LSR','zeropage'])    # opcode $46
    table.append(['???','inherent'])    # opcode $47
    table.append(['PHA','inherent'])    # opcode $48
    table.append(['EOR','immediate'])   # opcode $49
    table.append(['LSR','accumulator']) # opcode $4A
    table.append(['???','inherent'])    # opcode $4B
    table.append(['JMP','absolute'])    # opcode $4C
    table.append(['EOR','absolute'])    # opcode $4D
    table.append(['LSR','absolute'])    # opcode $4E
    table.append(['???','inherent'])    # opcode $4F
    table.append(['BVC','relative'])    # opcode $50
    table.append(['EOR','indzeroy'])    # opcode $51
    table.append(['???','inherent'])    # opcode $52
    table.append(['???','inherent'])    # opcode $53
    table.append(['???','inherent'])    # opcode $54
    table.append(['EOR','zeropagex'])   # opcode $55
    table.append(['LSR','zeropagex'])   # opcode $56
    table.append(['???','inherent'])    # opcode $57
    table.append(['CLI','inherent'])    # opcode $58
    table.append(['EOR','absoly'])      # opcode $59
    table.append(['???','inherent'])    # opcode $5A
    table.append(['???','inherent'])    # opcode $5B
    table.append(['???','inherent'])    # opcode $5C
    table.append(['EOR','absolx'])      # opcode $5D
    table.append(['LSR','absolx'])      # opcode $5E
    table.append(['???','inherent'])    # opcode $5F
    table.append(['RTS','inherent'])    # opcode $60
    table.append(['ADC','indzerox'])    # opcode $61
    table.append(['???','inherent'])    # opcode $62
    table.append(['???','inherent'])    # opcode $63
    table.append(['???','inherent'])    # opcode $64
    table.append(['ADC','zeropage'])    # opcode $65
    table.append(['ROR','zeropage'])    # opcode $66
    table.append(['???','inherent'])    # opcode $67
    table.append(['PLA','inherent'])    # opcode $68
    table.append(['ADC','immediate'])   # opcode $69
    table.append(['ROR','accumulator']) # opcode $6A
    table.append(['???','inherent'])    # opcode $6B
    table.append(['JMP','indirect'])    # opcode $6C
    table.append(['ADC','absolute'])    # opcode $6D
    table.append(['ROR','absolute'])    # opcode $6E
    table.append(['???','inherent'])    # opcode $6F
    table.append(['BCS','relative'])    # opcode $70
    table.append(['ADC','indzeroy'])    # opcode $71
    table.append(['???','inherent'])    # opcode $72
    table.append(['???','inherent'])    # opcode $73
    table.append(['???','inherent'])    # opcode $74
    table.append(['ADC','zeropagex'])   # opcode $75
    table.append(['ROR','zeropagex'])   # opcode $76
    table.append(['???','inherent'])    # opcode $77
    table.append(['SEI','inherent'])    # opcode $78
    table.append(['ADC','absoly'])      # opcode $79
    table.append(['???','inherent'])    # opcode $7A
    table.append(['???','inherent'])    # opcode $7B
    table.append(['???','inherent'])    # opcode $7C
    table.append(['ADC','absolx'])      # opcode $7D
    table.append(['ROR','absolx'])      # opcode $7E
    table.append(['???','inherent'])    # opcode $7F
    table.append(['???','inherent'])    # opcode $80
    table.append(['STA','indzerox'])    # opcode $81
    table.append(['???','inherent'])    # opcode $82
    table.append(['???','inherent'])    # opcode $83
    table.append(['STY','zeropage'])    # opcode $84
    table.append(['STA','zeropage'])    # opcode $85
    table.append(['STX','zeropage'])    # opcode $86
    table.append(['???','inherent'])    # opcode $87
    table.append(['DEY','inherent'])    # opcode $88
    table.append(['???','inherent'])    # opcode $89
    table.append(['TXA','inherent'])    # opcode $8A
    table.append(['???','inherent'])    # opcode $8B
    table.append(['STY','absolute'])    # opcode $8C
    table.append(['STA','absolute'])    # opcode $8D
    table.append(['STX','absolute'])    # opcode $8E
    table.append(['???','inherent'])    # opcode $8F
    table.append(['BCC','relative'])    # opcode $90
    table.append(['STA','indzeroy'])    # opcode $91
    table.append(['???','inherent'])    # opcode $92
    table.append(['???','inherent'])    # opcode $93
    table.append(['STY','zeropagex'])   # opcode $94
    table.append(['STA','zeropagex'])   # opcode $95
    table.append(['STX','zeropagey'])   # opcode $96
    table.append(['???','inherent'])    # opcode $97
    table.append(['TYA','inherent'])    # opcode $98
    table.append(['STA','absoly'])      # opcode $99
    table.append(['TXS','inherent'])    # opcode $9A
    table.append(['???','inherent'])    # opcode $9B
    table.append(['???','inherent'])    # opcode $9C
    table.append(['STA','absolx'])      # opcode $9D
    table.append(['???','inherent'])    # opcode $9E
    table.append(['???','inherent'])    # opcode $9F
    table.append(['LDY','immediate'])   # opcode $A0
    table.append(['LDA','indzerox'])    # opcode $A1
    table.append(['LDX','immediate'])   # opcode $A2
    table.append(['???','inherent'])    # opcode $A3
    table.append(['LDY','zeropage'])    # opcode $A4
    table.append(['LDA','zeropage'])    # opcode $A5
    table.append(['LDX','zeropage'])    # opcode $A6
    table.append(['???','inherent'])    # opcode $A7
    table.append(['TAY','inherent'])    # opcode $A8
    table.append(['LDA','immediate'])   # opcode $A9
    table.append(['TAX','inherent'])    # opcode $AA
    table.append(['???','inherent'])    # opcode $AB
    table.append(['LDY','absolute'])    # opcode $AC
    table.append(['LDA','absolute'])    # opcode $AD
    table.append(['LDX','absolute'])    # opcode $AE
    table.append(['???','inherent'])    # opcode $AF
    table.append(['BCS','relative'])    # opcode $B0
    table.append(['LDA','indzeroy'])    # opcode $B1
    table.append(['???','inherent'])    # opcode $B2
    table.append(['???','inherent'])    # opcode $B3
    table.append(['LDY','zeropagex'])   # opcode $B4
    table.append(['LDA','zeropagex'])   # opcode $B5
    table.append(['LDX','zeropagey'])   # opcode $B6
    table.append(['???','inherent'])    # opcode $B7
    table.append(['CLV','inherent'])    # opcode $B8
    table.append(['LDA','absoly'])      # opcode $B9
    table.append(['TSX','inherent'])    # opcode $BA
    table.append(['???','inherent'])    # opcode $BB
    table.append(['LDY','absolx'])      # opcode $BC
    table.append(['LDA','absolx'])      # opcode $BD
    table.append(['LDX','absoly'])      # opcode $BE
    table.append(['???','inherent'])    # opcode $BF
    table.append(['CPY','immediate'])   # opcode $C0
    table.append(['CMP','indzerox'])    # opcode $C1
    table.append(['???','inherent'])    # opcode $C2
    table.append(['???','inherent'])    # opcode $C3
    table.append(['CPY','zeropage'])    # opcode $C4
    table.append(['CMP','zeropage'])    # opcode $C5
    table.append(['DEC','zeropage'])    # opcode $C6
    table.append(['???','inherent'])    # opcode $C7
    table.append(['INY','inherent'])    # opcode $C8
    table.append(['CMP','immediate'])   # opcode $C9
    table.append(['DEX','inherent'])    # opcode $CA
    table.append(['???','inherent'])    # opcode $CB
    table.append(['CPY','absolute'])    # opcode $CC
    table.append(['CMP','absolute'])    # opcode $CD
    table.append(['DEC','absolute'])    # opcode $CE
    table.append(['???','inherent'])    # opcode $CF
    table.append(['BNE','relative'])    # opcode $D0
    table.append(['CMP','indzeroy'])    # opcode $D1
    table.append(['???','inherent'])    # opcode $D2
    table.append(['???','inherent'])    # opcode $D3
    table.append(['???','inherent'])    # opcode $D4
    table.append(['CMP','zeropagex'])   # opcode $D5
    table.append(['DEC','zeropagex'])   # opcode $D6
    table.append(['???','inherent'])    # opcode $D7
    table.append(['CLD','inherent'])    # opcode $D8
    table.append(['CMP','absoly'])      # opcode $D9
    table.append(['???','inherent'])    # opcode $DA
    table.append(['???','inherent'])    # opcode $DB
    table.append(['???','inherent'])    # opcode $DC
    table.append(['CMP','absolx'])      # opcode $DD
    table.append(['DEC','absolx'])      # opcode $DE
    table.append(['???','inherent'])    # opcode $DF
    table.append(['CPX','immediate'])   # opcode $E0
    table.append(['SBC','indzerox'])    # opcode $E1
    table.append(['???','inherent'])    # opcode $E2
    table.append(['???','inherent'])    # opcode $E3
    table.append(['CPX','zeropage'])    # opcode $E4
    table.append(['SBC','zeropage'])    # opcode $E5
    table.append(['INC','zeropage'])    # opcode $E6
    table.append(['???','inherent'])    # opcode $E7
    table.append(['INX','inherent'])    # opcode $E8
    table.append(['SBC','immediate'])   # opcode $E9
    table.append(['NOP','inherent'])    # opcode $EA
    table.append(['???','inherent'])    # opcode $EB
    table.append(['CPX','absolute'])    # opcode $EC
    table.append(['SBC','absolute'])    # opcode $ED
    table.append(['INC','absolute'])    # opcode $EE
    table.append(['???','inherent'])    # opcode $EF
    table.append(['BEQ','relative'])    # opcode $F0
    table.append(['SBC','indzeroy'])    # opcode $F1
    table.append(['???','inherent'])    # opcode $F2
    table.append(['???','inherent'])    # opcode $F3
    table.append(['???','inherent'])    # opcode $F4
    table.append(['SBC','zeropagex'])   # opcode $F5
    table.append(['INC','zeropagex'])   # opcode $F6
    table.append(['???','inherent'])    # opcode $F7
    table.append(['SED','inherent'])    # opcode $F8
    table.append(['SBC','absoly'])      # opcode $F9
    table.append(['???','inherent'])    # opcode $FA
    table.append(['???','inherent'])    # opcode $FB
    table.append(['???','inherent'])    # opcode $FC
    table.append(['SBC','absolx'])      # opcode $FD
    table.append(['INC','absolx'])      # opcode $FE
    table.append(['???','inherent'])    # opcode $FF

def get8BitsValueText():
    return "$%02X"%random.randint(0, 255)

def get16BitsValueText():
    return "$%04X"%random.randint(256, 65535)

def format_sub(items, table_name, nb_cols=8, width=5, quote=True):
    writeln("%s = ("%table_name)
    for num, label in enumerate(items):
        if not (num % nb_cols):
            line = "    "

        if label != None:
            if quote:
                label = "'%s'"%label
            else:
                label = "%s"%label.upper()
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
    writeln("    )\n")

def format(labels):
    opcodes = []
    mnemos = []
    modes = []
    def_modes = []

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
        if not mode in def_modes:
            if mode != None:
                def_modes.append(mode)
                    
    format_sub(opcodes, "OPCODES")
    format_sub(mnemos, "MNEMOS")
    for mode in def_modes:
        writeln("%s = '%s'"%(mode.upper(), mode))
    writeln("")
    
    format_sub(modes, "MODES", nb_cols=4, width=11, quote=False)
    
def createTestProgram(fp=sys.stdout):
    writeln("\n    ; -------------------------------------------------------------;", fp)
    writeln("    ; this program uses all the official opcodes for 6502 processor;", fp)
    writeln("    ; -------------------------------------------------------------;\n", fp)
    writeln("    ;* = $200 ; uncomment if neccessary\n", fp)
    nb_valid = 0
    items = [item for item in table]
    for index, item in enumerate(items):
        if not (index % 16):
            label = "label_%02d"%(index / 16 + 1)
            writeln("%s:"%label, fp)
        
        opcode = item[0]
        mode = item[1]
        if opcode == "???":
            writeln("                 ; illegal opcode $%02x"%(index), fp)
        else:
            nb_valid += 1
            
            if mode == 'inherent':
                text = opcode
            elif mode == 'immediate':
                text = opcode + ' #' + get8BitsValueText()
            elif mode == 'indirect':
                text = opcode + '(' + get16BitsValueText() + ')'
            elif mode == 'accumulator':
                text = opcode + ' A'
            elif mode == 'absolute':
                text = opcode + ' ' + get16BitsValueText()
            elif mode == 'absolx':
                text = opcode + ' ' + get16BitsValueText() + ',X'
            elif mode == 'absoly':
                text = opcode + ' ' + get16BitsValueText() + ',Y'
            elif mode == 'indzerox':
                text = opcode + ' ' + '(' + get8BitsValueText() + ',X)'
            elif mode == 'indzeroy':
                text = opcode + ' ' + '(' + get8BitsValueText() + '),Y'
            elif mode == 'relative':
                text = opcode + ' ' + label
            elif mode == 'zeropage':
                text = opcode + ' ' + get8BitsValueText()
            elif mode == 'zeropagex':
                text = opcode + ' ' + get8BitsValueText() + ',X'
            elif mode == 'zeropagey':
                text = opcode + ' ' + get8BitsValueText() + ',Y'
                
                
            else:
                text = opcode + ' ???'

            writeln("    %-12s ; opcode $%02x"%(text, index), fp)

    return nb_valid


if __name__ == "__main__":

    # first of all, some modes have to be modified due to a bug
    table[0x0a][1] = "accumulator"
    table[0x2a][1] = "accumulator"
    table[0x4a][1] = "accumulator"
    table[0x6a][1] = "accumulator"
                        

    format(table)

    with open("/media/pfeuh/70b90f4a-e5a6-4a83-bf19-1feffc44cab0/Documents/sources/C_language/linux/vosc6502/sample/test_opcodes/test_opcodes.asm", "w") as fp:
        nb_valid = createTestProgram(fp)
    writeln("%d 6502-opcodes created"%nb_valid)
