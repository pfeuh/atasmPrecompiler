. 000009     CHAR_RETURN = $0a
  --------                              
. (variable) CHAR_RETURN                CHAR_RETURN      ------
. (keyword) =                           
X (variable) $0a                        $0a              0x000a
----------------------------------------
. 000012     PUTSCR_REG = $bf00
  --------                              
. (variable) PUTSCR_REG                 PUTSCR_REG       ------
. (keyword) =                           
X (variable) $bf00                      $bf00            0xbf00
----------------------------------------
. 000014     op1 = 0
  --------                              
. (variable) op1                        op1              ------
. (keyword) =                           
X (variable) 0                          0                0x0000
----------------------------------------
. 000015     op2 = 2
  --------                              
. (variable) op2                        op2              ------
. (keyword) =                           
X (variable) 2                          2                0x0002
----------------------------------------
. 000016     op3 = 4
  --------                              
. (variable) op3                        op3              ------
. (keyword) =                           
X (variable) 4                          4                0x0004
----------------------------------------
. 000017     zp  = 6
  --------                              
. (variable) zp                         zp               ------
. (keyword) =                           
X (variable) 6                          6                0x0006
----------------------------------------
. 000020     * = $f000
  --------                              
. (keyword) *                           
. (keyword) =                           
X (variable) $f000                      $f000            0xf000
----------------------------------------
. 000022 source_start
. (variable) source_start               source_start     ------
----------------------------------------
. 000024 hooks
. (variable) hooks                      hooks            ------
----------------------------------------
. 000025     .word print
  --------                              
. (keyword) .word                       
. (variable) print                      print            ------
----------------------------------------
. 000026     .word print_nibble
  --------                              
. (keyword) .word                       
. (variable) print_nibble               print_nibble     ------
----------------------------------------
. 000027     .word print_byte
  --------                              
. (keyword) .word                       
. (variable) print_byte                 print_byte       ------
----------------------------------------
. 000028     .word print_word
  --------                              
. (keyword) .word                       
. (variable) print_word                 print_word       ------
----------------------------------------
. 000030 main
. (variable) main                       main             ------
----------------------------------------
. 000031     jmp start
  --------                              
X (mnemo) jmp                           
. (variable) start                      start            ------
----------------------------------------
. 000035 println
. (variable) println                    println          ------
----------------------------------------
. 000036     jsr print
  --------                              
X (mnemo) jsr                           
. (variable) print                      print            ------
----------------------------------------
. 000037     lda #CHAR_RETURN
  --------                              
X (mnemo) lda                           
. (variable) CHAR_RETURN                CHAR_RETURN      ------
----------------------------------------
. 000038     sta PUTSCR_REG
  --------                              
X (mnemo) sta                           
. (variable) PUTSCR_REG                 PUTSCR_REG       ------
----------------------------------------
X 000039     rts
  --------                              
X (mnemo) rts                           
----------------------------------------
. 000041 print
. (variable) print                      print            ------
----------------------------------------
. 000043     stx op1
  --------                              
X (mnemo) stx                           
. (variable) op1                        op1              ------
----------------------------------------
. 000044     sty op1+1
  --------                              
X (mnemo) sty                           
. (variable) op1                        op1              ------
. (keyword) +                           
X (variable) 1                          1                0x0001
----------------------------------------
X 000045     ldy #0
  --------                              
X (mnemo) ldy                           
X (variable) 0                          0                0x0000
----------------------------------------
. 000047 print_l1
. (variable) print_l1                   print_l1         ------
----------------------------------------
. 000048     lda (op1),y
  --------                              
X (mnemo) lda                           
. (variable) op1                        op1              ------
----------------------------------------
X 000049     cmp #0
  --------                              
X (mnemo) cmp                           
X (variable) 0                          0                0x0000
----------------------------------------
. 000050     beq print_out
  --------                              
X (mnemo) beq                           
. (variable) print_out                  print_out        ------
----------------------------------------
. 000051     sta PUTSCR_REG
  --------                              
X (mnemo) sta                           
. (variable) PUTSCR_REG                 PUTSCR_REG       ------
----------------------------------------
X 000052     iny
  --------                              
X (mnemo) iny                           
----------------------------------------
. 000053     bne print_l1
  --------                              
X (mnemo) bne                           
. (variable) print_l1                   print_l1         ------
----------------------------------------
. 000055 print_out
. (variable) print_out                  print_out        ------
----------------------------------------
X 000056     rts
  --------                              
X (mnemo) rts                           
----------------------------------------
. 000058 print_nibble
. (variable) print_nibble               print_nibble     ------
----------------------------------------
. 000059     phx
  --------                              
. (variable) phx                        phx              ------
----------------------------------------
X 000060     and #$0f
  --------                              
X (mnemo) and                           
X (variable) $0f                        $0f              0x000f
----------------------------------------
X 000061     tax
  --------                              
X (mnemo) tax                           
----------------------------------------
. 000062     lda hextab, x
  --------                              
X (mnemo) lda                           
. (variable) hextab                     hextab           ------
. (keyword) ,                           
. (keyword) x                           
----------------------------------------
. 000063     sta PUTSCR_REG
  --------                              
X (mnemo) sta                           
. (variable) PUTSCR_REG                 PUTSCR_REG       ------
----------------------------------------
X 000064     rts
  --------                              
X (mnemo) rts                           
----------------------------------------
. 000066 print_byte
. (variable) print_byte                 print_byte       ------
----------------------------------------
X 000067     pha
  --------                              
X (mnemo) pha                           
----------------------------------------
X 000068     lsr a
  --------                              
X (mnemo) lsr                           
----------------------------------------
X 000069     lsr a
  --------                              
X (mnemo) lsr                           
----------------------------------------
X 000070     lsr a
  --------                              
X (mnemo) lsr                           
----------------------------------------
X 000071     lsr a
  --------                              
X (mnemo) lsr                           
----------------------------------------
. 000072     jsr print_nibble
  --------                              
X (mnemo) jsr                           
. (variable) print_nibble               print_nibble     ------
----------------------------------------
X 000073     pla
  --------                              
X (mnemo) pla                           
----------------------------------------
. 000074     jmp print_nibble
  --------                              
X (mnemo) jmp                           
. (variable) print_nibble               print_nibble     ------
----------------------------------------
. 000076 print_word
. (variable) print_word                 print_word       ------
----------------------------------------
X 000077     pha
  --------                              
X (mnemo) pha                           
----------------------------------------
X 000078     tax
  --------                              
X (mnemo) tax                           
----------------------------------------
. 000079     jsr print_byte
  --------                              
X (mnemo) jsr                           
. (variable) print_byte                 print_byte       ------
----------------------------------------
X 000080     pla
  --------                              
X (mnemo) pla                           
----------------------------------------
. 000081     jmp print_byte
  --------                              
X (mnemo) jmp                           
. (variable) print_byte                 print_byte       ------
----------------------------------------
. 000085 start
. (variable) start                      start            ------
----------------------------------------
. 000087     value = $1234
  --------                              
. (variable) value                      value            ------
. (keyword) =                           
X (variable) $1234                      $1234            0x1234
----------------------------------------
. 000088     ldx #<value
  --------                              
X (mnemo) ldx                           
. (keyword) <                           
. (variable) value                      value            ------
----------------------------------------
. 000089     lda #>value
  --------                              
X (mnemo) lda                           
. (keyword) >                           
. (variable) value                      value            ------
----------------------------------------
. 000090     jsr print_word
  --------                              
X (mnemo) jsr                           
. (variable) print_word                 print_word       ------
----------------------------------------
. 000091 loop
. (variable) loop                       loop             ------
----------------------------------------
. 000092     jmp loop
  --------                              
X (mnemo) jmp                           
. (variable) loop                       loop             ------
----------------------------------------
. 000096     ldx #<splash1
  --------                              
X (mnemo) ldx                           
. (keyword) <                           
. (variable) splash1                    splash1          ------
----------------------------------------
. 000097     ldy #>splash1
  --------                              
X (mnemo) ldy                           
. (keyword) >                           
. (variable) splash1                    splash1          ------
----------------------------------------
. 000098     jsr print
  --------                              
X (mnemo) jsr                           
. (variable) print                      print            ------
----------------------------------------
. 000101     ldx #<splash2
  --------                              
X (mnemo) ldx                           
. (keyword) <                           
. (variable) splash2                    splash2          ------
----------------------------------------
. 000102     ldy #>splash2
  --------                              
X (mnemo) ldy                           
. (keyword) >                           
. (variable) splash2                    splash2          ------
----------------------------------------
. 000103     jsr print
  --------                              
X (mnemo) jsr                           
. (variable) print                      print            ------
----------------------------------------
. 000106     ldx #<main
  --------                              
X (mnemo) ldx                           
. (keyword) <                           
. (variable) main                       main             ------
----------------------------------------
. 000107     ldy #>main
  --------                              
X (mnemo) ldy                           
. (keyword) >                           
. (variable) main                       main             ------
----------------------------------------
. 000108     jsr print
  --------                              
X (mnemo) jsr                           
. (variable) print                      print            ------
----------------------------------------
. 000111     ldx #<start_mes
  --------                              
X (mnemo) ldx                           
. (keyword) <                           
. (variable) start_mes                  start_mes        ------
----------------------------------------
. 000112     lda #>start_mes
  --------                              
X (mnemo) lda                           
. (keyword) >                           
. (variable) start_mes                  start_mes        ------
----------------------------------------
. 000113     jsr print_word
  --------                              
X (mnemo) jsr                           
. (variable) print_word                 print_word       ------
----------------------------------------
. 000116     ldx #<stop
  --------                              
X (mnemo) ldx                           
. (keyword) <                           
. (variable) stop                       stop             ------
----------------------------------------
. 000117     ldy #>stop
  --------                              
X (mnemo) ldy                           
. (keyword) >                           
. (variable) stop                       stop             ------
----------------------------------------
. 000118     jsr print
  --------                              
X (mnemo) jsr                           
. (variable) print                      print            ------
----------------------------------------
. 000121     ldx #<stop_mes
  --------                              
X (mnemo) ldx                           
. (keyword) <                           
. (variable) stop_mes                   stop_mes         ------
----------------------------------------
. 000122     lda #>stop_mes
  --------                              
X (mnemo) lda                           
. (keyword) >                           
. (variable) stop_mes                   stop_mes         ------
----------------------------------------
. 000123     jsr print_word
  --------                              
X (mnemo) jsr                           
. (variable) print_word                 print_word       ------
----------------------------------------
. 000125 stop
. (variable) stop                       stop             ------
----------------------------------------
X 000126     brk
  --------                              
X (mnemo) brk                           
----------------------------------------
. 000128 irq
. (variable) irq                        irq              ------
----------------------------------------
. 000130     ldx #<irq_mes
  --------                              
X (mnemo) ldx                           
. (keyword) <                           
. (variable) irq_mes                    irq_mes          ------
----------------------------------------
. 000131     ldy #>irq_mes
  --------                              
X (mnemo) ldy                           
. (keyword) >                           
. (variable) irq_mes                    irq_mes          ------
----------------------------------------
. 000132     jsr print
  --------                              
X (mnemo) jsr                           
. (variable) print                      print            ------
----------------------------------------
. 000133 irq_loop
. (variable) irq_loop                   irq_loop         ------
----------------------------------------
. 000134     jmp irq_loop
  --------                              
X (mnemo) jmp                           
. (variable) irq_loop                   irq_loop         ------
----------------------------------------
. 000136 nmi
. (variable) nmi                        nmi              ------
----------------------------------------
. 000138     ldx #<nmi_mes
  --------                              
X (mnemo) ldx                           
. (keyword) <                           
. (variable) nmi_mes                    nmi_mes          ------
----------------------------------------
. 000139     ldy #>nmi_mes
  --------                              
X (mnemo) ldy                           
. (keyword) >                           
. (variable) nmi_mes                    nmi_mes          ------
----------------------------------------
. 000140     jsr print
  --------                              
X (mnemo) jsr                           
. (variable) print                      print            ------
----------------------------------------
. 000141 nmi_loop
. (variable) nmi_loop                   nmi_loop         ------
----------------------------------------
. 000142     jmp nmi_loop
  --------                              
X (mnemo) jmp                           
. (variable) nmi_loop                   nmi_loop         ------
----------------------------------------
. 000144 splash1 ; .string "\"VOSC6502\" (Virtual Old School Computer with a 6502 processor)\n"
. (variable) splash1                    splash1          ------
----------------------------------------
. 000145     .byte $22, $56, $4f, $53, $43, $36, $35
  --------                              
. (keyword) .byte                       
X (variable) $22                        $22              0x0022
. (keyword) ,                           
X (variable) $56                        $56              0x0056
. (keyword) ,                           
X (variable) $4f                        $4f              0x004f
. (keyword) ,                           
X (variable) $53                        $53              0x0053
. (keyword) ,                           
X (variable) $43                        $43              0x0043
. (keyword) ,                           
X (variable) $36                        $36              0x0036
. (keyword) ,                           
X (variable) $35                        $35              0x0035
----------------------------------------
. 000146     .byte $30, $32, $22, $20, $28, $56, $69
  --------                              
. (keyword) .byte                       
X (variable) $30                        $30              0x0030
. (keyword) ,                           
X (variable) $32                        $32              0x0032
. (keyword) ,                           
X (variable) $22                        $22              0x0022
. (keyword) ,                           
X (variable) $20                        $20              0x0020
. (keyword) ,                           
X (variable) $28                        $28              0x0028
. (keyword) ,                           
X (variable) $56                        $56              0x0056
. (keyword) ,                           
X (variable) $69                        $69              0x0069
----------------------------------------
. 000147     .byte $72, $74, $75, $61, $6c, $20, $4f
  --------                              
. (keyword) .byte                       
X (variable) $72                        $72              0x0072
. (keyword) ,                           
X (variable) $74                        $74              0x0074
. (keyword) ,                           
X (variable) $75                        $75              0x0075
. (keyword) ,                           
X (variable) $61                        $61              0x0061
. (keyword) ,                           
X (variable) $6c                        $6c              0x006c
. (keyword) ,                           
X (variable) $20                        $20              0x0020
. (keyword) ,                           
X (variable) $4f                        $4f              0x004f
----------------------------------------
. 000148     .byte $6c, $64, $20, $53, $63, $68, $6f
  --------                              
. (keyword) .byte                       
X (variable) $6c                        $6c              0x006c
. (keyword) ,                           
X (variable) $64                        $64              0x0064
. (keyword) ,                           
X (variable) $20                        $20              0x0020
. (keyword) ,                           
X (variable) $53                        $53              0x0053
. (keyword) ,                           
X (variable) $63                        $63              0x0063
. (keyword) ,                           
X (variable) $68                        $68              0x0068
. (keyword) ,                           
X (variable) $6f                        $6f              0x006f
----------------------------------------
. 000149     .byte $6f, $6c, $20, $43, $6f, $6d, $70
  --------                              
. (keyword) .byte                       
X (variable) $6f                        $6f              0x006f
. (keyword) ,                           
X (variable) $6c                        $6c              0x006c
. (keyword) ,                           
X (variable) $20                        $20              0x0020
. (keyword) ,                           
X (variable) $43                        $43              0x0043
. (keyword) ,                           
X (variable) $6f                        $6f              0x006f
. (keyword) ,                           
X (variable) $6d                        $6d              0x006d
. (keyword) ,                           
X (variable) $70                        $70              0x0070
----------------------------------------
. 000150     .byte $75, $74, $65, $72, $20, $77, $69
  --------                              
. (keyword) .byte                       
X (variable) $75                        $75              0x0075
. (keyword) ,                           
X (variable) $74                        $74              0x0074
. (keyword) ,                           
X (variable) $65                        $65              0x0065
. (keyword) ,                           
X (variable) $72                        $72              0x0072
. (keyword) ,                           
X (variable) $20                        $20              0x0020
. (keyword) ,                           
X (variable) $77                        $77              0x0077
. (keyword) ,                           
X (variable) $69                        $69              0x0069
----------------------------------------
. 000151     .byte $74, $68, $20, $61, $20, $36, $35
  --------                              
. (keyword) .byte                       
X (variable) $74                        $74              0x0074
. (keyword) ,                           
X (variable) $68                        $68              0x0068
. (keyword) ,                           
X (variable) $20                        $20              0x0020
. (keyword) ,                           
X (variable) $61                        $61              0x0061
. (keyword) ,                           
X (variable) $20                        $20              0x0020
. (keyword) ,                           
X (variable) $36                        $36              0x0036
. (keyword) ,                           
X (variable) $35                        $35              0x0035
----------------------------------------
. 000152     .byte $30, $32, $20, $70, $72, $6f, $63
  --------                              
. (keyword) .byte                       
X (variable) $30                        $30              0x0030
. (keyword) ,                           
X (variable) $32                        $32              0x0032
. (keyword) ,                           
X (variable) $20                        $20              0x0020
. (keyword) ,                           
X (variable) $70                        $70              0x0070
. (keyword) ,                           
X (variable) $72                        $72              0x0072
. (keyword) ,                           
X (variable) $6f                        $6f              0x006f
. (keyword) ,                           
X (variable) $63                        $63              0x0063
----------------------------------------
. 000153     .byte $65, $73, $73, $6f, $72, $29, $0a
  --------                              
. (keyword) .byte                       
X (variable) $65                        $65              0x0065
. (keyword) ,                           
X (variable) $73                        $73              0x0073
. (keyword) ,                           
X (variable) $73                        $73              0x0073
. (keyword) ,                           
X (variable) $6f                        $6f              0x006f
. (keyword) ,                           
X (variable) $72                        $72              0x0072
. (keyword) ,                           
X (variable) $29                        $29              0x0029
. (keyword) ,                           
X (variable) $0a                        $0a              0x000a
----------------------------------------
. 000154     .byte $00
  --------                              
. (keyword) .byte                       
X (variable) $00                        $00              0x0000
----------------------------------------
. 000156 splash2 ; .string "version 0.99 -------------------------- MMXX - Pierre Faller\n"
. (variable) splash2                    splash2          ------
----------------------------------------
. 000157     .byte $76, $65, $72, $73, $69, $6f, $6e
  --------                              
. (keyword) .byte                       
X (variable) $76                        $76              0x0076
. (keyword) ,                           
X (variable) $65                        $65              0x0065
. (keyword) ,                           
X (variable) $72                        $72              0x0072
. (keyword) ,                           
X (variable) $73                        $73              0x0073
. (keyword) ,                           
X (variable) $69                        $69              0x0069
. (keyword) ,                           
X (variable) $6f                        $6f              0x006f
. (keyword) ,                           
X (variable) $6e                        $6e              0x006e
----------------------------------------
. 000158     .byte $20, $30, $2e, $39, $39, $20, $2d
  --------                              
. (keyword) .byte                       
X (variable) $20                        $20              0x0020
. (keyword) ,                           
X (variable) $30                        $30              0x0030
. (keyword) ,                           
X (variable) $2e                        $2e              0x002e
. (keyword) ,                           
X (variable) $39                        $39              0x0039
. (keyword) ,                           
X (variable) $39                        $39              0x0039
. (keyword) ,                           
X (variable) $20                        $20              0x0020
. (keyword) ,                           
X (variable) $2d                        $2d              0x002d
----------------------------------------
. 000159     .byte $2d, $2d, $2d, $2d, $2d, $2d, $2d
  --------                              
. (keyword) .byte                       
X (variable) $2d                        $2d              0x002d
. (keyword) ,                           
X (variable) $2d                        $2d              0x002d
. (keyword) ,                           
X (variable) $2d                        $2d              0x002d
. (keyword) ,                           
X (variable) $2d                        $2d              0x002d
. (keyword) ,                           
X (variable) $2d                        $2d              0x002d
. (keyword) ,                           
X (variable) $2d                        $2d              0x002d
. (keyword) ,                           
X (variable) $2d                        $2d              0x002d
----------------------------------------
. 000160     .byte $2d, $2d, $2d, $2d, $2d, $2d, $2d
  --------                              
. (keyword) .byte                       
X (variable) $2d                        $2d              0x002d
. (keyword) ,                           
X (variable) $2d                        $2d              0x002d
. (keyword) ,                           
X (variable) $2d                        $2d              0x002d
. (keyword) ,                           
X (variable) $2d                        $2d              0x002d
. (keyword) ,                           
X (variable) $2d                        $2d              0x002d
. (keyword) ,                           
X (variable) $2d                        $2d              0x002d
. (keyword) ,                           
X (variable) $2d                        $2d              0x002d
----------------------------------------
. 000161     .byte $2d, $2d, $2d, $2d, $2d, $2d, $2d
  --------                              
. (keyword) .byte                       
X (variable) $2d                        $2d              0x002d
. (keyword) ,                           
X (variable) $2d                        $2d              0x002d
. (keyword) ,                           
X (variable) $2d                        $2d              0x002d
. (keyword) ,                           
X (variable) $2d                        $2d              0x002d
. (keyword) ,                           
X (variable) $2d                        $2d              0x002d
. (keyword) ,                           
X (variable) $2d                        $2d              0x002d
. (keyword) ,                           
X (variable) $2d                        $2d              0x002d
----------------------------------------
. 000162     .byte $2d, $2d, $2d, $2d, $20, $4d, $4d
  --------                              
. (keyword) .byte                       
X (variable) $2d                        $2d              0x002d
. (keyword) ,                           
X (variable) $2d                        $2d              0x002d
. (keyword) ,                           
X (variable) $2d                        $2d              0x002d
. (keyword) ,                           
X (variable) $2d                        $2d              0x002d
. (keyword) ,                           
X (variable) $20                        $20              0x0020
. (keyword) ,                           
X (variable) $4d                        $4d              0x004d
. (keyword) ,                           
X (variable) $4d                        $4d              0x004d
----------------------------------------
. 000163     .byte $58, $58, $20, $2d, $20, $50, $69
  --------                              
. (keyword) .byte                       
X (variable) $58                        $58              0x0058
. (keyword) ,                           
X (variable) $58                        $58              0x0058
. (keyword) ,                           
X (variable) $20                        $20              0x0020
. (keyword) ,                           
X (variable) $2d                        $2d              0x002d
. (keyword) ,                           
X (variable) $20                        $20              0x0020
. (keyword) ,                           
X (variable) $50                        $50              0x0050
. (keyword) ,                           
X (variable) $69                        $69              0x0069
----------------------------------------
. 000164     .byte $65, $72, $72, $65, $20, $46, $61
  --------                              
. (keyword) .byte                       
X (variable) $65                        $65              0x0065
. (keyword) ,                           
X (variable) $72                        $72              0x0072
. (keyword) ,                           
X (variable) $72                        $72              0x0072
. (keyword) ,                           
X (variable) $65                        $65              0x0065
. (keyword) ,                           
X (variable) $20                        $20              0x0020
. (keyword) ,                           
X (variable) $46                        $46              0x0046
. (keyword) ,                           
X (variable) $61                        $61              0x0061
----------------------------------------
. 000165     .byte $6c, $6c, $65, $72, $0a, $00
  --------                              
. (keyword) .byte                       
X (variable) $6c                        $6c              0x006c
. (keyword) ,                           
X (variable) $6c                        $6c              0x006c
. (keyword) ,                           
X (variable) $65                        $65              0x0065
. (keyword) ,                           
X (variable) $72                        $72              0x0072
. (keyword) ,                           
X (variable) $0a                        $0a              0x000a
. (keyword) ,                           
X (variable) $00                        $00              0x0000
----------------------------------------
. 000167 start_mes ; .string "free rom "
. (variable) start_mes                  start_mes        ------
----------------------------------------
. 000168     .byte $66, $72, $65, $65, $20, $72, $6f
  --------                              
. (keyword) .byte                       
X (variable) $66                        $66              0x0066
. (keyword) ,                           
X (variable) $72                        $72              0x0072
. (keyword) ,                           
X (variable) $65                        $65              0x0065
. (keyword) ,                           
X (variable) $65                        $65              0x0065
. (keyword) ,                           
X (variable) $20                        $20              0x0020
. (keyword) ,                           
X (variable) $72                        $72              0x0072
. (keyword) ,                           
X (variable) $6f                        $6f              0x006f
----------------------------------------
. 000169     .byte $6d, $20, $00
  --------                              
. (keyword) .byte                       
X (variable) $6d                        $6d              0x006d
. (keyword) ,                           
X (variable) $20                        $20              0x0020
. (keyword) ,                           
X (variable) $00                        $00              0x0000
----------------------------------------
. 000171 stop_mes ; .string " bytes\n"
. (variable) stop_mes                   stop_mes         ------
----------------------------------------
. 000172     .byte $20, $62, $79, $74, $65, $73, $0a
  --------                              
. (keyword) .byte                       
X (variable) $20                        $20              0x0020
. (keyword) ,                           
X (variable) $62                        $62              0x0062
. (keyword) ,                           
X (variable) $79                        $79              0x0079
. (keyword) ,                           
X (variable) $74                        $74              0x0074
. (keyword) ,                           
X (variable) $65                        $65              0x0065
. (keyword) ,                           
X (variable) $73                        $73              0x0073
. (keyword) ,                           
X (variable) $0a                        $0a              0x000a
----------------------------------------
. 000173     .byte $00
  --------                              
. (keyword) .byte                       
X (variable) $00                        $00              0x0000
----------------------------------------
. 000175 nmi_mes ; .string " NMI occured\n"
. (variable) nmi_mes                    nmi_mes          ------
----------------------------------------
. 000176     .byte $20, $4e, $4d, $49, $20, $6f, $63
  --------                              
. (keyword) .byte                       
X (variable) $20                        $20              0x0020
. (keyword) ,                           
X (variable) $4e                        $4e              0x004e
. (keyword) ,                           
X (variable) $4d                        $4d              0x004d
. (keyword) ,                           
X (variable) $49                        $49              0x0049
. (keyword) ,                           
X (variable) $20                        $20              0x0020
. (keyword) ,                           
X (variable) $6f                        $6f              0x006f
. (keyword) ,                           
X (variable) $63                        $63              0x0063
----------------------------------------
. 000177     .byte $63, $75, $72, $65, $64, $0a, $00
  --------                              
. (keyword) .byte                       
X (variable) $63                        $63              0x0063
. (keyword) ,                           
X (variable) $75                        $75              0x0075
. (keyword) ,                           
X (variable) $72                        $72              0x0072
. (keyword) ,                           
X (variable) $65                        $65              0x0065
. (keyword) ,                           
X (variable) $64                        $64              0x0064
. (keyword) ,                           
X (variable) $0a                        $0a              0x000a
. (keyword) ,                           
X (variable) $00                        $00              0x0000
----------------------------------------
. 000179 irq_mes ; .string " IRQ occured\n"
. (variable) irq_mes                    irq_mes          ------
----------------------------------------
. 000180     .byte $20, $49, $52, $51, $20, $6f, $63
  --------                              
. (keyword) .byte                       
X (variable) $20                        $20              0x0020
. (keyword) ,                           
X (variable) $49                        $49              0x0049
. (keyword) ,                           
X (variable) $52                        $52              0x0052
. (keyword) ,                           
X (variable) $51                        $51              0x0051
. (keyword) ,                           
X (variable) $20                        $20              0x0020
. (keyword) ,                           
X (variable) $6f                        $6f              0x006f
. (keyword) ,                           
X (variable) $63                        $63              0x0063
----------------------------------------
. 000181     .byte $63, $75, $72, $65, $64, $0a, $00
  --------                              
. (keyword) .byte                       
X (variable) $63                        $63              0x0063
. (keyword) ,                           
X (variable) $75                        $75              0x0075
. (keyword) ,                           
X (variable) $72                        $72              0x0072
. (keyword) ,                           
X (variable) $65                        $65              0x0065
. (keyword) ,                           
X (variable) $64                        $64              0x0064
. (keyword) ,                           
X (variable) $0a                        $0a              0x000a
. (keyword) ,                           
X (variable) $00                        $00              0x0000
----------------------------------------
. 000183 hextab ; .ch_array "0123456789ABCDEF"
. (variable) hextab                     hextab           ------
----------------------------------------
. 000184     .byte $30, $31, $32, $33, $34, $35, $36
  --------                              
. (keyword) .byte                       
X (variable) $30                        $30              0x0030
. (keyword) ,                           
X (variable) $31                        $31              0x0031
. (keyword) ,                           
X (variable) $32                        $32              0x0032
. (keyword) ,                           
X (variable) $33                        $33              0x0033
. (keyword) ,                           
X (variable) $34                        $34              0x0034
. (keyword) ,                           
X (variable) $35                        $35              0x0035
. (keyword) ,                           
X (variable) $36                        $36              0x0036
----------------------------------------
. 000185     .byte $37, $38, $39, $41, $42, $43, $44
  --------                              
. (keyword) .byte                       
X (variable) $37                        $37              0x0037
. (keyword) ,                           
X (variable) $38                        $38              0x0038
. (keyword) ,                           
X (variable) $39                        $39              0x0039
. (keyword) ,                           
X (variable) $41                        $41              0x0041
. (keyword) ,                           
X (variable) $42                        $42              0x0042
. (keyword) ,                           
X (variable) $43                        $43              0x0043
. (keyword) ,                           
X (variable) $44                        $44              0x0044
----------------------------------------
. 000186     .byte $45, $46
  --------                              
. (keyword) .byte                       
X (variable) $45                        $45              0x0045
. (keyword) ,                           
X (variable) $46                        $46              0x0046
----------------------------------------
. 000188 source_end
. (variable) source_end                 source_end       ------
----------------------------------------
