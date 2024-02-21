#!/bin/bash
echo "delete files older than 7 days"
path=$1
echo "$path"
find . $path -mtime +7 -delete
if[ $? -eq 0 ];
then
 echo "Deleted the files older than 7 days"
else
 echo "Deletion is having some issue"      
fi 
