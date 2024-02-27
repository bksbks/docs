#!/bin/bash


echo "Enter a number..?"
read n
r=`expr $n % 2`
if [ $r -eq 0 ];
then
 echo "Given number is even"
else
 echo "Given number is odd"
fi

