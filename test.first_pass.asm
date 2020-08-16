00007     CHAR_RETURN = $0a
    []
    --------
    (label)CHAR_RETURN      10
    (keyword)=                None
    (value)$0a              10

00010     PUTSCR_REG = $bf00
    []
    --------
    (label)PUTSCR_REG       48896
    (keyword)=                None
    (value)$bf00            48896

00012     x1 = 'a
    []
    --------
    (label)x1               97
    (keyword)=                None
    (value)'a               97

00013     x2 = ~10000001
    []
    --------
    (label)x2               129
    (keyword)=                None
    (value)~10000001        129

00014     x3 = "azerty"
    []
    --------
    (label)x3               None
    (keyword)=                None
    (string)"azerty"         "azerty"

00016     * = $f000
    []
    --------
    (keyword)*                None
    (keyword)=                None
    (value)$f000            61440

00018 source_start
    []
    (label)source_start     None

00020 hooks
    []
    (label)hooks            None

00021     .word print
    []
    --------
    (keyword).word            None
    (label)print            None

00022     .word print_nibble
    []
    --------
    (keyword).word            None
    (label)print_nibble     None

00023     .word print_byte
    []
    --------
    (keyword).word            None
    (label)print_byte       None

00024     .word print_word
    []
    --------
    (keyword).word            None
    (label)print_word       None

00026 splash1 .string "\"VOSC6502\" (Virtual Old School ; Computer with a 6502 processor)\n"
    []
    (label)splash1          None
    (keyword).string          None
    (string)"\"VOSC6502\" (Virtual Old School ; Computer with a 6502 processor)\n" "\"VOSC6502\" (Virtual Old School ; Computer with a 6502 processor)\n"

00028 splash2 .string "version 0.99 -------------------------- MMXX - Pierre Faller\n"
    []
    (label)splash2          None
    (keyword).string          None
    (string)"version 0.99 -------------------------- MMXX - Pierre Faller\n" "version 0.99 -------------------------- MMXX - Pierre Faller\n"

00030 main
    []
    (label)main             None

00031     jmp start
    []
    --------
    (mnemo)jmp              None
    (label)start            None

00033     nop
    []
    --------
    (mnemo)nop              None

00034     nop
    []
    --------
    (mnemo)nop              None

00035     nop
    []
    --------
    (mnemo)nop              None

00036     brk
    []
    --------
    (mnemo)brk              None

00038 println
    []
    (label)println          None

00039     jsr print
    []
    --------
    (mnemo)jsr              None
    (label)print            None

00040     lda #CHAR_RETURN
    []
    --------
    (mnemo)lda              None
    (keyword)#                None
    (label)CHAR_RETURN      None

00041     sta PUTSCR_REG
    []
    --------
    (mnemo)sta              None
    (label)PUTSCR_REG       None

00042     rts
    []
    --------
    (mnemo)rts              None

00044 print
    []
    (label)print            None

00046     stx op1
    []
    --------
    (mnemo)stx              None
    (label)op1              None

00047     sty op1+1
    []
    --------
    (mnemo)sty              None
    (label)op1              None
    (keyword)+                None
    (value)1                1

00048     ldy #0
    []
    --------
    (mnemo)ldy              None
    (keyword)#                None
    (value)0                0

00050 print_l1
    []
    (label)print_l1         None

00051     lda (op1),y
    []
    --------
    (mnemo)lda              None
    (keyword)(                None
    (label)op1              None
    (keyword))                None
    (keyword),                None
    (label)y                None

00052     cmp #0
    []
    --------
    (mnemo)cmp              None
    (keyword)#                None
    (value)0                0

00053     beq print_out
    []
    --------
    (mnemo)beq              None
    (label)print_out        None

00054     sta PUTSCR_REG
    []
    --------
    (mnemo)sta              None
    (label)PUTSCR_REG       None

00055     iny
    []
    --------
    (mnemo)iny              None

00056     bne print_l1
    []
    --------
    (mnemo)bne              None
    (label)print_l1         None

00058 print_out
    []
    (label)print_out        None

00059     rts
    []
    --------
    (mnemo)rts              None

00061 print_nibble
    []
    (label)print_nibble     None

00062     and #$0f
    []
    --------
    (mnemo)and              None
    (keyword)#                None
    (value)$0f              15

00063     tax
    []
    --------
    (mnemo)tax              None

00064     lda hextab, x
    []
    --------
    (mnemo)lda              None
    (label)hextab           None
    (keyword),                None
    (label)x                None

00065     sta PUTSCR_REG
    []
    --------
    (mnemo)sta              None
    (label)PUTSCR_REG       None

00066     rts
    []
    --------
    (mnemo)rts              None

00068 print_byte
    []
    (label)print_byte       None

00069     pha
    []
    --------
    (mnemo)pha              None

00070     lsr
    []
    --------
    (mnemo)lsr              None

00071     lsr
    []
    --------
    (mnemo)lsr              None

00072     lsr
    []
    --------
    (mnemo)lsr              None

00073     lsr
    []
    --------
    (mnemo)lsr              None

00074     jsr print_nibble
    []
    --------
    (mnemo)jsr              None
    (label)print_nibble     None

00075     pla
    []
    --------
    (mnemo)pla              None

00076     jmp print_nibble
    []
    --------
    (mnemo)jmp              None
    (label)print_nibble     None

00078 print_word
    []
    (label)print_word       None

00079     pha
    []
    --------
    (mnemo)pha              None

00080     tax
    []
    --------
    (mnemo)tax              None

00081     jsr print_byte
    []
    --------
    (mnemo)jsr              None
    (label)print_byte       None

00082     pla
    []
    --------
    (mnemo)pla              None

00083     jmp print_byte
    []
    --------
    (mnemo)jmp              None
    (label)print_byte       None

00085 start
    []
    (label)start            None

00087     value = $1234
    []
    --------
    (label)value            4660
    (keyword)=                None
    (value)$1234            4660

00088     ldx #<value
    []
    --------
    (mnemo)ldx              None
    (keyword)#                None
    (keyword)<                None
    (label)value            None

00089     lda #>value
    []
    --------
    (mnemo)lda              None
    (keyword)#                None
    (keyword)>                None
    (label)value            None

00090     jsr print_word
    []
    --------
    (mnemo)jsr              None
    (label)print_word       None

00091 loop
    []
    (label)loop             None

00092     jmp loop
    []
    --------
    (mnemo)jmp              None
    (label)loop             None

00096     ldx #<splash1
    []
    --------
    (mnemo)ldx              None
    (keyword)#                None
    (keyword)<                None
    (label)splash1          None

00097     ldy #>splash1
    []
    --------
    (mnemo)ldy              None
    (keyword)#                None
    (keyword)>                None
    (label)splash1          None

00098     jsr print
    []
    --------
    (mnemo)jsr              None
    (label)print            None

00101     ldx #<splash2 + 3
    []
    --------
    (mnemo)ldx              None
    (keyword)#                None
    (keyword)<                None
    (label)splash2          None
    (keyword)+                None
    (value)3                3

00102     ldy #>splash2
    []
    --------
    (mnemo)ldy              None
    (keyword)#                None
    (keyword)>                None
    (label)splash2          None

00103     jsr print
    []
    --------
    (mnemo)jsr              None
    (label)print            None

00106     ldx #<main
    []
    --------
    (mnemo)ldx              None
    (keyword)#                None
    (keyword)<                None
    (label)main             None

00107     ldy #>main
    []
    --------
    (mnemo)ldy              None
    (keyword)#                None
    (keyword)>                None
    (label)main             None

00108     jsr print
    []
    --------
    (mnemo)jsr              None
    (label)print            None

00111     ldx #<start_mes
    []
    --------
    (mnemo)ldx              None
    (keyword)#                None
    (keyword)<                None
    (label)start_mes        None

00112     lda #>start_mes
    []
    --------
    (mnemo)lda              None
    (keyword)#                None
    (keyword)>                None
    (label)start_mes        None

00113     jsr print_word
    []
    --------
    (mnemo)jsr              None
    (label)print_word       None

00116     ldx #<stop
    []
    --------
    (mnemo)ldx              None
    (keyword)#                None
    (keyword)<                None
    (label)stop             None

00117     ldy #>stop
    []
    --------
    (mnemo)ldy              None
    (keyword)#                None
    (keyword)>                None
    (label)stop             None

00118     jsr print
    []
    --------
    (mnemo)jsr              None
    (label)print            None

00121     ldx #<stop_mes
    []
    --------
    (mnemo)ldx              None
    (keyword)#                None
    (keyword)<                None
    (label)stop_mes         None

00122     lda #>stop_mes
    []
    --------
    (mnemo)lda              None
    (keyword)#                None
    (keyword)>                None
    (label)stop_mes         None

00123     jsr print_word
    []
    --------
    (mnemo)jsr              None
    (label)print_word       None

00125 stop
    []
    (label)stop             None

00126     brk
    []
    --------
    (mnemo)brk              None

00128 irq
    []
    (label)irq              None

00130     ldx #<irq_mes
    []
    --------
    (mnemo)ldx              None
    (keyword)#                None
    (keyword)<                None
    (label)irq_mes          None

00131     ldy #>irq_mes
    []
    --------
    (mnemo)ldy              None
    (keyword)#                None
    (keyword)>                None
    (label)irq_mes          None

00132     jsr print
    []
    --------
    (mnemo)jsr              None
    (label)print            None

00133 irq_loop
    []
    (label)irq_loop         None

00134     jmp irq_loop
    []
    --------
    (mnemo)jmp              None
    (label)irq_loop         None

00136 nmi
    []
    (label)nmi              None

00138     ldx #<nmi_mes
    []
    --------
    (mnemo)ldx              None
    (keyword)#                None
    (keyword)<                None
    (label)nmi_mes          None

00139     ldy #>nmi_mes
    []
    --------
    (mnemo)ldy              None
    (keyword)#                None
    (keyword)>                None
    (label)nmi_mes          None

00140     jsr       print
    []
    --------
    (mnemo)jsr              None
    (label)print            None

00141 nmi_loop
    []
    (label)nmi_loop         None

00142     jmp nmi_loop
    []
    --------
    (mnemo)jmp              None
    (label)nmi_loop         None

00144 start_mes .string "free rom "
    []
    (label)start_mes        None
    (keyword).string          None
    (string)"free rom "      "free rom "

00146 stop_mes .string " bytes\n"
    []
    (label)stop_mes         None
    (keyword).string          None
    (string)" bytes\n"       " bytes\n"

00148 nmi_mes .string " NMI occured\n"
    []
    (label)nmi_mes          None
    (keyword).string          None
    (string)" NMI occured\n" " NMI occured\n"

00150 irq_mes .string " IRQ occured\n"
    []
    (label)irq_mes          None
    (keyword).string          None
    (string)" IRQ occured\n" " IRQ occured\n"

00152 hextab .ch_array "0123456789ABCDEF"
    []
    (label)hextab           None
    (keyword).ch_array        None
    (string)"0123456789ABCDEF" "0123456789ABCDEF"

00154 source_end
    []
    (label)source_end       None

