#!/usr/bin/python3
import hidden_4


def discovery():
    n = dir(hidden_4)
    for i in n:
        if i[:2] != '__':
            print("{:s}".format(i))

if __name__ == "__main__":
    discovery()