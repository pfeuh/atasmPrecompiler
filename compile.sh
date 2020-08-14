#!/bin/sh
echo $SHELL $0 "launched by" $USER $(date)
cd ./

./precompile.py -ifname monitor.asm -ofname precompiled.asm -dfname full_prec.asm -nb_cols 7 -lfname prelabels.txt -Wall 

errnum=$?
if test $errnum -eq 0;then
echo PRECOMPILATION SUCCESSFUL!
else
echo PRECOMPILATION FAILED error $errnum
exit 1
fi

export PATH=$PATH:/media/pfeuh/70b90f4a-e5a6-4a83-bf19-1feffc44cab0/PROGS
#~ echo $PATH
atasm  -r-v -lmonitor.lbl precompiled.asm -omonitor.bin

errnum=$?
if test $errnum -eq 0;then
echo COMPILATION SUCCESSFUL!
fi


