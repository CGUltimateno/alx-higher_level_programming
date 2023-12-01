#!/bin/bash
# Bash script that sends a JSON POST request to a URL passed as the first argument, and displays the body of the response.
curl -sx POST -H "Content-type: application/json" -d @2 $1
