#!/bin/bash

echo Enter a table number ....?
read a
for i in `seq 10`
do
   echo $a*$i=$(($a*$i))
done   
    
