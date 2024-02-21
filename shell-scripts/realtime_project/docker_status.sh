#!/bin/bash
echo "----------Checking docker service status------------"
status="`service docker status|awk 'NR==3 {print}'|cut -d ':' -f 2 |cut -d '(' -f 1`"

if [ $status = "active" ];
then
   echo "Docker is up and running"	
else
    echo "Docker is not running"
    service docker start
fi    
