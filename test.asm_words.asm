000007     CHAR_RETURN = $0a
  --------                              
. (variable) CHAR_RETURN                CHAR_RETURN      ------
. (keyword) =                           
. (variable) $0a                        $0a              0x000a
----------------------------------------
000010     PUTSCR_REG = $bf00
  --------                              
. (variable) PUTSCR_REG                 PUTSCR_REG       ------
. (keyword) =                           
. (variable) $bf00                      $bf00            0xbf00
----------------------------------------
000012     x1 = 'a;blablabla...
  --------                              
. (variable) x1                         x1               ------
. (keyword) =                           
. (variable) 'a                         'a               0x0061
----------------------------------------
000013     x2 = ~10000001
  --------                              
. (variable) x2                         x2               ------
. (keyword) =                           
. (variable) ~10000001                  ~10000001        0x0081
----------------------------------------
000014     x3 = "azerty"
  --------                              
. (variable) x3                         x3               ------
. (keyword) =                           
. (variable) "azerty"                   "azerty"         ------
----------------------------------------
000016     * = $f000
  --------                              
. (keyword) *                           
. (keyword) =                           
. (variable) $f000                      $f000            0xf000
----------------------------------------
000017     y
  --------                              
. (keyword) y                           
----------------------------------------
000019     adc ($44,x)
  --------                              
X (mnemo) adc                           
. (variable) $44                        $44              0x0044
----------------------------------------
000020   ADC ($44,X)
  --------                              
X (mnemo) ADC                           
. (variable) $44                        $44              0x0044
----------------------------------------
000022 source_start
. (variable) source_start               source_start     ------
----------------------------------------
000024 hooks
. (variable) hooks                      hooks            ------
----------------------------------------
000025     .word print
  --------                              
. (keyword) .word                       
. (variable) print                      print            ------
----------------------------------------
000026     .word print_nibble
  --------                              
. (keyword) .word                       
. (variable) print_nibble               print_nibble     ------
----------------------------------------
000027     .word print_byte
  --------                              
. (keyword) .word                       
. (variable) print_byte                 print_byte       ------
----------------------------------------
000028     .word print_word
  --------                              
. (keyword) .word                       
. (variable) print_word                 print_word       ------
----------------------------------------
000030 splash1 .string "\"VOSC6502\" (Virtual Old School ; Computer with a 6502 processor)\n";blablabla...
. (variable) splash1                    splash1          ------
. (keyword) .string                     
. (variable) "\"VOSC6502\" (Virtual Old School ; Computer with a 6502 processor)\n" "\"VOSC6502\" (Virtual Old School ; Computer with a 6502 processor)\n" ------
----------------------------------------
000032 splash2 .string "version 0.99 -------------------------- MMXX - Pierre Faller\n"
. (variable) splash2                    splash2          ------
. (keyword) .string                     
. (variable) "version 0.99 -------------------------- MMXX - Pierre Faller\n" "version 0.99 -------------------------- MMXX - Pierre Faller\n" ------
----------------------------------------
000034 main
. (variable) main                       main             ------
----------------------------------------
000035     jmp start
  --------                              
. (mnemo) jmp                           
. (variable) start                      start            ------
----------------------------------------
000037     nop
  --------                              
X (mnemo) nop                           
----------------------------------------
000038     nop
  --------                              
X (mnemo) nop                           
----------------------------------------
000039     nop
  --------                              
X (mnemo) nop                           
----------------------------------------
000040     brk
  --------                              
X (mnemo) brk                           
----------------------------------------
000042 println
. (variable) println                    println          ------
----------------------------------------
000043     jsr print
  --------                              
. (mnemo) jsr                           
. (variable) print                      print            ------
----------------------------------------
000044     lda #CHAR_RETURN
  --------                              
X (mnemo) lda                           
. (variable) CHAR_RETURN                CHAR_RETURN      ------
----------------------------------------
000045     sta PUTSCR_REG
  --------                              
. (mnemo) sta                           
. (variable) PUTSCR_REG                 PUTSCR_REG       ------
----------------------------------------
000046     rts
  --------                              
X (mnemo) rts                           
----------------------------------------
000048 print
. (variable) print                      print            ------
----------------------------------------
000050     stx op1
  --------                              
. (mnemo) stx                           
. (variable) op1                        op1              ------
----------------------------------------
000051     sty op1+1
  --------                              
. (mnemo) sty                           
. (variable) op1                        op1              ------
. (keyword) +                           
. (variable) 1                          1                0x0001
----------------------------------------
000052     ldy #0
  --------                              
X (mnemo) ldy                           
. (variable) 0                          0                0x0000
----------------------------------------
000054 print_l1
. (variable) print_l1                   print_l1         ------
----------------------------------------
000055     lda (op1),y
  --------                              
X (mnemo) lda                           
. (keyword) (                           
. (variable) op1                        op1              ------
. (keyword) )                           
----------------------------------------
000056     cmp #0
  --------                              
X (mnemo) cmp                           
. (variable) 0                          0                0x0000
----------------------------------------
000057     beq print_out
  --------                              
. (mnemo) beq                           
. (variable) print_out                  print_out        ------
----------------------------------------
000058     sta PUTSCR_REG
  --------                              
. (mnemo) sta                           
. (variable) PUTSCR_REG                 PUTSCR_REG       ------
----------------------------------------
000059     iny
  --------                              
X (mnemo) iny                           
----------------------------------------
000060     bne print_l1
  --------                              
. (mnemo) bne                           
. (variable) print_l1                   print_l1         ------
----------------------------------------
000062 print_out
. (variable) print_out                  print_out        ------
----------------------------------------
000063     rts
  --------                              
X (mnemo) rts                           
----------------------------------------
000065 print_nibble
. (variable) print_nibble               print_nibble     ------
----------------------------------------
000066     and #$0f
  --------                              
X (mnemo) and                           
. (variable) $0f                        $0f              0x000f
----------------------------------------
000067     tax
  --------                              
X (mnemo) tax                           
----------------------------------------
000068     lda hextab, x
  --------                              
X (mnemo) lda                           
. (variable) hextab                     hextab           ------
----------------------------------------
000069     sta PUTSCR_REG
  --------                              
. (mnemo) sta                           
. (variable) PUTSCR_REG                 PUTSCR_REG       ------
----------------------------------------
000070     rts
  --------                              
X (mnemo) rts                           
----------------------------------------
000072 print_byte
. (variable) print_byte                 print_byte       ------
----------------------------------------
000073     pha
  --------                              
X (mnemo) pha                           
----------------------------------------
000074     lsr
  --------                              
X (mnemo) lsr                           
----------------------------------------
000075     lsr
  --------                              
X (mnemo) lsr                           
----------------------------------------
000076     lsr
  --------                              
X (mnemo) lsr                           
----------------------------------------
000077     lsr
  --------                              
X (mnemo) lsr                           
----------------------------------------
000078     jsr print_nibble
  --------                              
. (mnemo) jsr                           
. (variable) print_nibble               print_nibble     ------
----------------------------------------
000079     pla
  --------                              
X (mnemo) pla                           
----------------------------------------
000080     jmp print_nibble
  --------                              
. (mnemo) jmp                           
. (variable) print_nibble               print_nibble     ------
----------------------------------------
000082 print_word
. (variable) print_word                 print_word       ------
----------------------------------------
000083     pha
  --------                              
X (mnemo) pha                           
----------------------------------------
000084     tax
  --------                              
X (mnemo) tax                           
----------------------------------------
000085     jsr print_byte
  --------                              
. (mnemo) jsr                           
. (variable) print_byte                 print_byte       ------
----------------------------------------
000086     pla
  --------                              
X (mnemo) pla                           
----------------------------------------
000087     jmp print_byte
  --------                              
. (mnemo) jmp                           
. (variable) print_byte                 print_byte       ------
----------------------------------------
000089 start
. (variable) start                      start            ------
----------------------------------------
000091     value = $1234
  --------                              
. (variable) value                      value            ------
. (keyword) =                           
. (variable) $1234                      $1234            0x1234
----------------------------------------
000092     ldx #<value
  --------                              
X (mnemo) ldx                           
. (keyword) <                           
. (variable) value                      value            ------
----------------------------------------
000093     lda #>value
  --------                              
X (mnemo) lda                           
. (keyword) >                           
. (variable) value                      value            ------
----------------------------------------
000094     jsr print_word
  --------                              
. (mnemo) jsr                           
. (variable) print_word                 print_word       ------
----------------------------------------
000095 loop
. (variable) loop                       loop             ------
----------------------------------------
000096     jmp loop
  --------                              
. (mnemo) jmp                           
. (variable) loop                       loop             ------
----------------------------------------
000100     ldx #<splash1
  --------                              
X (mnemo) ldx                           
. (keyword) <                           
. (variable) splash1                    splash1          ------
----------------------------------------
000101     ldy #>splash1
  --------                              
X (mnemo) ldy                           
. (keyword) >                           
. (variable) splash1                    splash1          ------
----------------------------------------
000102     jsr print
  --------                              
. (mnemo) jsr                           
. (variable) print                      print            ------
----------------------------------------
000105     ldx #<splash2 + 3
  --------                              
X (mnemo) ldx                           
. (keyword) <                           
. (variable) splash2                    splash2          ------
. (keyword) +                           
. (variable) 3                          3                0x0003
----------------------------------------
000106     ldy #>splash2
  --------                              
X (mnemo) ldy                           
. (keyword) >                           
. (variable) splash2                    splash2          ------
----------------------------------------
000107     jsr print
  --------                              
. (mnemo) jsr                           
. (variable) print                      print            ------
----------------------------------------
000110     ldx #<main
  --------                              
X (mnemo) ldx                           
. (keyword) <                           
. (variable) main                       main             ------
----------------------------------------
000111     ldy #>main
  --------                              
X (mnemo) ldy                           
. (keyword) >                           
. (variable) main                       main             ------
----------------------------------------
000112     jsr print
  --------                              
. (mnemo) jsr                           
. (variable) print                      print            ------
----------------------------------------
000115     ldx #<start_mes
  --------                              
X (mnemo) ldx                           
. (keyword) <                           
. (variable) start_mes                  start_mes        ------
----------------------------------------
000116     lda #>start_mes
  --------                              
X (mnemo) lda                           
. (keyword) >                           
. (variable) start_mes                  start_mes        ------
----------------------------------------
000117     jsr print_word
  --------                              
. (mnemo) jsr                           
. (variable) print_word                 print_word       ------
----------------------------------------
000120     ldx #<stop
  --------                              
X (mnemo) ldx                           
. (keyword) <                           
. (variable) stop                       stop             ------
----------------------------------------
000121     ldy #>stop
  --------                              
X (mnemo) ldy                           
. (keyword) >                           
. (variable) stop                       stop             ------
----------------------------------------
000122     jsr print
  --------                              
. (mnemo) jsr                           
. (variable) print                      print            ------
----------------------------------------
000125     ldx #<stop_mes;blablabla
  --------                              
X (mnemo) ldx                           
. (keyword) <                           
. (variable) stop_mes                   stop_mes         ------
----------------------------------------
000126     lda #>stop_mes; blablabla
  --------                              
X (mnemo) lda                           
. (keyword) >                           
. (variable) stop_mes                   stop_mes         ------
----------------------------------------
000127     jsr print_word ;blablabla
  --------                              
. (mnemo) jsr                           
. (variable) print_word                 print_word       ------
----------------------------------------
000129 stop
. (variable) stop                       stop             ------
----------------------------------------
000130     brk
  --------                              
X (mnemo) brk                           
----------------------------------------
000132 irq
. (variable) irq                        irq              ------
----------------------------------------
000134     ldx #<irq_mes
  --------                              
X (mnemo) ldx                           
. (keyword) <                           
. (variable) irq_mes                    irq_mes          ------
----------------------------------------
000135     ldy #>irq_mes
  --------                              
X (mnemo) ldy                           
. (keyword) >                           
. (variable) irq_mes                    irq_mes          ------
----------------------------------------
000136     jsr print
  --------                              
. (mnemo) jsr                           
. (variable) print                      print            ------
----------------------------------------
000137 irq_loop
. (variable) irq_loop                   irq_loop         ------
----------------------------------------
000138     jmp irq_loop
  --------                              
. (mnemo) jmp                           
. (variable) irq_loop                   irq_loop         ------
----------------------------------------
000140 nmi
. (variable) nmi                        nmi              ------
----------------------------------------
000142     ldx #<nmi_mes
  --------                              
X (mnemo) ldx                           
. (keyword) <                           
. (variable) nmi_mes                    nmi_mes          ------
----------------------------------------
000143     ldy #>nmi_mes;blablabla...
  --------                              
X (mnemo) ldy                           
. (keyword) >                           
. (variable) nmi_mes                    nmi_mes          ------
----------------------------------------
000144     jsr       print
  --------                              
. (mnemo) jsr                           
. (variable) print                      print            ------
----------------------------------------
000145 nmi_loop
. (variable) nmi_loop                   nmi_loop         ------
----------------------------------------
000146     jmp nmi_loop
  --------                              
. (mnemo) jmp                           
. (variable) nmi_loop                   nmi_loop         ------
----------------------------------------
000148     lda 1234, x
  --------                              
X (mnemo) lda                           
. (variable) 1234                       1234             0x04d2
----------------------------------------
000149     lda 12, x
  --------                              
X (mnemo) lda                           
. (variable) 12                         12               0x000c
----------------------------------------
000150     lda 1234, y
  --------                              
X (mnemo) lda                           
. (variable) 1234                       1234             0x04d2
----------------------------------------
000151     lda 12, y
  --------                              
X (mnemo) lda                           
. (variable) 12                         12               0x000c
----------------------------------------
000152     jmp (print)
  --------                              
X (mnemo) jmp                           
. (variable) print                      print            ------
----------------------------------------
000157 start_mes .string "free rom "
. (variable) start_mes                  start_mes        ------
. (keyword) .string                     
. (variable) "free rom "                "free rom "      ------
----------------------------------------
000159 stop_mes .string " bytes\n"
. (variable) stop_mes                   stop_mes         ------
. (keyword) .string                     
. (variable) " bytes\n"                 " bytes\n"       ------
----------------------------------------
000161 nmi_mes .string " NMI occured\n"
. (variable) nmi_mes                    nmi_mes          ------
. (keyword) .string                     
. (variable) " NMI occured\n"           " NMI occured\n" ------
----------------------------------------
000163 irq_mes .string " IRQ occured\n"
. (variable) irq_mes                    irq_mes          ------
. (keyword) .string                     
. (variable) " IRQ occured\n"           " IRQ occured\n" ------
----------------------------------------
000165 hextab .ch_array "0123456789ABCDEF"
. (variable) hextab                     hextab           ------
. (keyword) .ch_array                   
. (variable) "0123456789ABCDEF"         "0123456789ABCDEF" ------
----------------------------------------
000167 source_end
. (variable) source_end                 source_end       ------
----------------------------------------
