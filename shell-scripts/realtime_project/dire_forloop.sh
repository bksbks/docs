#!/bin/bash

for folder in $(find -type d);
do
    echo "the folder is $fodler"
    if [ -d test ];
    then
     
         echo "this folder exist"
         rm -rf test
    else
         echo "folder doesn't exist"	   
    fi
done
