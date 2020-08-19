
    ;---------------------------------;
    ; a 4ko ROM monitor for vosc6502  ;
    ;---------------------------------;

;    .include monitor_equates.asm

    ; special characters
    CHAR_RETURN = $0a
    
    ;hardware registers
    PUTSCR_REG = $bf00
    
    * = $f000

source_start

hooks
    .word print
    .word print_nibble
    .word print_byte
    .word print_word

main
    jmp start
    ; .include monitor_sub.asm

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

splash1 .string "\"VOSC6502\" (Virtual Old School Computer with a 6502 processor)\n"
    
splash2 .string "version 0.99 -------------------------- MMXX - Pierre Faller\n"

start_mes .string "free rom "

stop_mes .string " bytes\n"

nmi_mes .string " NMI occured\n"

irq_mes .string " IRQ occured\n"

hextab .ch_array "0123456789ABCDEF"

source_end
