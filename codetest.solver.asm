    .word print
print
-> None
----------------------------------------
    .word print_nibble
print_nibble
-> None
----------------------------------------
    .word print_byte
print_byte
-> None
----------------------------------------
    .word print_word
print_word
-> None
----------------------------------------
    ldx #<value
4660
-> (18,)
----------------------------------------
    lda #>value
4660
-> (52,)
----------------------------------------
    ldx #<splash1
splash1
-> None
----------------------------------------
    ldy #>splash1
splash1
-> None
----------------------------------------
    ldx #<splash2
splash2
-> None
----------------------------------------
    ldy #>splash2
splash2
-> None
----------------------------------------
    ldx #<main
1536
-> (6,)
----------------------------------------
    ldy #>main
1536
-> (0,)
----------------------------------------
    ldx #<start_mes
start_mes
-> None
----------------------------------------
    lda #>start_mes
start_mes
-> None
----------------------------------------
    ldx #<stop
stop
-> None
----------------------------------------
    ldy #>stop
stop
-> None
----------------------------------------
    ldx #<stop_mes
stop_mes
-> None
----------------------------------------
    lda #>stop_mes
stop_mes
-> None
----------------------------------------
    ldx #<irq_mes
irq_mes
-> None
----------------------------------------
    ldy #>irq_mes
irq_mes
-> None
----------------------------------------
    ldx #<nmi_mes
nmi_mes
-> None
----------------------------------------
    ldy #>nmi_mes
nmi_mes
-> None
----------------------------------------
splash1 .string "\"VOSC6502\" (Virtual Old School Computer with a 6502 processor)\n"
"\"VOSC6502\" (Virtual Old School Computer with a 6502 processor)\n"
----------------------------------------
splash2 .string "version 0.99 -------------------------- MMXX - Pierre Faller\n"
"version 0.99 -------------------------- MMXX - Pierre Faller\n"
----------------------------------------
start_mes .string "free rom "
"free rom "
----------------------------------------
stop_mes .string " bytes\n"
" bytes\n"
----------------------------------------
nmi_mes .string " NMI occured\n"
" NMI occured\n"
----------------------------------------
irq_mes .string " IRQ occured\n"
" IRQ occured\n"
----------------------------------------
hextab .ch_array "0123456789ABCDEF"
"0123456789ABCDEF"
----------------------------------------
hextab2 .byte $30, $31, $32, $33, $34, $35, $36, $37, $38, $39, op1 |$80
48 , 49 , 50 , 51 , 52 , 53 , 54 , 55 , 56 , 57 , 0 | 128
----------------------------------------
hextab3 .word $1234, $2345, $3456, $5678, $6789
4660 , 9029 , 13398 , 22136 , 26505
----------------------------------------
DU_GRAS .ds 34
34
----------------------------------------
Dummmy .byte ~00011000
24
----------------------------------------
dubidu .byte $33,<mni_mes,>nmi_mes
mni_mes
-> None
----------------------------------------
dubidu .byte $33,<mni_mes,>nmi_mes
1821
-> (29,)
----------------------------------------
    .word print
1548
----------------------------------------
    .word print_nibble
1569
----------------------------------------
    .word print_byte
1579
----------------------------------------
    .word print_word
1591
----------------------------------------
    ldx #<value
4660
-> (18,)
----------------------------------------
    lda #>value
4660
-> (52,)
----------------------------------------
    ldx #<splash1
1677
-> (6,)
----------------------------------------
    ldy #>splash1
1677
-> (141,)
----------------------------------------
    ldx #<splash2
1741
-> (6,)
----------------------------------------
    ldy #>splash2
1741
-> (205,)
----------------------------------------
    ldx #<main
1536
-> (6,)
----------------------------------------
    ldy #>main
1536
-> (0,)
----------------------------------------
    ldx #<start_mes
1803
-> (7,)
----------------------------------------
    lda #>start_mes
1803
-> (11,)
----------------------------------------
    ldx #<stop
1656
-> (6,)
----------------------------------------
    ldy #>stop
1656
-> (120,)
----------------------------------------
    ldx #<stop_mes
1813
-> (7,)
----------------------------------------
    lda #>stop_mes
1813
-> (21,)
----------------------------------------
    ldx #<irq_mes
1835
-> (7,)
----------------------------------------
    ldy #>irq_mes
1835
-> (43,)
----------------------------------------
    ldx #<nmi_mes
1821
-> (7,)
----------------------------------------
    ldy #>nmi_mes
1821
-> (29,)
----------------------------------------
dubidu .byte $33,<mni_mes,>nmi_mes
mni_mes
-> None
----------------------------------------
dubidu .byte $33,<mni_mes,>nmi_mes
1821
-> (29,)
----------------------------------------
    ldx #<value
4660
-> (18,)
----------------------------------------
    lda #>value
4660
-> (52,)
----------------------------------------
    ldx #<splash1
1677
-> (6,)
----------------------------------------
    ldy #>splash1
1677
-> (141,)
----------------------------------------
    ldx #<splash2
1741
-> (6,)
----------------------------------------
    ldy #>splash2
1741
-> (205,)
----------------------------------------
    ldx #<main
1536
-> (6,)
----------------------------------------
    ldy #>main
1536
-> (0,)
----------------------------------------
    ldx #<start_mes
1803
-> (7,)
----------------------------------------
    lda #>start_mes
1803
-> (11,)
----------------------------------------
    ldx #<stop
1656
-> (6,)
----------------------------------------
    ldy #>stop
1656
-> (120,)
----------------------------------------
    ldx #<stop_mes
1813
-> (7,)
----------------------------------------
    lda #>stop_mes
1813
-> (21,)
----------------------------------------
    ldx #<irq_mes
1835
-> (7,)
----------------------------------------
    ldy #>irq_mes
1835
-> (43,)
----------------------------------------
    ldx #<nmi_mes
1821
-> (7,)
----------------------------------------
    ldy #>nmi_mes
1821
-> (29,)
----------------------------------------
dubidu .byte $33,<mni_mes,>nmi_mes
mni_mes
-> None
----------------------------------------
dubidu .byte $33,<mni_mes,>nmi_mes
1821
-> (29,)
----------------------------------------
    ldx #<value
4660
-> (18,)
----------------------------------------
    lda #>value
4660
-> (52,)
----------------------------------------
    ldx #<splash1
1677
-> (6,)
----------------------------------------
    ldy #>splash1
1677
-> (141,)
----------------------------------------
    ldx #<splash2
1741
-> (6,)
----------------------------------------
    ldy #>splash2
1741
-> (205,)
----------------------------------------
    ldx #<main
1536
-> (6,)
----------------------------------------
    ldy #>main
1536
-> (0,)
----------------------------------------
    ldx #<start_mes
1803
-> (7,)
----------------------------------------
    lda #>start_mes
1803
-> (11,)
----------------------------------------
    ldx #<stop
1656
-> (6,)
----------------------------------------
    ldy #>stop
1656
-> (120,)
----------------------------------------
    ldx #<stop_mes
1813
-> (7,)
----------------------------------------
    lda #>stop_mes
1813
-> (21,)
----------------------------------------
    ldx #<irq_mes
1835
-> (7,)
----------------------------------------
    ldy #>irq_mes
1835
-> (43,)
----------------------------------------
    ldx #<nmi_mes
1821
-> (7,)
----------------------------------------
    ldy #>nmi_mes
1821
-> (29,)
----------------------------------------
dubidu .byte $33,<mni_mes,>nmi_mes
mni_mes
-> None
----------------------------------------
dubidu .byte $33,<mni_mes,>nmi_mes
1821
-> (29,)
----------------------------------------
    ldx #<value
4660
-> (18,)
----------------------------------------
    lda #>value
4660
-> (52,)
----------------------------------------
    ldx #<splash1
1677
-> (6,)
----------------------------------------
    ldy #>splash1
1677
-> (141,)
----------------------------------------
    ldx #<splash2
1741
-> (6,)
----------------------------------------
    ldy #>splash2
1741
-> (205,)
----------------------------------------
    ldx #<main
1536
-> (6,)
----------------------------------------
    ldy #>main
1536
-> (0,)
----------------------------------------
    ldx #<start_mes
1803
-> (7,)
----------------------------------------
    lda #>start_mes
1803
-> (11,)
----------------------------------------
    ldx #<stop
1656
-> (6,)
----------------------------------------
    ldy #>stop
1656
-> (120,)
----------------------------------------
    ldx #<stop_mes
1813
-> (7,)
----------------------------------------
    lda #>stop_mes
1813
-> (21,)
----------------------------------------
    ldx #<irq_mes
1835
-> (7,)
----------------------------------------
    ldy #>irq_mes
1835
-> (43,)
----------------------------------------
    ldx #<nmi_mes
1821
-> (7,)
----------------------------------------
    ldy #>nmi_mes
1821
-> (29,)
----------------------------------------
dubidu .byte $33,<mni_mes,>nmi_mes
mni_mes
-> None
----------------------------------------
dubidu .byte $33,<mni_mes,>nmi_mes
1821
-> (29,)
----------------------------------------
    ldx #<value
4660
-> (18,)
----------------------------------------
    lda #>value
4660
-> (52,)
----------------------------------------
    ldx #<splash1
1677
-> (6,)
----------------------------------------
    ldy #>splash1
1677
-> (141,)
----------------------------------------
    ldx #<splash2
1741
-> (6,)
----------------------------------------
    ldy #>splash2
1741
-> (205,)
----------------------------------------
    ldx #<main
1536
-> (6,)
----------------------------------------
    ldy #>main
1536
-> (0,)
----------------------------------------
    ldx #<start_mes
1803
-> (7,)
----------------------------------------
    lda #>start_mes
1803
-> (11,)
----------------------------------------
    ldx #<stop
1656
-> (6,)
----------------------------------------
    ldy #>stop
1656
-> (120,)
----------------------------------------
    ldx #<stop_mes
1813
-> (7,)
----------------------------------------
    lda #>stop_mes
1813
-> (21,)
----------------------------------------
    ldx #<irq_mes
1835
-> (7,)
----------------------------------------
    ldy #>irq_mes
1835
-> (43,)
----------------------------------------
    ldx #<nmi_mes
1821
-> (7,)
----------------------------------------
    ldy #>nmi_mes
1821
-> (29,)
----------------------------------------
dubidu .byte $33,<mni_mes,>nmi_mes
mni_mes
-> None
----------------------------------------
dubidu .byte $33,<mni_mes,>nmi_mes
1821
-> (29,)
----------------------------------------
    ldx #<value
4660
-> (18,)
----------------------------------------
    lda #>value
4660
-> (52,)
----------------------------------------
    ldx #<splash1
1677
-> (6,)
----------------------------------------
    ldy #>splash1
1677
-> (141,)
----------------------------------------
    ldx #<splash2
1741
-> (6,)
----------------------------------------
    ldy #>splash2
1741
-> (205,)
----------------------------------------
    ldx #<main
1536
-> (6,)
----------------------------------------
    ldy #>main
1536
-> (0,)
----------------------------------------
    ldx #<start_mes
1803
-> (7,)
----------------------------------------
    lda #>start_mes
1803
-> (11,)
----------------------------------------
    ldx #<stop
1656
-> (6,)
----------------------------------------
    ldy #>stop
1656
-> (120,)
----------------------------------------
    ldx #<stop_mes
1813
-> (7,)
----------------------------------------
    lda #>stop_mes
1813
-> (21,)
----------------------------------------
    ldx #<irq_mes
1835
-> (7,)
----------------------------------------
    ldy #>irq_mes
1835
-> (43,)
----------------------------------------
    ldx #<nmi_mes
1821
-> (7,)
----------------------------------------
    ldy #>nmi_mes
1821
-> (29,)
----------------------------------------
dubidu .byte $33,<mni_mes,>nmi_mes
mni_mes
-> None
----------------------------------------
dubidu .byte $33,<mni_mes,>nmi_mes
1821
-> (29,)
----------------------------------------
    ldx #<value
4660
-> (18,)
----------------------------------------
    lda #>value
4660
-> (52,)
----------------------------------------
    ldx #<splash1
1677
-> (6,)
----------------------------------------
    ldy #>splash1
1677
-> (141,)
----------------------------------------
    ldx #<splash2
1741
-> (6,)
----------------------------------------
    ldy #>splash2
1741
-> (205,)
----------------------------------------
    ldx #<main
1536
-> (6,)
----------------------------------------
    ldy #>main
1536
-> (0,)
----------------------------------------
    ldx #<start_mes
1803
-> (7,)
----------------------------------------
    lda #>start_mes
1803
-> (11,)
----------------------------------------
    ldx #<stop
1656
-> (6,)
----------------------------------------
    ldy #>stop
1656
-> (120,)
----------------------------------------
    ldx #<stop_mes
1813
-> (7,)
----------------------------------------
    lda #>stop_mes
1813
-> (21,)
----------------------------------------
    ldx #<irq_mes
1835
-> (7,)
----------------------------------------
    ldy #>irq_mes
1835
-> (43,)
----------------------------------------
    ldx #<nmi_mes
1821
-> (7,)
----------------------------------------
    ldy #>nmi_mes
1821
-> (29,)
----------------------------------------
dubidu .byte $33,<mni_mes,>nmi_mes
mni_mes
-> None
----------------------------------------
dubidu .byte $33,<mni_mes,>nmi_mes
1821
-> (29,)
----------------------------------------
    ldx #<value
4660
-> (18,)
----------------------------------------
    lda #>value
4660
-> (52,)
----------------------------------------
    ldx #<splash1
1677
-> (6,)
----------------------------------------
    ldy #>splash1
1677
-> (141,)
----------------------------------------
    ldx #<splash2
1741
-> (6,)
----------------------------------------
    ldy #>splash2
1741
-> (205,)
----------------------------------------
    ldx #<main
1536
-> (6,)
----------------------------------------
    ldy #>main
1536
-> (0,)
----------------------------------------
    ldx #<start_mes
1803
-> (7,)
----------------------------------------
    lda #>start_mes
1803
-> (11,)
----------------------------------------
    ldx #<stop
1656
-> (6,)
----------------------------------------
    ldy #>stop
1656
-> (120,)
----------------------------------------
    ldx #<stop_mes
1813
-> (7,)
----------------------------------------
    lda #>stop_mes
1813
-> (21,)
----------------------------------------
    ldx #<irq_mes
1835
-> (7,)
----------------------------------------
    ldy #>irq_mes
1835
-> (43,)
----------------------------------------
    ldx #<nmi_mes
1821
-> (7,)
----------------------------------------
    ldy #>nmi_mes
1821
-> (29,)
----------------------------------------
dubidu .byte $33,<mni_mes,>nmi_mes
mni_mes
-> None
----------------------------------------
dubidu .byte $33,<mni_mes,>nmi_mes
1821
-> (29,)
----------------------------------------
    ldx #<value
4660
-> (18,)
----------------------------------------
    lda #>value
4660
-> (52,)
----------------------------------------
    ldx #<splash1
1677
-> (6,)
----------------------------------------
    ldy #>splash1
1677
-> (141,)
----------------------------------------
    ldx #<splash2
1741
-> (6,)
----------------------------------------
    ldy #>splash2
1741
-> (205,)
----------------------------------------
    ldx #<main
1536
-> (6,)
----------------------------------------
    ldy #>main
1536
-> (0,)
----------------------------------------
    ldx #<start_mes
1803
-> (7,)
----------------------------------------
    lda #>start_mes
1803
-> (11,)
----------------------------------------
    ldx #<stop
1656
-> (6,)
----------------------------------------
    ldy #>stop
1656
-> (120,)
----------------------------------------
    ldx #<stop_mes
1813
-> (7,)
----------------------------------------
    lda #>stop_mes
1813
-> (21,)
----------------------------------------
    ldx #<irq_mes
1835
-> (7,)
----------------------------------------
    ldy #>irq_mes
1835
-> (43,)
----------------------------------------
    ldx #<nmi_mes
1821
-> (7,)
----------------------------------------
    ldy #>nmi_mes
1821
-> (29,)
----------------------------------------
dubidu .byte $33,<mni_mes,>nmi_mes
mni_mes
-> None
----------------------------------------
dubidu .byte $33,<mni_mes,>nmi_mes
1821
-> (29,)
----------------------------------------
