#!/bin/sh
echo $SHELL $0 "launched by" $USER $(date)

export PATH=$PATH:/media/pfeuh/70b90f4a-e5a6-4a83-bf19-1feffc44cab0/PROGS

atasm test_opcodes_atasm.asm -oTEST_OPCODES_ATASM.BIN
atasm test_opcodes_atasm.asm -oTEST_OPCODES_ATASM107.BIN
atasm test_jmp_indirect_atasm.asm -oTEST_JMP_INDIRECT_ATASM.BIN
cl65 -O -t atari test_opcodes_cc65.asm -o TEST_OPCODES_CC65.BIN

errnum=$?
if test $errnum -eq 0;then
echo COMPILATION SUCCESSFUL!
else
echo COMPILATION FAILED
fi
