#!/bin/bash
# Script that takes URL, sends a request, and displays the http status 
curl -sLX PUT -d "user_id=98" -H "Origin: HolbertonSchool" 0.0.0.0:5000/catch_me 
