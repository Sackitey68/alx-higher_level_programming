#!/usr/bin/python3
"""
The program accepts a URL and sends a request to the URL then shows
the value of the X-Request-Id variable found in the header of the response
"""
if __name__ == "__main__":
    import urllib.request as request
    from sys import argv
    req = request.Request(argv[1])
    with request.urlopen(req) as r:
        print(r.headers.get('X-Request-Id'))
