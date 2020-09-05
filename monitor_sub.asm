
    .include monitor_equates.asm

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

