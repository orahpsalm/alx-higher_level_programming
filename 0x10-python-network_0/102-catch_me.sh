#!/bin/bash
#Cath a specific message
curl -sL -d "user_id=98" -H "Origin: HolbertonSchool" -X PUT 0.0.0.0:5000/catch_me
