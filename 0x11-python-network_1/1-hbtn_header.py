#!/usr/bin/python3
""" Respond with header value"""
import urllib.request
import sys


url = sys.argv[1]

with urllib.request.urlopen(url) as response:
    headers = response.info()
    x_request_id = headers.get("X-Request-Id")
    print("X-Request-Id:", x_request_id)
