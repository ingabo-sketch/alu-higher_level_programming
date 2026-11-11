#!/bin/bash
# Sends a GET request with the School user id header and displays the body
curl -sH "X-School-User-Id: 98" -H "X-HolbertonSchool-User-Id: 98" "$1"
