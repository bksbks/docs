#!/bin/bash

num=10
a=0

while [ $a -le $num ]
do
    echo $a
    a=`expr $a + 1`
done    
