
    ;---------------------------------;
    ; a 4ko ROM monitor for vosc6502  ;
    ;---------------------------------;

    .include monitor_equates.asm

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
    .include monitor_stuff.asm

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

splash1 .string "\"VOSC6502\" (Virtual Old School Computer with a 6502 processor)\n"
    
splash2 .string "version 0.99 -------------------------- MMXX - Pierre Faller\n"

start_mes .string "start point is "

stop_mes .string "stop point is "

hextab .ch_array "0123456789ABCDEF"

source_end
