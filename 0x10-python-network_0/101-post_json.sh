#!/bin/bash
# Script that takes URL, sends a request
curl -sX POST -H "Content-type: application/json" -H "Accept: application/json" -d "@$2" "$1"
