#!/bin/bash

find . -type f -name "*jpg"|for file;do  
var=shasum $"file"|awk -v mavar="$file" '{print mavar" :" $0}' 
echo "${var}" >> empreintes.txt
done 











