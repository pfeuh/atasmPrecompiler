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
000018 source_start
. (variable) source_start               source_start     ------

----------------------------------------
000020 hooks
. (variable) hooks                      hooks            ------

----------------------------------------
000021     .word print
  --------                              
. (keyword) .word                       
. (variable) print                      print            ------

----------------------------------------
000022     .word print_nibble
  --------                              
. (keyword) .word                       
. (variable) print_nibble               print_nibble     ------

----------------------------------------
000023     .word print_byte
  --------                              
. (keyword) .word                       
. (variable) print_byte                 print_byte       ------

----------------------------------------
000024     .word print_word
  --------                              
. (keyword) .word                       
. (variable) print_word                 print_word       ------

----------------------------------------
000026 splash1 .string "\"VOSC6502\" (Virtual Old School ; Computer with a 6502 processor)\n";blablabla...
. (variable) splash1                    splash1          ------

. (keyword) .string                     
. (variable) "\"VOSC6502\" (Virtual Old School ; Computer with a 6502 processor)\n" "\"VOSC6502\" (Virtual Old School ; Computer with a 6502 processor)\n" ------

----------------------------------------
000028 splash2 .string "version 0.99 -------------------------- MMXX - Pierre Faller\n"
. (variable) splash2                    splash2          ------

. (keyword) .string                     
. (variable) "version 0.99 -------------------------- MMXX - Pierre Faller\n" "version 0.99 -------------------------- MMXX - Pierre Faller\n" ------

----------------------------------------
000030 main
. (variable) main                       main             ------

----------------------------------------
000031     jmp start
  --------                              
. (mnemo) jmp                           
. (variable) start                      start            ------

----------------------------------------
000033     nop
  --------                              
X (mnemo) nop                           
----------------------------------------
000034     nop
  --------                              
X (mnemo) nop                           
----------------------------------------
000035     nop
  --------                              
X (mnemo) nop                           
----------------------------------------
000036     brk
  --------                              
X (mnemo) brk                           
----------------------------------------
000038 println
. (variable) println                    println          ------

----------------------------------------
000039     jsr print
  --------                              
. (mnemo) jsr                           
. (variable) print                      print            ------

----------------------------------------
000040     lda #CHAR_RETURN
  --------                              
. (mnemo) lda                           
. (keyword) #                           
. (variable) CHAR_RETURN                CHAR_RETURN      ------

----------------------------------------
000041     sta PUTSCR_REG
  --------                              
. (mnemo) sta                           
. (variable) PUTSCR_REG                 PUTSCR_REG       ------

----------------------------------------
000042     rts
  --------                              
X (mnemo) rts                           
----------------------------------------
000044 print
. (variable) print                      print            ------

----------------------------------------
000046     stx op1
  --------                              
. (mnemo) stx                           
. (variable) op1                        op1              ------

----------------------------------------
000047     sty op1+1
  --------                              
. (mnemo) sty                           
. (variable) op1                        op1              ------

. (keyword) +                           
. (variable) 1                          1                0x0001

----------------------------------------
000048     ldy #0
  --------                              
. (mnemo) ldy                           
. (keyword) #                           
. (variable) 0                          0                0x0000

----------------------------------------
000050 print_l1
. (variable) print_l1                   print_l1         ------

----------------------------------------
000051     lda (op1),y
  --------                              
. (mnemo) lda                           
. (keyword) (                           
. (variable) op1                        op1              ------

. (keyword) )                           
. (keyword) ,                           
. (keyword) y                           
----------------------------------------
000052     cmp #0
  --------                              
. (mnemo) cmp                           
. (keyword) #                           
. (variable) 0                          0                0x0000

----------------------------------------
000053     beq print_out
  --------                              
. (mnemo) beq                           
. (variable) print_out                  print_out        ------

----------------------------------------
000054     sta PUTSCR_REG
  --------                              
. (mnemo) sta                           
. (variable) PUTSCR_REG                 PUTSCR_REG       ------

----------------------------------------
000055     iny
  --------                              
X (mnemo) iny                           
----------------------------------------
000056     bne print_l1
  --------                              
. (mnemo) bne                           
. (variable) print_l1                   print_l1         ------

----------------------------------------
000058 print_out
. (variable) print_out                  print_out        ------

----------------------------------------
000059     rts
  --------                              
X (mnemo) rts                           
----------------------------------------
000061 print_nibble
. (variable) print_nibble               print_nibble     ------

----------------------------------------
000062     and #$0f
  --------                              
. (mnemo) and                           
. (keyword) #                           
. (variable) $0f                        $0f              0x000f

----------------------------------------
000063     tax
  --------                              
X (mnemo) tax                           
----------------------------------------
000064     lda hextab, x
  --------                              
. (mnemo) lda                           
. (variable) hextab                     hextab           ------

. (keyword) ,                           
. (keyword) x                           
----------------------------------------
000065     sta PUTSCR_REG
  --------                              
. (mnemo) sta                           
. (variable) PUTSCR_REG                 PUTSCR_REG       ------

----------------------------------------
000066     rts
  --------                              
X (mnemo) rts                           
----------------------------------------
000068 print_byte
. (variable) print_byte                 print_byte       ------

----------------------------------------
000069     pha
  --------                              
X (mnemo) pha                           
----------------------------------------
000070     lsr
  --------                              
X (mnemo) lsr                           
----------------------------------------
000071     lsr
  --------                              
X (mnemo) lsr                           
----------------------------------------
000072     lsr
  --------                              
X (mnemo) lsr                           
----------------------------------------
000073     lsr
  --------                              
X (mnemo) lsr                           
----------------------------------------
000074     jsr print_nibble
  --------                              
. (mnemo) jsr                           
. (variable) print_nibble               print_nibble     ------

----------------------------------------
000075     pla
  --------                              
X (mnemo) pla                           
----------------------------------------
000076     jmp print_nibble
  --------                              
. (mnemo) jmp                           
. (variable) print_nibble               print_nibble     ------

----------------------------------------
000078 print_word
. (variable) print_word                 print_word       ------

----------------------------------------
000079     pha
  --------                              
X (mnemo) pha                           
----------------------------------------
000080     tax
  --------                              
X (mnemo) tax                           
----------------------------------------
000081     jsr print_byte
  --------                              
. (mnemo) jsr                           
. (variable) print_byte                 print_byte       ------

----------------------------------------
000082     pla
  --------                              
X (mnemo) pla                           
----------------------------------------
000083     jmp print_byte
  --------                              
. (mnemo) jmp                           
. (variable) print_byte                 print_byte       ------

----------------------------------------
000085 start
. (variable) start                      start            ------

----------------------------------------
000087     value = $1234
  --------                              
. (variable) value                      value            ------

. (keyword) =                           
. (variable) $1234                      $1234            0x1234

----------------------------------------
000088     ldx #<value
  --------                              
. (mnemo) ldx                           
. (keyword) #                           
. (keyword) <                           
. (variable) value                      value            ------

----------------------------------------
000089     lda #>value
  --------                              
. (mnemo) lda                           
. (keyword) #                           
. (keyword) >                           
. (variable) value                      value            ------

----------------------------------------
000090     jsr print_word
  --------                              
. (mnemo) jsr                           
. (variable) print_word                 print_word       ------

----------------------------------------
000091 loop
. (variable) loop                       loop             ------

----------------------------------------
000092     jmp loop
  --------                              
. (mnemo) jmp                           
. (variable) loop                       loop             ------

----------------------------------------
000096     ldx #<splash1
  --------                              
. (mnemo) ldx                           
. (keyword) #                           
. (keyword) <                           
. (variable) splash1                    splash1          ------

----------------------------------------
000097     ldy #>splash1
  --------                              
. (mnemo) ldy                           
. (keyword) #                           
. (keyword) >                           
. (variable) splash1                    splash1          ------

----------------------------------------
000098     jsr print
  --------                              
. (mnemo) jsr                           
. (variable) print                      print            ------

----------------------------------------
000101     ldx #<splash2 + 3
  --------                              
. (mnemo) ldx                           
. (keyword) #                           
. (keyword) <                           
. (variable) splash2                    splash2          ------

. (keyword) +                           
. (variable) 3                          3                0x0003

----------------------------------------
000102     ldy #>splash2
  --------                              
. (mnemo) ldy                           
. (keyword) #                           
. (keyword) >                           
. (variable) splash2                    splash2          ------

----------------------------------------
000103     jsr print
  --------                              
. (mnemo) jsr                           
. (variable) print                      print            ------

----------------------------------------
000106     ldx #<main
  --------                              
. (mnemo) ldx                           
. (keyword) #                           
. (keyword) <                           
. (variable) main                       main             ------

----------------------------------------
000107     ldy #>main
  --------                              
. (mnemo) ldy                           
. (keyword) #                           
. (keyword) >                           
. (variable) main                       main             ------

----------------------------------------
000108     jsr print
  --------                              
. (mnemo) jsr                           
. (variable) print                      print            ------

----------------------------------------
000111     ldx #<start_mes
  --------                              
. (mnemo) ldx                           
. (keyword) #                           
. (keyword) <                           
. (variable) start_mes                  start_mes        ------

----------------------------------------
000112     lda #>start_mes
  --------                              
. (mnemo) lda                           
. (keyword) #                           
. (keyword) >                           
. (variable) start_mes                  start_mes        ------

----------------------------------------
000113     jsr print_word
  --------                              
. (mnemo) jsr                           
. (variable) print_word                 print_word       ------

----------------------------------------
000116     ldx #<stop
  --------                              
. (mnemo) ldx                           
. (keyword) #                           
. (keyword) <                           
. (variable) stop                       stop             ------

----------------------------------------
000117     ldy #>stop
  --------                              
. (mnemo) ldy                           
. (keyword) #                           
. (keyword) >                           
. (variable) stop                       stop             ------

----------------------------------------
000118     jsr print
  --------                              
. (mnemo) jsr                           
. (variable) print                      print            ------

----------------------------------------
000121     ldx #<stop_mes;blablabla
  --------                              
. (mnemo) ldx                           
. (keyword) #                           
. (keyword) <                           
. (variable) stop_mes                   stop_mes         ------

----------------------------------------
000122     lda #>stop_mes; blablabla
  --------                              
. (mnemo) lda                           
. (keyword) #                           
. (keyword) >                           
. (variable) stop_mes                   stop_mes         ------

----------------------------------------
000123     jsr print_word ;blablabla
  --------                              
. (mnemo) jsr                           
. (variable) print_word                 print_word       ------

----------------------------------------
000125 stop
. (variable) stop                       stop             ------

----------------------------------------
000126     brk
  --------                              
X (mnemo) brk                           
----------------------------------------
000128 irq
. (variable) irq                        irq              ------

----------------------------------------
000130     ldx #<irq_mes
  --------                              
. (mnemo) ldx                           
. (keyword) #                           
. (keyword) <                           
. (variable) irq_mes                    irq_mes          ------

----------------------------------------
000131     ldy #>irq_mes
  --------                              
. (mnemo) ldy                           
. (keyword) #                           
. (keyword) >                           
. (variable) irq_mes                    irq_mes          ------

----------------------------------------
000132     jsr print
  --------                              
. (mnemo) jsr                           
. (variable) print                      print            ------

----------------------------------------
000133 irq_loop
. (variable) irq_loop                   irq_loop         ------

----------------------------------------
000134     jmp irq_loop
  --------                              
. (mnemo) jmp                           
. (variable) irq_loop                   irq_loop         ------

----------------------------------------
000136 nmi
. (variable) nmi                        nmi              ------

----------------------------------------
000138     ldx #<nmi_mes
  --------                              
. (mnemo) ldx                           
. (keyword) #                           
. (keyword) <                           
. (variable) nmi_mes                    nmi_mes          ------

----------------------------------------
000139     ldy #>nmi_mes;blablabla...
  --------                              
. (mnemo) ldy                           
. (keyword) #                           
. (keyword) >                           
. (variable) nmi_mes                    nmi_mes          ------

----------------------------------------
000140     jsr       print
  --------                              
. (mnemo) jsr                           
. (variable) print                      print            ------

----------------------------------------
000141 nmi_loop
. (variable) nmi_loop                   nmi_loop         ------

----------------------------------------
000142     jmp nmi_loop
  --------                              
. (mnemo) jmp                           
. (variable) nmi_loop                   nmi_loop         ------

----------------------------------------
000144 start_mes .string "free rom "
. (variable) start_mes                  start_mes        ------

. (keyword) .string                     
. (variable) "free rom "                "free rom "      ------

----------------------------------------
000146 stop_mes .string " bytes\n"
. (variable) stop_mes                   stop_mes         ------

. (keyword) .string                     
. (variable) " bytes\n"                 " bytes\n"       ------

----------------------------------------
000148 nmi_mes .string " NMI occured\n"
. (variable) nmi_mes                    nmi_mes          ------

. (keyword) .string                     
. (variable) " NMI occured\n"           " NMI occured\n" ------

----------------------------------------
000150 irq_mes .string " IRQ occured\n"
. (variable) irq_mes                    irq_mes          ------

. (keyword) .string                     
. (variable) " IRQ occured\n"           " IRQ occured\n" ------

----------------------------------------
000152 hextab .ch_array "0123456789ABCDEF"
. (variable) hextab                     hextab           ------

. (keyword) .ch_array                   
. (variable) "0123456789ABCDEF"         "0123456789ABCDEF" ------

----------------------------------------
000154 source_end
. (variable) source_end                 source_end       ------

----------------------------------------
