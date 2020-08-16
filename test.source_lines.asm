File "test.asm", line 1, 
File "test.asm", line 2,     ;---------------------------------;
File "test.asm", line 3,     ; a 4ko ROM monitor for vosc6502  ;
File "test.asm", line 4,     ;---------------------------------;
File "test.asm", line 5, 
File "test.asm", line 6,     ; special characters
File "test.asm", line 7,     CHAR_RETURN = $0a
File "test.asm", line 8, 
File "test.asm", line 9,     ;hardware registers
File "test.asm", line 10,     PUTSCR_REG = $bf00
File "test.asm", line 11, 
File "test.asm", line 12,     x1 = 'a;blablabla...
File "test.asm", line 13,     x2 = ~10000001
File "test.asm", line 14,     x3 = "azerty"
File "test.asm", line 15, 
File "test.asm", line 16,     * = $f000
File "test.asm", line 17, 
File "test.asm", line 18, source_start
File "test.asm", line 19, 
File "test.asm", line 20, hooks
File "test.asm", line 21,     .word print
File "test.asm", line 22,     .word print_nibble
File "test.asm", line 23,     .word print_byte
File "test.asm", line 24,     .word print_word
File "test.asm", line 25, 
File "test.asm", line 26, splash1 .string "\"VOSC6502\" (Virtual Old School ; Computer with a 6502 processor)\n";blablabla...
File "test.asm", line 27, 
File "test.asm", line 28, splash2 .string "version 0.99 -------------------------- MMXX - Pierre Faller\n"
File "test.asm", line 29, 
File "test.asm", line 30, main
File "test.asm", line 31,     jmp start
File "test.asm", line 32, 
File "test.asm", line 33,     nop
File "test.asm", line 34,     nop
File "test.asm", line 35,     nop
File "test.asm", line 36,     brk
File "test.asm", line 37, 
File "test.asm", line 38, println
File "test.asm", line 39,     jsr print
File "test.asm", line 40,     lda #CHAR_RETURN
File "test.asm", line 41,     sta PUTSCR_REG
File "test.asm", line 42,     rts
File "test.asm", line 43, 
File "test.asm", line 44, print
File "test.asm", line 45,     ; op1 = 0
File "test.asm", line 46,     stx op1
File "test.asm", line 47,     sty op1+1
File "test.asm", line 48,     ldy #0
File "test.asm", line 49, 
File "test.asm", line 50, print_l1
File "test.asm", line 51,     lda (op1),y
File "test.asm", line 52,     cmp #0
File "test.asm", line 53,     beq print_out
File "test.asm", line 54,     sta PUTSCR_REG
File "test.asm", line 55,     iny
File "test.asm", line 56,     bne print_l1
File "test.asm", line 57, 
File "test.asm", line 58, print_out
File "test.asm", line 59,     rts
File "test.asm", line 60, 
File "test.asm", line 61, print_nibble
File "test.asm", line 62,     and #$0f
File "test.asm", line 63,     tax
File "test.asm", line 64,     lda hextab, x
File "test.asm", line 65,     sta PUTSCR_REG
File "test.asm", line 66,     rts
File "test.asm", line 67, 
File "test.asm", line 68, print_byte
File "test.asm", line 69,     pha
File "test.asm", line 70,     lsr
File "test.asm", line 71,     lsr
File "test.asm", line 72,     lsr
File "test.asm", line 73,     lsr
File "test.asm", line 74,     jsr print_nibble
File "test.asm", line 75,     pla
File "test.asm", line 76,     jmp print_nibble
File "test.asm", line 77, 
File "test.asm", line 78, print_word
File "test.asm", line 79,     pha
File "test.asm", line 80,     tax
File "test.asm", line 81,     jsr print_byte
File "test.asm", line 82,     pla
File "test.asm", line 83,     jmp print_byte
File "test.asm", line 84, 
File "test.asm", line 85, start
File "test.asm", line 86, 
File "test.asm", line 87,     value = $1234
File "test.asm", line 88,     ldx #<value
File "test.asm", line 89,     lda #>value
File "test.asm", line 90,     jsr print_word
File "test.asm", line 91, loop
File "test.asm", line 92,     jmp loop
File "test.asm", line 93, 
File "test.asm", line 94, 
File "test.asm", line 95,     ; print "vosc6502...
File "test.asm", line 96,     ldx #<splash1
File "test.asm", line 97,     ldy #>splash1
File "test.asm", line 98,     jsr print
File "test.asm", line 99, 
File "test.asm", line 100,     ; print "version ...
File "test.asm", line 101,     ldx #<splash2 + 3
File "test.asm", line 102,     ldy #>splash2
File "test.asm", line 103,     jsr print
File "test.asm", line 104, 
File "test.asm", line 105,     ; print "start point is
File "test.asm", line 106,     ldx #<main
File "test.asm", line 107,     ldy #>main
File "test.asm", line 108,     jsr print
File "test.asm", line 109, 
File "test.asm", line 110,     ; print "start point value
File "test.asm", line 111,     ldx #<start_mes
File "test.asm", line 112,     lda #>start_mes
File "test.asm", line 113,     jsr print_word
File "test.asm", line 114, 
File "test.asm", line 115,     ; print "stop point is
File "test.asm", line 116,     ldx #<stop
File "test.asm", line 117,     ldy #>stop
File "test.asm", line 118,     jsr print
File "test.asm", line 119, 
File "test.asm", line 120,     ; print "start point value
File "test.asm", line 121,     ldx #<stop_mes;blablabla
File "test.asm", line 122,     lda #>stop_mes; blablabla
File "test.asm", line 123,     jsr print_word ;blablabla
File "test.asm", line 124, 
File "test.asm", line 125, stop
File "test.asm", line 126,     brk
File "test.asm", line 127, 
File "test.asm", line 128, irq
File "test.asm", line 129,     ; print "IRQ...
File "test.asm", line 130,     ldx #<irq_mes
File "test.asm", line 131,     ldy #>irq_mes
File "test.asm", line 132,     jsr print
File "test.asm", line 133, irq_loop
File "test.asm", line 134,     jmp irq_loop
File "test.asm", line 135, 
File "test.asm", line 136, nmi
File "test.asm", line 137,     ; print "MNI...
File "test.asm", line 138,     ldx #<nmi_mes
File "test.asm", line 139,     ldy #>nmi_mes;blablabla...
File "test.asm", line 140,     jsr       print
File "test.asm", line 141, nmi_loop
File "test.asm", line 142,     jmp nmi_loop
File "test.asm", line 143, 
File "test.asm", line 144, start_mes .string "free rom "
File "test.asm", line 145, 
File "test.asm", line 146, stop_mes .string " bytes\n"
File "test.asm", line 147, 
File "test.asm", line 148, nmi_mes .string " NMI occured\n"
File "test.asm", line 149, 
File "test.asm", line 150, irq_mes .string " IRQ occured\n"
File "test.asm", line 151, 
File "test.asm", line 152, hextab .ch_array "0123456789ABCDEF"
File "test.asm", line 153, 
File "test.asm", line 154, source_end
