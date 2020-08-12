#!/usr/bin/python
# -*- coding: utf-8 -*-

import sys
import os
import preATasm as pco

write = pco.write
writeln = pco.writeln
LINE = pco.SOURCE_LINE
getLabel = pco.getLabel
removeComment = pco.removeComment
extractWord = pco.extractWord
commentLine = pco.commentLine
labelIsOk = pco.labelIsOk

def getGlyphe(car):
    value = ord(car)
    if value < 32:
        return '.'
    elif value < 128:
        return chr(value)
    else:
        return '.'

def compareStrings(s1, s2):
    for index in range(max((len(s1), len(s2)))):
        word1 = "  "
        word2 = " "
        word3 = "  "
        word4 = " "
        pointer = ""
        
        if index < len(s1):
            car = s1[index]
            word1 = "%02x"%ord(car)
            word2 = "%c"%getGlyphe(car)
        if index < len(s2):
            car = s2[index]
            word3 = "%02x"%ord(car)
            word4 = "%c"%getGlyphe(car)
        if word1 != word3:
            pointer = "<--"
        writeln("%s '%s' - '%s' %s %s"%(word1, word2, word4, word3, pointer))
            

if __name__ == "__main__":

    assert labelIsOk("label")
    assert labelIsOk("_label")
    assert not labelIsOk("_")
    assert labelIsOk("_1")
    assert not labelIsOk("1234")
    assert not labelIsOk("1")
    assert labelIsOk("a1")
    assert not labelIsOk("1a")
    assert not labelIsOk("azerty;")
    assert not labelIsOk(";azerty")
    assert not labelIsOk("aze;rty")
    assert not labelIsOk("az erty;")
    assert labelIsOk("azerty")



    assert removeComment("   ; azerty") == ""
    assert removeComment("toto; azerty") == "toto"
    assert removeComment(" toto ; azerty") == " toto"
    assert removeComment(" toto     ; azerty") == " toto"
    assert removeComment(" ; ;toto ; azerty") == ""
    assert removeComment(" ; toto ; azerty") == ""
    assert removeComment('toto .string "azerty";"azerty"') == 'toto .string "azerty"'
    assert removeComment('toto .string "aze;rty";"azerty"') == 'toto .string "aze;rty"'
    # TODO: a test with '/"'  or ';' in a string... don't know how to do now

    line = LINE("noname", "", 123)    

    line.setText("toto")    
    assert getLabel(line) == "toto"
    
    line.setText(";toto")    
    assert getLabel(line) == None
    
    line.setText(" toto")    
    assert getLabel(line) == None;
    
    line.setText(" toto;")    
    assert getLabel(line) == None
    
    line.setText("toto   ;")    
    assert getLabel(line) == "toto"

    line.setText("toto blablabla...  ;")    
    assert getLabel(line) == "toto"

    line.setText(";toto titi tata ; comment")    
    assert getLabel(line) == None

    line.setText("     ;toto titi tata ; comment")    
    assert getLabel(line) == None


    
    text = "label op1 op2 op3" 
    assert extractWord(text, 0) == "label"
    assert extractWord(text, 1) == "op1"
    assert extractWord(text, 2) == "op2"
    assert extractWord(text, 3) == "op3"
    
    text = " label op1 op2 op3" 
    assert extractWord(text, 1) == "label"
    assert extractWord(text, 2) == "op1"
    
    text = ";label op1 op2 op3" 
    assert extractWord(text, 1) == None
    assert extractWord(text, 2) == None
    
    text = "  ;    label op1 op2 op3" 
    assert extractWord(text, 1) == None
    assert extractWord(text, 2) == None
    
    text = "   label;op1 op2 op3" 
    assert extractWord(text, 0) == None
    assert extractWord(text, 1) == "label"
    assert extractWord(text, 2) == None
    
    text = "   label   ;   op1 op2 op3" 
    assert extractWord(text, 0) == None
    assert extractWord(text, 1) == "label"
    assert extractWord(text, 2) == None
    
    text = "   label     op1  ;  op2 op3" 
    assert extractWord(text, 0) == None
    assert extractWord(text, 1) == "label"
    assert extractWord(text, 2) == "op1"
    assert extractWord(text, 3) == None
    
    text = ";toto titi tata ; comment"
    assert commentLine(text) == ";toto titi tata ; comment"

    text = "    ;toto titi tata ; comment"
    assert commentLine(text) == ";    ;toto titi tata ; comment"

    text = "     toto titi tata ; comment"
    assert commentLine(text) == ";     toto titi tata ; comment"




    
    writeln("A L L   T E S T S   P A S S E D !")
