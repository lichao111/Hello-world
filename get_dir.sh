#!/bin/bash
function get_dir()
{
	ls -R $1 > $2
	echo $1
}

usage="position argument\n the directory that the the path start to query;\nthe output prefix"

if [ -z $1 ]; then
	echo "please input the directory! Now exit!"
	exit
else
	get_dir $1 $2
fi

echo $1
