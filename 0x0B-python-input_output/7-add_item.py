#!/usr/bin/python3
"""Module that adds all arguments to a Python list, and then save them to a file"""
from sys import argv
from os.path import exists

save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file

name_file = "add_item.json"
argc = len(argv)

my_list = []

if exists(name_file):
    my_list = load_from_json_file(name_file)

if argc == 1:
    save_to_json_file(my_list, name_file)
else:
    for i in range(1, argc):
        my_list.append(argv[i])
    save_to_json_file(my_list, name_file)
