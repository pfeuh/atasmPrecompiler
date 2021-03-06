#!/usr/bin/python
# -*- coding: utf-8 -*-

ap = None

import sys
import os

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

def getArgumentParserParams(asm, args):
    ap = asm.ARGUMENTS()
    asm.ap =  ap
    ap.addArgument(asm.ARGUMENT('-ifname', str, check_minus=True))  # input file to assemble
    ap.addArgument(asm.ARGUMENT('-debug'))   # useful for programer only
    ap.addArgument(asm.ARGUMENT('-nb_cols', int))  # number of columns of the bytes generator
    ap.addArgument(asm.ARGUMENT('-org', int, check_minus=True))  # start address of code segment
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

    def test_precompiler():
        import precompiler as pco
        write = pco.write
        writeln = pco.writeln
        LINE = pco.SOURCE_LINE
        getLabel = pco.getLabel
        removeComment = pco.removeComment
        extractWord = pco.extractWord
        commentLine = pco.commentLine
        labelIsOk = pco.labelIsOk

        assert labelIsOk("label")
        assert labelIsOk("_label")
        assert not labelIsOk("_")
        assert labelIsOk("_1")
        assert not labelIsOk("1234")
        assert not labelIsOk("1")
        assert labelIsOk("a1")
        assert not labelIsOk("1a")
        assert not labelIsOk("azerty;")
        assert not labelIsOk(";azerty")
        assert not labelIsOk("aze;rty")
        assert not labelIsOk("az erty;")
        assert labelIsOk("azerty")

        assert removeComment("   ; azerty") == ""
        assert removeComment("toto; azerty") == "toto"
        assert removeComment(" toto ; azerty") == " toto"
        assert removeComment(" toto     ; azerty") == " toto"
        assert removeComment(" ; ;toto ; azerty") == ""
        assert removeComment(" ; toto ; azerty") == ""
        assert removeComment('toto .string "azerty";"azerty"') == 'toto .string "azerty"'
        text = 'test5 ; .string "\\x00\\x01\\x02\\x03\\x04\\x05\\x06\\x07\\x08\\x09\\x0a\\x0b\\x0c\\x0d\\x0e\\x0f"'
        assert removeComment(text) == 'test5'
        text = 'toto .string "aze;rty"   "qwerty" ;   "uiop"'
        assert removeComment(text) == 'toto .string "aze;rty"   "qwerty"'
        # testing string not closed
        text = 'toto .string "aze;rty"   "qwerty ;   uiop'
        try:
            assert removeComment(text) == 'toto .string "aze;rty"   "qwerty"'
        except:
            pass
        else:
            raise Exception("there should have been an exception.")

        line = LINE("noname", "", 123)    

        line.setText("toto")    
        assert getLabel(line) == "toto"
        
        line.setText(";toto")    
        assert getLabel(line) == None
        
        line.setText(" toto")    
        assert getLabel(line) == None;
        
        line.setText(" toto;")    
        assert getLabel(line) == None
        
        line.setText("toto   ;")    
        assert getLabel(line) == "toto"

        line.setText("toto blablabla...  ;")    
        assert getLabel(line) == "toto"

        line.setText(";toto titi tata ; comment")    
        assert getLabel(line) == None

        line.setText("     ;toto titi tata ; comment")    
        assert getLabel(line) == None


        
        text = "label op1 op2 op3" 
        assert extractWord(text, 0) == "label"
        assert extractWord(text, 1) == "op1"
        assert extractWord(text, 2) == "op2"
        assert extractWord(text, 3) == "op3"
        
        text = " label op1 op2 op3" 
        assert extractWord(text, 1) == "label"
        assert extractWord(text, 2) == "op1"
        
        text = ";label op1 op2 op3" 
        assert extractWord(text, 1) == None
        assert extractWord(text, 2) == None
        
        text = "  ;    label op1 op2 op3" 
        assert extractWord(text, 1) == None
        assert extractWord(text, 2) == None
        
        text = "   label;op1 op2 op3" 
        assert extractWord(text, 0) == None
        assert extractWord(text, 1) == "label"
        assert extractWord(text, 2) == None
        
        text = "   label   ;   op1 op2 op3" 
        assert extractWord(text, 0) == None
        assert extractWord(text, 1) == "label"
        assert extractWord(text, 2) == None
        
        text = "   label     op1  ;  op2 op3" 
        assert extractWord(text, 0) == None
        assert extractWord(text, 1) == "label"
        assert extractWord(text, 2) == "op1"
        assert extractWord(text, 3) == None
        
        text = ";toto titi tata ; comment"
        assert commentLine(text) == ";toto titi tata ; comment"

        text = "    ;toto titi tata ; comment"
        assert commentLine(text) == ";    ;toto titi tata ; comment"

        text = "     toto titi tata ; comment"
        assert commentLine(text) == ";     toto titi tata ; comment"

        text = 'test5 .string "\\x00\\x01\\x02\\x03\\x04\\x05\\x06\\x07\\x08\\x09\\x0a\\x0b\\x0c\\x0d\\x0e\\x0f"'
        assert commentLine(text) == 'test5 ; .string "\\x00\\x01\\x02\\x03\\x04\\x05\\x06\\x07\\x08\\x09\\x0a\\x0b\\x0c\\x0d\\x0e\\x0f"'
    
    def utests():
        test_precompiler()

    utests()
    sys.stdout.write("A L L   T E S T S   S U C C E S S F U L Y   P A S S E D !\n")
