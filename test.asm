
    ;---------------------------------;
    ; a 4ko ROM monitor for vosc6502  ;
    ;---------------------------------;

    ; special characters
    CHAR_RETURN = $0a
    
    ;hardware registers
    PUTSCR_REG = $bf00
    
    x1 = 'a;blablabla...
    x2 = ~10000001
    x3 = "azerty"

    * = $f000

source_start

hooks
    .word print
    .word print_nibble
    .word print_byte
    .word print_word

splash1 .string "\"VOSC6502\" (Virtual Old School ; Computer with a 6502 processor)\n";blablabla...
    
splash2 .string "version 0.99 -------------------------- MMXX - Pierre Faller\n"

main
    jmp start

    nop
    nop
    nop
    brk

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
    ldx #<splash2 + 3
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
    ldx #<stop_mes;blablabla
    lda #>stop_mes; blablabla
    jsr print_word ;blablabla

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
    ldy #>nmi_mes;blablabla...
    jsr       print
nmi_loop
    jmp nmi_loop

start_mes .string "free rom "

stop_mes .string " bytes\n"

nmi_mes .string " NMI occured\n"

irq_mes .string " IRQ occured\n"

hextab .ch_array "0123456789ABCDEF"

source_end
