#!/bin/bash
#this  script will send request to the server and retrieve  
curl -s -sI "$1" | grep -i 'Content-length'|awk '{print $2}'
