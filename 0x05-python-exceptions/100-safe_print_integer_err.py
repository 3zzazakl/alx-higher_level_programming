#!/usr/bin/python3
import sys


def safe_print_integer_err(value):
    try:
        print("{}".format(value))
        return (value)
    except (TypeError, ValueError) as e:
        print("Exception {}".format(e), file=sys.stderr)
