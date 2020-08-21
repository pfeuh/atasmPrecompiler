. 000009     CHAR_RETURN = $0a
  --------
. (variable) CHAR_RETURN 
  (keyword) = 
X (variable) $0a 
----------------------------------------
. 000012     PUTSCR_REG = $bf00
  --------
. (variable) PUTSCR_REG 
  (keyword) = 
X (variable) $bf00 
----------------------------------------
. 000014     op1 = 0
  --------
. (variable) op1 
  (keyword) = 
X (variable) 0 
----------------------------------------
. 000015     op2 = 2
  --------
. (variable) op2 
  (keyword) = 
X (variable) 2 
----------------------------------------
. 000016     op3 = 4
  --------
. (variable) op3 
  (keyword) = 
X (variable) 4 
----------------------------------------
. 000017     zp  = 6
  --------
. (variable) zp 
  (keyword) = 
X (variable) 6 
----------------------------------------
. 000020     * = $f000
  --------
  (keyword) * 
  (keyword) = 
X (variable) $f000 
----------------------------------------
. 000022 source_start
. (variable) source_start 
----------------------------------------
. 000024 hooks
. (variable) hooks 
----------------------------------------
. 000025     .word print
  --------
  (keyword) .word 
. (variable) print 
----------------------------------------
. 000026     .word print_nibble
  --------
  (keyword) .word 
. (variable) print_nibble 
----------------------------------------
. 000027     .word print_byte
  --------
  (keyword) .word 
. (variable) print_byte 
----------------------------------------
. 000028     .word print_word
  --------
  (keyword) .word 
. (variable) print_word 
----------------------------------------
. 000030 main
. (variable) main 
----------------------------------------
. 000031     jmp start
  --------
  (mnemo) jmp 
. (variable) start 
----------------------------------------
. 000035 println
. (variable) println 
----------------------------------------
. 000036     jsr print
  --------
  (mnemo) jsr 
. (variable) print 
----------------------------------------
. 000037     lda #CHAR_RETURN
  --------
  (mnemo) lda 
  (keyword) # 
. (variable) CHAR_RETURN 
----------------------------------------
. 000038     sta PUTSCR_REG
  --------
  (mnemo) sta 
. (variable) PUTSCR_REG 
----------------------------------------
. 000039     rts
  --------
  (mnemo) rts 
----------------------------------------
. 000041 print
. (variable) print 
----------------------------------------
. 000043     stx op1
  --------
  (mnemo) stx 
. (variable) op1 
----------------------------------------
. 000044     sty op1+1
  --------
  (mnemo) sty 
. (variable) op1 
  (keyword) + 
X (variable) 1 
----------------------------------------
. 000045     ldy #0
  --------
  (mnemo) ldy 
  (keyword) # 
X (variable) 0 
----------------------------------------
. 000047 print_l1
. (variable) print_l1 
----------------------------------------
. 000048     lda (op1),y
  --------
  (mnemo) lda 
  (keyword) ( 
. (variable) op1 
  (keyword) ) 
  (keyword) , 
  (keyword) y 
----------------------------------------
. 000049     cmp #0
  --------
  (mnemo) cmp 
  (keyword) # 
X (variable) 0 
----------------------------------------
. 000050     beq print_out
  --------
  (mnemo) beq 
. (variable) print_out 
----------------------------------------
. 000051     sta PUTSCR_REG
  --------
  (mnemo) sta 
. (variable) PUTSCR_REG 
----------------------------------------
. 000052     iny
  --------
  (mnemo) iny 
----------------------------------------
. 000053     bne print_l1
  --------
  (mnemo) bne 
. (variable) print_l1 
----------------------------------------
. 000055 print_out
. (variable) print_out 
----------------------------------------
. 000056     rts
  --------
  (mnemo) rts 
----------------------------------------
. 000058 print_nibble
. (variable) print_nibble 
----------------------------------------
. 000059     phx
  --------
. (variable) phx 
----------------------------------------
. 000060     and #$0f
  --------
  (mnemo) and 
  (keyword) # 
X (variable) $0f 
----------------------------------------
. 000061     tax
  --------
  (mnemo) tax 
----------------------------------------
. 000062     lda hextab, x
  --------
  (mnemo) lda 
. (variable) hextab 
  (keyword) , 
  (keyword) x 
----------------------------------------
. 000063     sta PUTSCR_REG
  --------
  (mnemo) sta 
. (variable) PUTSCR_REG 
----------------------------------------
. 000064     rts
  --------
  (mnemo) rts 
----------------------------------------
. 000066 print_byte
. (variable) print_byte 
----------------------------------------
. 000067     pha
  --------
  (mnemo) pha 
----------------------------------------
. 000068     lsr a
  --------
  (mnemo) lsr 
. (variable) a 
----------------------------------------
. 000069     lsr a
  --------
  (mnemo) lsr 
. (variable) a 
----------------------------------------
. 000070     lsr a
  --------
  (mnemo) lsr 
. (variable) a 
----------------------------------------
. 000071     lsr a
  --------
  (mnemo) lsr 
. (variable) a 
----------------------------------------
. 000072     jsr print_nibble
  --------
  (mnemo) jsr 
. (variable) print_nibble 
----------------------------------------
. 000073     pla
  --------
  (mnemo) pla 
----------------------------------------
. 000074     jmp print_nibble
  --------
  (mnemo) jmp 
. (variable) print_nibble 
----------------------------------------
. 000076 print_word
. (variable) print_word 
----------------------------------------
. 000077     pha
  --------
  (mnemo) pha 
----------------------------------------
. 000078     tax
  --------
  (mnemo) tax 
----------------------------------------
. 000079     jsr print_byte
  --------
  (mnemo) jsr 
. (variable) print_byte 
----------------------------------------
. 000080     pla
  --------
  (mnemo) pla 
----------------------------------------
. 000081     jmp print_byte
  --------
  (mnemo) jmp 
. (variable) print_byte 
----------------------------------------
. 000085 start
. (variable) start 
----------------------------------------
. 000087     value = $1234
  --------
. (variable) value 
  (keyword) = 
X (variable) $1234 
----------------------------------------
. 000088     ldx #<value
  --------
  (mnemo) ldx 
  (keyword) # 
  (keyword) < 
. (variable) value 
----------------------------------------
. 000089     lda #>value
  --------
  (mnemo) lda 
  (keyword) # 
  (keyword) > 
. (variable) value 
----------------------------------------
. 000090     jsr print_word
  --------
  (mnemo) jsr 
. (variable) print_word 
----------------------------------------
. 000091 loop
. (variable) loop 
----------------------------------------
. 000092     jmp loop
  --------
  (mnemo) jmp 
. (variable) loop 
----------------------------------------
. 000096     ldx #<splash1
  --------
  (mnemo) ldx 
  (keyword) # 
  (keyword) < 
. (variable) splash1 
----------------------------------------
. 000097     ldy #>splash1
  --------
  (mnemo) ldy 
  (keyword) # 
  (keyword) > 
. (variable) splash1 
----------------------------------------
. 000098     jsr print
  --------
  (mnemo) jsr 
. (variable) print 
----------------------------------------
. 000101     ldx #<splash2
  --------
  (mnemo) ldx 
  (keyword) # 
  (keyword) < 
. (variable) splash2 
----------------------------------------
. 000102     ldy #>splash2
  --------
  (mnemo) ldy 
  (keyword) # 
  (keyword) > 
. (variable) splash2 
----------------------------------------
. 000103     jsr print
  --------
  (mnemo) jsr 
. (variable) print 
----------------------------------------
. 000106     ldx #<main
  --------
  (mnemo) ldx 
  (keyword) # 
  (keyword) < 
. (variable) main 
----------------------------------------
. 000107     ldy #>main
  --------
  (mnemo) ldy 
  (keyword) # 
  (keyword) > 
. (variable) main 
----------------------------------------
. 000108     jsr print
  --------
  (mnemo) jsr 
. (variable) print 
----------------------------------------
. 000111     ldx #<start_mes
  --------
  (mnemo) ldx 
  (keyword) # 
  (keyword) < 
. (variable) start_mes 
----------------------------------------
. 000112     lda #>start_mes
  --------
  (mnemo) lda 
  (keyword) # 
  (keyword) > 
. (variable) start_mes 
----------------------------------------
. 000113     jsr print_word
  --------
  (mnemo) jsr 
. (variable) print_word 
----------------------------------------
. 000116     ldx #<stop
  --------
  (mnemo) ldx 
  (keyword) # 
  (keyword) < 
. (variable) stop 
----------------------------------------
. 000117     ldy #>stop
  --------
  (mnemo) ldy 
  (keyword) # 
  (keyword) > 
. (variable) stop 
----------------------------------------
. 000118     jsr print
  --------
  (mnemo) jsr 
. (variable) print 
----------------------------------------
. 000121     ldx #<stop_mes
  --------
  (mnemo) ldx 
  (keyword) # 
  (keyword) < 
. (variable) stop_mes 
----------------------------------------
. 000122     lda #>stop_mes
  --------
  (mnemo) lda 
  (keyword) # 
  (keyword) > 
. (variable) stop_mes 
----------------------------------------
. 000123     jsr print_word
  --------
  (mnemo) jsr 
. (variable) print_word 
----------------------------------------
. 000125 stop
. (variable) stop 
----------------------------------------
. 000126     brk
  --------
  (mnemo) brk 
----------------------------------------
. 000128 irq
. (variable) irq 
----------------------------------------
. 000130     ldx #<irq_mes
  --------
  (mnemo) ldx 
  (keyword) # 
  (keyword) < 
. (variable) irq_mes 
----------------------------------------
. 000131     ldy #>irq_mes
  --------
  (mnemo) ldy 
  (keyword) # 
  (keyword) > 
. (variable) irq_mes 
----------------------------------------
. 000132     jsr print
  --------
  (mnemo) jsr 
. (variable) print 
----------------------------------------
. 000133 irq_loop
. (variable) irq_loop 
----------------------------------------
. 000134     jmp irq_loop
  --------
  (mnemo) jmp 
. (variable) irq_loop 
----------------------------------------
. 000136 nmi
. (variable) nmi 
----------------------------------------
. 000138     ldx #<nmi_mes
  --------
  (mnemo) ldx 
  (keyword) # 
  (keyword) < 
. (variable) nmi_mes 
----------------------------------------
. 000139     ldy #>nmi_mes
  --------
  (mnemo) ldy 
  (keyword) # 
  (keyword) > 
. (variable) nmi_mes 
----------------------------------------
. 000140     jsr print
  --------
  (mnemo) jsr 
. (variable) print 
----------------------------------------
. 000141 nmi_loop
. (variable) nmi_loop 
----------------------------------------
. 000142     jmp nmi_loop
  --------
  (mnemo) jmp 
. (variable) nmi_loop 
----------------------------------------
. 000144 splash1 .string "\"VOSC6502\" (Virtual Old School Computer with a 6502 processor)\n"
. (variable) splash1 
  (keyword) .string 
. (variable) "\"VOSC6502\" (Virtual Old School Computer with a 6502 processor)\n" 
----------------------------------------
. 000146 splash2 .string "version 0.99 -------------------------- MMXX - Pierre Faller\n"
. (variable) splash2 
  (keyword) .string 
. (variable) "version 0.99 -------------------------- MMXX - Pierre Faller\n" 
----------------------------------------
. 000148 start_mes .string "free rom "
. (variable) start_mes 
  (keyword) .string 
. (variable) "free rom " 
----------------------------------------
. 000150 stop_mes .string " bytes\n"
. (variable) stop_mes 
  (keyword) .string 
. (variable) " bytes\n" 
----------------------------------------
. 000152 nmi_mes .string " NMI occured\n"
. (variable) nmi_mes 
  (keyword) .string 
. (variable) " NMI occured\n" 
----------------------------------------
. 000154 irq_mes .string " IRQ occured\n"
. (variable) irq_mes 
  (keyword) .string 
. (variable) " IRQ occured\n" 
----------------------------------------
. 000156 hextab .ch_array "0123456789ABCDEF"
. (variable) hextab 
  (keyword) .ch_array 
. (variable) "0123456789ABCDEF" 
----------------------------------------
. 000158 source_end
. (variable) source_end 
----------------------------------------
