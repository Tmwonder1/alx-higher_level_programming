# Project 0x10. Python - Network #0

## Description

This project is part of the Holberton School curriculum for backend software development. It focuses on networking concepts using Python, specifically on how to interact with web services and manipulate data from these services. The project includes scripts that demonstrate HTTP requests, response parsing, and other basic networking tasks using Python libraries.

## Learning Objectives

- How to fetch internet resources with the Python package `urllib`
- How to decode `urllib` body response
- How to use the Python package `requests` #requestsAreWayEasierThanUrllib
- How to make HTTP `GET` request
- How to make HTTP `POST`/`PUT`/etc. request
- How to fetch JSON resources
- How to manipulate data from an external service

## Requirements

- All your files will be interpreted/compiled on Ubuntu 20.04 LTS using `python3` (version 3.8.5)
- All your files should end with a new line
- The first line of all your Python files should be exactly `#!/usr/bin/python3`
- A `README.md` file, at the root of the folder of the project, is mandatory
- Your code should use the `pycodestyle` (version 2.8.*)
- All your files must be executable
- The length of your files will be tested using `wc`

## Tasks

### 0. What's my status? #0

Write a Python script that fetches `https://intranet.hbtn.io/status`

- You must use the package `urllib`
- You are not allowed to import any packages other than `urllib`
- The body of the response must be displayed like the following example (tabulation before `-`)
- You must use a `with` statement

### 1. Response header value #0

Write a Python script that takes in a URL, sends a request to the URL, and displays the value of the `X-Request-Id` variable found in the header of the response.

- You must use `urllib`
- You must not use any other packages other than `urllib`
- The value of this variable is different for each request
- You must use a `with` statement

### [Additional tasks as needed]

## Author

[Your Name]
