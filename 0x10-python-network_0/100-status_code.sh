#!/bin/bash
# Script that takes URL, sends a request, and displays the http status 
curl -o /dev/null -sw "%{http_code}" "$1"
