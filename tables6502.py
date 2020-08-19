#!/usr/bin/python
# -*- coding: utf-8 -*-

# This file is autogenerated... If you modify it,
# it will be overwritten by the next update!

# https://www.atarimax.com/jindroush.atari.org/aopc.html
# Implied       BRK           $00
# Accumulator   ASL A         $0A
# Immediate     ADC #$44      $69
# Zero Page     ADC $44       $65
# Zero Page,X   ADC $44,X     $75
# Zero Page,Y   LDX $44,Y     $B6
# Absolute      ADC $4400     $6D
# Absolute,X    ADC $4400,X   $7D
# Absolute,Y    ADC $4400,Y   $79
# Indirect      JMP ($5597)   $6C
# Indirect,X    ADC ($44,X)   $61
# Indirect,Y    ADC ($44),Y   $71
# Relative      BEQ           $10

OPCODES = (
    'brk', 'ora', 'asl', 'php', 'bpl', 'clc', 'jsr', 'and', 'bit', 'rol', 'plp', 'bmi', 'sec', 'rti', 'eor', 'lsr', 
    'pha', 'jmp', 'bvc', 'cli', 'rts', 'adc', 'ror', 'pla', 'bcs', 'sei', 'sta', 'sty', 'stx', 'dey', 'txa', 'bcc', 
    'tya', 'txs', 'ldy', 'lda', 'ldx', 'tay', 'tax', 'clv', 'tsx', 'cpy', 'cmp', 'dec', 'iny', 'dex', 'bne', 'cld', 
    'cpx', 'sbc', 'inc', 'inx', 'nop', 'beq', 'sed', 
    )

MNEMOS = (
    'brk', 'ora', None , None , None , 'ora', 'asl', None , 'php', 'ora', 'asl', None , None , 'ora', 'asl', None , 
    'bpl', 'ora', None , None , None , 'ora', 'asl', None , 'clc', 'ora', None , None , None , 'ora', 'asl', None , 
    'jsr', 'and', None , None , 'bit', 'and', 'rol', None , 'plp', 'and', 'rol', None , 'bit', 'and', 'rol', None , 
    'bmi', 'and', None , None , None , 'and', 'rol', None , 'sec', 'and', None , None , None , 'ora', 'asl', None , 
    'rti', 'eor', None , None , None , 'eor', 'lsr', None , 'pha', 'eor', 'lsr', None , 'jmp', 'eor', 'lsr', None , 
    'bvc', 'eor', None , None , None , 'eor', 'lsr', None , 'cli', 'eor', None , None , None , 'eor', 'lsr', None , 
    'rts', 'adc', None , None , None , 'adc', 'ror', None , 'pla', 'adc', 'ror', None , 'jmp', 'adc', 'ror', None , 
    'bcs', 'adc', None , None , None , 'adc', 'ror', None , 'sei', 'adc', None , None , None , 'adc', 'ror', None , 
    None , 'sta', None , None , 'sty', 'sta', 'stx', None , 'dey', None , 'txa', None , 'sty', 'sta', 'stx', None , 
    'bcc', 'sta', None , None , 'sty', 'sta', 'stx', None , 'tya', 'sta', 'txs', None , None , 'sta', None , None , 
    'ldy', 'lda', 'ldx', None , 'ldy', 'lda', 'ldx', None , 'tay', 'lda', 'tax', None , 'ldy', 'lda', 'ldx', None , 
    'bcs', 'lda', None , None , 'ldy', 'lda', 'ldx', None , 'clv', 'lda', 'tsx', None , 'ldy', 'lda', 'ldx', None , 
    'cpy', 'cmp', None , None , 'cpy', 'cmp', 'dec', None , 'iny', 'cmp', 'dex', None , 'cpy', 'cmp', 'dec', None , 
    'bne', 'cmp', None , None , None , 'cmp', 'dec', None , 'cld', 'cmp', None , None , None , 'cmp', 'dec', None , 
    'cpx', 'sbc', None , None , 'cpx', 'sbc', 'inc', None , 'inx', 'sbc', 'nop', None , 'cpx', 'sbc', 'inc', None , 
    'beq', 'sbc', None , None , None , 'sbc', 'inc', None , 'sed', 'sbc', None , None , None , 'sbc', 'inc', None , 
    )

IMPLIED = 'Implied'
INDIRECTX = 'IndirectX'
ZEROPAGE = 'ZeroPage'
IMMEDIATE = 'Immediate'
ACCUMULATOR = 'Accumulator'
ABSOLUTE = 'Absolute'
RELATIVE = 'Relative'
INDIRECTY = 'IndirectY'
ZEROPAGEX = 'ZeroPageX'
ABSOLUTEY = 'AbsoluteY'
ABSOLUTEX = 'AbsoluteX'
INDIRECT = 'Indirect'
ZEROPAGEY = 'ZeroPageY'

MODES = (
    IMPLIED    , INDIRECTX  , None       , None       , 
    None       , ZEROPAGE   , ZEROPAGE   , None       , 
    IMPLIED    , IMMEDIATE  , ACCUMULATOR, None       , 
    None       , ABSOLUTE   , ABSOLUTE   , None       , 
    RELATIVE   , INDIRECTY  , None       , None       , 
    None       , ZEROPAGEX  , ZEROPAGEX  , None       , 
    IMPLIED    , ABSOLUTEY  , None       , None       , 
    None       , ABSOLUTEX  , ABSOLUTEX  , None       , 
    ABSOLUTE   , INDIRECTX  , None       , None       , 
    ZEROPAGE   , ZEROPAGE   , ZEROPAGE   , None       , 
    IMPLIED    , IMMEDIATE  , ACCUMULATOR, None       , 
    ABSOLUTE   , ABSOLUTE   , ABSOLUTE   , None       , 
    RELATIVE   , INDIRECTY  , None       , None       , 
    None       , ZEROPAGEX  , ZEROPAGEX  , None       , 
    IMPLIED    , ABSOLUTEY  , None       , None       , 
    None       , ABSOLUTEX  , ABSOLUTEX  , None       , 
    IMPLIED    , INDIRECTX  , None       , None       , 
    None       , ZEROPAGE   , ZEROPAGE   , None       , 
    IMPLIED    , IMMEDIATE  , ACCUMULATOR, None       , 
    ABSOLUTE   , ABSOLUTE   , ABSOLUTE   , None       , 
    RELATIVE   , INDIRECTY  , None       , None       , 
    None       , ZEROPAGEX  , ZEROPAGEX  , None       , 
    IMPLIED    , ABSOLUTEY  , None       , None       , 
    None       , ABSOLUTEX  , ABSOLUTEX  , None       , 
    IMPLIED    , INDIRECTX  , None       , None       , 
    None       , ZEROPAGE   , ZEROPAGE   , None       , 
    IMPLIED    , IMMEDIATE  , ACCUMULATOR, None       , 
    INDIRECT   , ABSOLUTE   , ABSOLUTE   , None       , 
    RELATIVE   , INDIRECTY  , None       , None       , 
    None       , ZEROPAGEX  , ZEROPAGEX  , None       , 
    IMPLIED    , ABSOLUTEY  , None       , None       , 
    None       , ABSOLUTEX  , ABSOLUTEX  , None       , 
    None       , INDIRECTX  , None       , None       , 
    ZEROPAGE   , ZEROPAGE   , ZEROPAGE   , None       , 
    IMPLIED    , None       , IMPLIED    , None       , 
    ABSOLUTE   , ABSOLUTE   , ABSOLUTE   , None       , 
    RELATIVE   , INDIRECTY  , None       , None       , 
    ZEROPAGEX  , ZEROPAGEX  , ZEROPAGEY  , None       , 
    IMPLIED    , ABSOLUTEY  , IMPLIED    , None       , 
    None       , ABSOLUTEX  , None       , None       , 
    IMMEDIATE  , INDIRECTX  , IMMEDIATE  , None       , 
    ZEROPAGE   , ZEROPAGE   , ZEROPAGE   , None       , 
    IMPLIED    , IMMEDIATE  , IMPLIED    , None       , 
    ABSOLUTE   , ABSOLUTE   , ABSOLUTE   , None       , 
    RELATIVE   , INDIRECTY  , None       , None       , 
    ZEROPAGEX  , ZEROPAGEX  , ZEROPAGEY  , None       , 
    IMPLIED    , ABSOLUTEY  , IMPLIED    , None       , 
    ABSOLUTEX  , ABSOLUTEX  , ABSOLUTEY  , None       , 
    IMMEDIATE  , INDIRECTX  , None       , None       , 
    ZEROPAGE   , ZEROPAGE   , ZEROPAGE   , None       , 
    IMPLIED    , IMMEDIATE  , IMPLIED    , None       , 
    ABSOLUTE   , ABSOLUTE   , ABSOLUTE   , None       , 
    RELATIVE   , INDIRECTY  , None       , None       , 
    None       , ZEROPAGEX  , ZEROPAGEX  , None       , 
    IMPLIED    , ABSOLUTEY  , None       , None       , 
    None       , ABSOLUTEX  , ABSOLUTEX  , None       , 
    IMMEDIATE  , INDIRECTX  , None       , None       , 
    ZEROPAGE   , ZEROPAGE   , ZEROPAGE   , None       , 
    IMPLIED    , IMMEDIATE  , IMPLIED    , None       , 
    ABSOLUTE   , ABSOLUTE   , ABSOLUTE   , None       , 
    RELATIVE   , INDIRECTY  , None       , None       , 
    None       , ZEROPAGEX  , ZEROPAGEX  , None       , 
    IMPLIED    , ABSOLUTEY  , None       , None       , 
    None       , ABSOLUTEX  , ABSOLUTEX  , None       , 
    )

RELATIVE_OPCODES = (
    'bpl', 'bmi', 'bvc', 'bcs', 'bcc', 'bcs', 'bne', 'beq', 
    )

IMPLIED_OPCODES = (
    'brk', 'php', 'clc', 'plp', 'sec', 'rti', 'pha', 'cli', 
    'rts', 'pla', 'sei', 'dey', 'txa', 'tya', 'txs', 'tay', 
    'tax', 'clv', 'tsx', 'iny', 'dex', 'cld', 'inx', 'nop', 
    'sed', 
    )

