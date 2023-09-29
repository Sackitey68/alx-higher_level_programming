#!/bin/bash
# Send JSON POST request to a URL passed as the initial argument, and shows the body of the response.
curl -s -H "Content-Type: application/json" -d @"$2" "$1"
