#!/bin/bash
#this will be good
curl -I -s -o /dev/null -w "%{http_code}" "$1"
