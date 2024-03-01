#!/bin/bash
# Write a Bash script that sends a request to a URL passed

curl -so /dev/null -w "%{http_code}" "$1"
