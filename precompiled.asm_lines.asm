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
000037    lda CHAR_RETURN 
000038    sta PUTSCR_REG 
000039    rts 
000041 print
000043    stx op1 
000044    sty op1 + 1 
000045    ldy 0 
000047 print_l1
000048    lda op1 
000049    cmp 0 
000050    beq print_out 
000051    sta PUTSCR_REG 
000052    iny 
000053    bne print_l1 
000055 print_out
000056    rts 
000058 print_nibble
000059    phx 
000060    and $0f 
000061    tax 
000062    lda hextab , x 
000063    sta PUTSCR_REG 
000064    rts 
000066 print_byte
000067    pha 
000068    lsr 
000069    lsr 
000070    lsr 
000071    lsr 
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
000088    ldx < value 
000089    lda > value 
000090    jsr print_word 
000091 loop
000092    jmp loop 
000096    ldx < splash1 
000097    ldy > splash1 
000098    jsr print 
000101    ldx < splash2 
000102    ldy > splash2 
000103    jsr print 
000106    ldx < main 
000107    ldy > main 
000108    jsr print 
000111    ldx < start_mes 
000112    lda > start_mes 
000113    jsr print_word 
000116    ldx < stop 
000117    ldy > stop 
000118    jsr print 
000121    ldx < stop_mes 
000122    lda > stop_mes 
000123    jsr print_word 
000125 stop
000126    brk 
000128 irq
000130    ldx < irq_mes 
000131    ldy > irq_mes 
000132    jsr print 
000133 irq_loop
000134    jmp irq_loop 
000136 nmi
000138    ldx < nmi_mes 
000139    ldy > nmi_mes 
000140    jsr print 
000141 nmi_loop
000142    jmp nmi_loop 
000144 splash1
000145    .byte $22 , $56 , $4f , $53 , $43 , $36 , $35 
000146    .byte $30 , $32 , $22 , $20 , $28 , $56 , $69 
000147    .byte $72 , $74 , $75 , $61 , $6c , $20 , $4f 
000148    .byte $6c , $64 , $20 , $53 , $63 , $68 , $6f 
000149    .byte $6f , $6c , $20 , $43 , $6f , $6d , $70 
000150    .byte $75 , $74 , $65 , $72 , $20 , $77 , $69 
000151    .byte $74 , $68 , $20 , $61 , $20 , $36 , $35 
000152    .byte $30 , $32 , $20 , $70 , $72 , $6f , $63 
000153    .byte $65 , $73 , $73 , $6f , $72 , $29 , $0a 
000154    .byte $00 
000156 splash2
000157    .byte $76 , $65 , $72 , $73 , $69 , $6f , $6e 
000158    .byte $20 , $30 , $2e , $39 , $39 , $20 , $2d 
000159    .byte $2d , $2d , $2d , $2d , $2d , $2d , $2d 
000160    .byte $2d , $2d , $2d , $2d , $2d , $2d , $2d 
000161    .byte $2d , $2d , $2d , $2d , $2d , $2d , $2d 
000162    .byte $2d , $2d , $2d , $2d , $20 , $4d , $4d 
000163    .byte $58 , $58 , $20 , $2d , $20 , $50 , $69 
000164    .byte $65 , $72 , $72 , $65 , $20 , $46 , $61 
000165    .byte $6c , $6c , $65 , $72 , $0a , $00 
000167 start_mes
000168    .byte $66 , $72 , $65 , $65 , $20 , $72 , $6f 
000169    .byte $6d , $20 , $00 
000171 stop_mes
000172    .byte $20 , $62 , $79 , $74 , $65 , $73 , $0a 
000173    .byte $00 
000175 nmi_mes
000176    .byte $20 , $4e , $4d , $49 , $20 , $6f , $63 
000177    .byte $63 , $75 , $72 , $65 , $64 , $0a , $00 
000179 irq_mes
000180    .byte $20 , $49 , $52 , $51 , $20 , $6f , $63 
000181    .byte $63 , $75 , $72 , $65 , $64 , $0a , $00 
000183 hextab
000184    .byte $30 , $31 , $32 , $33 , $34 , $35 , $36 
000185    .byte $37 , $38 , $39 , $41 , $42 , $43 , $44 
000186    .byte $45 , $46 
000188 source_end
