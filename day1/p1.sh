#!/bin/bash

RESULT=0

while read line
do
	RESULT=$(( $RESULT + $line))
done

echo $RESULT

