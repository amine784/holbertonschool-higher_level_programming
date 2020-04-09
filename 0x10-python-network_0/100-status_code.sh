#!/bin/bash
# Bash script that sends a request to a URL passed as
curl -o /dev/null -w "%{http_code}" -s "$1"
