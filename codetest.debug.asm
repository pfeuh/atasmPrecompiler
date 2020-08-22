 65.09% assembled (69/106) 000009 X --------  (variable)CHAR_RETURN=0x000a 
000012 X --------  (variable)PUTSCR_REG=0xbf00 
000014 X --------  (variable)op1=0x0000 
000015 X --------  (variable)op2=0x0002 
000016 X --------  (variable)op3=0x0004 
000017 X --------  (variable)zp=0x0006 
000022 X (variable)source_start=0x0600 
000024 X (variable)hooks=0x0600 
000025 . --------  (command).word=None (variable)print=0x060c 
000026 . --------  (command).word=None (variable)print_nibble=0x0621 
000027 . --------  (command).word=None (variable)print_byte=0x062b 
000028 . --------  (command).word=None (variable)print_word=0x0637 
000030 X (variable)main=0x0600 
000031 X --------  (opcode)jmp=0x004c (variable)start=0x0640 
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
000048 X --------  (opcode)lda=0x00b1 (variable)op1=0x0000 
000049 X --------  (opcode)cmp=0x00c9 (variable)0=0x0000 
000050 X --------  (opcode)beq=0x00f0 (variable)print_out=0x0620 
000051 X --------  (opcode)sta=0x008d (variable)PUTSCR_REG=0xbf00 
000052 X --------  (opcode)iny=0x00c8 
000053 X --------  (opcode)bne=0x00d0 (variable)print_l1=0x0614 
000055 X (variable)print_out=0x0620 
000056 X --------  (opcode)rts=0x0060 
000058 X (variable)print_nibble=0x0621 
000059 . --------  (variable)phx=None 
000060 X --------  (opcode)and=0x0029 (variable)$0f=0x000f 
000061 X --------  (opcode)tax=0x00aa 
000062 . --------  (opcode)lda=0x00ad (variable)hextab=0x0739 (keyword),=None (keyword)x=None 
000063 X --------  (opcode)sta=0x008d (variable)PUTSCR_REG=0xbf00 
000064 X --------  (opcode)rts=0x0060 
000066 X (variable)print_byte=0x062b 
000067 X --------  (opcode)pha=0x0048 
000068 X --------  (opcode)lsr=0x004a 
000069 X --------  (opcode)lsr=0x004a 
000070 X --------  (opcode)lsr=0x004a 
000071 X --------  (opcode)lsr=0x004a 
000072 X --------  (opcode)jsr=0x0020 (variable)print_nibble=0x0621 
000073 X --------  (opcode)pla=0x0068 
000074 X --------  (opcode)jmp=0x004c (variable)print_nibble=0x0621 
000076 X (variable)print_word=0x0637 
000077 X --------  (opcode)pha=0x0048 
000078 X --------  (opcode)tax=0x00aa 
000079 X --------  (opcode)jsr=0x0020 (variable)print_byte=0x062b 
000080 X --------  (opcode)pla=0x0068 
000081 X --------  (opcode)jmp=0x004c (variable)print_byte=0x062b 
000085 X (variable)start=0x0640 
000087 X --------  (variable)value=0x1234 
000088 . (variable)value=0x1234 --------  (opcode)ldx=0x00a2 (keyword)<=(18,) (variable)value=0x1234 
000089 . (variable)value=0x1234 --------  (opcode)lda=0x00a9 (keyword)>=(52,) (variable)value=0x1234 
000090 X --------  (opcode)jsr=0x0020 (variable)print_word=0x0637 
000091 X (variable)loop=0x0649 
000092 X --------  (opcode)jmp=0x004c (variable)loop=0x0649 
000096 . --------  (opcode)ldx=0x00a2 (keyword)<=None (variable)splash1=0x068d 
000097 . --------  (opcode)ldy=0x00a0 (keyword)>=None (variable)splash1=0x068d 
000098 X --------  (opcode)jsr=0x0020 (variable)print=0x060c 
000101 . --------  (opcode)ldx=0x00a2 (keyword)<=None (variable)splash2=0x06cd 
000102 . --------  (opcode)ldy=0x00a0 (keyword)>=None (variable)splash2=0x06cd 
000103 X --------  (opcode)jsr=0x0020 (variable)print=0x060c 
000106 . (variable)main=0x0600 --------  (opcode)ldx=0x00a2 (keyword)<=(6,) (variable)main=0x0600 
000107 . (variable)main=0x0600 --------  (opcode)ldy=0x00a0 (keyword)>=(0,) (variable)main=0x0600 
000108 X --------  (opcode)jsr=0x0020 (variable)print=0x060c 
000111 . --------  (opcode)ldx=0x00a2 (keyword)<=None (variable)start_mes=0x070b 
000112 . --------  (opcode)lda=0x00a9 (keyword)>=None (variable)start_mes=0x070b 
000113 X --------  (opcode)jsr=0x0020 (variable)print_word=0x0637 
000116 . --------  (opcode)ldx=0x00a2 (keyword)<=None (variable)stop=0x0678 
000117 . --------  (opcode)ldy=0x00a0 (keyword)>=None (variable)stop=0x0678 
000118 X --------  (opcode)jsr=0x0020 (variable)print=0x060c 
000121 . --------  (opcode)ldx=0x00a2 (keyword)<=None (variable)stop_mes=0x0715 
000122 . --------  (opcode)lda=0x00a9 (keyword)>=None (variable)stop_mes=0x0715 
000123 X --------  (opcode)jsr=0x0020 (variable)print_word=0x0637 
000125 X (variable)stop=0x0678 
000126 X --------  (opcode)brk=0x0000 
000128 X (variable)irq=0x0679 
000130 . --------  (opcode)ldx=0x00a2 (keyword)<=None (variable)irq_mes=0x072b 
000131 . --------  (opcode)ldy=0x00a0 (keyword)>=None (variable)irq_mes=0x072b 
000132 X --------  (opcode)jsr=0x0020 (variable)print=0x060c 
000133 X (variable)irq_loop=0x0680 
000134 X --------  (opcode)jmp=0x004c (variable)irq_loop=0x0680 
000136 X (variable)nmi=0x0683 
000138 . --------  (opcode)ldx=0x00a2 (keyword)<=None (variable)nmi_mes=0x071d 
000139 . --------  (opcode)ldy=0x00a0 (keyword)>=None (variable)nmi_mes=0x071d 
000140 X --------  (opcode)jsr=0x0020 (variable)print=0x060c 
000141 X (variable)nmi_loop=0x068a 
000142 X --------  (opcode)jmp=0x004c (variable)nmi_loop=0x068a 
000144 . (variable)splash1=0x068d (command).string=(34, 86, 79, 83, 67, 54, 53, 48, 50, 34, 32, 40, 86, 105, 114, 116, 117, 97, 108, 32, 79, 108, 100, 32, 83, 99, 104, 111, 111, 108, 32, 67, 111, 109, 112, 117, 116, 101, 114, 32, 119, 105, 116, 104, 32, 97, 32, 54, 53, 48, 50, 32, 112, 114, 111, 99, 101, 115, 115, 111, 114, 41, 10, 0) 
000146 . (variable)splash2=0x06cd (command).string=(118, 101, 114, 115, 105, 111, 110, 32, 48, 46, 57, 57, 32, 45, 45, 45, 45, 45, 45, 45, 45, 45, 45, 45, 45, 45, 45, 45, 45, 45, 45, 45, 45, 45, 45, 45, 45, 45, 45, 32, 77, 77, 88, 88, 32, 45, 32, 80, 105, 101, 114, 114, 101, 32, 70, 97, 108, 108, 101, 114, 10, 0) 
000148 . (variable)start_mes=0x070b (command).string=(102, 114, 101, 101, 32, 114, 111, 109, 32, 0) 
000150 . (variable)stop_mes=0x0715 (command).string=(32, 98, 121, 116, 101, 115, 10, 0) 
000152 . (variable)nmi_mes=0x071d (command).string=(32, 78, 77, 73, 32, 111, 99, 99, 117, 114, 101, 100, 10, 0) 
000154 . (variable)irq_mes=0x072b (command).string=(32, 73, 82, 81, 32, 111, 99, 99, 117, 114, 101, 100, 10, 0) 
000156 . (variable)hextab=0x0739 (command).ch_array=(48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 65, 66, 67, 68, 69, 70) 
000158 . (variable)hextab2=0x0749 (command).byte=(48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 128) 
000160 . (variable)hextab3=0x0754 (command).word=(52, 18, 69, 35, 86, 52, 120, 86, 137, 103) 
000162 . (variable)DU_GRAS=0x075e (command).ds=(0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0) 
000164 . (variable)Dummmy=0x0780 (command).byte=(24,) 
000165 . (variable)nmi_mes=0x071d (variable)dubidu=0x0781 (command).byte=None (variable)$33=0x0033 (keyword),=None (keyword)<=None (variable)mni_mes=None (keyword),=None (keyword)>=(29,) (variable)nmi_mes=0x071d 
000166 X (variable)source_end=0x0782 
(variable)" IRQ occured\n"=None
(variable)" NMI occured\n"=None
(variable)" bytes\n"=None
(variable)"0123456789ABCDEF"=None
(variable)"\"VOSC6502\" (Virtual Old School Computer with a 6502 processor)\n"=None
(variable)"free rom "=None
(variable)"version 0.99 -------------------------- MMXX - Pierre Faller\n"=None
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
(variable)0=0x0000
(variable)1=0x0001
(variable)2=0x0002
(variable)34=0x0022
(variable)4=0x0004
(variable)6=0x0006
(variable)CHAR_RETURN=0x000a
(variable)DU_GRAS=0x075e
(variable)Dummmy=0x0780
(variable)PUTSCR_REG=0xbf00
(variable)a=None
(variable)dubidu=0x0781
(variable)hextab=0x0739
(variable)hextab2=0x0749
(variable)hextab3=0x0754
(variable)hooks=0x0600
(variable)irq=0x0679
(variable)irq_loop=0x0680
(variable)irq_mes=0x072b
(variable)loop=0x0649
(variable)main=0x0600
(variable)mni_mes=None
(variable)nmi=0x0683
(variable)nmi_loop=0x068a
(variable)nmi_mes=0x071d
(variable)op1=0x0000
(variable)op2=0x0002
(variable)op3=0x0004
(variable)phx=None
(variable)print=0x060c
(variable)print_byte=0x062b
(variable)print_l1=0x0614
(variable)print_nibble=0x0621
(variable)print_out=0x0620
(variable)print_word=0x0637
(variable)println=0x0603
(variable)source_end=0x0782
(variable)source_start=0x0600
(variable)splash1=0x068d
(variable)splash2=0x06cd
(variable)start=0x0640
(variable)start_mes=0x070b
(variable)stop=0x0678
(variable)stop_mes=0x0715
(variable)value=0x1234
(variable)zp=0x0006
(variable)~00011000=0x0018
