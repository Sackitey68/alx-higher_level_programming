#!/bin/bash
# Script that accepts a URL and show all HTTP methods the server will accept
curl -sI "$1" | grep -i "Allow" | awk -F ": " '{ print $2 }'
