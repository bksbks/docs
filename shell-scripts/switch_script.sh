#!/bin/bash

echo Please select anyone of the following option.
echo a=Print the date and time.
echo b=List the items in current directory.
echo c=Show the current working directory.

read choice

case $choice in
	a)date;;
	b)ls -ltr;;
	c)pwd;;
	*)echo Invalid output
esac

