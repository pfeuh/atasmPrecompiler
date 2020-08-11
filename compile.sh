#!/bin/sh
echo $SHELL $0 "launched by" $USER $(date)
cd ./

./precompile.py -ifname monitor.asm -ofname precompiled.asm -rom -ram_start 200 -code_start f000 -trace debug.txt

errnum=$?
if test $errnum -eq 0;then
echo PRECOMPILATION SUCCESSFUL!
else
echo PRECOMPILATION FAILED error $errnum
exit 1
fi
atasm  -r-v -llabels.txt precompiled.asm -omonitor.o

errnum=$?
if test $errnum -eq 0;then
echo COMPILATION SUCCESSFUL!
fi
