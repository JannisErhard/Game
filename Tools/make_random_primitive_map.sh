for i in `seq 1 25`;  do for j in `seq 1 25`; do shuf -i 1-4 -n 1 | awk '$1<2{printf "\x27%s\x27, ", "#"}$1>=2{printf "\x27%s\x27, ", " "}'; done  | awk '{printf "[ %s ],\n", $0}';  done
