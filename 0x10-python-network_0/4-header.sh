#!/bin/bash
#script that takes in a URL as an argument, sends a GET request
curl -H "X-HolbertonSchool-User-Id:98" -s"$1"
