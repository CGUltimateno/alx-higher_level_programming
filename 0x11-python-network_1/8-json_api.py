#!/usr/bin/python3
""" a Python script that takes in a letter and
sends a POST request to http://0.0.0.0:5000/search_user
with the letter as a parameter. """
import requests
import sys

if __name__ == '__main__':
    url = 'http://0.0.0.0:5000/search_user'
    try:
        q = sys.argv[1]
    except:
        q = ""
    payload = {'q': q}
    r = requests.post(url, data=payload)
    try:
        json = r.json()
        if json:
            print("[{}] {}".format(json.get('id'), json.get('name')))
        else:
            print("No result")
    except:
        print("Not a valid JSON")
