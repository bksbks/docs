#!/bin/bash
if [ $EUID -eq 0 ]
then
  echo 'You are not a root user'
else
  echo 'you are a root user'
fi  

