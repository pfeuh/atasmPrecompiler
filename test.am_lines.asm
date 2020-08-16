   CHAR_RETURN = $0a 

   PUTSCR_REG = $bf00 

   x1 = $0061 

   x2 = ~10000001 

   x3 = "azerty" 

   * = $f000 

   

   

   .word print 

   .word print_nibble 

   .word print_byte 

   .word print_word 

   .string "\"VOSC6502\" (Virtual Old School ; Computer with a 6502 processor)\n" 

   .string "version 0.99 -------------------------- MMXX - Pierre Faller\n" 

   

   jmp start 

   nop 

   nop 

   nop 

   brk 

   

   jsr print 

   lda # CHAR_RETURN 

   sta PUTSCR_REG 

   rts 

   

   stx op1 

   sty op1 + 1 

   ldy # 0 

   

   lda ( op1 ) , y 

   cmp # 0 

   beq print_out 

   sta PUTSCR_REG 

   iny 

   bne print_l1 

   

   rts 

   

   and # $0f 

   tax 

   lda hextab , x 

   sta PUTSCR_REG 

   rts 

   

   pha 

   lsr 

   lsr 

   lsr 

   lsr 

   jsr print_nibble 

   pla 

   jmp print_nibble 

   

   pha 

   tax 

   jsr print_byte 

   pla 

   jmp print_byte 

   

   value = $1234 

   ldx # < value 

   lda # > value 

   jsr print_word 

   

   jmp loop 

   ldx # < splash1 

   ldy # > splash1 

   jsr print 

   ldx # < splash2 + 3 

   ldy # > splash2 

   jsr print 

   ldx # < main 

   ldy # > main 

   jsr print 

   ldx # < start_mes 

   lda # > start_mes 

   jsr print_word 

   ldx # < stop 

   ldy # > stop 

   jsr print 

   ldx # < stop_mes 

   lda # > stop_mes 

   jsr print_word 

   

   brk 

   

   ldx # < irq_mes 

   ldy # > irq_mes 

   jsr print 

   

   jmp irq_loop 

   

   ldx # < nmi_mes 

   ldy # > nmi_mes 

   jsr print 

   

   jmp nmi_loop 

   .string "free rom " 

   .string " bytes\n" 

   .string " NMI occured\n" 

   .string " IRQ occured\n" 

   .ch_array "0123456789ABCDEF" 

   

