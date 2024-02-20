#!/bin/bash
echo "Install prometheus"
if [ -e /home/barkath/distros/prometheus.tar.gz ];
then
  echo "Extracting prometheus"
  tar -zxvf /home/barkath/distros/prometheus.tar.gz
else
  echo "Installing and extracting the prometheus"
  wget https://prometheus.tar.gz
  tar -zxvf /home/barkath/distros/prometheus.tar.gz
fi  
