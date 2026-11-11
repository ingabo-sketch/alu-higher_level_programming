#!/bin/bash
# Sends a JSON file in a POST request and displays the body of the response
curl -sH "Content-Type: application/json" -d @"$2" "$1"
