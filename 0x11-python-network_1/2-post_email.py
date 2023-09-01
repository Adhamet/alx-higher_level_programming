#!/usr/bin/python3
"""
Script takes in URL and an email, sends a POST request to passed
URL with email as a parameter, displays the body of the response (utf-8)
"""
from sys import argv
from urllib.parse import urlencode
from urllib.request import Request, urlopen


if __name__ == "__main__":
    url = argv[1]
    value = {"email": argv[2]}

    data = urlencode(value).encode('ascii')
    req = Request(url, data)
    with urlopen(req) as response:
        print(response.read().decode())
