#!/bin/bash
# Sends a GET request with the Holberton user id header and displays the body
curl -sH "X-HolbertonSchool-User-Id: 98" "$1"
