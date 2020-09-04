
    ;---------------------------------;
    ; a 4ko ROM monitor for vosc6502  ;
    ;---------------------------------;

;    .include monitor_equates.asm

    ; special characters
    CHAR_RETURN = $0a

    ;hardware registers
    PUTSCR_REG = $bf00

    op1 = 0
    op2 = 2
    op3 = 4
    zp  = 6
;   End of inclusion of file monitor_equates.asm

    * = $f000

source_start

hooks
    .word print
    .word print_nibble
    .word print_byte
    .word print_word

main
    jmp start
;    .include monitor_sub.asm


println
    jsr print
    lda #CHAR_RETURN
    sta PUTSCR_REG
    rts

print
    ; op1 = 0
    stx op1
    sty op1+1
    ldy #0

print_l1
    lda (op1),y
    cmp #0
    beq print_out
    sta PUTSCR_REG
    iny
    bne print_l1

print_out
    rts

print_nibble
    pha
    and #$0f
    tax
    lda hextab, x
    sta PUTSCR_REG
    rts

print_byte
    pha
    lsr a
    lsr a
    lsr a
    lsr a
    jsr print_nibble
    pla
    jmp print_nibble

print_word
    pha
    tax
    jsr print_byte
    pla
    jmp print_byte

;   End of inclusion of file monitor_sub.asm

start

    value = $1234
    ldx #<value
    lda #>value
    jsr print_word
loop
    jmp loop


    ; print "vosc6502...
    ldx #<splash1
    ldy #>splash1
    jsr print

    ; print "version ...
    ldx #<splash2
    ldy #>splash2
    jsr print

    ; print "start point is
    ldx #<main
    ldy #>main
    jsr print

    ; print "start point value
    ldx #<start_mes
    lda #>start_mes
    jsr print_word

    ; print "stop point is
    ldx #<stop
    ldy #>stop
    jsr print

    ; print "start point value
    ldx #<stop_mes
    lda #>stop_mes
    jsr print_word

stop
    brk

irq
    ; print "IRQ...
    ldx #<irq_mes
    ldy #>irq_mes
    jsr print
irq_loop
    jmp irq_loop

nmi
    ; print "MNI...
    ldx #<nmi_mes
    ldy #>nmi_mes
    jsr print
nmi_loop
    jmp nmi_loop

splash1 ; .string "\"VOSC6502\" (Virtual Old School Computer with a 6502 processor)\n"
    .byte $22, $56, $4f, $53, $43, $36, $35
    .byte $30, $32, $22, $20, $28, $56, $69
    .byte $72, $74, $75, $61, $6c, $20, $4f
    .byte $6c, $64, $20, $53, $63, $68, $6f
    .byte $6f, $6c, $20, $43, $6f, $6d, $70
    .byte $75, $74, $65, $72, $20, $77, $69
    .byte $74, $68, $20, $61, $20, $36, $35
    .byte $30, $32, $20, $70, $72, $6f, $63
    .byte $65, $73, $73, $6f, $72, $29, $0a
    .byte $00

splash2 ; .string "version 0.99 -------------------------- MMXX - Pierre Faller\n"
    .byte $76, $65, $72, $73, $69, $6f, $6e
    .byte $20, $30, $2e, $39, $39, $20, $2d
    .byte $2d, $2d, $2d, $2d, $2d, $2d, $2d
    .byte $2d, $2d, $2d, $2d, $2d, $2d, $2d
    .byte $2d, $2d, $2d, $2d, $2d, $2d, $2d
    .byte $2d, $2d, $2d, $2d, $20, $4d, $4d
    .byte $58, $58, $20, $2d, $20, $50, $69
    .byte $65, $72, $72, $65, $20, $46, $61
    .byte $6c, $6c, $65, $72, $0a, $00

start_mes ; .string "free rom "
    .byte $66, $72, $65, $65, $20, $72, $6f
    .byte $6d, $20, $00

stop_mes ; .string " bytes\n"
    .byte $20, $62, $79, $74, $65, $73, $0a
    .byte $00

nmi_mes ; .string " NMI occured\n"
    .byte $20, $4e, $4d, $49, $20, $6f, $63
    .byte $63, $75, $72, $65, $64, $0a, $00

irq_mes ; .string " IRQ occured\n"
    .byte $20, $49, $52, $51, $20, $6f, $63
    .byte $63, $75, $72, $65, $64, $0a, $00

hextab ; .ch_array "0123456789ABCDEF"
    .byte $30, $31, $32, $33, $34, $35, $36
    .byte $37, $38, $39, $41, $42, $43, $44
    .byte $45, $46

source_end
