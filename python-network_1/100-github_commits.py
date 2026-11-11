#!/usr/bin/python3
"""Lists the ten most recent commits of a GitHub repository."""
import sys
import requests

if __name__ == "__main__":
    repo = sys.argv[1]
    owner = sys.argv[2]
    url = "https://api.github.com/repos/{}/{}/commits".format(owner, repo)
    response = requests.get(url, params={"per_page": 10})
    commits = response.json()
    for commit in commits:
        sha = commit.get("sha")
        commit_info = commit.get("commit")
        author = commit_info.get("author")
        print("{}: {}".format(sha, author.get("name")))
