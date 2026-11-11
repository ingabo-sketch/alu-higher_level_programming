#!/bin/bash
# Sends a POST request with an email and a subject and displays the body
curl -sX POST -d "email=test@gmail.com&subject=I will always be here for PLD" "$1"
