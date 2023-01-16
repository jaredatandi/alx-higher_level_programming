#!/bin/bash
# Script that takes URL, sends a request, and displays the http methods the server will accept 
curl -sX GET -H "X-School-User-Id: 98" "$1"
