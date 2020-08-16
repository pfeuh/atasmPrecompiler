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
monitor_equates.asm#8                        zp = 0
monitor_equates.asm#9                    
monitor_equates.asm#10                       zp = zp + 2
monitor_equates.asm#11                       op1 = zp
monitor_equates.asm#12                   
monitor_equates.asm#13                       zp = zp + 2
monitor_equates.asm#14                       op2 = zp
monitor_equates.asm#15                   
monitor_equates.asm#16                       zp = zp + 2
monitor_equates.asm#17                       op3 = zp
<precompiler>#1                          ;   End of inclusion of file monitor_equates.asm
monitor.asm#7                            
monitor.asm#8                                * = $f000
monitor.asm#9                            
monitor.asm#10                           source_start
monitor.asm#11                           
monitor.asm#12                           hooks
monitor.asm#13                               .word print
monitor.asm#14                               .word print_nibble
monitor.asm#15                               .word print_byte
monitor.asm#16                               .word print_word
monitor.asm#17                           
monitor.asm#18                           main
monitor.asm#19                               jmp start
monitor.asm#20                           ;    .include monitor_sub.asm
monitor_sub.asm#1                        
monitor_sub.asm#3                        
monitor_sub.asm#4                        println
monitor_sub.asm#5                            jsr print
monitor_sub.asm#6                            lda #CHAR_RETURN
monitor_sub.asm#7                            sta PUTSCR_REG
monitor_sub.asm#8                            rts
monitor_sub.asm#9                        
monitor_sub.asm#10                       print
monitor_sub.asm#11                           ; op1 = 0
monitor_sub.asm#12                           stx op1
monitor_sub.asm#13                           sty op1+1
monitor_sub.asm#14                           ldy #0
monitor_sub.asm#15                       
monitor_sub.asm#16                       print_l1
monitor_sub.asm#17                           lda (op1),y
monitor_sub.asm#18                           cmp #0
monitor_sub.asm#19                           beq print_out
monitor_sub.asm#20                           sta PUTSCR_REG
monitor_sub.asm#21                           iny
monitor_sub.asm#22                           bne print_l1
monitor_sub.asm#23                       
monitor_sub.asm#24                       print_out
monitor_sub.asm#25                           rts
monitor_sub.asm#26                       
monitor_sub.asm#27                       print_nibble
monitor_sub.asm#28                           phx
monitor_sub.asm#29                           and #$0f
monitor_sub.asm#30                           tax
monitor_sub.asm#31                           lda hextab, x
monitor_sub.asm#32                           sta PUTSCR_REG
monitor_sub.asm#33                           rts
monitor_sub.asm#34                       
monitor_sub.asm#35                       print_byte
monitor_sub.asm#36                           pha
monitor_sub.asm#37                           lsr
monitor_sub.asm#38                           lsr
monitor_sub.asm#39                           lsr
monitor_sub.asm#40                           lsr
monitor_sub.asm#41                           jsr print_nibble
monitor_sub.asm#42                           pla
monitor_sub.asm#43                           jmp print_nibble
monitor_sub.asm#44                       
monitor_sub.asm#45                       print_word
monitor_sub.asm#46                           pha
monitor_sub.asm#47                           tax
monitor_sub.asm#48                           jsr print_byte
monitor_sub.asm#49                           pla
monitor_sub.asm#50                           jmp print_byte
monitor_sub.asm#51                       
<precompiler>#2                          ;   End of inclusion of file monitor_sub.asm
monitor.asm#21                           
monitor.asm#22                           start
monitor.asm#23                           
monitor.asm#24                               value = $1234
monitor.asm#25                               ldx #<value
monitor.asm#26                               lda #>value
monitor.asm#27                               jsr print_word
monitor.asm#28                           loop
monitor.asm#29                               jmp loop
monitor.asm#30                           
monitor.asm#31                           
monitor.asm#32                               ; print "vosc6502...
monitor.asm#33                               ldx #<splash1
monitor.asm#34                               ldy #>splash1
monitor.asm#35                               jsr print
monitor.asm#36                           
monitor.asm#37                               ; print "version ...
monitor.asm#38                               ldx #<splash2
monitor.asm#39                               ldy #>splash2
monitor.asm#40                               jsr print
monitor.asm#41                           
monitor.asm#42                               ; print "start point is
monitor.asm#43                               ldx #<main
monitor.asm#44                               ldy #>main
monitor.asm#45                               jsr print
monitor.asm#46                           
monitor.asm#47                               ; print "start point value
monitor.asm#48                               ldx #<start_mes
monitor.asm#49                               lda #>start_mes
monitor.asm#50                               jsr print_word
monitor.asm#51                           
monitor.asm#52                               ; print "stop point is
monitor.asm#53                               ldx #<stop
monitor.asm#54                               ldy #>stop
monitor.asm#55                               jsr print
monitor.asm#56                           
monitor.asm#57                               ; print "start point value
monitor.asm#58                               ldx #<stop_mes
monitor.asm#59                               lda #>stop_mes
monitor.asm#60                               jsr print_word
monitor.asm#61                           
monitor.asm#62                           stop
monitor.asm#63                               brk
monitor.asm#64                           
monitor.asm#65                           irq
monitor.asm#66                               ; print "IRQ...
monitor.asm#67                               ldx #<irq_mes
monitor.asm#68                               ldy #>irq_mes
monitor.asm#69                               jsr print
monitor.asm#70                           irq_loop
monitor.asm#71                               jmp irq_loop
monitor.asm#72                           
monitor.asm#73                           nmi
monitor.asm#74                               ; print "MNI...
monitor.asm#75                               ldx #<nmi_mes
monitor.asm#76                               ldy #>nmi_mes
monitor.asm#77                               jsr print
monitor.asm#78                           nmi_loop
monitor.asm#79                               jmp nmi_loop
monitor.asm#80                           
monitor.asm#81                           splash1 ; .string "\"VOSC6502\" (Virtual Old School Computer with a 6502 processor)\n"
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
monitor.asm#82                           
monitor.asm#83                           splash2 ; .string "version 0.99 -------------------------- MMXX - Pierre Faller\n"
<precompiler>#13                             .byte $76, $65, $72, $73, $69, $6f, $6e
<precompiler>#14                             .byte $20, $30, $2e, $39, $39, $20, $2d
<precompiler>#15                             .byte $2d, $2d, $2d, $2d, $2d, $2d, $2d
<precompiler>#16                             .byte $2d, $2d, $2d, $2d, $2d, $2d, $2d
<precompiler>#17                             .byte $2d, $2d, $2d, $2d, $2d, $2d, $2d
<precompiler>#18                             .byte $2d, $2d, $2d, $2d, $20, $4d, $4d
<precompiler>#19                             .byte $58, $58, $20, $2d, $20, $50, $69
<precompiler>#20                             .byte $65, $72, $72, $65, $20, $46, $61
<precompiler>#21                             .byte $6c, $6c, $65, $72, $0a, $00
monitor.asm#84                           
monitor.asm#85                           start_mes ; .string "free rom "
<precompiler>#22                             .byte $66, $72, $65, $65, $20, $72, $6f
<precompiler>#23                             .byte $6d, $20, $00
monitor.asm#86                           
monitor.asm#87                           stop_mes ; .string " bytes\n"
<precompiler>#24                             .byte $20, $62, $79, $74, $65, $73, $0a
<precompiler>#25                             .byte $00
monitor.asm#88                           
monitor.asm#89                           nmi_mes ; .string " NMI occured\n"
<precompiler>#26                             .byte $20, $4e, $4d, $49, $20, $6f, $63
<precompiler>#27                             .byte $63, $75, $72, $65, $64, $0a, $00
monitor.asm#90                           
monitor.asm#91                           irq_mes ; .string " IRQ occured\n"
<precompiler>#28                             .byte $20, $49, $52, $51, $20, $6f, $63
<precompiler>#29                             .byte $63, $75, $72, $65, $64, $0a, $00
monitor.asm#92                           
monitor.asm#93                           hextab ; .ch_array "0123456789ABCDEF"
<precompiler>#30                             .byte $30, $31, $32, $33, $34, $35, $36
<precompiler>#31                             .byte $37, $38, $39, $41, $42, $43, $44
<precompiler>#32                             .byte $45, $46
monitor.asm#94                           
monitor.asm#95                           source_end
