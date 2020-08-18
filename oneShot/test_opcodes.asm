
    ; ------------------------------------------------------------;
    ; this progra uses all the official opcodes for 6502 processor;
    ; ------------------------------------------------------------;

    * = $200

label_01
    BRK          ; opcode $00
    ORA ($69,X)  ; opcode $01
                 ; illegal opcode $02
                 ; illegal opcode $03
                 ; illegal opcode $04
    ORA $FE      ; opcode $05
    ASL $35      ; opcode $06
                 ; illegal opcode $07
    PHP          ; opcode $08
    ORA #$78     ; opcode $09
    ASL A        ; opcode $0a
                 ; illegal opcode $0b
                 ; illegal opcode $0c
    ORA $9B4D    ; opcode $0d
    ASL $7519    ; opcode $0e
                 ; illegal opcode $0f
label_02
    BPL label_02 ; opcode $10
    ORA ($58),Y  ; opcode $11
                 ; illegal opcode $12
                 ; illegal opcode $13
                 ; illegal opcode $14
    ORA $0A,X    ; opcode $15
    ASL $85,X    ; opcode $16
                 ; illegal opcode $17
    CLC          ; opcode $18
    ORA $25A1,Y  ; opcode $19
                 ; illegal opcode $1a
                 ; illegal opcode $1b
                 ; illegal opcode $1c
    ORA $6D53,X  ; opcode $1d
    ASL $02B7,X  ; opcode $1e
                 ; illegal opcode $1f
label_03
    JSR $2C04    ; opcode $20
    AND ($7E,X)  ; opcode $21
                 ; illegal opcode $22
                 ; illegal opcode $23
    BIT $05      ; opcode $24
    AND $92      ; opcode $25
    ROL $96      ; opcode $26
                 ; illegal opcode $27
    PLP          ; opcode $28
    AND #$13     ; opcode $29
    ROL A        ; opcode $2a
                 ; illegal opcode $2b
    BIT $B782    ; opcode $2c
    AND $F680    ; opcode $2d
    ROL $5FFE    ; opcode $2e
                 ; illegal opcode $2f
label_04
    BMI label_04 ; opcode $30
    AND ($79),Y  ; opcode $31
                 ; illegal opcode $32
                 ; illegal opcode $33
                 ; illegal opcode $34
    AND $86,X    ; opcode $35
    ROL $45,X    ; opcode $36
                 ; illegal opcode $37
    SEC          ; opcode $38
    AND $792A,Y  ; opcode $39
                 ; illegal opcode $3a
                 ; illegal opcode $3b
                 ; illegal opcode $3c
    ORA $FBAE,X  ; opcode $3d
    ASL $0DEE,X  ; opcode $3e
                 ; illegal opcode $3f
label_05
    RTI          ; opcode $40
    EOR ($B7,X)  ; opcode $41
                 ; illegal opcode $42
                 ; illegal opcode $43
                 ; illegal opcode $44
    EOR $87      ; opcode $45
    LSR $9C      ; opcode $46
                 ; illegal opcode $47
    PHA          ; opcode $48
    EOR #$31     ; opcode $49
    LSR A        ; opcode $4a
                 ; illegal opcode $4b
    JMP $05CA    ; opcode $4c
    EOR $3700    ; opcode $4d
    LSR $B509    ; opcode $4e
                 ; illegal opcode $4f
label_06
    BVC label_06 ; opcode $50
    EOR ($D1),Y  ; opcode $51
                 ; illegal opcode $52
                 ; illegal opcode $53
                 ; illegal opcode $54
    EOR $7E,X    ; opcode $55
    LSR $1C,X    ; opcode $56
                 ; illegal opcode $57
    CLI          ; opcode $58
    EOR $CBC8,Y  ; opcode $59
                 ; illegal opcode $5a
                 ; illegal opcode $5b
                 ; illegal opcode $5c
    EOR $3EA5,X  ; opcode $5d
    LSR $3A78,X  ; opcode $5e
                 ; illegal opcode $5f
label_07
    RTS          ; opcode $60
    ADC ($6E,X)  ; opcode $61
                 ; illegal opcode $62
                 ; illegal opcode $63
                 ; illegal opcode $64
    ADC $F6      ; opcode $65
    ROR $1A      ; opcode $66
                 ; illegal opcode $67
    PLA          ; opcode $68
    ADC #$DF     ; opcode $69
    ROR A        ; opcode $6a
                 ; illegal opcode $6b
    JMP($DD86)   ; opcode $6c
    ADC $4EE7    ; opcode $6d
    ROR $B364    ; opcode $6e
                 ; illegal opcode $6f
label_08
    BCS label_08 ; opcode $70
    ADC ($BE),Y  ; opcode $71
                 ; illegal opcode $72
                 ; illegal opcode $73
                 ; illegal opcode $74
    ADC $A6,X    ; opcode $75
    ROR $6B,X    ; opcode $76
                 ; illegal opcode $77
    SEI          ; opcode $78
    ADC $5335,Y  ; opcode $79
                 ; illegal opcode $7a
                 ; illegal opcode $7b
                 ; illegal opcode $7c
    ADC $1B85,X  ; opcode $7d
    ROR $C641,X  ; opcode $7e
                 ; illegal opcode $7f
label_09
                 ; illegal opcode $80
    STA ($1B,X)  ; opcode $81
                 ; illegal opcode $82
                 ; illegal opcode $83
    STY $3D      ; opcode $84
    STA $61      ; opcode $85
    STX $1A      ; opcode $86
                 ; illegal opcode $87
    DEY          ; opcode $88
                 ; illegal opcode $89
    TXA          ; opcode $8a
                 ; illegal opcode $8b
    STY $E89C    ; opcode $8c
    STA $11FE    ; opcode $8d
    STX $7EAC    ; opcode $8e
                 ; illegal opcode $8f
label_10
    BCC label_10 ; opcode $90
    STA ($E6),Y  ; opcode $91
                 ; illegal opcode $92
                 ; illegal opcode $93
    STY          ; opcode $94
    STA $AE,X    ; opcode $95
    STX $43,Y    ; opcode $96
                 ; illegal opcode $97
    TYA          ; opcode $98
    STA $6CF5,Y  ; opcode $99
    TXS          ; opcode $9a
                 ; illegal opcode $9b
                 ; illegal opcode $9c
    STA $B13E,X  ; opcode $9d
                 ; illegal opcode $9e
                 ; illegal opcode $9f
label_11
    LDY #$ED     ; opcode $a0
    LDA ($82,X)  ; opcode $a1
    LDX #$4D     ; opcode $a2
                 ; illegal opcode $a3
    LDY $CF      ; opcode $a4
    LDA $0F      ; opcode $a5
    LDX $8A      ; opcode $a6
                 ; illegal opcode $a7
    TAY          ; opcode $a8
    LDA #$BD     ; opcode $a9
    TAX          ; opcode $aa
                 ; illegal opcode $ab
    LDY $6248    ; opcode $ac
    LDA $F69F    ; opcode $ad
    LDX $7B4F    ; opcode $ae
                 ; illegal opcode $af
label_12
    BCS label_12 ; opcode $b0
    LDA ($80),Y  ; opcode $b1
                 ; illegal opcode $b2
                 ; illegal opcode $b3
    LDY $D1,X    ; opcode $b4
    LDA $93,X    ; opcode $b5
    LDX $71,Y    ; opcode $b6
                 ; illegal opcode $b7
    CLV          ; opcode $b8
    LDA $9A80,Y  ; opcode $b9
    TSX          ; opcode $ba
                 ; illegal opcode $bb
    LDY          ; opcode $bc
    LDA $C83C,X  ; opcode $bd
    LDX $CB10,Y  ; opcode $be
                 ; illegal opcode $bf
label_13
    CPY #$5A     ; opcode $c0
    CMP ($5E,X)  ; opcode $c1
                 ; illegal opcode $c2
                 ; illegal opcode $c3
    CPY $31      ; opcode $c4
    CMP $B2      ; opcode $c5
    DEC $07      ; opcode $c6
                 ; illegal opcode $c7
    INY          ; opcode $c8
    CMP #$9E     ; opcode $c9
    DEX          ; opcode $ca
                 ; illegal opcode $cb
    CPY $39CA    ; opcode $cc
    CMP $5CB9    ; opcode $cd
    DEC $A6DF    ; opcode $ce
                 ; illegal opcode $cf
label_14
    BNE label_14 ; opcode $d0
    CMP ($7F),Y  ; opcode $d1
                 ; illegal opcode $d2
                 ; illegal opcode $d3
                 ; illegal opcode $d4
    CMP $C0,X    ; opcode $d5
    DEC $74,X    ; opcode $d6
                 ; illegal opcode $d7
    CLD          ; opcode $d8
    CMP $BEA7,Y  ; opcode $d9
                 ; illegal opcode $da
                 ; illegal opcode $db
                 ; illegal opcode $dc
    CMP $64E2,X  ; opcode $dd
    DEC $6189,X  ; opcode $de
                 ; illegal opcode $df
label_15
    CPX #$95     ; opcode $e0
    SBC ($5F,X)  ; opcode $e1
                 ; illegal opcode $e2
                 ; illegal opcode $e3
    CPX $BD      ; opcode $e4
    SBC $27      ; opcode $e5
    INC $75      ; opcode $e6
                 ; illegal opcode $e7
    INX          ; opcode $e8
    SBC #$E7     ; opcode $e9
    NOP          ; opcode $ea
    SBC          ; opcode $eb
    CPX $B943    ; opcode $ec
    SBC $C98A    ; opcode $ed
    INC $4BCC    ; opcode $ee
                 ; illegal opcode $ef
label_16
    BEQ label_16 ; opcode $f0
    SBC ($F2),Y  ; opcode $f1
                 ; illegal opcode $f2
                 ; illegal opcode $f3
                 ; illegal opcode $f4
    SBC $12,X    ; opcode $f5
    INC $62,X    ; opcode $f6
                 ; illegal opcode $f7
    SED          ; opcode $f8
    SBC $33E6,Y  ; opcode $f9
                 ; illegal opcode $fa
                 ; illegal opcode $fb
                 ; illegal opcode $fc
    SBC $0A2F,X  ; opcode $fd
    INC $8659,X  ; opcode $fe
                 ; illegal opcode $ff
