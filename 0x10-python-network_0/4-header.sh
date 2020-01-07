#!/bin/bash
# this script shows the body response send a request GET method with header variable
curl -s "$1" -H "X-HolbertonSchool-User-Id: 98"
