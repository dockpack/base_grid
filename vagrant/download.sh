#!/bin/sh
for box in `cat boxes.txt`
do
    curl -O $box
done
