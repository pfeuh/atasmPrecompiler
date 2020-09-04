#!/usr/bin/python
# -*- coding: utf-8 -*-

ap = None

import sys
import os
from assembler6502 import *

if 1:
    REF_OPCODES = """00 	BRK 	
    01 	ORA 	INDIRECTX
    02 		
    03 		
    04 		
    05 	ORA 	ZEROPAGE
    06 	ASL 	ZEROPAGE
    07 		
    08 	PHP 	
    09 	ORA 	IMMEDIATE
    0A 	ASL 	ACCUMULATOR
    0B 		
    0C 		
    0D 	ORA 	ABSOLUTE
    0E 	ASL 	ABSOLUTE
    0F 		
    10 	BPL 	RELATIVE
    11 	ORA 	INDIRECTY
    12 		
    13 		
    14 		
    15 	ORA 	ZEROPAGEX
    16 	ASL 	ZEROPAGEX
    17 		
    18 	CLC 	
    19 	ORA 	ABSOLUTEY
    1A 		
    1B 		
    1C 		
    1D 	ORA 	ABSOLUTEX
    1E 	ASL 	ABSOLUTEX
    1F 		
    20 	JSR 	ABSOLUTE
    21 	AND 	INDIRECTX
    22 		
    23 		
    24 	BIT 	ZEROPAGE
    25 	AND 	ZEROPAGE
    26 	ROL 	ZEROPAGE
    27 		
    28 	PLP 	
    29 	AND 	IMMEDIATE
    2A 	ROL 	ACCUMULATOR
    2B 		
    2C 	BIT 	ABSOLUTE
    2D 	AND 	ABSOLUTE
    2E 	ROL 	ABSOLUTE
    2F 		
    30 	BMI 	RELATIVE
    31 	AND 	INDIRECTY
    32 		
    33 		
    34 		
    35 	AND 	ZEROPAGEX
    36 	ROL 	ZEROPAGEX
    37 		
    38 	SEC 	
    39 	AND 	ABSOLUTEY
    3A 		
    3B 		
    3C 		
    3D 	AND 	ABSOLUTEX
    3E 	ROL 	ABSOLUTEX
    3F 		
    40 	RTI 	
    41 	EOR 	INDIRECTX
    42 		
    43 		
    44 		
    45 	EOR 	ZEROPAGE
    46 	LSR 	ZEROPAGE
    47 		
    48 	PHA 	
    49 	EOR 	IMMEDIATE
    4A 	LSR 	ACCUMULATOR
    4B 		
    4C 	JMP 	ABSOLUTE
    4D 	EOR 	ABSOLUTE
    4E 	LSR 	ABSOLUTE
    4F 		
    50 	BVC 	RELATIVE
    51 	EOR 	INDIRECTY
    52 		
    53 		
    54 		
    55 	EOR 	ZEROPAGEX
    56 	LSR 	ZEROPAGEX
    57 		
    58 	CLI 	
    59 	EOR 	ABSOLUTEY
    5A 		
    5B 		
    5C 		
    5D 	EOR 	ABSOLUTEX
    5E 	LSR 	ABSOLUTEX
    5F 		
    60 	RTS 	
    61 	ADC 	INDIRECTX
    62 		
    63 		
    64 		
    65 	ADC 	ZEROPAGE
    66 	ROR 	ZEROPAGE
    67 		
    68 	PLA 	
    69 	ADC 	IMMEDIATE
    6A 	ROR 	ACCUMULATOR
    6B 		
    6C 	JMP 	INDIRECT
    6D 	ADC 	ABSOLUTE
    6E 	ROR 	ABSOLUTE
    6F 		
    70 	BVS 	RELATIVE
    71 	ADC 	INDIRECTY
    72 		
    73 		
    74 		
    75 	ADC 	ZEROPAGEX
    76 	ROR 	ZEROPAGEX
    77 		
    78 	SEI 	
    79 	ADC 	ABSOLUTEY
    7A 		
    7B 		
    7C 		
    7D 	ADC 	ABSOLUTEX
    7E 	ROR 	ABSOLUTEX
    7F 		
    80 		
    81 	STA 	INDIRECTX
    82 		
    83 		
    84 	STY 	ZEROPAGE
    85 	STA 	ZEROPAGE
    86 	STX 	ZEROPAGE
    87 		
    88 	DEY 	
    89 		
    8A 	TXA 	
    8B 		
    8C 	STY 	ABSOLUTE
    8D 	STA 	ABSOLUTE
    8E 	STX 	ABSOLUTE
    8F 		
    90 	BCC 	RELATIVE
    91 	STA 	INDIRECTY
    92 		
    93 		
    94 	STY 	ZEROPAGEX
    95 	STA 	ZEROPAGEX
    96 	STX 	ZEROPAGEY
    97 		
    98 	TYA 	
    99 	STA 	ABSOLUTEY
    9A 	TXS 	
    9B 		
    9C 		
    9D 	STA 	ABSOLUTEX
    9E 		
    9F 		
    A0 	LDY 	IMMEDIATE
    A1 	LDA 	INDIRECTX
    A2 	LDX 	IMMEDIATE
    A3 		
    A4 	LDY 	ZEROPAGE
    A5 	LDA 	ZEROPAGE
    A6 	LDX 	ZEROPAGE
    A7 		
    A8 	TAY 	
    A9 	LDA 	IMMEDIATE
    AA 	TAX 	
    AB 		
    AC 	LDY 	ABSOLUTE
    AD 	LDA 	ABSOLUTE
    AE 	LDX 	ABSOLUTE
    AF 		
    B0 	BCS 	RELATIVE
    B1 	LDA 	INDIRECTY
    B2 		
    B3 		
    B4 	LDY 	ZEROPAGEX
    B5 	LDA 	ZEROPAGEX
    B6 	LDX 	ZEROPAGEY
    B7 		
    B8 	CLV 	
    B9 	LDA 	ABSOLUTEY
    BA 	TSX 	
    BB 		
    BC 	LDY 	ABSOLUTEX
    BD 	LDA 	ABSOLUTEX
    BE 	LDX 	ABSOLUTEY
    BF 		
    C0 	CPY 	IMMEDIATE
    C1 	CMP 	INDIRECTX
    C2 		
    C3 		
    C4 	CPY 	ZEROPAGE
    C5 	CMP 	ZEROPAGE
    C6 	DEC 	ZEROPAGE
    C7 		
    C8 	INY 	
    C9 	CMP 	IMMEDIATE
    CA 	DEX 	
    CB 		
    CC 	CPY 	ABSOLUTE
    CD 	CMP 	ABSOLUTE
    CE 	DEC 	ABSOLUTE
    CF 		
    D0 	BNE 	RELATIVE
    D1 	CMP 	INDIRECTY
    D2 		
    D3 		
    D4 		
    D5 	CMP 	ZEROPAGEX
    D6 	DEC 	ZEROPAGEX
    D7 		
    D8 	CLD 	
    D9 	CMP 	ABSOLUTEY
    DA 		
    DB 		
    DC 		
    DD 	CMP 	ABSOLUTEX
    DE 	DEC 	ABSOLUTEX
    DF 		
    E0 	CPX 	IMMEDIATE
    E1 	SBC 	INDIRECTX
    E2 		
    E3 		
    E4 	CPX 	ZEROPAGE
    E5 	SBC 	ZEROPAGE
    E6 	INC 	ZEROPAGE
    E7 		
    E8 	INX 	
    E9 	SBC 	IMMEDIATE
    EA 	NOP 	
    EB 		
    EC 	CPX 	ABSOLUTE
    ED 	SBC 	ABSOLUTE
    EE 	INC 	ABSOLUTE
    EF 		
    F0 	BEQ 	RELATIVE
    F1 	SBC 	INDIRECTY
    F2 		
    F3 		
    F4 		
    F5 	SBC 	ZEROPAGEX
    F6 	INC 	ZEROPAGEX
    F7 		
    F8 	SED 	
    F9 	SBC 	ABSOLUTEY
    FA 		
    FB 		
    FC 		
    FD 	SBC 	ABSOLUTEX
    FE 	INC 	ABSOLUTEX
    FF 		"""

def stopSilentMode():
    for x, arg in enumerate(sys.argv):
        if arg == "-silent":
            del sys.argv[x]

def startSilentMode():
    if not '-silent' in sys.argv:
        sys.argv.append('-silent')

def stopDebugMode():
    for x, arg in enumerate(sys.argv):
        if arg == "-debug":
            del sys.argv[x]

def startDebugMode():
    if not '-debug' in sys.argv:
        sys.argv.append('-debug')

def getRefTable():
    # got from http://www.thealmightyguru.com/Games/Hacking/Wiki/index.php?title=6502_Opcodes
    # find some errors fixed in the present table
    ref_opcodes = [line.strip() for line in REF_OPCODES.split("\n")]
    assert len(ref_opcodes) == 256
    temp_list = []
    for x in range(256):
        words = [word.strip() for word in ref_opcodes[x].split()]
        assert words[0] == "%02X"%x
        if len(words) == 2:
            words.append('IMPLIED')
        temp_list.append(words)
    return temp_list
    
def getGlyphe(car):
    value = ord(car)
    if value < 32:
        return '.'
    elif value < 128:
        return chr(value)
    else:
        return '.'

def compareStrings(s1, s2):
    for index in range(max((len(s1), len(s2)))):
        word1 = "  "
        word2 = " "
        word3 = "  "
        word4 = " "
        pointer = ""
        
        if index < len(s1):
            car = s1[index]
            word1 = "%02x"%ord(car)
            word2 = "%c"%getGlyphe(car)
        if index < len(s2):
            car = s2[index]
            word3 = "%02x"%ord(car)
            word4 = "%c"%getGlyphe(car)
        if word1 != word3:
            pointer = "<--"
        writeln("%s '%s' - '%s' %s %s"%(word1, word2, word4, word3, pointer))

def compareFiles(fname1, fname2):
    with open(fname1, "rb") as fp:
        s1 = fp.read(-1)
    with open(fname2, "rb") as fp:
        s2 = fp.read(-1)
    compareStrings(s1, s2)
    
def write(text, fp=sys.stdout):
    if fp != None:
        fp.write(str(text))
    
def writeln(text, fp=sys.stdout):
    write(text, fp)
    write("\n", fp)

def makeFile(fname, lines):
    with open(fname, "w") as fp:
        for line in lines:
            line = line.rstrip() +"\n"
            fp.write(line)

def readWord(fp):
    b_lo = fp.read(1)
    b_hi = fp.read(1)
    if b_lo == "" or b_hi == "":
        return None
    else:
        value = ord(b_hi) * 256 + ord(b_lo)
        return value

def readAtariFile(fname):
    with open(fname, "rb") as fp:
        magic_word = readWord(fp)
        first = readWord(fp)
        last = readWord(fp)
        if magic_word != 0xFFFF:
            raise Exception("%s is not an Atari binary file!got bytes %s, %s"%(fname, magic_word / 256, magic_word & 255))
        else:
            if first != None and last != None:
                size = 1 +last - first
                chars = fp.read(size)
                bytes = [ord(car) for car in chars]
                if len(bytes) == size:
                    return first, bytes
                else:
                    raise Exception("unexpected end of file %s!"%fname)
            else:
                raise Exception("unexpected end of file %s!"%fname)

def xx__getArgumentParserParams(args):
    ap = ARGUMENTS()
    ap.addArgument(ARGUMENT('-ifname', str, check_minus=True))  # input file to assemble
    ap.addArgument(ARGUMENT('-debug'))   # useful for programer only
    ap.addArgument(ARGUMENT('-nb_cols', int))  # number of columns of the bytes generator
    ap.addArgument(ARGUMENT('-org', int, check_minus=True))  # start address of code segment
    ap.parse(args)
    return ap.getArgsDictionary()

def saveBytes(fname, bytes):
    with open(fname, "wb") as fp:
        for byte in bytes:
            fp.write(chr(byte))

def getLineWord(assembler, line_num, item, strict=False):
    lines = assembler.getAsmLines()
    if line_num < len(lines):
        line = lines[line_num]
        words = line.getWords()
        if type(item) == int:
            if item < len(words):
                word = words[item]
                return word
            else:
                if strict:
                    raise Exception("bad word_num:%d line has %d words"%(item, len(lines)))
                else:
                    return None
        elif type(item) == str:
            for word in words:
                if word.getLabel() == item:
                    return word
            if strict:
                raise Exception("word with label '%s' not found"%(item))
            else:
                return None
    else:
        if strict:
            raise Exception("bad line_num:%d source has %d lines"%(line_num, len(lines)))
        else:
            return None

def getGlobalWord(assembler, word_label, strict=False):
        return assembler.getWord(word_label, strict=strict)

def getException(hook, *args, **kwds):
    try:
        hook(*args, **kwds)
        return False
    except:
        return True

def compareBinaries(refname, assembler):
    # let's compare bytes with reference file's bytes assembled with atasm
    ref_start, ref_bytes = readAtariFile(refname)
    ref_buffer = BUFFER(ref_bytes)

    # test continuity
    pc = ref_start
    for line in assembler.getAsmLines():
        if line.getBytes() != None:
            assert line.getAddress() == pc
            pc += len(line.getBytes())

    for line in assembler.getAsmLines():
        if line.getBytes() != None:
            for index, byte in enumerate(line.getBytes()):
                ref_byte = ref_buffer.get()
                if not "-silent" in sys.argv:
                    if ref_byte == None:
                        raise Exception("unexpected enf of reference file!")
                    
                    write("%04X "%(line.getAddress()+index))
                    if byte != ref_byte:
                        write("%02x <%02x> "%(ref_byte, byte))
                    else:
                        write("%02x  %02x "%(ref_byte, byte))
                    if not index:
                        write(line.getLine().getText())
                    writeln("")
                else:
                    assert ref_byte == byte

class BUFFER():
    def __init__(self,bytes):
        self.__bytes = bytes
        self.__ptr = 0
        
    def get(self):
        if len(self.__bytes) > self.__ptr:
            byte = self.__bytes[self.__ptr]
            self.__ptr += 1
            return byte
        else:
            return None

if __name__ == "__main__":

    def utest_getArguments():
        arguments = ('toto.py', ARG_IFNAME, '"toto.asm"', ARG_NB_COLS, '16', ARG_ORG, '0x600', ARG_DEBUG)
        args = getArguments(arguments, ('-ifname', '-nb_cols', '-org'))
        assert args[ARG_IFNAME] == 'toto.asm'
        assert args[ARG_NB_COLS] == 16
        assert args[ARG_ORG] == 1536
        assert args[ARG_DEBUG]
        assert args[ARG_IFNAME] == 'toto.asm'
        
    def test_solveExpression():
        
        fname = "utest/testfile.asm"
        makeFile(fname, [])
        args = ('toto.py', '-ifname', fname, '-nb_cols', '16', '-org', '0x600', '-debug')
        params = getArguments(args, ('-ifname', '-nb_cols', '-org'))
        info = SOURCE_LINE("None", "utest", 0)
 
        assembler = ASSEMBLER(params) 
        assert len(assembler.getAsmLines()) == 0
        
        words = []
        words.append(WORD("toto", TYPE_VARIABLE, value=3))
        words.append(WORD("+", TYPE_PONCTUATION, value='+'))
        words.append(WORD("titi", TYPE_VARIABLE, value=4))
        assert solveExpression(words, info) == 7
        
        word = WORD('toto', TYPE_VARIABLE, value='"azerty"')
        assert solveString(word, info) == (97, 122, 101, 114, 116, 121)

        word = WORD('toto', TYPE_VARIABLE, value='"abcde\\n"')
        assert solveString(word, info) == (97, 98, 99, 100, 101, 10)

        value='"µ\\x003345"'
        word = WORD('toto', TYPE_VARIABLE, value = value)
        assert solveString(word, info) == (194, 181, 0, 51, 51, 52, 53)

        value='123'
        word = WORD('toto', TYPE_VARIABLE, value = value)
        assert solveString(word, info) == None

        fname = "utest/testfile.asm"
        makeFile(fname, ['100 start', '110  jsr stop', '120  jmp start', '130 stop: ', ' nop'])
        args = ('toto.py', '-ifname', fname, '-nb_cols', '16', '-org', '0x600', '-debug-')
        params = getArguments(args, ('-ifname', '-nb_cols', '-org'))
        info = SOURCE_LINE("None", "utest", 0)

        assembler = ASSEMBLER(params) 
        assert len(assembler.getAsmLines()) == 5
        assembler.assemble()
        
        assert getLineWord(assembler, 0, 0, strict=False).isSolved()
        assert not getLineWord(assembler, 1, 1, strict=False).isSolved()
        assert getLineWord(assembler, 1, 2, strict=False).isSolved()
        
        assembler.assemble()
        assert getLineWord(assembler, 0, 0, strict=False).isSolved()
        assert getLineWord(assembler, 1, 1, strict=False).isSolved()
        assert getLineWord(assembler, 1, 2, strict=False).isSolved()

    def test_assemblyShort():
        fname = "utest/test_jmp_indirect_atasm.asm"
        args = ('toto.py', '-ifname', fname, '-nb_cols', '16')
        params = getArguments(args, ('-ifname', '-nb_cols', '-org'))

        assembler = ASSEMBLER(params)
        assembler.assemble()
        assembler.assemble()
        assembler.reset()
        assembler.assemble()
        assembler.assemble()

        compareBinaries("utest/TEST_JMP_INDIRECT_ATASM.BIN", assembler)
        
    def test_assembly():
        fname = "utest/test_opcodes_asm_cmp_cc65.asm"
        args = ('toto.py', '-ifname', fname, '-nb_cols', '16')
        params = getArguments(args, ('-ifname', '-nb_cols', '-org'))

        assembler = ASSEMBLER(params)
        assembler.assemble()
        assembler.assemble()
        assembler.reset()
        assembler.assemble()
        assembler.assemble()
        
        compareBinaries("utest/TEST_OPCODES_CC65_FLAT.BIN", assembler)

    def test_tables ():
        import tables6502

        # testing each opcode of the tables with a reference table.
        ref_table = getRefTable()

        for x in range(256):
            # testing each opcode of the tables with a reference table.
            if len(ref_table[x]) == 3:
                ref_opcode = ref_table[x][1]
                ref_mode   = ref_table[x][2]
            else:
                ref_opcode = "---"
                ref_mode   = "---"
            
            if tables6502.OPCODE_VALUES[x] == None:
                ut_opcode  = "---"
                ut_mode    = "---"
            else:
                ut_opcode  = tables6502.OPCODE_VALUES[x].upper()
                ut_mode    = tables6502.MODES[x].upper()
            
            if (ref_opcode != ut_opcode) or (ref_mode != ut_mode):
                raise Exception("Difference: %0X %s %-12s %s %-12s"%(x, ref_opcode, ref_mode, ut_opcode, ut_mode))

        fname = "utest/testfile.asm"
        makeFile(fname, [' STY $03,X', ' STX $0E,Y', ' jmp($1234)', ' nop'])
        args = ('toto.py', '-ifname', fname, '-nb_cols', '16', '-org', '0x600')
        params = getArguments(args, ('-ifname', '-nb_cols', '-org'))
        info = SOURCE_LINE("None", "utest", 0)
 
        assembler = ASSEMBLER(params) 
        assert len(assembler.getAsmLines()) == 4
        
        assembler.assemble()
        assembler.assemble()
        assembler.reset()
        assembler.assemble()
        assembler.assemble()
        assert assembler.getBytes() == [148, 3, 150, 14, 0x6c , 0x34, 0x12, 234]

    def test_getOpcodeValue():
        # with a mnemonic and an addressing mode, getOpcodeValue return the matching opcode
        
        fname = "utest/test_opcodes.asm"
        args = ('toto.py', '-ifname', fname, '-nb_cols', '16', '-org', '0x600')
        params = getArguments(args, ('-ifname', '-nb_cols', '-org'))
 
        ref_table = getRefTable()
        info = SOURCE_LINE("None", "utest", 0)
        
        for x in range(256):
            line = ref_table[x]
            ref_opcode = int("0x%s"%line[0], 16)
            if len(line) == 3:
                # opcode exists for the 6502
                ref_mnemo =  line[1].lower()
                ref_mode =  line[2].lower()
                mnemo = OPCODE_VALUES[x]
                mode = MODES[x]
                opcode = getOpcodeValue(mnemo, mode, info, strict=False)
                if opcode != ref_opcode:
                    raise Exception("\nreference      : %s %s %02x\ngetOpcodeValue : %s %s %s"%(ref_mnemo, ref_mode, ref_opcode, mnemo, mode, opcode))
            else:
                # opcode doesn't exist for the 6502
                pass

    def test_createAsmLines(fp=sys.stdout):
        fname = "utest/empty.asm"
        makeFile(fname, [])
        args = ('toto.py', '-ifname', fname, '-nb_cols', '16', '-org', '0x600')
        params = getArguments(args, ('-ifname', '-nb_cols', '-org'))
        info = SOURCE_LINE("None", "utest", 0)
 
        assembler = ASSEMBLER(params) 
        assert len(assembler.getAsmLines()) == 0
        assert len(assembler.getSourceLines()) == 0
        assert len(assembler.getWords()) == 0
        
        word1 = assembler.addWord(WORD("toto", wtype=TYPE_VARIABLE, value=133), strict=True)
        assert len(assembler.getWords()) == 1
        assert word1.get() == 133
        assert word1.getType() == TYPE_VARIABLE
        
        word2 = assembler.addWord(WORD("titi", wtype=TYPE_VARIABLE, value=None), strict=True)
        assert len(assembler.getWords()) == 2
        
        word3 = assembler.addWord(WORD("toto", wtype=TYPE_VARIABLE, value=None), strict=True)
        assert len(assembler.getWords()) == 2
        
        word4 = WORD("dummy", wtype=TYPE_OPCODE, value=None)
        assert len(assembler.getWords()) == 2
        
        assert getException(assembler.addWord, word4, strict=True) 
        assert len(assembler.getWords()) == 2
        word4 = assembler.addWord(WORD("dummy", wtype=TYPE_OPCODE, value=None), strict=False)
        assert len(assembler.getWords()) == 2
        
        assert assembler.getWord("toto").get() == 133

        assembler.getWord("toto").set(246)
        assert assembler.getWord("toto").get() == 246
        assert word1.get() == 246
        assert word3.get() == 246
        assert word2.get() == None
        
        word1.set(369)
        assert assembler.getWord("toto").get() == 369
        assert word1.get() == 369
        assert word3.get() == 369
        assert word2.get() == None

        fname = "utest/empty.asm"
        makeFile(fname, [' .byte 33,34,35,36,37'])
        args = ('toto.py', '-ifname', fname, '-nb_cols', '16', '-org', '0x600')
        params = getArguments(args, ('-ifname', '-nb_cols', '-org'))
        info = SOURCE_LINE("None", "utest", 0)
        
        assembler = ASSEMBLER(params) 
        line = assembler.getAsmLine(0)
        words = line.getWords()
        assert len(words) == 11
        assert getLineWord(assembler, 0, 10, strict=False).getLabel() == '37'
        
        # testing automatic deletion of last word if it's a comma
        fname = "utest/empty.asm"
        makeFile(fname, [' .byte 33,34,35,36,37 ,'])
        args = ('toto.py', '-ifname', fname, '-nb_cols', '16', '-org', '0x600')
        params = getArguments(args, ('-ifname', '-nb_cols', '-org'))
        info = SOURCE_LINE("None", "utest", 0)
        
        assembler = ASSEMBLER(params) 
        line = assembler.getAsmLine(0)
        words = line.getWords()
        assert len(words) == 12
        assert getLineWord(assembler, 0, 10, strict=False).getLabel() == '37'

    def test_AsmLine_hasLabel():
        fname = "utest/testfile.asm"
        makeFile(fname, ['start stop', '  start', '', '', ' start', 'stop'])
        args = ('toto.py', '-ifname', fname, '-nb_cols', '16', '-org', '0x600')
        params = getArguments(args, ('-ifname', '-nb_cols', '-org'))
        info = SOURCE_LINE("None", "utest", 0)
 
        assembler = ASSEMBLER(params) 
        assert len(assembler.getAsmLines()) == 4
        lines = assembler.getAsmLines()
        assert lines[0].hasLabel()
        assert not lines[1].hasLabel()
        assert not lines[2].hasLabel()
        assert lines[3].hasLabel()
        
        word = getGlobalWord(assembler, "start")
        word.set(2503)
        assert getLineWord(assembler, 0, 0).get() == 2503
        assert getLineWord(assembler, 1, 1).get() == 2503
        assert getLineWord(assembler, 2, 1).get() == 2503
        
        word = getGlobalWord(assembler, "stop")
        word.set(1234)
        assert getLineWord(assembler, 0, 1).get() == 1234
        assert getLineWord(assembler, 3, 0).get() == 1234

    def test_AsmLine_isMnemonicLine():
        fname = "utest/testfile.asm"
        makeFile(fname, ['start nop', '  beq $600', '', '', ' start', 'stop jmp start'])
        args = ('toto.py', '-ifname', fname, '-nb_cols', '16', '-org', '0x600')
        params = getArguments(args, ('-ifname', '-nb_cols', '-org'))
        info = SOURCE_LINE("None", "utest", 0)
 
        assembler = ASSEMBLER(params) 
        assert len(assembler.getAsmLines()) == 4
        lines = assembler.getAsmLines()
        assert lines[0].isMnemonicLine()
        assert lines[1].isMnemonicLine()
        assert not lines[2].isMnemonicLine()
        assert lines[3].isMnemonicLine()

    def test_AsmLine_isDirectiveLine():
        fname = "utest/testfile.asm"
        makeFile(fname, ['start nop', '  beq $600', 'hellomes .string "Hello, World!\\n"', ' .byte 12,12,15,15', ' start', 'stop jmp start'])
        args = ('toto.py', '-ifname', fname, '-nb_cols', '16', '-org', '0x600')
        params = getArguments(args, ('-ifname', '-nb_cols', '-org'))
        info = SOURCE_LINE("None", "utest", 0)
 
        assembler = ASSEMBLER(params) 
        assert len(assembler.getAsmLines()) == 6
        lines = assembler.getAsmLines()
        assert not lines[0].isDirectiveLine()
        assert not lines[1].isDirectiveLine()
        assert lines[2].isDirectiveLine()
        assert lines[3].isDirectiveLine()
        assert not lines[4].isDirectiveLine()
        assert not lines[5].isDirectiveLine()

    def test_AsmLine_isAffectationLine():
        fname = "utest/testfile.asm"
        makeFile(fname, [' start=3', 'start nop', '  beq $600 + $12 -7', 'hellomes .string "Hello, World!\\n"', ' .byte 12,12,15,15', ' start =', ' stop = 12', 'stop jmp start'])
        args = ('toto.py', '-ifname', fname, '-nb_cols', '16', '-org', '0x600')
        params = getArguments(args, ('-ifname', '-nb_cols', '-org'))
        info = SOURCE_LINE("None", "utest", 0)
 
        assembler = ASSEMBLER(params) 
        assert len(assembler.getAsmLines()) == 8
        lines = assembler.getAsmLines()
        assert lines[0].isAffectationLine()
        assert not lines[5].isAffectationLine()
        assert lines[6].isAffectationLine()

    def test_computeRelative():
        fname = "utest/testfile.asm"
        makeFile(fname, [' beq $600 - 100 + 100', ' beq $600', ' beq $600', ' beq $1234', ' beq $600'])
        args = ('toto.py', '-ifname', fname, '-nb_cols', '16', '-org', '0x600')
        params = getArguments(args, ('-ifname', '-nb_cols', '-org'))
        info = SOURCE_LINE("None", "utest", 0)
 
        assembler = ASSEMBLER(params) 
        assert len(assembler.getAsmLines()) == 5

        assert getLineWord(assembler, 0, 2).get() == 0x600
        assert getLineWord(assembler, 0, 4).get() == 100
        assert getLineWord(assembler, 0, 6).get() == 100
        assert getLineWord(assembler, 1, 2).get() == 0x600
        assert getLineWord(assembler, 2, 2).get() == 0x600

        assembler.assemble()

        target = 0xfe
        pc = 0x600
        for line_num in range(3):
            assert len(assembler.getAsmLine(line_num).getWords()) == 3
            assert assembler.getAsmLine(line_num).getWords()[1].get() == 0xf0
            if line_num == 0:
                assert assembler.getAsmLine(line_num).getWords()[2].get() != None
            assert assembler.getAsmLine(line_num).getBytes() == (0xf0, target)
            assert assembler.getAsmLine(line_num).getAddress() == pc
            target -= 2
            pc += 2

        pc = 0x600
        for line_num in range(3, 5):
            assert assembler.getAsmLine(line_num).getAddress() == pc + line_num * 2

    def test_computeImplied():
        fname = "utest/testfile.asm"
        makeFile(fname, [' nop', ' clc', ' inX', ' tAy', ' tAy 33'])
        args = ('toto.py', '-ifname', fname, '-nb_cols', '16', '-org', '0x600')
        params = getArguments(args, ('-ifname', '-nb_cols', '-org'))
        info = SOURCE_LINE("None", "utest", 0)
 
        assembler = ASSEMBLER(params) 
        assert len(assembler.getAsmLines()) == 5
        lines = assembler.getAsmLines()

        assembler.assemble()
        
        assert assembler.getAsmLine(0).getBytes() == (0xea,)
        assert assembler.getAsmLine(1).getBytes() == (0x18,)
        assert assembler.getAsmLine(2).getBytes() == (0xe8,)
        assert assembler.getAsmLine(3).getBytes() == (0xa8,)
        for index in range(5):
            assert assembler.getAsmLine(index).getAddress() == 0x600 + index
            
    def test_computeAccumulator():
        fname = "utest/testfile.asm"
        makeFile(fname, [' LSR A', ' ASL    A', '    ROL A', ' ror a'])
        args = ('toto.py', '-ifname', fname, '-nb_cols', '16', '-org', '0x600')
        params = getArguments(args, ('-ifname', '-nb_cols', '-org'))
        info = SOURCE_LINE("None", "utest", 0)
 
        assembler = ASSEMBLER(params) 
        assert len(assembler.getAsmLines()) == 4

        assembler.assemble()

        assert assembler.getAsmLine(0).getBytes() == (0x4a,)
        assert assembler.getAsmLine(1).getBytes() == (0x0a,)
        assert assembler.getAsmLine(2).getBytes() == (0x2a,)
        assert assembler.getAsmLine(3).getBytes() == (0x6a,)
        for index in range(4):
            assert assembler.getAsmLine(index).getAddress() == 0x600 + index

        
    def test_computeImmediate():
        fname = "utest/testfile.asm"
        makeFile(fname, [' lda #12', ' ldx #$12', '  sbc #44', ' ldx #$122', '  sbc #48'])
        args = ('toto.py', '-ifname', fname, '-nb_cols', '16', '-org', '0x600')
        params = getArguments(args, ('-ifname', '-nb_cols', '-org'))
        info = SOURCE_LINE("None", "utest", 0)
 
        assembler = ASSEMBLER(params) 
        assert len(assembler.getAsmLines()) == 5

        assembler.assemble()

        assert assembler.getAsmLine(0).getBytes() == (0xa9, 12)
        assert assembler.getAsmLine(1).getBytes() == (0xa2, 0x12)
        assert assembler.getAsmLine(2).getBytes() == (0xe9, 44)
        for index in range(5):
            assert assembler.getAsmLine(index).getAddress() == 0x600 + index * 2

    def test_computeIndirecty():
        fname = "utest/testfile.asm"
        makeFile(fname, ['  sbc ($45), Y', ' lda (33),y', ' cmp ($44),y', '  sbc ($45), Y', '  sbc ($45), Y', '  sbc ($454), Y', '  sbc ($45), Y'])
        args = ('toto.py', '-ifname', fname, '-nb_cols', '16', '-org', '0x600', '-debug-')
        params = getArguments(args, ('-ifname', '-nb_cols', '-org'))
        info = SOURCE_LINE("None", "utest", 0)
 
        assembler = ASSEMBLER(params) 
        assert len(assembler.getAsmLines()) == 7

        assembler.assemble()
        assert assembler.getAsmLine(0).getBytes() == (0xf1, 0x45)
        assert assembler.getAsmLine(1).getBytes() == (0xb1, 0x21)
        assert assembler.getAsmLine(2).getBytes() == (0xd1, 0x44)
        assert assembler.getAsmLine(3).getBytes() == (0xf1, 0x45)
        assert assembler.getAsmLine(4).getBytes() == (0xf1, 0x45)
        for index in range(7):
            assert assembler.getAsmLine(index).getAddress() == 0x600 + index * 2

    def test_computeIndirectx():
        fname = "utest/testfile.asm"
        makeFile(fname, ['  sbc ($45, x)', ' lda (33, x)', ' cmp ($44, x)', '  sbc ($45, x)', '  sbc ($45, x)', '  sbc ($456, x)', '  sbc ($45, x)'])
        args = ('toto.py', '-ifname', fname, '-nb_cols', '16', '-org', '0x600', '-debug-')
        params = getArguments(args, ('-ifname', '-nb_cols', '-org'))
        info = SOURCE_LINE("None", "utest", 0)
 
        assembler = ASSEMBLER(params) 
        assert len(assembler.getAsmLines()) == 7

        assembler.assemble()
        assert assembler.getAsmLine(0).getBytes() == (0xe1, 0x45)
        assert assembler.getAsmLine(1).getBytes() == (0xa1, 0x21)
        assert assembler.getAsmLine(2).getBytes() == (0xc1, 0x44)
        assert assembler.getAsmLine(3).getBytes() == (0xe1, 0x45)
        assert assembler.getAsmLine(4).getBytes() == (0xe1, 0x45)
        for index in range(7):
            assert assembler.getAsmLine(index).getAddress() == 0x600 + index * 2

    def test_computeIndirect():
        fname = "utest/testfile.asm"
        makeFile(fname, ['  jmp ($1234)', '  jmp ($5678)', '  jmp ($90ab)', '  jmp ($2468)', '  jmp ($90abc)', '  jmp ($2468)', ])
        args = ('toto.py', '-ifname', fname, '-nb_cols', '16', '-org', '0x600', '-debug-')
        params = getArguments(args, ('-ifname', '-nb_cols', '-org'))
        info = SOURCE_LINE("None", "utest", 0)
 
        assembler = ASSEMBLER(params) 
        assert len(assembler.getAsmLines()) == 6

        assembler.assemble()
        assert assembler.getAsmLine(0).getBytes() == (0x6c, 0x34, 0x12)
        assert assembler.getAsmLine(1).getBytes() == (0x6c, 0x78, 0x56)
        assert assembler.getAsmLine(2).getBytes() == (0x6c, 0xab, 0x90)
        assert assembler.getAsmLine(3).getBytes() == (0x6c, 0x68, 0x24)
        for index in range(6):
            assert assembler.getAsmLine(index).getAddress() == 0x600 + index * 3

    def test_computeAbsolute():
        fname = "utest/testfile.asm"
        makeFile(fname, ['  lda $1234', '  sta $4567', '  jmp $90ab', '  jmp $2468', '  jmp $980ab', '  jmp $2468', 'jmp toto'])
        args = ('toto.py', '-ifname', fname, '-nb_cols', '16', '-org', '0x600', '-debug-')
        params = getArguments(args, ('-ifname', '-nb_cols', '-org'))
        info = SOURCE_LINE("None", "utest", 0)
 
        assembler = ASSEMBLER(params) 
        assert len(assembler.getAsmLines()) == 7

        assembler.assemble()
        assert assembler.getAsmLine(0).getBytes() == (0xad, 0x34, 0x12)
        assert assembler.getAsmLine(1).getBytes() == (0x8d, 0x67, 0x45)
        assert assembler.getAsmLine(2).getBytes() == (0x4c, 0xab, 0x90)
        assert assembler.getAsmLine(3).getBytes() == (0x4c, 0x68, 0x24)
        for index in range(6):
            assert assembler.getAsmLine(index).getAddress() == 0x600 + index * 3

    def test_computeAbsoluteX():
        fname = "utest/testfile.asm"
        makeFile(fname, ['  lda $1234, x', '  sta $4567, x', '  adc $4321, x', '  and $8765, x', '  adc $43210, x', '  and $8765, x', ])
        args = ('toto.py', '-ifname', fname, '-nb_cols', '16', '-org', '0x600', '-debug-')
        params = getArguments(args, ('-ifname', '-nb_cols', '-org'))
        info = SOURCE_LINE("None", "utest", 0)
 
        assembler = ASSEMBLER(params) 
        assert len(assembler.getAsmLines()) == 6

        assembler.assemble()
        assert assembler.getAsmLine(0).getBytes() == (0xbd, 0x34, 0x12)
        assert assembler.getAsmLine(1).getBytes() == (0x9d, 0x67, 0x45)
        assert assembler.getAsmLine(2).getBytes() == (0x7d, 0x21, 0x43)
        assert assembler.getAsmLine(3).getBytes() == (0x3d, 0x65, 0x87)
        for index in range(6):
            assert assembler.getAsmLine(index).getAddress() == 0x600 + index * 3

    def test_computeAbsoluteY():
        fname = "utest/testfile.asm"
        makeFile(fname, ['  lda $1234, y', '  sta $4567, y', '  adc $4321, y', '  and $8765, y', '  adc $43210, y', '  and $8765, y', ])
        args = ('toto.py', '-ifname', fname, '-nb_cols', '16', '-org', '0x600', '-debug-')
        params = getArguments(args, ('-ifname', '-nb_cols', '-org'))
        info = SOURCE_LINE("None", "utest", 0)
 
        assembler = ASSEMBLER(params) 
        assert len(assembler.getAsmLines()) == 6

        assembler.assemble()
        assert assembler.getAsmLine(0).getBytes() == (0xb9, 0x34, 0x12)
        assert assembler.getAsmLine(1).getBytes() == (0x99, 0x67, 0x45)
        assert assembler.getAsmLine(2).getBytes() == (0x79, 0x21, 0x43)
        assert assembler.getAsmLine(3).getBytes() == (0x39, 0x65, 0x87)
        for index in range(6):
            assert assembler.getAsmLine(index).getAddress() == 0x600 + index * 3

    def test_computeAffectation():
        fname = "utest/testfile.asm"
        makeFile(fname, [' result = b + c', ' b = 3 * c', '  c = 12'])
        args = ('toto.py', '-ifname', fname, '-nb_cols', '16', '-org', '0x600')
        params = getArguments(args, ('-ifname', '-nb_cols', '-org'))
        info = SOURCE_LINE("None", "utest", 0)
 
        assembler = ASSEMBLER(params) 
        assert len(assembler.getAsmLines()) == 3

        #solving c
        assembler.assemble()
        assert assembler.getAsmLine(2).getWords()[1].get() == 12
        assert len(assembler.getAsmLine(2).getWords()) == 2
        assert assembler.getAsmLine(0).getWords()[5].get() == 12

        #solving b
        assembler.assemble()
        assert assembler.getAsmLine(1).getWords()[1].get() == 36
        assert len(assembler.getAsmLine(1).getWords()) == 2
        assert assembler.getAsmLine(0).getWords()[3].get() == 36

        #solving result
        assembler.assemble()
        assert assembler.getAsmLine(0).getWords()[1].get() == 48
        assert len(assembler.getAsmLine(0).getWords()) == 2

    def test_computeByte():
        fname = "utest/testfile.asm"
        makeFile(fname, [' toto = 6','  .byte >256, >512, >768, ', '  .byte 4, 5, toto, ', ' .byte 7, 8, toto + 3,', ' .byte 10, 11, titi + 3,', ' .byte 1234', ' .byte 14'])
        args = ('toto.py', '-ifname', fname, '-nb_cols', '16', '-org', '0x600', '-debug-')
        params = getArguments(args, ('-ifname', '-nb_cols', '-org'))
        info = SOURCE_LINE("None", "utest", 0)
 
        assembler = ASSEMBLER(params) 
        assert len(assembler.getAsmLines()) == 7
        lines = assembler.getAsmLines()
        
        assert len(lines[0].getWords()) == 4
        assert len(lines[1].getWords()) == 11
        assert len(lines[2].getWords()) == 8
        assert len(lines[3].getWords()) == 10

        assembler.assemble()
        
        assert lines[1].getBytes() == (1,2,3)
        assert lines[2].getBytes() == (4,5,6)
        assert lines[3].getBytes() == (7,8,9)
        assert lines[4].getBytes() == None

        assert lines[1].getAddress() == 1536
        assert lines[2].getAddress() == 1539
        assert lines[3].getAddress() == 1542
        assert lines[4].getAddress() == 1545
        assert lines[5].getAddress() == 1548
        assert lines[6].getAddress() == 1549

    def test_computeWord():
        fname = "utest/testfile.asm"
        makeFile(fname, [' toto = 6','  .word 3 * 3 - 8, 2, 3, ', '  .word 4, 5, toto, ', ' .word 7, 8, toto + 3,', ' .word 10, 11, titi + 3,', ' .word 1234', ' .word 14'])
        args = ('toto.py', '-ifname', fname, '-nb_cols', '16', '-org', '0x600', '-debug-')
        params = getArguments(args, ('-ifname', '-nb_cols', '-org'))
        info = SOURCE_LINE("None", "utest", 0)
 
        assembler = ASSEMBLER(params) 
        assert len(assembler.getAsmLines()) == 7
        lines = assembler.getAsmLines()
        
        assert len(lines[0].getWords()) == 4
        assert len(lines[1].getWords()) == 12
        assert len(lines[2].getWords()) == 8
        assert len(lines[3].getWords()) == 10

        assembler.assemble()
        
        assert lines[1].getBytes() == (1,0,2,0,3,0)
        assert lines[2].getBytes() == (4,0,5,0,6,0)
        assert lines[3].getBytes() == (7,0,8,0,9,0)
        assert lines[4].getBytes() == None

        assert lines[1].getAddress() == 1536
        assert lines[2].getAddress() == 1542
        assert lines[3].getAddress() == 1548
        assert lines[4].getAddress() == 1554
        assert lines[5].getAddress() == 1560
        assert lines[6].getAddress() == 1562

    def test_computeDbyte():
        fname = "utest/testfile.asm"
        makeFile(fname, [' toto = 6','  .dbyte 1, 2, 3, ', '  .dbyte 4, 5, toto, ', ' .dbyte 7, 8, toto + 3,', ' .dbyte 10, 11, titi + 3,', ' .dbyte 1234', ' .dbyte 14'])
        args = ('toto.py', '-ifname', fname, '-nb_cols', '16', '-org', '0x600', '-debug-')
        params = getArguments(args, ('-ifname', '-nb_cols', '-org'))
        info = SOURCE_LINE("None", "utest", 0)
 
        assembler = ASSEMBLER(params) 
        assert len(assembler.getAsmLines()) == 7
        lines = assembler.getAsmLines()
        
        assert len(lines[0].getWords()) == 4
        assert len(lines[1].getWords()) == 8
        assert len(lines[2].getWords()) == 8
        assert len(lines[3].getWords()) == 10

        assembler.assemble()
        
        assert lines[1].getBytes() == (0,1,0,2,0,3)
        assert lines[2].getBytes() == (0,4,0,5,0,6)
        assert lines[3].getBytes() == (0,7,0,8,0,9)
        assert lines[4].getBytes() == None

        assert lines[1].getAddress() == 1536
        assert lines[2].getAddress() == 1542
        assert lines[3].getAddress() == 1548
        assert lines[4].getAddress() == 1554
        assert lines[5].getAddress() == 1560
        assert lines[6].getAddress() == 1562

    def test_computeString():
        fname = "utest/testfile.asm"
        makeFile(fname, [' toto = 6','  .string "abc\\x00def"', '  .string "0123456\\n"', ' nop'])
        args = ('toto.py', '-ifname', fname, '-nb_cols', '16', '-org', '0x600', '-debug-')
        params = getArguments(args, ('-ifname', '-nb_cols', '-org'))
        info = SOURCE_LINE("None", "utest", 0)
 
        assembler = ASSEMBLER(params) 
        assert len(assembler.getAsmLines()) == 4
        lines = assembler.getAsmLines()
        
        assert len(lines[0].getWords()) == 4
        assert len(lines[1].getWords()) == 3
        assert len(lines[2].getWords()) == 3
        assert len(lines[3].getWords()) == 2

        assembler.assemble()

        assert lines[1].getBytes() == (97, 98, 99, 0, 100, 101, 102, 0)
        assert lines[2].getBytes() == (48, 49, 50, 51, 52, 53, 54, 10, 0)
        assert lines[1].getAddress() == 0x600
        assert lines[2].getAddress() == 0x608
        assert lines[3].getAddress() == 0x611

    def test_computeChArray():
        fname = "utest/testfile.asm"
        makeFile(fname, [' toto = 6','  .ch_array "abc\\x00def"', '  .ch_array "0123456\\n"', ' nop'])
        args = ('toto.py', '-ifname', fname, '-nb_cols', '16', '-org', '0x600', '-debug-')
        params = getArguments(args, ('-ifname', '-nb_cols', '-org'))
        info = SOURCE_LINE("None", "utest", 0)
 
        assembler = ASSEMBLER(params) 
        assert len(assembler.getAsmLines()) == 4
        lines = assembler.getAsmLines()
        
        assert len(lines[0].getWords()) == 4
        assert len(lines[1].getWords()) == 3
        assert len(lines[2].getWords()) == 3
        assert len(lines[3].getWords()) == 2

        assembler.assemble()

        assert lines[1].getBytes() == (97, 98, 99, 0, 100, 101, 102)
        assert lines[2].getBytes() == (48, 49, 50, 51, 52, 53, 54, 10)
        assert lines[1].getAddress() == 0x600
        assert lines[2].getAddress() == 0x607
        assert lines[3].getAddress() == 0x60f

    def test_computeDbs():
        fname = "utest/testfile.asm"
        makeFile(fname, [' a0 = b', ' .dbs 3', ' .dbs 4', ' .dbs 5', ' .dbs 6', ' nop'])
        args = ('toto.py', '-ifname', fname, '-nb_cols', '16', '-org', '0x600', '-debug-')
        params = getArguments(args, ('-ifname', '-nb_cols', '-org'))
        info = SOURCE_LINE("None", "utest", 0)
 
        assembler = ASSEMBLER(params) 
        assert len(assembler.getAsmLines()) == 6
        lines = assembler.getAsmLines()
        
        assert len(lines[0].getWords()) == 4
        assert len(lines[1].getWords()) == 3
        assert len(lines[2].getWords()) == 3
        assert len(lines[3].getWords()) == 3
        assert len(lines[4].getWords()) == 3

        assembler.assemble()

        assert lines[1].getBytes() == (0,0,0)
        assert lines[2].getBytes() == (0,0,0,0)
        assert lines[3].getBytes() == (0,0,0,0,0)
        assert lines[4].getBytes() == (0,0,0,0,0,0)
        assert lines[1].getAddress() == 0x600
        assert lines[2].getAddress() == 0x603
        assert lines[3].getAddress() == 0x607
        assert lines[4].getAddress() == 0x60c
        assert lines[5].getAddress() == 0x612

    def test_computeDws():
        fname = "utest/testfile.asm"
        makeFile(fname, [' a0 = b', ' .dws 3', ' .dws 4', ' .dws 5', ' .dws 6', ' nop'])
        args = ('toto.py', '-ifname', fname, '-nb_cols', '16', '-org', '0x600', '-debug-')
        params = getArguments(args, ('-ifname', '-nb_cols', '-org'))
        info = SOURCE_LINE("None", "utest", 0)
 
        assembler = ASSEMBLER(params) 
        assert len(assembler.getAsmLines()) == 6
        lines = assembler.getAsmLines()
        
        assert len(lines[0].getWords()) == 4
        assert len(lines[1].getWords()) == 3
        assert len(lines[2].getWords()) == 3
        assert len(lines[3].getWords()) == 3
        assert len(lines[4].getWords()) == 3

        assembler.assemble()

        assert lines[1].getBytes() == (0,0,0,0,0,0)
        assert lines[2].getBytes() == (0,0,0,0,0,0,0,0)
        assert lines[3].getBytes() == (0,0,0,0,0,0,0,0,0,0)
        assert lines[4].getBytes() == (0,0,0,0,0,0,0,0,0,0,0,0)
        assert lines[1].getAddress() == 0x600
        assert lines[2].getAddress() == 0x606
        assert lines[3].getAddress() == 0x60e
        assert lines[4].getAddress() == 0x618
        assert lines[5].getAddress() == 0x624
    
    def test_getModesByMnemonic():
        assert getModesByMnemonic("nop") == ('Implied',)
        assert getModesByMnemonic("lda") == ('IndirectX', 'ZeroPage', 'Immediate', 'Absolute', 'IndirectY', 'ZeroPageX', 'AbsoluteY', 'AbsoluteX')
    
    def test_isByte():
        word = WORD("toto", TYPE_OPCODE, '0')
        assert not word.isByte()
        
        word = WORD("toto", TYPE_VARIABLE)
        assert not word.isByte()
        
        word = WORD("toto", TYPE_VARIABLE, -1)
        assert not word.isByte()
        
        for x in [65536, 300, 256, -100, -1]:
            word = WORD("toto", TYPE_VARIABLE, x)
            assert not word.isByte()
        
        for x in range(256):
            word = WORD("toto", TYPE_VARIABLE, x)
            assert word.isByte()

    def test_isZeroPage():
        fname = "utest/testfile.asm"
        makeFile(fname, ['  lda $1234', '  lda $45', '  nop', ])
        args = ('toto.py', '-ifname', fname, '-nb_cols', '16', '-org', '0x600', '-debug-')
        params = getArguments(args, ('-ifname', '-nb_cols', '-org'))
        info = SOURCE_LINE("None", "utest", 0)
 
        assembler = ASSEMBLER(params) 
        assembler.assemble()
        
        assert len(assembler.getAsmLines()) == 3
        
        line = assembler.getAsmLine(0)
        assert line.isAbsolute()
        assert not line.isZeroPage()
        assert line.getAddress() == 0x600

        line = assembler.getAsmLine(1)
        assert line.isAbsolute()
        assert line.isZeroPage()
        assert line.getAddress() == 0x603

    def test_isZeroPageX():
        fname = "utest/testfile.asm"
        makeFile(fname, ['  lda $1234,x', '  lda $45,x', '  nop', ])
        args = ('toto.py', '-ifname', fname, '-nb_cols', '16', '-org', '0x600', '-debug-')
        params = getArguments(args, ('-ifname', '-nb_cols', '-org'))
        info = SOURCE_LINE("None", "utest", 0)
 
        assembler = ASSEMBLER(params) 
        assembler.assemble()
        
        assert len(assembler.getAsmLines()) == 3
        
        line = assembler.getAsmLine(0)
        
        assert line.isAbsoluteX()
        assert not line.isZeroPageX()
        assert line.getAddress() == 0x600

        line = assembler.getAsmLine(1)
        assert line.isAbsoluteX()
        assert line.isZeroPageX()
        assert line.getAddress() == 0x603

    def test_isZeroPageY():
        fname = "utest/testfile.asm"
        makeFile(fname, ['  lda $1234,y', '  lda $45,y', '  nop', ])
        args = ('toto.py', '-ifname', fname, '-nb_cols', '16', '-org', '0x600', '-debug-')
        params = getArguments(args, ('-ifname', '-nb_cols', '-org'))
        info = SOURCE_LINE("None", "utest", 0)
 
        assembler = ASSEMBLER(params) 
        assembler.assemble()
        
        assert len(assembler.getAsmLines()) == 3
        
        line = assembler.getAsmLine(0)
        
        assert line.isAbsoluteY()
        assert not line.isZeroPageY()
        assert line.getAddress() == 0x600

        line = assembler.getAsmLine(1)
        assert line.isAbsoluteY()
        assert not line.isZeroPageY() # lda $xx,y doesn't exists
        assert line.getAddress() == 0x603

    def test_truncator():
        fname = "utest/testfile.asm"
        makeFile(fname, ['  lda #>$1234', '  lda #<$1234', '  nop', ])
        args = ('toto.py', '-ifname', fname, '-nb_cols', '16', '-org', '0x600', '-debug-')
        params = getArguments(args, ('-ifname', '-nb_cols', '-org'))
        info = SOURCE_LINE("None", "utest", 0)
 
        assembler = ASSEMBLER(params) 
        assembler.assemble()
        
        assert len(assembler.getAsmLines()) == 3
        
        line = assembler.getAsmLine(0)
        
        assert line.getAddress() == 0x600
        assert line.getBytes()[1] == 0x12

        line = assembler.getAsmLine(1)
        assert line.getAddress() == 0x602
        assert line.getBytes()[1] == 0x34

        line = assembler.getAsmLine(2)
        assert line.getAddress() == 0x604

    def text_extractLabelsFromLine():
        fname = "utest/testfile.asm"
        makeFile(fname, ['100 start lda #>$1234', '200  lda #<$1234', '300  nop', ])
        args = ('toto.py', '-ifname', fname, '-nb_cols', '16', '-org', '0x600', '-debug-')
        params = getArguments(args, ('-ifname', '-nb_cols', '-org')) 
        assembler1 = ASSEMBLER(params) 

        makeFile(fname, ['start  lda #>$1234', ' lda #<$1234', ' nop', ])
        assembler2 = ASSEMBLER(params) 
        
        lines1 = assembler1.getAsmLines()
        lines2 = assembler2.getAsmLines()
        
        for ln in range(3):
            line1 = lines1[ln]
            line2 = lines2[ln]
            for x in range(len(line1.getWords())):
                word1 = line1.getWords()[x]
                word2 = line2.getWords()[x]
                assert word1.get() == word2.get()
                assert word1.getLabel() == word2.getLabel()
                assert word1.getType() == word2.getType()

    def utests():
        utest_getArguments()
        test_solveExpression()
        test_tables()
        test_getOpcodeValue()
        test_createAsmLines()
        test_AsmLine_hasLabel()
        test_AsmLine_isMnemonicLine()
        test_AsmLine_isDirectiveLine()
        test_AsmLine_isAffectationLine()
        test_computeRelative()
        test_computeImplied()
        test_computeAccumulator()
        test_computeImmediate()
        test_computeAffectation()
        test_computeIndirecty()
        test_computeIndirectx()
        test_computeIndirect()
        test_computeAbsolute()
        test_computeAbsoluteX()
        test_computeAbsoluteY()
        test_computeByte()
        test_computeWord()
        test_computeDbyte()
        test_computeString()
        test_computeChArray()
        test_computeDbs()
        test_computeDws()
        test_getModesByMnemonic()   
        test_isByte()
        test_isZeroPage()
        test_isZeroPageX()
        test_isZeroPageY()
        test_truncator()
        text_extractLabelsFromLine()
        test_assembly()
        test_assemblyShort()

    #~ stopDebugMode()
    #~ stopSilentMode()
    startSilentMode()
    #~ test_assembly()
    utests()
    sys.stdout.write("A L L   T E S T S   S U C C E S S F U L Y   P A S S E D !\n")
