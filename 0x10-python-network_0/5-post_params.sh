#!/bin/bash
# this script shows the body response send a request POST method with 2 variables
curl -s "$1" -X POST -d "email=hr@holbertonschool.com" -d "subject=I will always be here for PLD"
