#!/bin/bash
# Script that takes URL, sends a request, and displays the http methods the server will accept 
curl -sI "$1" | grep "Allow: " | sed 's/Allow: //'
