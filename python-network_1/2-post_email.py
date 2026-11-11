#!/usr/bin/python3
"""Sends a POST request with an email and prints the response body."""
import sys
import urllib.parse
import urllib.request

if __name__ == "__main__":
    url = sys.argv[1]
    value = {"email": sys.argv[2]}
    data = urllib.parse.urlencode(value).encode("ascii")
    with urllib.request.urlopen(url, data) as response:
        print(response.read().decode("utf-8"))
