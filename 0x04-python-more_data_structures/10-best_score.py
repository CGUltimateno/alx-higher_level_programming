#!/usr/bin/python3
def best_score(a_dictionary):
    if a_dictionary is None or a_dictionary == {}:
        return None
    big = max(a_dictionary.values())
    for result, value in a_dictionary.items():
        if value is big:
            return result