#!/bin/bash
# Write a Bash script that takes in a URL, sends a request to that URL
curl -sI "$1" | grep -i Content-Length | sed 's/[^0-9]*//g'
