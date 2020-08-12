monitor.asm#1                            
monitor.asm#2                                ;---------------------------------;
monitor.asm#3                                ; a 4ko ROM monitor for vosc6502  ;
monitor.asm#4                                ;---------------------------------;
monitor.asm#5                            
monitor.asm#6                            ;    .include monitor_equates.asm
monitor_equates.asm#1                    
monitor_equates.asm#2                        ; special characters
monitor_equates.asm#3                        CHAR_RETURN = $0a
monitor_equates.asm#4                    
monitor_equates.asm#5                        ;hardware registers
monitor_equates.asm#6                        PUTSCR_REG = $bf00
monitor_equates.asm#7                    
<precompiler>#1                          ;   End of inclusion of file monitor_equates.asm
monitor.asm#7                            
monitor.asm#8                                * = $f000
monitor.asm#9                            
monitor.asm#10                           main
monitor.asm#11                               jmp start
monitor.asm#12                           ;    .include monitor_stuff.asm
monitor_stuff.asm#1                      
monitor_stuff.asm#2                      
monitor_stuff.asm#4                      
monitor_stuff.asm#5                      test1 ; .string "petite\n"
<precompiler>#2                              .byte $70, $65, $74, $69, $74, $65, $0a, $00
monitor_stuff.asm#6                      test2 ; .string "moyenne\n"
<precompiler>#3                              .byte $6d, $6f, $79, $65, $6e, $6e, $65, $0a, $00
monitor_stuff.asm#7                      test3 ; .string "un peu plus\n"
<precompiler>#4                              .byte $75, $6e, $20, $70, $65, $75, $20, $70, $6c, $75, $73, $0a, $00
monitor_stuff.asm#8                      test4 ; .string "un peu plus grande\n"
<precompiler>#5                              .byte $75, $6e, $20, $70, $65, $75, $20, $70, $6c, $75, $73, $20, $67
<precompiler>#6                              .byte $72, $61, $6e, $64, $65, $0a, $00
monitor_stuff.asm#9                      test5 ; .string "\x00\x01\x02\x03\x04\x05\x06\x07\x08\x09\x0a\x0b\x0c\x0d\x0e\x0f"
<precompiler>#7                              .byte $00, $01, $02, $03, $04, $05, $06, $07, $08, $09, $0a, $0b, $0c
<precompiler>#8                              .byte $0d, $0e, $0f, $00
monitor_stuff.asm#10                     
<precompiler>#9                          ;   End of inclusion of file monitor_stuff.asm
monitor.asm#13                           
monitor.asm#14                           start
monitor.asm#15                               ; print "vosc6502...
monitor.asm#16                               ldx #<splash1
monitor.asm#17                               ldy #>splash1
monitor.asm#18                               jsr println
monitor.asm#19                           dummylabel1
monitor.asm#20                               ; print "version ...
monitor.asm#21                               ldx #<splash2
monitor.asm#22                               ldy #>splash2
monitor.asm#23                               jsr println
monitor.asm#24                           dummylabel2
monitor.asm#25                               ; print "start point is
monitor.asm#26                               ldx #<main
monitor.asm#27                               ldy #>main
monitor.asm#28                               jsr print
monitor.asm#29                           
monitor.asm#30                               ; print "start point value
monitor.asm#31                               ldx #<start_mes
monitor.asm#32                               lda #>start_mes
monitor.asm#33                               jsr print_word
monitor.asm#34                           
monitor.asm#35                               ; print "stop point is
monitor.asm#36                               ldx #<stop
monitor.asm#37                               ldy #>stop
monitor.asm#38                               jsr print
monitor.asm#39                           
monitor.asm#40                               ; print "start point value
monitor.asm#41                               ldx #<stop_mes
monitor.asm#42                               lda #>stop_mes
monitor.asm#43                               jsr print_word
monitor.asm#44                           
monitor.asm#45                           stop
monitor.asm#46                               brk
monitor.asm#47                           
monitor.asm#48                           println
monitor.asm#49                               jsr print
monitor.asm#50                               lda #CHAR_RETURN
monitor.asm#51                               sta PUTSCR_REG
monitor.asm#52                               rts
monitor.asm#53                           
monitor.asm#54                           print
monitor.asm#55                               op1 = 0
monitor.asm#56                               stx op1
monitor.asm#57                               sty op1+1
monitor.asm#58                               ldy #0
monitor.asm#59                           
monitor.asm#60                           print_l1
monitor.asm#61                               lda (op1),y
monitor.asm#62                               cmp #0
monitor.asm#63                               beq print_out
monitor.asm#64                               sta PUTSCR_REG
monitor.asm#65                               iny
monitor.asm#66                               bne print_l1
monitor.asm#67                           
monitor.asm#68                           print_out
monitor.asm#69                               rts
monitor.asm#70                           
monitor.asm#71                           print_nibble
monitor.asm#72                               and #$0f
monitor.asm#73                               tax
monitor.asm#74                               lda hextab, x
monitor.asm#75                               sta PUTSCR_REG
monitor.asm#76                               rts
monitor.asm#77                           
monitor.asm#78                           print_byte
monitor.asm#79                               pha
monitor.asm#80                               lsr
monitor.asm#81                               lsr
monitor.asm#82                               lsr
monitor.asm#83                               lsr
monitor.asm#84                               jsr print_nibble
monitor.asm#85                               pla
monitor.asm#86                               jmp print_nibble
monitor.asm#87                           
monitor.asm#88                           print_word
monitor.asm#89                               pha
monitor.asm#90                               tax
monitor.asm#91                               jsr print_byte
monitor.asm#92                               pla
monitor.asm#93                               jmp print_byte
monitor.asm#94                           
monitor.asm#95                           irqz
monitor.asm#96                               pla
monitor.asm#97                               pla
monitor.asm#98                               pla
monitor.asm#99                               brk
monitor.asm#100                          
monitor.asm#101                          nmi
monitor.asm#102                              pla
monitor.asm#103                              pla
monitor.asm#104                              pla
monitor.asm#105                              brk
monitor.asm#106                          
monitor.asm#107                          source_end
monitor.asm#108                          
monitor.asm#109                          splash1 ; .string              "\"VOSC6502\" (Virtual Old School Computer with a 6502 processor)\n"
<precompiler>#10                             .byte $22, $56, $4f, $53, $43, $36, $35, $30, $32, $22, $20, $28, $56
<precompiler>#11                             .byte $69, $72, $74, $75, $61, $6c, $20, $4f, $6c, $64, $20, $53, $63
<precompiler>#12                             .byte $68, $6f, $6f, $6c, $20, $43, $6f, $6d, $70, $75, $74, $65, $72
<precompiler>#13                             .byte $20, $77, $69, $74, $68, $20, $61, $20, $36, $35, $30, $32, $20
<precompiler>#14                             .byte $70, $72, $6f, $63, $65, $73, $73, $6f, $72, $29, $0a, $00
monitor.asm#110                          
monitor.asm#111                          splash2
monitor.asm#112                          ;    .string            "version 0.99 -------------------------- MMXX - Pierre Faller\n"
<precompiler>#15                             .byte $76, $65, $72, $73, $69, $6f, $6e, $20, $30, $2e, $39, $39, $20
<precompiler>#16                             .byte $2d, $2d, $2d, $2d, $2d, $2d, $2d, $2d, $2d, $2d, $2d, $2d, $2d
<precompiler>#17                             .byte $2d, $2d, $2d, $2d, $2d, $2d, $2d, $2d, $2d, $2d, $2d, $2d, $2d
<precompiler>#18                             .byte $20, $4d, $4d, $58, $58, $20, $2d, $20, $50, $69, $65, $72, $72
<precompiler>#19                             .byte $65, $20, $46, $61, $6c, $6c, $65, $72, $0a, $00
monitor.asm#113                          
monitor.asm#114                          start_mes
monitor.asm#115                          ;    .string "start point is "
<precompiler>#20                             .byte $73, $74, $61, $72, $74, $20, $70, $6f, $69, $6e, $74, $20, $69
<precompiler>#21                             .byte $73, $20, $00
monitor.asm#116                          
monitor.asm#117                          stop_mes
monitor.asm#118                          ;    .string "stop point is "
<precompiler>#22                             .byte $73, $74, $6f, $70, $20, $70, $6f, $69, $6e, $74, $20, $69, $73
<precompiler>#23                             .byte $20, $00
monitor.asm#119                          ;    .string "searching the small beast..." " and don't find it" + chr(255)
<precompiler>#24                             .byte $73, $65, $61, $72, $63, $68, $69, $6e, $67, $20, $74, $68, $65
<precompiler>#25                             .byte $20, $73, $6d, $61, $6c, $6c, $20, $62, $65, $61, $73, $74, $2e
<precompiler>#26                             .byte $2e, $2e, $20, $61, $6e, $64, $20, $64, $6f, $6e, $27, $74, $20
<precompiler>#27                             .byte $66, $69, $6e, $64, $20, $69, $74, $ff, $00
monitor.asm#120                          
monitor.asm#121                          hextab ; .ch_array "0123456789ABCDEF"
<precompiler>#28                             .byte $30, $31, $32, $33, $34, $35, $36, $37, $38, $39, $41, $42, $43
<precompiler>#29                             .byte $44, $45, $46
monitor.asm#122                          
monitor.asm#123                          test6 ; .ch_array "\x00\x01\x02\x03\x04\x05\x06\x07\x08\x09\x0a\x0b\x0c\x0d\x0e\x0f"
<precompiler>#30                             .byte $00, $01, $02, $03, $04, $05, $06, $07, $08, $09, $0a, $0b, $0c
<precompiler>#31                             .byte $0d, $0e, $0f
monitor.asm#124                          
monitor.asm#125                              ; * = $fffa ; nmi vector
monitor.asm#126                              ; .word nmi
monitor.asm#127                          
monitor.asm#128                              ; * = $fffc ; run vector
monitor.asm#129                              ; .word main
monitor.asm#130                          
monitor.asm#131                              ; * = $fffe ; irq vector
monitor.asm#132                              ; .word irq
