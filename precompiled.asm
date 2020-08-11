
    ;---------------------------------;
    ; a 4ko ROM monitor for vosc6502  ;
    ;---------------------------------;

;     .include monitor_stuff.asm


;     .include monitor_equates.asm

    ; spaciel characters
    CHAR_RETURN = $0a

    ;hardware registers
    PUTSCR_REG = $bf00




;     ZP word op1
    op1 = 0
;     ZP word op2
    op2 = 2
;     ZP word op3
    op3 = 4

;     ZP byte titi
    titi = 6
;     ZP byte TATA
    tata = 7
;     ZP WORD wiwi
    wiwi = 8


    * = $c000

main
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
    jsr print16

    ; print "stop point is
    ldx #<stop
    ldy #>stop
    jsr print

    ; print "start point value
    ldx #<stop_mes
    lda #>stop_mes
    jsr print16

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

print4
    and #$0f
    tax
    lda hextab, x
    sta PUTSCR_REG
    rts

print8
    pha
    lsr
    lsr
    lsr
    lsr
    jsr print4
    pla
    jmp print4

print16
    pha
    tax
    jsr print8
    pla
    jmp print8

irq_in
    pla
    pla
    pla
    brk

nmi_in
    pla
    pla
    pla
    brk

splash1
    .byte "VOSC6502 (Virtual Old School Computer with a 6502 processor)", 0

splash2
    .byte "version 0.99 -------------------------- MMXX - Pierre Faller", 0

start_mes
    .byte "start point is ", 0

stop_mes
    .byte "stop point is ", 0

hextab
    .byte "0123456789ABCDEF", 0

    * = $fffa ; nmi vector
    .word nmi_in

    * = $fffc ; run vector
    .word main

    * = $fffe ; irq vector
    .word irq_in

