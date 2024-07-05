#!/usr/bin/python3
"""
This module fetches the status from a given URL using the 'requests' package.
It displays the type and content of the response body as specified.
"""

import requests

def fetch_status(url):
    """
    Fetches the status from the provided URL and prints the type and content of the response body.
    """
    response = requests.get(url)
    print("Body response:")
    print(f"\t- type: {type(response.text)}")
    print(f"\t- content: {response.text}")

if __name__ == "__main__":
    fetch_status("https://alx-intranet.hbtn.io/status")
