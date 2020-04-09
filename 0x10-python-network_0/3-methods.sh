#!/bin/bash
# script bash to display method
curl -I -s "$1" | grep Allow | cut -d -f2- " "
