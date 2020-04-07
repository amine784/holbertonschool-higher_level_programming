#!/bin/bash
#Bash script that makes a request to 0.0.0.0:5000/catch_me
curl -s 0.0.0.0:5000/catch_me -H "Origin: HolbertonSchool" -X PUT -Ld "user_id=98"
