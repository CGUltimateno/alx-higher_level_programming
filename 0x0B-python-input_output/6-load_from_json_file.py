#!/usr/bin/python3
"""Module that creates an Object from a JSON file"""
import json


def load_from_json_file(filename):
    """Read a file and convert the content (JSON) to python types"""
    with open(filename, mode="r", encoding="utf-8") as my_file:
        return json.loads(my_file.read())

