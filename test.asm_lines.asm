000007    CHAR_RETURN = $0a 
000010    PUTSCR_REG = $bf00 
000012    x1 = 'a 
000013    x2 = ~10000001 
000014    x3 = "azerty" 
000016    * = $f000 
000017    y 
000019    adc $44 
000020    ADC $44 
000022 source_start
000024 hooks
000025    .word print 
000026    .word print_nibble 
000027    .word print_byte 
000028    .word print_word 
000030 splash1.string "\"VOSC6502\" (Virtual Old School ; Computer with a 6502 processor)\n" 
000032 splash2.string "version 0.99 -------------------------- MMXX - Pierre Faller\n" 
000034 main
000035    jmp start 
000037    nop 
000038    nop 
000039    nop 
000040    brk 
000042 println
000043    jsr print 
000044    lda CHAR_RETURN 
000045    sta PUTSCR_REG 
000046    rts 
000048 print
000050    stx op1 
000051    sty op1 + 1 
000052    ldy 0 
000054 print_l1
000055    lda ( op1 ) 
000056    cmp 0 
000057    beq print_out 
000058    sta PUTSCR_REG 
000059    iny 
000060    bne print_l1 
000062 print_out
000063    rts 
000065 print_nibble
000066    and $0f 
000067    tax 
000068    lda hextab 
000069    sta PUTSCR_REG 
000070    rts 
000072 print_byte
000073    pha 
000074    lsr 
000075    lsr 
000076    lsr 
000077    lsr 
000078    jsr print_nibble 
000079    pla 
000080    jmp print_nibble 
000082 print_word
000083    pha 
000084    tax 
000085    jsr print_byte 
000086    pla 
000087    jmp print_byte 
000089 start
000091    value = $1234 
000092    ldx < value 
000093    lda > value 
000094    jsr print_word 
000095 loop
000096    jmp loop 
000100    ldx < splash1 
000101    ldy > splash1 
000102    jsr print 
000105    ldx < splash2 + 3 
000106    ldy > splash2 
000107    jsr print 
000110    ldx < main 
000111    ldy > main 
000112    jsr print 
000115    ldx < start_mes 
000116    lda > start_mes 
000117    jsr print_word 
000120    ldx < stop 
000121    ldy > stop 
000122    jsr print 
000125    ldx < stop_mes 
000126    lda > stop_mes 
000127    jsr print_word 
000129 stop
000130    brk 
000132 irq
000134    ldx < irq_mes 
000135    ldy > irq_mes 
000136    jsr print 
000137 irq_loop
000138    jmp irq_loop 
000140 nmi
000142    ldx < nmi_mes 
000143    ldy > nmi_mes 
000144    jsr print 
000145 nmi_loop
000146    jmp nmi_loop 
000148    lda 1234 
000149    lda 12 
000150    lda 1234 
000151    lda 12 
000152    jmp print 
000157 start_mes.string "free rom " 
000159 stop_mes.string " bytes\n" 
000161 nmi_mes.string " NMI occured\n" 
000163 irq_mes.string " IRQ occured\n" 
000165 hextab.ch_array "0123456789ABCDEF" 
000167 source_end
