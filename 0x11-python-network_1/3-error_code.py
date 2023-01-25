#!/usr/bin/python3
""" Modulde to print error"""
import urllib.request
import sys


url = sys.argv[1]

try:
    with urllib.request.urlopen(url) as response:
        data = response.read()
        print(data.decode('utf-8'))
except urllib.error.HTTPError as err:
    print("Error code: ", err.code)
