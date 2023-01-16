#!/bin/bash
# Script that takes URL, sends a request, and displays the http methods the server will accept 
curl -sd "email=test@gmail.com&subject=I%20will%20always%20be%20here%20for%20PLD" "$1"
