#!/usr/bin/python3
"""Sends a POST request with an email and prints the response body."""
import sys
import requests

if __name__ == "__main__":
    url = sys.argv[1]
    payload = {"email": sys.argv[2]}
    response = requests.post(url, data=payload)
    print(response.text)
