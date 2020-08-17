000007    CHAR_RETURN = $0a 
000010    PUTSCR_REG = $bf00 
000012    x1 = 'a 
000013    x2 = ~10000001 
000014    x3 = "azerty" 
000016    * = $f000 
000018 source_start
000020 hooks
000021    .word print 
000022    .word print_nibble 
000023    .word print_byte 
000024    .word print_word 
000026 splash1.string "\"VOSC6502\" (Virtual Old School ; Computer with a 6502 processor)\n" 
000028 splash2.string "version 0.99 -------------------------- MMXX - Pierre Faller\n" 
000030 main
000031    jmp start 
000033    nop 
000034    nop 
000035    nop 
000036    brk 
000038 println
000039    jsr print 
000040    lda # CHAR_RETURN 
000041    sta PUTSCR_REG 
000042    rts 
000044 print
000046    stx op1 
000047    sty op1 + 1 
000048    ldy # 0 
000050 print_l1
000051    lda ( op1 ) , y 
000052    cmp # 0 
000053    beq print_out 
000054    sta PUTSCR_REG 
000055    iny 
000056    bne print_l1 
000058 print_out
000059    rts 
000061 print_nibble
000062    and # $0f 
000063    tax 
000064    lda hextab , x 
000065    sta PUTSCR_REG 
000066    rts 
000068 print_byte
000069    pha 
000070    lsr 
000071    lsr 
000072    lsr 
000073    lsr 
000074    jsr print_nibble 
000075    pla 
000076    jmp print_nibble 
000078 print_word
000079    pha 
000080    tax 
000081    jsr print_byte 
000082    pla 
000083    jmp print_byte 
000085 start
000087    value = $1234 
000088    ldx # < value 
000089    lda # > value 
000090    jsr print_word 
000091 loop
000092    jmp loop 
000096    ldx # < splash1 
000097    ldy # > splash1 
000098    jsr print 
000101    ldx # < splash2 + 3 
000102    ldy # > splash2 
000103    jsr print 
000106    ldx # < main 
000107    ldy # > main 
000108    jsr print 
000111    ldx # < start_mes 
000112    lda # > start_mes 
000113    jsr print_word 
000116    ldx # < stop 
000117    ldy # > stop 
000118    jsr print 
000121    ldx # < stop_mes 
000122    lda # > stop_mes 
000123    jsr print_word 
000125 stop
000126    brk 
000128 irq
000130    ldx # < irq_mes 
000131    ldy # > irq_mes 
000132    jsr print 
000133 irq_loop
000134    jmp irq_loop 
000136 nmi
000138    ldx # < nmi_mes 
000139    ldy # > nmi_mes 
000140    jsr print 
000141 nmi_loop
000142    jmp nmi_loop 
000144 start_mes.string "free rom " 
000146 stop_mes.string " bytes\n" 
000148 nmi_mes.string " NMI occured\n" 
000150 irq_mes.string " IRQ occured\n" 
000152 hextab.ch_array "0123456789ABCDEF" 
000154 source_end
