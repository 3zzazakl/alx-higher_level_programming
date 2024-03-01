#!/bin/bash
# Write a Bash script that makes a request to 0.0.0.0:5000/catch_me that causes

curl -sLX PUT -Ld "user_id=98" -H "Origin: HolbertonSchool" -H "user-agent: HolbertonSchool" 0.0.0.0:5000/catch_me
