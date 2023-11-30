#!/bin/bash
#this  script will send request to the server and retrieve  
curl -s -sI "$1" | grep 'Content-length'|awk '{print $2}'
