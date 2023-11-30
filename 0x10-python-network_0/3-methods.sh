#!/bin/bash
#this line will do magic
curl -i -sX OPTIONS "$1" | awk '/Allow:/ {print substr($0, index($0, $2))}'
