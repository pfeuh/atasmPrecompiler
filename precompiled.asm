
    ;---------------------------------;
    ; a 4ko ROM monitor for vosc6502  ;
    ;---------------------------------;

;    .include monitor_equates.asm

    ; special characters
    CHAR_RETURN = $0a

    ;hardware registers
    PUTSCR_REG = $bf00

;   End of inclusion of file monitor_equates.asm

    * = $f000
source_start
hooks
    .word print
    .word println
    .word print_nibble
    .word print_byte
    .word print_word

main
    jmp start
;    .include monitor_stuff.asm



 ; TODO: perhaps some macros later


;   End of inclusion of file monitor_stuff.asm

start
    ; print "vosc6502...
    ldx #<splash1
    ldy #>splash1
    jsr println

    ; print "version ...
    ldx #<splash2
    ldy #>splash2
    jsr println

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

println
    jsr print
    lda #CHAR_RETURN
    sta PUTSCR_REG
    rts

print
    op1 = 0
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
    and #$0f
    tax
    lda hextab, x
    sta PUTSCR_REG
    rts

print_byte
    pha
    lsr
    lsr
    lsr
    lsr
    jsr print_nibble
    pla
    jmp print_nibble

print_word
    pha
    tax
    jsr print_byte
    pla
    jmp print_byte

irq
    pla
    pla
    pla
    brk

nmi
    pla
    pla
    pla
    brk

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

start_mes ; .string "start point is "
    .byte $73, $74, $61, $72, $74, $20, $70
    .byte $6f, $69, $6e, $74, $20, $69, $73
    .byte $20, $00

stop_mes ; .string "stop point is "
    .byte $73, $74, $6f, $70, $20, $70, $6f
    .byte $69, $6e, $74, $20, $69, $73, $20
    .byte $00

hextab ; .ch_array "0123456789ABCDEF"
    .byte $30, $31, $32, $33, $34, $35, $36
    .byte $37, $38, $39, $41, $42, $43, $44
    .byte $45, $46

source_end
