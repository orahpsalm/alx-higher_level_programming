#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv
    sum_args = 0
    for i, arg in enumerate(argv[1:]):
        sum_args += int(arg)
    print("{:d}".format(sum_args))
