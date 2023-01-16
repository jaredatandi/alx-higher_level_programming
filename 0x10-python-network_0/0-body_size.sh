#!/bin/bash
# Script that takes URL, sends a request, and displays the size of the body
curl -sI "$1" | grep "Content-Length" | cut -d ' ' -f 2
