#!/bin/bash
# this script send a delete request and shows the response
curl -sI "$1" | grep Allow: | cut -d ":" -f2 | cut -b 2- 
