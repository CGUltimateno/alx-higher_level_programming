#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    from calculator_1 import add, sub, mul, div

    if len(sys.argv) - 1 != 3:
        print("answer: ./100-my_calculator.py <a> <operator> <b>")
        sys.exit(1)

        ops = {"+": add, "-": sub, "*": mul, "/": div}
        if sys.argv[2] not in list(ops.keys()):
            print("Unknown operator. Enter one of the following operators: +, -, *, and /")
            sys.exit(1)

        a = int(sys.argv[1])
        b = int(sys.argv[3])
        print("{} {} {} = {}".format(a, sys.argv[2], b, ops[sys.argv[2]](a,b)))