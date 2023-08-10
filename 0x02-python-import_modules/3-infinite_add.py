#!/usr/bin/python3
from sys import argv

if __name__ == "__main__":
    i = 1
    res = 0
    args = len(argv) - 1

    if(args != 0):
        while(i <= args):
            res += int(argv[i])
            i += 1
            print(res)