#!/bin/sh
for box in `cat 7-boxes.txt`
do
    curl -O $box
done
