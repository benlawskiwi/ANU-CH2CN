#!/bin/sh
./shiftBInt CH2CN-26J4.bin CH2CN-26J4C.bin 1.2 74.55
./ProfileBInt -f CH2CN-26J4C.bin -dA 10 -o j
S=601
./Smooth -f j-000 -o js-000 -np $S > /dev/null 
./Smooth -f j-090 -o js-090 -np $S > /dev/null 
./Smooth -f j-180 -o js-180 -np $S > /dev/null 
./Smooth -f j-270 -o js-270 -np $S > /dev/null 
xmgrace js-000 js-090 js-180 js-270
rm j-???
