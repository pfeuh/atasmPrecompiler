#!/bin/sh
echo $SHELL $0 "launched by" $USER $(date)
cd ./

#~ cl65 -O -t atari test.asm -o TEST.BIN
/media/pfeuh/70b90f4a-e5a6-4a83-bf19-1feffc44cab0/PROGS/atasm106.exe -s test_opcodes_atasm.asm -oTEST_OPCODES_ATASM.BIN

errnum=$?
if test $errnum -eq 0;then
#~ ./vosc6502.exe
echo COMPILATION SUCCESSFUL!
else
echo COMPILATION FAILED
fi
