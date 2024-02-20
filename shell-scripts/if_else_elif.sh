#!/bin/bash

if [ "$(whoami)" == "barkath" ];
then
 
  echo "Installing nginx"
  sudo apt-get install nginx

elif [ "$(whoami)" == "srini" ];
then

   echo "installing httpd"
   sudo apt-get install httpd
else

   echo "Not anstalling anything" 
fi   
