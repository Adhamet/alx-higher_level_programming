#!/usr/bin/python3
"""
Script takes in URL, sends a request to URL and displays
value of X-Request-Id variable found in the header of the response

Usage: ./1-hbtn_header.py <URL>
"""
from sys import argv
from urllib.request import Request, urlopen


if __name__ == "__main__":
    url = argv[1]
    req = Request(url)

    with urlopen(req) as response:
        print(dict(response.headers).get("X-Request-Id"))
