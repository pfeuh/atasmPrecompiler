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
monitor.asm#9                            source_start
monitor.asm#10                           hooks
monitor.asm#11                               .word print
monitor.asm#12                               .word println
monitor.asm#13                               .word print_nibble
monitor.asm#14                               .word print_byte
monitor.asm#15                               .word print_word
monitor.asm#16                           
monitor.asm#17                           main
monitor.asm#18                               jmp start
monitor.asm#19                           ;    .include monitor_stuff.asm
monitor_stuff.asm#1                      
monitor_stuff.asm#2                      
monitor_stuff.asm#3                      
monitor_stuff.asm#4                       ; TODO: perhaps some macros later
monitor_stuff.asm#5                      
monitor_stuff.asm#6                      
<precompiler>#2                          ;   End of inclusion of file monitor_stuff.asm
monitor.asm#20                           
monitor.asm#21                           start
monitor.asm#22                               ; print "vosc6502...
monitor.asm#23                               ldx #<splash1
monitor.asm#24                               ldy #>splash1
monitor.asm#25                               jsr println
monitor.asm#26                           
monitor.asm#27                               ; print "version ...
monitor.asm#28                               ldx #<splash2
monitor.asm#29                               ldy #>splash2
monitor.asm#30                               jsr println
monitor.asm#31                           
monitor.asm#32                               ; print "start point is
monitor.asm#33                               ldx #<main
monitor.asm#34                               ldy #>main
monitor.asm#35                               jsr print
monitor.asm#36                           
monitor.asm#37                               ; print "start point value
monitor.asm#38                               ldx #<start_mes
monitor.asm#39                               lda #>start_mes
monitor.asm#40                               jsr print_word
monitor.asm#41                           
monitor.asm#42                               ; print "stop point is
monitor.asm#43                               ldx #<stop
monitor.asm#44                               ldy #>stop
monitor.asm#45                               jsr print
monitor.asm#46                           
monitor.asm#47                               ; print "start point value
monitor.asm#48                               ldx #<stop_mes
monitor.asm#49                               lda #>stop_mes
monitor.asm#50                               jsr print_word
monitor.asm#51                           
monitor.asm#52                           stop
monitor.asm#53                               brk
monitor.asm#54                           
monitor.asm#55                           println
monitor.asm#56                               jsr print
monitor.asm#57                               lda #CHAR_RETURN
monitor.asm#58                               sta PUTSCR_REG
monitor.asm#59                               rts
monitor.asm#60                           
monitor.asm#61                           print
monitor.asm#62                               op1 = 0
monitor.asm#63                               stx op1
monitor.asm#64                               sty op1+1
monitor.asm#65                               ldy #0
monitor.asm#66                           
monitor.asm#67                           print_l1
monitor.asm#68                               lda (op1),y
monitor.asm#69                               cmp #0
monitor.asm#70                               beq print_out
monitor.asm#71                               sta PUTSCR_REG
monitor.asm#72                               iny
monitor.asm#73                               bne print_l1
monitor.asm#74                           
monitor.asm#75                           print_out
monitor.asm#76                               rts
monitor.asm#77                           
monitor.asm#78                           print_nibble
monitor.asm#79                               and #$0f
monitor.asm#80                               tax
monitor.asm#81                               lda hextab, x
monitor.asm#82                               sta PUTSCR_REG
monitor.asm#83                               rts
monitor.asm#84                           
monitor.asm#85                           print_byte
monitor.asm#86                               pha
monitor.asm#87                               lsr
monitor.asm#88                               lsr
monitor.asm#89                               lsr
monitor.asm#90                               lsr
monitor.asm#91                               jsr print_nibble
monitor.asm#92                               pla
monitor.asm#93                               jmp print_nibble
monitor.asm#94                           
monitor.asm#95                           print_word
monitor.asm#96                               pha
monitor.asm#97                               tax
monitor.asm#98                               jsr print_byte
monitor.asm#99                               pla
monitor.asm#100                              jmp print_byte
monitor.asm#101                          
monitor.asm#102                          irq
monitor.asm#103                              pla
monitor.asm#104                              pla
monitor.asm#105                              pla
monitor.asm#106                              brk
monitor.asm#107                          
monitor.asm#108                          nmi
monitor.asm#109                              pla
monitor.asm#110                              pla
monitor.asm#111                              pla
monitor.asm#112                              brk
monitor.asm#113                          
monitor.asm#114                          splash1 ; .string "\"VOSC6502\" (Virtual Old School Computer with a 6502 processor)\n"
<precompiler>#3                              .byte $22, $56, $4f, $53, $43, $36, $35
<precompiler>#4                              .byte $30, $32, $22, $20, $28, $56, $69
<precompiler>#5                              .byte $72, $74, $75, $61, $6c, $20, $4f
<precompiler>#6                              .byte $6c, $64, $20, $53, $63, $68, $6f
<precompiler>#7                              .byte $6f, $6c, $20, $43, $6f, $6d, $70
<precompiler>#8                              .byte $75, $74, $65, $72, $20, $77, $69
<precompiler>#9                              .byte $74, $68, $20, $61, $20, $36, $35
<precompiler>#10                             .byte $30, $32, $20, $70, $72, $6f, $63
<precompiler>#11                             .byte $65, $73, $73, $6f, $72, $29, $0a
<precompiler>#12                             .byte $00
monitor.asm#115                          
monitor.asm#116                          splash2 ; .string "version 0.99 -------------------------- MMXX - Pierre Faller\n"
<precompiler>#13                             .byte $76, $65, $72, $73, $69, $6f, $6e
<precompiler>#14                             .byte $20, $30, $2e, $39, $39, $20, $2d
<precompiler>#15                             .byte $2d, $2d, $2d, $2d, $2d, $2d, $2d
<precompiler>#16                             .byte $2d, $2d, $2d, $2d, $2d, $2d, $2d
<precompiler>#17                             .byte $2d, $2d, $2d, $2d, $2d, $2d, $2d
<precompiler>#18                             .byte $2d, $2d, $2d, $2d, $20, $4d, $4d
<precompiler>#19                             .byte $58, $58, $20, $2d, $20, $50, $69
<precompiler>#20                             .byte $65, $72, $72, $65, $20, $46, $61
<precompiler>#21                             .byte $6c, $6c, $65, $72, $0a, $00
monitor.asm#117                          
monitor.asm#118                          start_mes ; .string "start point is "
<precompiler>#22                             .byte $73, $74, $61, $72, $74, $20, $70
<precompiler>#23                             .byte $6f, $69, $6e, $74, $20, $69, $73
<precompiler>#24                             .byte $20, $00
monitor.asm#119                          
monitor.asm#120                          stop_mes ; .string "stop point is "
<precompiler>#25                             .byte $73, $74, $6f, $70, $20, $70, $6f
<precompiler>#26                             .byte $69, $6e, $74, $20, $69, $73, $20
<precompiler>#27                             .byte $00
monitor.asm#121                          
monitor.asm#122                          hextab ; .ch_array "0123456789ABCDEF"
<precompiler>#28                             .byte $30, $31, $32, $33, $34, $35, $36
<precompiler>#29                             .byte $37, $38, $39, $41, $42, $43, $44
<precompiler>#30                             .byte $45, $46
monitor.asm#123                          
monitor.asm#124                          source_end
