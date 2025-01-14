#!/bin/bash

echo "Please enter the number"
read num
a=1

while [ $a -le $num ]
do
    echo $a
   a=`expr $a + 1`
done    
