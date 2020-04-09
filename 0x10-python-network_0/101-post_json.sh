#!/bin/bash
# Bash script that sends a JSON POST request to a URL passed
curl -H "content-Type: application/json" -s "$1" -X POST -d @"$2"
