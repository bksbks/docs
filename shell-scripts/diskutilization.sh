#!/bin/bash

echo "checking the diskspace"
disk_space=`df -h | grep /dev/sda6 | awk '{print $5}'|cut -d '%' -f 1`
if [ $disk_space -ge 80 ];
then
 echo "Disk space is morethan 80%, please expand disk or delete log files"	
else
  echo "Disk is having enough avaliable space"
  df -h | grep /dev/sda6 | awk '{print $5}'
fi  
