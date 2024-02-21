#!/bin/bash

echo "This script gets the first 5 biggest files"
path=$1
echo $path
du -ah $path | sort -hr | head -n 5 > /tmp/files.txt
cat /tmp/files.txt
