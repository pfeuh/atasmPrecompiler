X 000011 LABEL_01:
  --------                              
----------------------------------------
X 000012     BRK          ; opcode $00
  --------                              
X (mnemo) BRK                           
----------------------------------------
. 000013     ORA ($A7,X)  ; opcode $01
  --------                              
X (mnemo) ORA                           
. (variable) $A7                        $A7              0x00a7
----------------------------------------
. 000017     ORA $6C      ; opcode $05
  --------                              
X (mnemo) ORA                           
. (variable) $6C                        $6C              0x006c
----------------------------------------
. 000018     ASL $C1      ; opcode $06
  --------                              
X (mnemo) ASL                           
. (variable) $C1                        $C1              0x00c1
----------------------------------------
X 000020     PHP          ; opcode $08
  --------                              
X (mnemo) PHP                           
----------------------------------------
. 000021     ORA #$F5     ; opcode $09
  --------                              
X (mnemo) ORA                           
. (variable) $F5                        $F5              0x00f5
----------------------------------------
X 000022     ASL A        ; opcode $0a
  --------                              
X (mnemo) ASL                           
----------------------------------------
. 000025     ORA $87A6    ; opcode $0d
  --------                              
X (mnemo) ORA                           
. (variable) $87A6                      $87A6            0x87a6
----------------------------------------
. 000026     ASL $467E    ; opcode $0e
  --------                              
X (mnemo) ASL                           
. (variable) $467E                      $467E            0x467e
----------------------------------------
X 000028 LABEL_02:
  --------                              
----------------------------------------
. 000029     BPL LABEL_02 ; opcode $10
  --------                              
X (mnemo) BPL                           
. (variable) LABEL_02                   LABEL_02         ------
----------------------------------------
. 000030     ORA ($52),Y  ; opcode $11
  --------                              
X (mnemo) ORA                           
. (variable) $52                        $52              0x0052
----------------------------------------
. 000034     ORA $07,X    ; opcode $15
  --------                              
X (mnemo) ORA                           
. (variable) $07                        $07              0x0007
. (keyword) ,                           
. (keyword) X                           
----------------------------------------
. 000035     ASL $4D,X    ; opcode $16
  --------                              
X (mnemo) ASL                           
. (variable) $4D                        $4D              0x004d
. (keyword) ,                           
. (keyword) X                           
----------------------------------------
X 000037     CLC          ; opcode $18
  --------                              
X (mnemo) CLC                           
----------------------------------------
. 000038     ORA $E97E,Y  ; opcode $19
  --------                              
X (mnemo) ORA                           
. (variable) $E97E                      $E97E            0xe97e
. (keyword) ,                           
. (keyword) Y                           
----------------------------------------
. 000042     ORA $50F5,X  ; opcode $1d
  --------                              
X (mnemo) ORA                           
. (variable) $50F5                      $50F5            0x50f5
. (keyword) ,                           
. (keyword) X                           
----------------------------------------
. 000043     ASL $241E,X  ; opcode $1e
  --------                              
X (mnemo) ASL                           
. (variable) $241E                      $241E            0x241e
. (keyword) ,                           
. (keyword) X                           
----------------------------------------
X 000045 LABEL_03:
  --------                              
----------------------------------------
. 000046     JSR $B1DA    ; opcode $20
  --------                              
X (mnemo) JSR                           
. (variable) $B1DA                      $B1DA            0xb1da
----------------------------------------
. 000047     AND ($96,X)  ; opcode $21
  --------                              
X (mnemo) AND                           
. (variable) $96                        $96              0x0096
----------------------------------------
. 000050     BIT $D0      ; opcode $24
  --------                              
X (mnemo) BIT                           
. (variable) $D0                        $D0              0x00d0
----------------------------------------
. 000051     AND $D1      ; opcode $25
  --------                              
X (mnemo) AND                           
. (variable) $D1                        $D1              0x00d1
----------------------------------------
. 000052     ROL $D8      ; opcode $26
  --------                              
X (mnemo) ROL                           
. (variable) $D8                        $D8              0x00d8
----------------------------------------
X 000054     PLP          ; opcode $28
  --------                              
X (mnemo) PLP                           
----------------------------------------
. 000055     AND #$79     ; opcode $29
  --------                              
X (mnemo) AND                           
. (variable) $79                        $79              0x0079
----------------------------------------
X 000056     ROL A        ; opcode $2a
  --------                              
X (mnemo) ROL                           
----------------------------------------
. 000058     BIT $BC10    ; opcode $2c
  --------                              
X (mnemo) BIT                           
. (variable) $BC10                      $BC10            0xbc10
----------------------------------------
. 000059     AND $97CD    ; opcode $2d
  --------                              
X (mnemo) AND                           
. (variable) $97CD                      $97CD            0x97cd
----------------------------------------
. 000060     ROL $1678    ; opcode $2e
  --------                              
X (mnemo) ROL                           
. (variable) $1678                      $1678            0x1678
----------------------------------------
X 000062 LABEL_04:
  --------                              
----------------------------------------
. 000063     BMI LABEL_04 ; opcode $30
  --------                              
X (mnemo) BMI                           
. (variable) LABEL_04                   LABEL_04         ------
----------------------------------------
. 000064     AND ($66),Y  ; opcode $31
  --------                              
X (mnemo) AND                           
. (variable) $66                        $66              0x0066
----------------------------------------
. 000068     AND $72,X    ; opcode $35
  --------                              
X (mnemo) AND                           
. (variable) $72                        $72              0x0072
. (keyword) ,                           
. (keyword) X                           
----------------------------------------
. 000069     ROL $FB,X    ; opcode $36
  --------                              
X (mnemo) ROL                           
. (variable) $FB                        $FB              0x00fb
. (keyword) ,                           
. (keyword) X                           
----------------------------------------
X 000071     SEC          ; opcode $38
  --------                              
X (mnemo) SEC                           
----------------------------------------
. 000072     AND $9FBA,Y  ; opcode $39
  --------                              
X (mnemo) AND                           
. (variable) $9FBA                      $9FBA            0x9fba
. (keyword) ,                           
. (keyword) Y                           
----------------------------------------
. 000076     ORA $64AB,X  ; opcode $3d
  --------                              
X (mnemo) ORA                           
. (variable) $64AB                      $64AB            0x64ab
. (keyword) ,                           
. (keyword) X                           
----------------------------------------
. 000077     ASL $5D20,X  ; opcode $3e
  --------                              
X (mnemo) ASL                           
. (variable) $5D20                      $5D20            0x5d20
. (keyword) ,                           
. (keyword) X                           
----------------------------------------
X 000079 LABEL_05:
  --------                              
----------------------------------------
X 000080     RTI          ; opcode $40
  --------                              
X (mnemo) RTI                           
----------------------------------------
. 000081     EOR ($28,X)  ; opcode $41
  --------                              
X (mnemo) EOR                           
. (variable) $28                        $28              0x0028
----------------------------------------
. 000085     EOR $D7      ; opcode $45
  --------                              
X (mnemo) EOR                           
. (variable) $D7                        $D7              0x00d7
----------------------------------------
. 000086     LSR $15      ; opcode $46
  --------                              
X (mnemo) LSR                           
. (variable) $15                        $15              0x0015
----------------------------------------
X 000088     PHA          ; opcode $48
  --------                              
X (mnemo) PHA                           
----------------------------------------
. 000089     EOR #$A5     ; opcode $49
  --------                              
X (mnemo) EOR                           
. (variable) $A5                        $A5              0x00a5
----------------------------------------
X 000090     LSR A        ; opcode $4a
  --------                              
X (mnemo) LSR                           
----------------------------------------
. 000092     JMP $F3FE    ; opcode $4c
  --------                              
X (mnemo) JMP                           
. (variable) $F3FE                      $F3FE            0xf3fe
----------------------------------------
. 000093     EOR $6571    ; opcode $4d
  --------                              
X (mnemo) EOR                           
. (variable) $6571                      $6571            0x6571
----------------------------------------
. 000094     LSR $286C    ; opcode $4e
  --------                              
X (mnemo) LSR                           
. (variable) $286C                      $286C            0x286c
----------------------------------------
X 000096 LABEL_06:
  --------                              
----------------------------------------
. 000097     BVC LABEL_06 ; opcode $50
  --------                              
X (mnemo) BVC                           
. (variable) LABEL_06                   LABEL_06         ------
----------------------------------------
. 000098     EOR ($B2),Y  ; opcode $51
  --------                              
X (mnemo) EOR                           
. (variable) $B2                        $B2              0x00b2
----------------------------------------
. 000102     EOR $0C,X    ; opcode $55
  --------                              
X (mnemo) EOR                           
. (variable) $0C                        $0C              0x000c
. (keyword) ,                           
. (keyword) X                           
----------------------------------------
. 000103     LSR $A4,X    ; opcode $56
  --------                              
X (mnemo) LSR                           
. (variable) $A4                        $A4              0x00a4
. (keyword) ,                           
. (keyword) X                           
----------------------------------------
X 000105     CLI          ; opcode $58
  --------                              
X (mnemo) CLI                           
----------------------------------------
. 000106     EOR $2BB7,Y  ; opcode $59
  --------                              
X (mnemo) EOR                           
. (variable) $2BB7                      $2BB7            0x2bb7
. (keyword) ,                           
. (keyword) Y                           
----------------------------------------
. 000110     EOR $CD9D,X  ; opcode $5d
  --------                              
X (mnemo) EOR                           
. (variable) $CD9D                      $CD9D            0xcd9d
. (keyword) ,                           
. (keyword) X                           
----------------------------------------
. 000111     LSR $40B3,X  ; opcode $5e
  --------                              
X (mnemo) LSR                           
. (variable) $40B3                      $40B3            0x40b3
. (keyword) ,                           
. (keyword) X                           
----------------------------------------
X 000113 LABEL_07:
  --------                              
----------------------------------------
X 000114     RTS          ; opcode $60
  --------                              
X (mnemo) RTS                           
----------------------------------------
. 000115     ADC ($5E,X)  ; opcode $61
  --------                              
X (mnemo) ADC                           
. (variable) $5E                        $5E              0x005e
----------------------------------------
. 000119     ADC $59      ; opcode $65
  --------                              
X (mnemo) ADC                           
. (variable) $59                        $59              0x0059
----------------------------------------
. 000120     ROR $A2      ; opcode $66
  --------                              
X (mnemo) ROR                           
. (variable) $A2                        $A2              0x00a2
----------------------------------------
X 000122     PLA          ; opcode $68
  --------                              
X (mnemo) PLA                           
----------------------------------------
. 000123     ADC #$48     ; opcode $69
  --------                              
X (mnemo) ADC                           
. (variable) $48                        $48              0x0048
----------------------------------------
X 000124     ROR A        ; opcode $6a
  --------                              
X (mnemo) ROR                           
----------------------------------------
. 000126     JMP($E120)   ; opcode $6c
  --------                              
X (mnemo) JMP                           
. (variable) $E120                      $E120            0xe120
----------------------------------------
. 000127     ADC $5334    ; opcode $6d
  --------                              
X (mnemo) ADC                           
. (variable) $5334                      $5334            0x5334
----------------------------------------
. 000128     ROR $3D76    ; opcode $6e
  --------                              
X (mnemo) ROR                           
. (variable) $3D76                      $3D76            0x3d76
----------------------------------------
X 000130 LABEL_08:
  --------                              
----------------------------------------
. 000131     BCS LABEL_08 ; opcode $70
  --------                              
X (mnemo) BCS                           
. (variable) LABEL_08                   LABEL_08         ------
----------------------------------------
. 000132     ADC ($DD),Y  ; opcode $71
  --------                              
X (mnemo) ADC                           
. (variable) $DD                        $DD              0x00dd
----------------------------------------
. 000136     ADC $73,X    ; opcode $75
  --------                              
X (mnemo) ADC                           
. (variable) $73                        $73              0x0073
. (keyword) ,                           
. (keyword) X                           
----------------------------------------
. 000137     ROR $A3,X    ; opcode $76
  --------                              
X (mnemo) ROR                           
. (variable) $A3                        $A3              0x00a3
. (keyword) ,                           
. (keyword) X                           
----------------------------------------
X 000139     SEI          ; opcode $78
  --------                              
X (mnemo) SEI                           
----------------------------------------
. 000140     ADC $4001,Y  ; opcode $79
  --------                              
X (mnemo) ADC                           
. (variable) $4001                      $4001            0x4001
. (keyword) ,                           
. (keyword) Y                           
----------------------------------------
. 000144     ADC $6168,X  ; opcode $7d
  --------                              
X (mnemo) ADC                           
. (variable) $6168                      $6168            0x6168
. (keyword) ,                           
. (keyword) X                           
----------------------------------------
. 000145     ROR $50E3,X  ; opcode $7e
  --------                              
X (mnemo) ROR                           
. (variable) $50E3                      $50E3            0x50e3
. (keyword) ,                           
. (keyword) X                           
----------------------------------------
X 000147 LABEL_09:
  --------                              
----------------------------------------
. 000149     STA ($07,X)  ; opcode $81
  --------                              
X (mnemo) STA                           
. (variable) $07                        $07              0x0007
----------------------------------------
. 000152     STY $C1      ; opcode $84
  --------                              
X (mnemo) STY                           
. (variable) $C1                        $C1              0x00c1
----------------------------------------
. 000153     STA $3C      ; opcode $85
  --------                              
X (mnemo) STA                           
. (variable) $3C                        $3C              0x003c
----------------------------------------
. 000154     STX $82      ; opcode $86
  --------                              
X (mnemo) STX                           
. (variable) $82                        $82              0x0082
----------------------------------------
X 000156     DEY          ; opcode $88
  --------                              
X (mnemo) DEY                           
----------------------------------------
X 000158     TXA          ; opcode $8a
  --------                              
X (mnemo) TXA                           
----------------------------------------
. 000160     STY $D1A1    ; opcode $8c
  --------                              
X (mnemo) STY                           
. (variable) $D1A1                      $D1A1            0xd1a1
----------------------------------------
. 000161     STA $7DD2    ; opcode $8d
  --------                              
X (mnemo) STA                           
. (variable) $7DD2                      $7DD2            0x7dd2
----------------------------------------
. 000162     STX $51E3    ; opcode $8e
  --------                              
X (mnemo) STX                           
. (variable) $51E3                      $51E3            0x51e3
----------------------------------------
X 000164 LABEL_10:
  --------                              
----------------------------------------
. 000165     BCC LABEL_10 ; opcode $90
  --------                              
X (mnemo) BCC                           
. (variable) LABEL_10                   LABEL_10         ------
----------------------------------------
. 000166     STA ($3B),Y  ; opcode $91
  --------                              
X (mnemo) STA                           
. (variable) $3B                        $3B              0x003b
----------------------------------------
. 000169     STY $03,X    ; opcode $94
  --------                              
X (mnemo) STY                           
. (variable) $03                        $03              0x0003
. (keyword) ,                           
. (keyword) X                           
----------------------------------------
. 000170     STA $21,X    ; opcode $95
  --------                              
X (mnemo) STA                           
. (variable) $21                        $21              0x0021
. (keyword) ,                           
. (keyword) X                           
----------------------------------------
. 000171     STX $0E,Y    ; opcode $96
  --------                              
X (mnemo) STX                           
. (variable) $0E                        $0E              0x000e
. (keyword) ,                           
. (keyword) Y                           
----------------------------------------
X 000173     TYA          ; opcode $98
  --------                              
X (mnemo) TYA                           
----------------------------------------
. 000174     STA $A2FF,Y  ; opcode $99
  --------                              
X (mnemo) STA                           
. (variable) $A2FF                      $A2FF            0xa2ff
. (keyword) ,                           
. (keyword) Y                           
----------------------------------------
X 000175     TXS          ; opcode $9a
  --------                              
X (mnemo) TXS                           
----------------------------------------
. 000178     STA $0AFB,X  ; opcode $9d
  --------                              
X (mnemo) STA                           
. (variable) $0AFB                      $0AFB            0x0afb
. (keyword) ,                           
. (keyword) X                           
----------------------------------------
X 000181 LABEL_11:
  --------                              
----------------------------------------
. 000182     LDY #$06     ; opcode $a0
  --------                              
X (mnemo) LDY                           
. (variable) $06                        $06              0x0006
----------------------------------------
. 000183     LDA ($0A,X)  ; opcode $a1
  --------                              
X (mnemo) LDA                           
. (variable) $0A                        $0A              0x000a
----------------------------------------
. 000184     LDX #$C6     ; opcode $a2
  --------                              
X (mnemo) LDX                           
. (variable) $C6                        $C6              0x00c6
----------------------------------------
. 000186     LDY $C8      ; opcode $a4
  --------                              
X (mnemo) LDY                           
. (variable) $C8                        $C8              0x00c8
----------------------------------------
. 000187     LDA $90      ; opcode $a5
  --------                              
X (mnemo) LDA                           
. (variable) $90                        $90              0x0090
----------------------------------------
. 000188     LDX $CE      ; opcode $a6
  --------                              
X (mnemo) LDX                           
. (variable) $CE                        $CE              0x00ce
----------------------------------------
X 000190     TAY          ; opcode $a8
  --------                              
X (mnemo) TAY                           
----------------------------------------
. 000191     LDA #$33     ; opcode $a9
  --------                              
X (mnemo) LDA                           
. (variable) $33                        $33              0x0033
----------------------------------------
X 000192     TAX          ; opcode $aa
  --------                              
X (mnemo) TAX                           
----------------------------------------
. 000194     LDY $DD3D    ; opcode $ac
  --------                              
X (mnemo) LDY                           
. (variable) $DD3D                      $DD3D            0xdd3d
----------------------------------------
. 000195     LDA $CD98    ; opcode $ad
  --------                              
X (mnemo) LDA                           
. (variable) $CD98                      $CD98            0xcd98
----------------------------------------
. 000196     LDX $E51D    ; opcode $ae
  --------                              
X (mnemo) LDX                           
. (variable) $E51D                      $E51D            0xe51d
----------------------------------------
X 000198 LABEL_12:
  --------                              
----------------------------------------
. 000199     BCS LABEL_12 ; opcode $b0
  --------                              
X (mnemo) BCS                           
. (variable) LABEL_12                   LABEL_12         ------
----------------------------------------
. 000200     LDA ($F3),Y  ; opcode $b1
  --------                              
X (mnemo) LDA                           
. (variable) $F3                        $F3              0x00f3
----------------------------------------
. 000203     LDY $E0,X    ; opcode $b4
  --------                              
X (mnemo) LDY                           
. (variable) $E0                        $E0              0x00e0
. (keyword) ,                           
. (keyword) X                           
----------------------------------------
. 000204     LDA $F7,X    ; opcode $b5
  --------                              
X (mnemo) LDA                           
. (variable) $F7                        $F7              0x00f7
. (keyword) ,                           
. (keyword) X                           
----------------------------------------
. 000205     LDX $F1,Y    ; opcode $b6
  --------                              
X (mnemo) LDX                           
. (variable) $F1                        $F1              0x00f1
. (keyword) ,                           
. (keyword) Y                           
----------------------------------------
X 000207     CLV          ; opcode $b8
  --------                              
X (mnemo) CLV                           
----------------------------------------
. 000208     LDA $CEAA,Y  ; opcode $b9
  --------                              
X (mnemo) LDA                           
. (variable) $CEAA                      $CEAA            0xceaa
. (keyword) ,                           
. (keyword) Y                           
----------------------------------------
X 000209     TSX          ; opcode $ba
  --------                              
X (mnemo) TSX                           
----------------------------------------
. 000211     LDY $6EE1,X  ; opcode $bc
  --------                              
X (mnemo) LDY                           
. (variable) $6EE1                      $6EE1            0x6ee1
. (keyword) ,                           
. (keyword) X                           
----------------------------------------
. 000212     LDA $095C,X  ; opcode $bd
  --------                              
X (mnemo) LDA                           
. (variable) $095C                      $095C            0x095c
. (keyword) ,                           
. (keyword) X                           
----------------------------------------
. 000213     LDX $98EB,Y  ; opcode $be
  --------                              
X (mnemo) LDX                           
. (variable) $98EB                      $98EB            0x98eb
. (keyword) ,                           
. (keyword) Y                           
----------------------------------------
X 000215 LABEL_13:
  --------                              
----------------------------------------
. 000216     CPY #$DE     ; opcode $c0
  --------                              
X (mnemo) CPY                           
. (variable) $DE                        $DE              0x00de
----------------------------------------
. 000217     CMP ($45,X)  ; opcode $c1
  --------                              
X (mnemo) CMP                           
. (variable) $45                        $45              0x0045
----------------------------------------
. 000220     CPY $71      ; opcode $c4
  --------                              
X (mnemo) CPY                           
. (variable) $71                        $71              0x0071
----------------------------------------
. 000221     CMP $E3      ; opcode $c5
  --------                              
X (mnemo) CMP                           
. (variable) $E3                        $E3              0x00e3
----------------------------------------
. 000222     DEC $B5      ; opcode $c6
  --------                              
X (mnemo) DEC                           
. (variable) $B5                        $B5              0x00b5
----------------------------------------
X 000224     INY          ; opcode $c8
  --------                              
X (mnemo) INY                           
----------------------------------------
. 000225     CMP #$74     ; opcode $c9
  --------                              
X (mnemo) CMP                           
. (variable) $74                        $74              0x0074
----------------------------------------
X 000226     DEX          ; opcode $ca
  --------                              
X (mnemo) DEX                           
----------------------------------------
. 000228     CPY $0E77    ; opcode $cc
  --------                              
X (mnemo) CPY                           
. (variable) $0E77                      $0E77            0x0e77
----------------------------------------
. 000229     CMP $C1FF    ; opcode $cd
  --------                              
X (mnemo) CMP                           
. (variable) $C1FF                      $C1FF            0xc1ff
----------------------------------------
. 000230     DEC $12DD    ; opcode $ce
  --------                              
X (mnemo) DEC                           
. (variable) $12DD                      $12DD            0x12dd
----------------------------------------
X 000232 LABEL_14:
  --------                              
----------------------------------------
. 000233     BNE LABEL_14 ; opcode $d0
  --------                              
X (mnemo) BNE                           
. (variable) LABEL_14                   LABEL_14         ------
----------------------------------------
. 000234     CMP ($CA),Y  ; opcode $d1
  --------                              
X (mnemo) CMP                           
. (variable) $CA                        $CA              0x00ca
----------------------------------------
. 000238     CMP $41,X    ; opcode $d5
  --------                              
X (mnemo) CMP                           
. (variable) $41                        $41              0x0041
. (keyword) ,                           
. (keyword) X                           
----------------------------------------
. 000239     DEC $81,X    ; opcode $d6
  --------                              
X (mnemo) DEC                           
. (variable) $81                        $81              0x0081
. (keyword) ,                           
. (keyword) X                           
----------------------------------------
X 000241     CLD          ; opcode $d8
  --------                              
X (mnemo) CLD                           
----------------------------------------
. 000242     CMP $7063,Y  ; opcode $d9
  --------                              
X (mnemo) CMP                           
. (variable) $7063                      $7063            0x7063
. (keyword) ,                           
. (keyword) Y                           
----------------------------------------
. 000246     CMP $999A,X  ; opcode $dd
  --------                              
X (mnemo) CMP                           
. (variable) $999A                      $999A            0x999a
. (keyword) ,                           
. (keyword) X                           
----------------------------------------
. 000247     DEC $55D2,X  ; opcode $de
  --------                              
X (mnemo) DEC                           
. (variable) $55D2                      $55D2            0x55d2
. (keyword) ,                           
. (keyword) X                           
----------------------------------------
X 000249 LABEL_15:
  --------                              
----------------------------------------
. 000250     CPX #$E5     ; opcode $e0
  --------                              
X (mnemo) CPX                           
. (variable) $E5                        $E5              0x00e5
----------------------------------------
. 000251     SBC ($FD,X)  ; opcode $e1
  --------                              
X (mnemo) SBC                           
. (variable) $FD                        $FD              0x00fd
----------------------------------------
. 000254     CPX $C9      ; opcode $e4
  --------                              
X (mnemo) CPX                           
. (variable) $C9                        $C9              0x00c9
----------------------------------------
. 000255     SBC $70      ; opcode $e5
  --------                              
X (mnemo) SBC                           
. (variable) $70                        $70              0x0070
----------------------------------------
. 000256     INC $83      ; opcode $e6
  --------                              
X (mnemo) INC                           
. (variable) $83                        $83              0x0083
----------------------------------------
X 000258     INX          ; opcode $e8
  --------                              
X (mnemo) INX                           
----------------------------------------
. 000259     SBC #$C8     ; opcode $e9
  --------                              
X (mnemo) SBC                           
. (variable) $C8                        $C8              0x00c8
----------------------------------------
X 000260     NOP          ; opcode $ea
  --------                              
X (mnemo) NOP                           
----------------------------------------
. 000262     CPX $2EF5    ; opcode $ec
  --------                              
X (mnemo) CPX                           
. (variable) $2EF5                      $2EF5            0x2ef5
----------------------------------------
. 000263     SBC $56CE    ; opcode $ed
  --------                              
X (mnemo) SBC                           
. (variable) $56CE                      $56CE            0x56ce
----------------------------------------
. 000264     INC $CF16    ; opcode $ee
  --------                              
X (mnemo) INC                           
. (variable) $CF16                      $CF16            0xcf16
----------------------------------------
X 000266 LABEL_16:
  --------                              
----------------------------------------
. 000267     BEQ LABEL_16 ; opcode $f0
  --------                              
X (mnemo) BEQ                           
. (variable) LABEL_16                   LABEL_16         ------
----------------------------------------
. 000268     SBC ($6E),Y  ; opcode $f1
  --------                              
X (mnemo) SBC                           
. (variable) $6E                        $6E              0x006e
----------------------------------------
. 000272     SBC $DD,X    ; opcode $f5
  --------                              
X (mnemo) SBC                           
. (variable) $DD                        $DD              0x00dd
. (keyword) ,                           
. (keyword) X                           
----------------------------------------
. 000273     INC $B7,X    ; opcode $f6
  --------                              
X (mnemo) INC                           
. (variable) $B7                        $B7              0x00b7
. (keyword) ,                           
. (keyword) X                           
----------------------------------------
X 000275     SED          ; opcode $f8
  --------                              
X (mnemo) SED                           
----------------------------------------
. 000276     SBC $8429,Y  ; opcode $f9
  --------                              
X (mnemo) SBC                           
. (variable) $8429                      $8429            0x8429
. (keyword) ,                           
. (keyword) Y                           
----------------------------------------
. 000280     SBC $2BE1,X  ; opcode $fd
  --------                              
X (mnemo) SBC                           
. (variable) $2BE1                      $2BE1            0x2be1
. (keyword) ,                           
. (keyword) X                           
----------------------------------------
. 000281     INC $B023,X  ; opcode $fe
  --------                              
X (mnemo) INC                           
. (variable) $B023                      $B023            0xb023
. (keyword) ,                           
. (keyword) X                           
----------------------------------------
