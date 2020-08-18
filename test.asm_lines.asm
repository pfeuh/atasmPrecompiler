000007    CHAR_RETURN = $0a 
000010    PUTSCR_REG = $bf00 
000012    x1 = 'a 
000013    x2 = ~10000001 
000014    x3 = "azerty" 
000016    * = $f000 
000017    y 
000019    adc $44 
000020    ADC $44 
000021    ADC $44 
000023 source_start
000025 hooks
000026    .word print 
000027    .word print_nibble 
000028    .word print_byte 
000029    .word print_word 
000031 splash1.string "\"VOSC6502\" (Virtual Old School ; Computer with a 6502 processor)\n" 
000033 splash2.string "version 0.99 -------------------------- MMXX - Pierre Faller\n" 
000035 main
000036    jmp start 
000038    nop 
000039    nop 
000040    nop 
000041    brk 
000043 println
000044    jsr print 
000045    lda CHAR_RETURN 
000046    sta PUTSCR_REG 
000047    rts 
000049 print
000051    stx op1 
000052    sty op1 + 1 
000053    ldy 0 
000055 print_l1
000056    lda op1 
000057    cmp 0 
000058    beq print_out 
000059    sta PUTSCR_REG 
000060    iny 
000061    bne print_l1 
000063 print_out
000064    rts 
000066 print_nibble
000067    and $0f 
000068    tax 
000069    lda hextab 
000070    sta PUTSCR_REG 
000071    rts 
000073 print_byte
000074    pha 
000075    lsr 
000076    lsr 
000077    lsr 
000078    lsr 
000079    jsr print_nibble 
000080    pla 
000081    jmp print_nibble 
000083 print_word
000084    pha 
000085    tax 
000086    jsr print_byte 
000087    pla 
000088    jmp print_byte 
000090 start
000092    value = $1234 
000093    ldx < value 
000094    lda > value 
000095    jsr print_word 
000096 loop
000097    jmp loop 
000101    ldx < splash1 
000102    ldy > splash1 
000103    jsr print 
000106    ldx < splash2 + 3 
000107    ldy > splash2 
000108    jsr print 
000111    ldx < main 
000112    ldy > main 
000113    jsr print 
000116    ldx < start_mes 
000117    lda > start_mes 
000118    jsr print_word 
000121    ldx < stop 
000122    ldy > stop 
000123    jsr print 
000126    ldx < stop_mes 
000127    lda > stop_mes 
000128    jsr print_word 
000130 stop
000131    brk 
000133 irq
000135    ldx < irq_mes 
000136    ldy > irq_mes 
000137    jsr print 
000138 irq_loop
000139    jmp irq_loop 
000141 nmi
000143    ldx < nmi_mes 
000144    ldy > nmi_mes 
000145    jsr print 
000146 nmi_loop
000147    jmp nmi_loop 
000149    lda 1234 
000150    lda 12 
000151    lda 1234 
000152    lda 12 
000153    jmp print 
000158 start_mes.string "free rom " 
000160 stop_mes.string " bytes\n" 
000162 nmi_mes.string " NMI occured\n" 
000164 irq_mes.string " IRQ occured\n" 
000166 hextab.ch_array "0123456789ABCDEF" 
000168 source_end
