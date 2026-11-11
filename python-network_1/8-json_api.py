#!/usr/bin/python3
"""Sends a letter to the search route and prints the matching user."""
import sys
import requests

if __name__ == "__main__":
    letter = "" if len(sys.argv) == 1 else sys.argv[1]
    payload = {"q": letter}
    url = "http://0.0.0.0:5000/search_user"
    response = requests.post(url, data=payload)
    try:
        data = response.json()
        if data:
            print("[{}] {}".format(data.get("id"), data.get("name")))
        else:
            print("No result")
    except ValueError:
        print("Not a valid JSON")
