#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    a = len(sys.argv) - 1
    if a == 0:
        print("0 arguments.")
    elif a == 1:
        print("1 argument:")
    else:
        print("{} arguments:".format(a))
    for x in range(a):
        print("{}: {}".format(x + 1, sys.argv[x + 1]))
