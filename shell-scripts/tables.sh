#!/bin/bash

a=2

for i in `seq 20`
do
  echo $a*$i=$(($a*$i))	
done  
