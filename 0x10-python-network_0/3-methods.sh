#!/bin/bash
# script bash to display method
curl -s "$1" | grep Allow | cut -d " " -f2-
