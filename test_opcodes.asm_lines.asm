000011    
000012    BRK 
000013    ORA $A7 
000017    ORA $6C 
000018    ASL $C1 
000020    PHP 
000021    ORA $F5 
000022    ASL 
000025    ORA $87A6 
000026    ASL $467E 
000028    
000029    BPL LABEL_02 
000030    ORA $52 
000034    ORA $07 , X 
000035    ASL $4D , X 
000037    CLC 
000038    ORA $E97E , Y 
000042    ORA $50F5 , X 
000043    ASL $241E , X 
000045    
000046    JSR $B1DA 
000047    AND $96 
000050    BIT $D0 
000051    AND $D1 
000052    ROL $D8 
000054    PLP 
000055    AND $79 
000056    ROL 
000058    BIT $BC10 
000059    AND $97CD 
000060    ROL $1678 
000062    
000063    BMI LABEL_04 
000064    AND $66 
000068    AND $72 , X 
000069    ROL $FB , X 
000071    SEC 
000072    AND $9FBA , Y 
000076    ORA $64AB , X 
000077    ASL $5D20 , X 
000079    
000080    RTI 
000081    EOR $28 
000085    EOR $D7 
000086    LSR $15 
000088    PHA 
000089    EOR $A5 
000090    LSR 
000092    JMP $F3FE 
000093    EOR $6571 
000094    LSR $286C 
000096    
000097    BVC LABEL_06 
000098    EOR $B2 
000102    EOR $0C , X 
000103    LSR $A4 , X 
000105    CLI 
000106    EOR $2BB7 , Y 
000110    EOR $CD9D , X 
000111    LSR $40B3 , X 
000113    
000114    RTS 
000115    ADC $5E 
000119    ADC $59 
000120    ROR $A2 
000122    PLA 
000123    ADC $48 
000124    ROR 
000126    JMP $E120 
000127    ADC $5334 
000128    ROR $3D76 
000130    
000131    BCS LABEL_08 
000132    ADC $DD 
000136    ADC $73 , X 
000137    ROR $A3 , X 
000139    SEI 
000140    ADC $4001 , Y 
000144    ADC $6168 , X 
000145    ROR $50E3 , X 
000147    
000149    STA $07 
000152    STY $C1 
000153    STA $3C 
000154    STX $82 
000156    DEY 
000158    TXA 
000160    STY $D1A1 
000161    STA $7DD2 
000162    STX $51E3 
000164    
000165    BCC LABEL_10 
000166    STA $3B 
000169    STY $03 , X 
000170    STA $21 , X 
000171    STX $0E , Y 
000173    TYA 
000174    STA $A2FF , Y 
000175    TXS 
000178    STA $0AFB , X 
000181    
000182    LDY $06 
000183    LDA $0A 
000184    LDX $C6 
000186    LDY $C8 
000187    LDA $90 
000188    LDX $CE 
000190    TAY 
000191    LDA $33 
000192    TAX 
000194    LDY $DD3D 
000195    LDA $CD98 
000196    LDX $E51D 
000198    
000199    BCS LABEL_12 
000200    LDA $F3 
000203    LDY $E0 , X 
000204    LDA $F7 , X 
000205    LDX $F1 , Y 
000207    CLV 
000208    LDA $CEAA , Y 
000209    TSX 
000211    LDY $6EE1 , X 
000212    LDA $095C , X 
000213    LDX $98EB , Y 
000215    
000216    CPY $DE 
000217    CMP $45 
000220    CPY $71 
000221    CMP $E3 
000222    DEC $B5 
000224    INY 
000225    CMP $74 
000226    DEX 
000228    CPY $0E77 
000229    CMP $C1FF 
000230    DEC $12DD 
000232    
000233    BNE LABEL_14 
000234    CMP $CA 
000238    CMP $41 , X 
000239    DEC $81 , X 
000241    CLD 
000242    CMP $7063 , Y 
000246    CMP $999A , X 
000247    DEC $55D2 , X 
000249    
000250    CPX $E5 
000251    SBC $FD 
000254    CPX $C9 
000255    SBC $70 
000256    INC $83 
000258    INX 
000259    SBC $C8 
000260    NOP 
000262    CPX $2EF5 
000263    SBC $56CE 
000264    INC $CF16 
000266    
000267    BEQ LABEL_16 
000268    SBC $6E 
000272    SBC $DD , X 
000273    INC $B7 , X 
000275    SED 
000276    SBC $8429 , Y 
000280    SBC $2BE1 , X 
000281    INC $B023 , X 
