#!/bin/bash
#Print decremental numbers based on user input
#n...8 7 6 5 4 3 2 1
echo "Input number"
read i
while  [ $i -ne 0 ]
do
    echo "$i"
    i="$(( i - 1 ))"
done

