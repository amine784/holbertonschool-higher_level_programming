#!/bin/bash
# script bash to display method
curl -sI $1 | grep Allow | cut -d -f2 " "
