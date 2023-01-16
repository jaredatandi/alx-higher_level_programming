#!/bin/bash
# Script that takes URL, sends a request, and displays the size of the body
url=$1
response=$(curl -s -o /dev/null -w "%{http_code}" $url)

# Check for the code
if [ $response -eq 200 ]; then
	# show the body
	curl -s $url
else
	# Display error message if status code is not 200
	echo "Error: Response status code is $response"
fi
