#!/bin/bash

echo What is your age?
read age


if [ $age -ge 18 ]
then
      echo You can vote
else
      echo You cannot vote!
fi     
