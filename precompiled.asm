
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

main
    jmp start
;    .include monitor_stuff.asm



test1 ; .string "petite\n"
    .byte $70, $65, $74, $69, $74, $65, $0a, $00
test2 ; .string "moyenne\n"
    .byte $6d, $6f, $79, $65, $6e, $6e, $65, $0a, $00
test3 ; .string "un peu plus\n"
    .byte $75, $6e, $20, $70, $65, $75, $20, $70, $6c, $75, $73, $0a, $00
test4 ; .string "un peu plus grande\n"
    .byte $75, $6e, $20, $70, $65, $75, $20, $70, $6c, $75, $73, $20, $67
    .byte $72, $61, $6e, $64, $65, $0a, $00
test5 ; .string "\x00\x01\x02\x03\x04\x05\x06\x07\x08\x09\x0a\x0b\x0c\x0d\x0e\x0f"
    .byte $00, $01, $02, $03, $04, $05, $06, $07, $08, $09, $0a, $0b, $0c
    .byte $0d, $0e, $0f, $00

;   End of inclusion of file monitor_stuff.asm

start
    ; print "vosc6502...
    ldx #<splash1
    ldy #>splash1
    jsr println
dummylabel1
    ; print "version ...
    ldx #<splash2
    ldy #>splash2
    jsr println
dummylabel2
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

irqz
    pla
    pla
    pla
    brk

nmi
    pla
    pla
    pla
    brk

source_end

splash1 ; .string              "\"VOSC6502\" (Virtual Old School Computer with a 6502 processor)\n"
    .byte $22, $56, $4f, $53, $43, $36, $35, $30, $32, $22, $20, $28, $56
    .byte $69, $72, $74, $75, $61, $6c, $20, $4f, $6c, $64, $20, $53, $63
    .byte $68, $6f, $6f, $6c, $20, $43, $6f, $6d, $70, $75, $74, $65, $72
    .byte $20, $77, $69, $74, $68, $20, $61, $20, $36, $35, $30, $32, $20
    .byte $70, $72, $6f, $63, $65, $73, $73, $6f, $72, $29, $0a, $00

splash2
;    .string            "version 0.99 -------------------------- MMXX - Pierre Faller\n"
    .byte $76, $65, $72, $73, $69, $6f, $6e, $20, $30, $2e, $39, $39, $20
    .byte $2d, $2d, $2d, $2d, $2d, $2d, $2d, $2d, $2d, $2d, $2d, $2d, $2d
    .byte $2d, $2d, $2d, $2d, $2d, $2d, $2d, $2d, $2d, $2d, $2d, $2d, $2d
    .byte $20, $4d, $4d, $58, $58, $20, $2d, $20, $50, $69, $65, $72, $72
    .byte $65, $20, $46, $61, $6c, $6c, $65, $72, $0a, $00

start_mes
;    .string "start point is "
    .byte $73, $74, $61, $72, $74, $20, $70, $6f, $69, $6e, $74, $20, $69
    .byte $73, $20, $00

stop_mes
;    .string "stop point is "
    .byte $73, $74, $6f, $70, $20, $70, $6f, $69, $6e, $74, $20, $69, $73
    .byte $20, $00
;    .string "searching the small beast..." " and don't find it" + chr(255)
    .byte $73, $65, $61, $72, $63, $68, $69, $6e, $67, $20, $74, $68, $65
    .byte $20, $73, $6d, $61, $6c, $6c, $20, $62, $65, $61, $73, $74, $2e
    .byte $2e, $2e, $20, $61, $6e, $64, $20, $64, $6f, $6e, $27, $74, $20
    .byte $66, $69, $6e, $64, $20, $69, $74, $ff, $00

hextab ; .ch_array "0123456789ABCDEF"
    .byte $30, $31, $32, $33, $34, $35, $36, $37, $38, $39, $41, $42, $43
    .byte $44, $45, $46

test6 ; .ch_array "\x00\x01\x02\x03\x04\x05\x06\x07\x08\x09\x0a\x0b\x0c\x0d\x0e\x0f"
    .byte $00, $01, $02, $03, $04, $05, $06, $07, $08, $09, $0a, $0b, $0c
    .byte $0d, $0e, $0f

    ; * = $fffa ; nmi vector
    ; .word nmi

    ; * = $fffc ; run vector
    ; .word main

    ; * = $fffe ; irq vector
    ; .word irq
