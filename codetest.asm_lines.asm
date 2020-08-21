000009    CHAR_RETURN = $0a 
000012    PUTSCR_REG = $bf00 
000014    op1 = 0 
000015    op2 = 2 
000016    op3 = 4 
000017    zp = 6 
000020    * = $f000 
000022 source_start
000024 hooks
000025    .word print 
000026    .word print_nibble 
000027    .word print_byte 
000028    .word print_word 
000030 main
000031    jmp start 
000035 println
000036    jsr print 
000037    lda # CHAR_RETURN 
000038    sta PUTSCR_REG 
000039    rts 
000041 print
000043    stx op1 
000044    sty op1 + 1 
000045    ldy # 0 
000047 print_l1
000048    lda ( op1 ) , y 
000049    cmp # 0 
000050    beq print_out 
000051    sta PUTSCR_REG 
000052    iny 
000053    bne print_l1 
000055 print_out
000056    rts 
000058 print_nibble
000059    phx 
000060    and # $0f 
000061    tax 
000062    lda hextab , x 
000063    sta PUTSCR_REG 
000064    rts 
000066 print_byte
000067    pha 
000068    lsr a 
000069    lsr a 
000070    lsr a 
000071    lsr a 
000072    jsr print_nibble 
000073    pla 
000074    jmp print_nibble 
000076 print_word
000077    pha 
000078    tax 
000079    jsr print_byte 
000080    pla 
000081    jmp print_byte 
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
000101    ldx # < splash2 
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
000144 splash1.string "\"VOSC6502\" (Virtual Old School Computer with a 6502 processor)\n" 
000146 splash2.string "version 0.99 -------------------------- MMXX - Pierre Faller\n" 
000148 start_mes.string "free rom " 
000150 stop_mes.string " bytes\n" 
000152 nmi_mes.string " NMI occured\n" 
000154 irq_mes.string " IRQ occured\n" 
000156 hextab.ch_array "0123456789ABCDEF" 
000158 source_end
