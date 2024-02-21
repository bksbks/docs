#/bin/bash

read -p "Enter your service name: " service
echo "============Checking the $service status=========="
if [ -z $service ];
then
  echo "Enter teh correct service name"
else
   service $service status
fi  
