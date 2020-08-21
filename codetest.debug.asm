 61.32% assembled (65/106) 000009 X --------  (variable)CHAR_RETURN=0x000a 
000012 X --------  (variable)PUTSCR_REG=0xbf00 
000014 X --------  (variable)op1=0x0000 
000015 X --------  (variable)op2=0x0002 
000016 X --------  (variable)op3=0x0004 
000017 X --------  (variable)zp=0x0006 
000022 X (variable)source_start=0x0600 
000024 X (variable)hooks=0x0600 
000025 . --------  (command).word=(52, 18, 69, 35, 86, 52, 120, 86, 137, 103) (variable)print=0x060c 
000026 . --------  (command).word=(52, 18, 69, 35, 86, 52, 120, 86, 137, 103) (variable)print_nibble=0x061b 
000027 . --------  (command).word=(52, 18, 69, 35, 86, 52, 120, 86, 137, 103) (variable)print_byte=0x061e 
000028 . --------  (command).word=(52, 18, 69, 35, 86, 52, 120, 86, 137, 103) (variable)print_word=0x0621 
000030 X (variable)main=0x0600 
000031 X --------  (opcode)jmp=0x004c (variable)start=0x0621 
000035 X (variable)println=0x0603 
000036 X --------  (opcode)jsr=0x0020 (variable)print=0x060c 
000037 X --------  (opcode)lda=0x00a9 (variable)CHAR_RETURN=0x000a 
000038 X --------  (opcode)sta=0x008d (variable)PUTSCR_REG=0xbf00 
000039 X --------  (opcode)rts=0x0060 
000041 X (variable)print=0x060c 
000043 X --------  (opcode)stx=0x008e (variable)op1=0x0000 
000044 . --------  (opcode)sty=0x008c (variable)op1=0x0000 (keyword)+=None (variable)1=0x0001 
000045 X --------  (opcode)ldy=0x00a0 (variable)0=0x0000 
000047 X (variable)print_l1=0x0614 
000048 . --------  (opcode)lda=0x00a9 (keyword)(=None (variable)op1=0x0000 (keyword))=None (keyword),=None (keyword)y=None 
000049 X --------  (opcode)cmp=0x00c9 (variable)0=0x0000 
000050 X --------  (opcode)beq=0x00f0 (variable)print_out=0x061b 
000051 X --------  (opcode)sta=0x008d (variable)PUTSCR_REG=0xbf00 
000052 X --------  (opcode)iny=0x00c8 
000053 X --------  (opcode)bne=0x00d0 (variable)print_l1=0x0614 
000055 X (variable)print_out=0x061b 
000056 X --------  (opcode)rts=0x0060 
000058 X (variable)print_nibble=0x061b 
000059 . --------  (variable)phx=None 
000060 X --------  (opcode)and=0x0029 (variable)$0f=0x000f 
000061 X --------  (opcode)tax=0x00aa 
000062 . --------  (opcode)lda=0x00a9 (variable)hextab=0x06d4 (keyword),=None (keyword)x=None 
000063 X --------  (opcode)sta=0x008d (variable)PUTSCR_REG=0xbf00 
000064 X --------  (opcode)rts=0x0060 
000066 X (variable)print_byte=0x061e 
000067 X --------  (opcode)pha=0x0048 
000068 X --------  (opcode)lsr=0x004a 
000069 . --------  (opcode)lsr=0x004a (variable)a=None 
000070 . --------  (opcode)lsr=0x004a (variable)a=None 
000071 . --------  (opcode)lsr=0x004a (variable)a=None 
000072 X --------  (opcode)jsr=0x0020 (variable)print_nibble=0x061b 
000073 X --------  (opcode)pla=0x0068 
000074 X --------  (opcode)jmp=0x004c (variable)print_nibble=0x061b 
000076 X (variable)print_word=0x0621 
000077 X --------  (opcode)pha=0x0048 
000078 X --------  (opcode)tax=0x00aa 
000079 X --------  (opcode)jsr=0x0020 (variable)print_byte=0x061e 
000080 X --------  (opcode)pla=0x0068 
000081 X --------  (opcode)jmp=0x004c (variable)print_byte=0x061e 
000085 X (variable)start=0x0621 
000087 X --------  (variable)value=0x1234 
000088 . --------  (opcode)ldx=0x00a2 (keyword)<=(18,) (variable)value=0x1234 
000089 . --------  (opcode)lda=0x00a9 (keyword)#=None (keyword)>=(52,) (variable)value=0x1234 
000090 X --------  (opcode)jsr=0x0020 (variable)print_word=0x0621 
000091 X (variable)loop=0x0625 
000092 X --------  (opcode)jmp=0x004c (variable)loop=0x0625 
000096 . --------  (opcode)ldx=0x00a2 (keyword)#=None (keyword)<=(18,) (variable)splash1=0x0628 
000097 . --------  (opcode)ldy=0x00a0 (keyword)#=None (keyword)>=(52,) (variable)splash1=0x0628 
000098 X --------  (opcode)jsr=0x0020 (variable)print=0x060c 
000101 . --------  (opcode)ldx=0x00a2 (keyword)#=None (keyword)<=(18,) (variable)splash2=0x0668 
000102 . --------  (opcode)ldy=0x00a0 (keyword)#=None (keyword)>=(52,) (variable)splash2=0x0668 
000103 X --------  (opcode)jsr=0x0020 (variable)print=0x060c 
000106 . --------  (opcode)ldx=0x00a2 (keyword)#=None (keyword)<=(18,) (variable)main=0x0600 
000107 . --------  (opcode)ldy=0x00a0 (keyword)#=None (keyword)>=(52,) (variable)main=0x0600 
000108 X --------  (opcode)jsr=0x0020 (variable)print=0x060c 
000111 . --------  (opcode)ldx=0x00a2 (keyword)#=None (keyword)<=(18,) (variable)start_mes=0x06a6 
000112 . --------  (opcode)lda=0x00a9 (keyword)#=None (keyword)>=(52,) (variable)start_mes=0x06a6 
000113 X --------  (opcode)jsr=0x0020 (variable)print_word=0x0621 
000116 . --------  (opcode)ldx=0x00a2 (keyword)#=None (keyword)<=(18,) (variable)stop=0x0627 
000117 . --------  (opcode)ldy=0x00a0 (keyword)#=None (keyword)>=(52,) (variable)stop=0x0627 
000118 X --------  (opcode)jsr=0x0020 (variable)print=0x060c 
000121 . --------  (opcode)ldx=0x00a2 (keyword)#=None (keyword)<=(18,) (variable)stop_mes=0x06b0 
000122 . --------  (opcode)lda=0x00a9 (keyword)#=None (keyword)>=(52,) (variable)stop_mes=0x06b0 
000123 X --------  (opcode)jsr=0x0020 (variable)print_word=0x0621 
000125 X (variable)stop=0x0627 
000126 X --------  (opcode)brk=0x0000 
000128 X (variable)irq=0x0628 
000130 . --------  (opcode)ldx=0x00a2 (keyword)#=None (keyword)<=(18,) (variable)irq_mes=0x06c6 
000131 . --------  (opcode)ldy=0x00a0 (keyword)#=None (keyword)>=(52,) (variable)irq_mes=0x06c6 
000132 X --------  (opcode)jsr=0x0020 (variable)print=0x060c 
000133 X (variable)irq_loop=0x0628 
000134 X --------  (opcode)jmp=0x004c (variable)irq_loop=0x0628 
000136 X (variable)nmi=0x0628 
000138 . --------  (opcode)ldx=0x00a2 (keyword)#=None (keyword)<=(18,) (variable)nmi_mes=0x06b8 
000139 . --------  (opcode)ldy=0x00a0 (keyword)#=None (keyword)>=(52,) (variable)nmi_mes=0x06b8 
000140 X --------  (opcode)jsr=0x0020 (variable)print=0x060c 
000141 X (variable)nmi_loop=0x0628 
000142 X --------  (opcode)jmp=0x004c (variable)nmi_loop=0x0628 
000144 . (variable)splash1=0x0628 (command).string=(34, 86, 79, 83, 67, 54, 53, 48, 50, 34, 32, 40, 86, 105, 114, 116, 117, 97, 108, 32, 79, 108, 100, 32, 83, 99, 104, 111, 111, 108, 32, 67, 111, 109, 112, 117, 116, 101, 114, 32, 119, 105, 116, 104, 32, 97, 32, 54, 53, 48, 50, 32, 112, 114, 111, 99, 101, 115, 115, 111, 114, 41, 10, 0) (variable)"\"VOSC6502\" (Virtual Old School Computer with a 6502 processor)\n"=None 
000146 . (variable)splash2=0x0668 (command).string=(34, 86, 79, 83, 67, 54, 53, 48, 50, 34, 32, 40, 86, 105, 114, 116, 117, 97, 108, 32, 79, 108, 100, 32, 83, 99, 104, 111, 111, 108, 32, 67, 111, 109, 112, 117, 116, 101, 114, 32, 119, 105, 116, 104, 32, 97, 32, 54, 53, 48, 50, 32, 112, 114, 111, 99, 101, 115, 115, 111, 114, 41, 10, 0) (variable)"version 0.99 -------------------------- MMXX - Pierre Faller\n"=None 
000148 . (variable)start_mes=0x06a6 (command).string=(34, 86, 79, 83, 67, 54, 53, 48, 50, 34, 32, 40, 86, 105, 114, 116, 117, 97, 108, 32, 79, 108, 100, 32, 83, 99, 104, 111, 111, 108, 32, 67, 111, 109, 112, 117, 116, 101, 114, 32, 119, 105, 116, 104, 32, 97, 32, 54, 53, 48, 50, 32, 112, 114, 111, 99, 101, 115, 115, 111, 114, 41, 10, 0) (variable)"free rom "=None 
000150 . (variable)stop_mes=0x06b0 (command).string=(34, 86, 79, 83, 67, 54, 53, 48, 50, 34, 32, 40, 86, 105, 114, 116, 117, 97, 108, 32, 79, 108, 100, 32, 83, 99, 104, 111, 111, 108, 32, 67, 111, 109, 112, 117, 116, 101, 114, 32, 119, 105, 116, 104, 32, 97, 32, 54, 53, 48, 50, 32, 112, 114, 111, 99, 101, 115, 115, 111, 114, 41, 10, 0) (variable)" bytes\n"=None 
000152 . (variable)nmi_mes=0x06b8 (command).string=(34, 86, 79, 83, 67, 54, 53, 48, 50, 34, 32, 40, 86, 105, 114, 116, 117, 97, 108, 32, 79, 108, 100, 32, 83, 99, 104, 111, 111, 108, 32, 67, 111, 109, 112, 117, 116, 101, 114, 32, 119, 105, 116, 104, 32, 97, 32, 54, 53, 48, 50, 32, 112, 114, 111, 99, 101, 115, 115, 111, 114, 41, 10, 0) (variable)" NMI occured\n"=None 
000154 . (variable)irq_mes=0x06c6 (command).string=(34, 86, 79, 83, 67, 54, 53, 48, 50, 34, 32, 40, 86, 105, 114, 116, 117, 97, 108, 32, 79, 108, 100, 32, 83, 99, 104, 111, 111, 108, 32, 67, 111, 109, 112, 117, 116, 101, 114, 32, 119, 105, 116, 104, 32, 97, 32, 54, 53, 48, 50, 32, 112, 114, 111, 99, 101, 115, 115, 111, 114, 41, 10, 0) (variable)" IRQ occured\n"=None 
000156 . (variable)hextab=0x06d4 (command).ch_array=(48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 65, 66, 67, 68, 69, 70) (variable)"0123456789ABCDEF"=None 
000158 . (variable)hextab2=0x06e4 (command).byte=(48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 128) (variable)$30=0x0030 (keyword),=None (variable)$31=0x0031 (keyword),=None (variable)$32=0x0032 (keyword),=None (variable)$33=0x0033 (keyword),=None (variable)$34=0x0034 (keyword),=None (variable)$35=0x0035 (keyword),=None (variable)$36=0x0036 (keyword),=None (variable)$37=0x0037 (keyword),=None (variable)$38=0x0038 (keyword),=None (variable)$39=0x0039 (keyword),=None (variable)op1=0x0000 (keyword)|=None (variable)$80=0x0080 
000160 . (variable)hextab3=0x06ef (command).word=(52, 18, 69, 35, 86, 52, 120, 86, 137, 103) (variable)$1234=0x1234 (keyword),=None (variable)$2345=0x2345 (keyword),=None (variable)$3456=0x3456 (keyword),=None (variable)$5678=0x5678 (keyword),=None (variable)$6789=0x6789 
000162 . (variable)DU_GRAS=0x06f9 (command).ds=(0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0) (variable)34=0x0022 
000164 . (variable)Dummmy=0x071b (command).byte=(48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 128) (variable)~00011000=0x0018 
000165 . (variable)dubidu=0x071c (command).byte=(48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 128) (variable)$33=0x0033 (keyword),=None (keyword)<=(18,) (variable)mni_mes=None (keyword),=None (keyword)>=(52,) (variable)nmi_mes=0x06b8 
000166 X (variable)source_end=0x071d 
-------- 
(variable)" IRQ occured\n"=None
(variable)" NMI occured\n"=None
(variable)" bytes\n"=None
(variable)"0123456789ABCDEF"=None
(variable)"\"VOSC6502\" (Virtual Old School Computer with a 6502 processor)\n"=None
(variable)"free rom "=None
(variable)"version 0.99 -------------------------- MMXX - Pierre Faller\n"=None
(keyword)#=None
(variable)$0a=0x000a
(variable)$0f=0x000f
(variable)$1234=0x1234
(variable)$2345=0x2345
(variable)$30=0x0030
(variable)$31=0x0031
(variable)$32=0x0032
(variable)$33=0x0033
(variable)$34=0x0034
(variable)$3456=0x3456
(variable)$35=0x0035
(variable)$36=0x0036
(variable)$37=0x0037
(variable)$38=0x0038
(variable)$39=0x0039
(variable)$5678=0x5678
(variable)$6789=0x6789
(variable)$80=0x0080
(variable)$bf00=0xbf00
(keyword)(=None
(keyword))=None
(keyword)+=None
(keyword),=None
(command).byte=(48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 128)
(command).ch_array=(48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 65, 66, 67, 68, 69, 70)
(command).ds=(0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
(command).string=(34, 86, 79, 83, 67, 54, 53, 48, 50, 34, 32, 40, 86, 105, 114, 116, 117, 97, 108, 32, 79, 108, 100, 32, 83, 99, 104, 111, 111, 108, 32, 67, 111, 109, 112, 117, 116, 101, 114, 32, 119, 105, 116, 104, 32, 97, 32, 54, 53, 48, 50, 32, 112, 114, 111, 99, 101, 115, 115, 111, 114, 41, 10, 0)
(command).word=(52, 18, 69, 35, 86, 52, 120, 86, 137, 103)
(variable)0=0x0000
(variable)1=0x0001
(variable)2=0x0002
(variable)34=0x0022
(variable)4=0x0004
(variable)6=0x0006
(keyword)<=(18,)
(keyword)==None
(keyword)>=(52,)
(variable)CHAR_RETURN=0x000a
(variable)DU_GRAS=0x06f9
(variable)Dummmy=0x071b
(variable)PUTSCR_REG=0xbf00
(variable)a=None
(opcode)and=0x0029
(opcode)beq=0x00f0
(opcode)bne=0x00d0
(opcode)brk=0x0000
(opcode)cmp=0x00c9
(variable)dubidu=0x071c
(variable)hextab=0x06d4
(variable)hextab2=0x06e4
(variable)hextab3=0x06ef
(variable)hooks=0x0600
(opcode)iny=0x00c8
(variable)irq=0x0628
(variable)irq_loop=0x0628
(variable)irq_mes=0x06c6
(opcode)jmp=0x004c
(opcode)jsr=0x0020
(opcode)lda=0x00a9
(opcode)ldx=0x00a2
(opcode)ldy=0x00a0
(variable)loop=0x0625
(opcode)lsr=0x004a
(variable)main=0x0600
(variable)mni_mes=None
(variable)nmi=0x0628
(variable)nmi_loop=0x0628
(variable)nmi_mes=0x06b8
(variable)op1=0x0000
(variable)op2=0x0002
(variable)op3=0x0004
(opcode)pha=0x0048
(variable)phx=None
(opcode)pla=0x0068
(variable)print=0x060c
(variable)print_byte=0x061e
(variable)print_l1=0x0614
(variable)print_nibble=0x061b
(variable)print_out=0x061b
(variable)print_word=0x0621
(variable)println=0x0603
(opcode)rts=0x0060
(variable)source_end=0x071d
(variable)source_start=0x0600
(variable)splash1=0x0628
(variable)splash2=0x0668
(opcode)sta=0x008d
(variable)start=0x0621
(variable)start_mes=0x06a6
(variable)stop=0x0627
(variable)stop_mes=0x06b0
(opcode)stx=0x008e
(opcode)sty=0x008c
(opcode)tax=0x00aa
(variable)value=0x1234
(keyword)x=None
(keyword)y=None
(variable)zp=0x0006
(keyword)|=None
(variable)~00011000=0x0018
