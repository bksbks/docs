#!/bin/bash

user=$(whoami)
if [ "$user" = "barkath" ];
then
 
  echo "create repo"
  mkdir test100

elif [ "$user" = "sudo" ];
then

   echo "update repo"
   sudo apt update
else

   echo "No change " 
fi   
