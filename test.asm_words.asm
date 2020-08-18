. 000007     CHAR_RETURN = $0a
  --------                              
. (variable) CHAR_RETURN                CHAR_RETURN      ------
. (keyword) =                           
. (variable) $0a                        $0a              0x000a
----------------------------------------
. 000010     PUTSCR_REG = $bf00
  --------                              
. (variable) PUTSCR_REG                 PUTSCR_REG       ------
. (keyword) =                           
. (variable) $bf00                      $bf00            0xbf00
----------------------------------------
. 000012     x1 = 'a;blablabla...
  --------                              
. (variable) x1                         x1               ------
. (keyword) =                           
. (variable) 'a                         'a               0x0061
----------------------------------------
. 000013     x2 = ~10000001
  --------                              
. (variable) x2                         x2               ------
. (keyword) =                           
. (variable) ~10000001                  ~10000001        0x0081
----------------------------------------
. 000014     x3 = "azerty"
  --------                              
. (variable) x3                         x3               ------
. (keyword) =                           
. (variable) "azerty"                   "azerty"         ------
----------------------------------------
. 000016     * = $f000
  --------                              
. (keyword) *                           
. (keyword) =                           
. (variable) $f000                      $f000            0xf000
----------------------------------------
. 000017     y
  --------                              
. (keyword) y                           
----------------------------------------
. 000019     adc ($44,x)
  --------                              
X (mnemo) adc                           
. (variable) $44                        $44              0x0044
----------------------------------------
. 000020   ADC ($44,X)
  --------                              
X (mnemo) ADC                           
. (variable) $44                        $44              0x0044
----------------------------------------
. 000021   ADC ($44),Y
  --------                              
X (mnemo) ADC                           
. (variable) $44                        $44              0x0044
----------------------------------------
. 000023 source_start
. (variable) source_start               source_start     ------
----------------------------------------
. 000025 hooks
. (variable) hooks                      hooks            ------
----------------------------------------
. 000026     .word print
  --------                              
. (keyword) .word                       
. (variable) print                      print            ------
----------------------------------------
. 000027     .word print_nibble
  --------                              
. (keyword) .word                       
. (variable) print_nibble               print_nibble     ------
----------------------------------------
. 000028     .word print_byte
  --------                              
. (keyword) .word                       
. (variable) print_byte                 print_byte       ------
----------------------------------------
. 000029     .word print_word
  --------                              
. (keyword) .word                       
. (variable) print_word                 print_word       ------
----------------------------------------
. 000031 splash1 .string "\"VOSC6502\" (Virtual Old School ; Computer with a 6502 processor)\n";blablabla...
. (variable) splash1                    splash1          ------
. (keyword) .string                     
. (variable) "\"VOSC6502\" (Virtual Old School ; Computer with a 6502 processor)\n" "\"VOSC6502\" (Virtual Old School ; Computer with a 6502 processor)\n" ------
----------------------------------------
. 000033 splash2 .string "version 0.99 -------------------------- MMXX - Pierre Faller\n"
. (variable) splash2                    splash2          ------
. (keyword) .string                     
. (variable) "version 0.99 -------------------------- MMXX - Pierre Faller\n" "version 0.99 -------------------------- MMXX - Pierre Faller\n" ------
----------------------------------------
. 000035 main
. (variable) main                       main             ------
----------------------------------------
. 000036     jmp start
  --------                              
. (mnemo) jmp                           
. (variable) start                      start            ------
----------------------------------------
X 000038     nop
  --------                              
X (mnemo) nop                           
----------------------------------------
X 000039     nop
  --------                              
X (mnemo) nop                           
----------------------------------------
X 000040     nop
  --------                              
X (mnemo) nop                           
----------------------------------------
X 000041     brk
  --------                              
X (mnemo) brk                           
----------------------------------------
. 000043 println
. (variable) println                    println          ------
----------------------------------------
. 000044     jsr print
  --------                              
. (mnemo) jsr                           
. (variable) print                      print            ------
----------------------------------------
. 000045     lda #CHAR_RETURN
  --------                              
X (mnemo) lda                           
. (variable) CHAR_RETURN                CHAR_RETURN      ------
----------------------------------------
. 000046     sta PUTSCR_REG
  --------                              
. (mnemo) sta                           
. (variable) PUTSCR_REG                 PUTSCR_REG       ------
----------------------------------------
X 000047     rts
  --------                              
X (mnemo) rts                           
----------------------------------------
. 000049 print
. (variable) print                      print            ------
----------------------------------------
. 000051     stx op1
  --------                              
. (mnemo) stx                           
. (variable) op1                        op1              ------
----------------------------------------
. 000052     sty op1+1
  --------                              
. (mnemo) sty                           
. (variable) op1                        op1              ------
. (keyword) +                           
. (variable) 1                          1                0x0001
----------------------------------------
. 000053     ldy #0
  --------                              
X (mnemo) ldy                           
. (variable) 0                          0                0x0000
----------------------------------------
. 000055 print_l1
. (variable) print_l1                   print_l1         ------
----------------------------------------
. 000056     lda (op1),y
  --------                              
X (mnemo) lda                           
. (variable) op1                        op1              ------
----------------------------------------
. 000057     cmp #0
  --------                              
X (mnemo) cmp                           
. (variable) 0                          0                0x0000
----------------------------------------
. 000058     beq print_out
  --------                              
. (mnemo) beq                           
. (variable) print_out                  print_out        ------
----------------------------------------
. 000059     sta PUTSCR_REG
  --------                              
. (mnemo) sta                           
. (variable) PUTSCR_REG                 PUTSCR_REG       ------
----------------------------------------
X 000060     iny
  --------                              
X (mnemo) iny                           
----------------------------------------
. 000061     bne print_l1
  --------                              
. (mnemo) bne                           
. (variable) print_l1                   print_l1         ------
----------------------------------------
. 000063 print_out
. (variable) print_out                  print_out        ------
----------------------------------------
X 000064     rts
  --------                              
X (mnemo) rts                           
----------------------------------------
. 000066 print_nibble
. (variable) print_nibble               print_nibble     ------
----------------------------------------
. 000067     and #$0f
  --------                              
X (mnemo) and                           
. (variable) $0f                        $0f              0x000f
----------------------------------------
X 000068     tax
  --------                              
X (mnemo) tax                           
----------------------------------------
. 000069     lda hextab, x
  --------                              
X (mnemo) lda                           
. (variable) hextab                     hextab           ------
----------------------------------------
. 000070     sta PUTSCR_REG
  --------                              
. (mnemo) sta                           
. (variable) PUTSCR_REG                 PUTSCR_REG       ------
----------------------------------------
X 000071     rts
  --------                              
X (mnemo) rts                           
----------------------------------------
. 000073 print_byte
. (variable) print_byte                 print_byte       ------
----------------------------------------
X 000074     pha
  --------                              
X (mnemo) pha                           
----------------------------------------
X 000075     lsr a
  --------                              
X (mnemo) lsr                           
----------------------------------------
X 000076     lsr A
  --------                              
X (mnemo) lsr                           
----------------------------------------
X 000077     lsr a
  --------                              
X (mnemo) lsr                           
----------------------------------------
X 000078     lsr a
  --------                              
X (mnemo) lsr                           
----------------------------------------
. 000079     jsr print_nibble
  --------                              
. (mnemo) jsr                           
. (variable) print_nibble               print_nibble     ------
----------------------------------------
X 000080     pla
  --------                              
X (mnemo) pla                           
----------------------------------------
. 000081     jmp print_nibble
  --------                              
. (mnemo) jmp                           
. (variable) print_nibble               print_nibble     ------
----------------------------------------
. 000083 print_word
. (variable) print_word                 print_word       ------
----------------------------------------
X 000084     pha
  --------                              
X (mnemo) pha                           
----------------------------------------
X 000085     tax
  --------                              
X (mnemo) tax                           
----------------------------------------
. 000086     jsr print_byte
  --------                              
. (mnemo) jsr                           
. (variable) print_byte                 print_byte       ------
----------------------------------------
X 000087     pla
  --------                              
X (mnemo) pla                           
----------------------------------------
. 000088     jmp print_byte
  --------                              
. (mnemo) jmp                           
. (variable) print_byte                 print_byte       ------
----------------------------------------
. 000090 start
. (variable) start                      start            ------
----------------------------------------
. 000092     value = $1234
  --------                              
. (variable) value                      value            ------
. (keyword) =                           
. (variable) $1234                      $1234            0x1234
----------------------------------------
. 000093     ldx #<value
  --------                              
X (mnemo) ldx                           
. (keyword) <                           
. (variable) value                      value            ------
----------------------------------------
. 000094     lda #>value
  --------                              
X (mnemo) lda                           
. (keyword) >                           
. (variable) value                      value            ------
----------------------------------------
. 000095     jsr print_word
  --------                              
. (mnemo) jsr                           
. (variable) print_word                 print_word       ------
----------------------------------------
. 000096 loop
. (variable) loop                       loop             ------
----------------------------------------
. 000097     jmp loop
  --------                              
. (mnemo) jmp                           
. (variable) loop                       loop             ------
----------------------------------------
. 000101     ldx #<splash1
  --------                              
X (mnemo) ldx                           
. (keyword) <                           
. (variable) splash1                    splash1          ------
----------------------------------------
. 000102     ldy #>splash1
  --------                              
X (mnemo) ldy                           
. (keyword) >                           
. (variable) splash1                    splash1          ------
----------------------------------------
. 000103     jsr print
  --------                              
. (mnemo) jsr                           
. (variable) print                      print            ------
----------------------------------------
. 000106     ldx #<splash2 + 3
  --------                              
X (mnemo) ldx                           
. (keyword) <                           
. (variable) splash2                    splash2          ------
. (keyword) +                           
. (variable) 3                          3                0x0003
----------------------------------------
. 000107     ldy #>splash2
  --------                              
X (mnemo) ldy                           
. (keyword) >                           
. (variable) splash2                    splash2          ------
----------------------------------------
. 000108     jsr print
  --------                              
. (mnemo) jsr                           
. (variable) print                      print            ------
----------------------------------------
. 000111     ldx #<main
  --------                              
X (mnemo) ldx                           
. (keyword) <                           
. (variable) main                       main             ------
----------------------------------------
. 000112     ldy #>main
  --------                              
X (mnemo) ldy                           
. (keyword) >                           
. (variable) main                       main             ------
----------------------------------------
. 000113     jsr print
  --------                              
. (mnemo) jsr                           
. (variable) print                      print            ------
----------------------------------------
. 000116     ldx #<start_mes
  --------                              
X (mnemo) ldx                           
. (keyword) <                           
. (variable) start_mes                  start_mes        ------
----------------------------------------
. 000117     lda #>start_mes
  --------                              
X (mnemo) lda                           
. (keyword) >                           
. (variable) start_mes                  start_mes        ------
----------------------------------------
. 000118     jsr print_word
  --------                              
. (mnemo) jsr                           
. (variable) print_word                 print_word       ------
----------------------------------------
. 000121     ldx #<stop
  --------                              
X (mnemo) ldx                           
. (keyword) <                           
. (variable) stop                       stop             ------
----------------------------------------
. 000122     ldy #>stop
  --------                              
X (mnemo) ldy                           
. (keyword) >                           
. (variable) stop                       stop             ------
----------------------------------------
. 000123     jsr print
  --------                              
. (mnemo) jsr                           
. (variable) print                      print            ------
----------------------------------------
. 000126     ldx #<stop_mes;blablabla
  --------                              
X (mnemo) ldx                           
. (keyword) <                           
. (variable) stop_mes                   stop_mes         ------
----------------------------------------
. 000127     lda #>stop_mes; blablabla
  --------                              
X (mnemo) lda                           
. (keyword) >                           
. (variable) stop_mes                   stop_mes         ------
----------------------------------------
. 000128     jsr print_word ;blablabla
  --------                              
. (mnemo) jsr                           
. (variable) print_word                 print_word       ------
----------------------------------------
. 000130 stop
. (variable) stop                       stop             ------
----------------------------------------
X 000131     brk
  --------                              
X (mnemo) brk                           
----------------------------------------
. 000133 irq
. (variable) irq                        irq              ------
----------------------------------------
. 000135     ldx #<irq_mes
  --------                              
X (mnemo) ldx                           
. (keyword) <                           
. (variable) irq_mes                    irq_mes          ------
----------------------------------------
. 000136     ldy #>irq_mes
  --------                              
X (mnemo) ldy                           
. (keyword) >                           
. (variable) irq_mes                    irq_mes          ------
----------------------------------------
. 000137     jsr print
  --------                              
. (mnemo) jsr                           
. (variable) print                      print            ------
----------------------------------------
. 000138 irq_loop
. (variable) irq_loop                   irq_loop         ------
----------------------------------------
. 000139     jmp irq_loop
  --------                              
. (mnemo) jmp                           
. (variable) irq_loop                   irq_loop         ------
----------------------------------------
. 000141 nmi
. (variable) nmi                        nmi              ------
----------------------------------------
. 000143     ldx #<nmi_mes
  --------                              
X (mnemo) ldx                           
. (keyword) <                           
. (variable) nmi_mes                    nmi_mes          ------
----------------------------------------
. 000144     ldy #>nmi_mes;blablabla...
  --------                              
X (mnemo) ldy                           
. (keyword) >                           
. (variable) nmi_mes                    nmi_mes          ------
----------------------------------------
. 000145     jsr       print
  --------                              
. (mnemo) jsr                           
. (variable) print                      print            ------
----------------------------------------
. 000146 nmi_loop
. (variable) nmi_loop                   nmi_loop         ------
----------------------------------------
. 000147     jmp nmi_loop
  --------                              
. (mnemo) jmp                           
. (variable) nmi_loop                   nmi_loop         ------
----------------------------------------
. 000149     lda 1234, x
  --------                              
X (mnemo) lda                           
. (variable) 1234                       1234             0x04d2
----------------------------------------
. 000150     lda 12, x
  --------                              
X (mnemo) lda                           
. (variable) 12                         12               0x000c
----------------------------------------
. 000151     lda 1234, y
  --------                              
X (mnemo) lda                           
. (variable) 1234                       1234             0x04d2
----------------------------------------
. 000152     lda 12, y
  --------                              
X (mnemo) lda                           
. (variable) 12                         12               0x000c
----------------------------------------
. 000153     jmp (print)
  --------                              
X (mnemo) jmp                           
. (variable) print                      print            ------
----------------------------------------
. 000158 start_mes .string "free rom "
. (variable) start_mes                  start_mes        ------
. (keyword) .string                     
. (variable) "free rom "                "free rom "      ------
----------------------------------------
. 000160 stop_mes .string " bytes\n"
. (variable) stop_mes                   stop_mes         ------
. (keyword) .string                     
. (variable) " bytes\n"                 " bytes\n"       ------
----------------------------------------
. 000162 nmi_mes .string " NMI occured\n"
. (variable) nmi_mes                    nmi_mes          ------
. (keyword) .string                     
. (variable) " NMI occured\n"           " NMI occured\n" ------
----------------------------------------
. 000164 irq_mes .string " IRQ occured\n"
. (variable) irq_mes                    irq_mes          ------
. (keyword) .string                     
. (variable) " IRQ occured\n"           " IRQ occured\n" ------
----------------------------------------
. 000166 hextab .ch_array "0123456789ABCDEF"
. (variable) hextab                     hextab           ------
. (keyword) .ch_array                   
. (variable) "0123456789ABCDEF"         "0123456789ABCDEF" ------
----------------------------------------
. 000168 source_end
. (variable) source_end                 source_end       ------
----------------------------------------
