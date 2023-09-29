#!/bin/bash
# Script that sends a DELETE request to the URL passed as the first argument 
# and shows the body of the response
curl -sX DELETE "$1"
