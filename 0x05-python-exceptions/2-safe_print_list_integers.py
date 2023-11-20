#!/usr/bin/python3

def safe_print_list_integers(my_list=[], x=0):
    count = 0
    l = 0
    try:
        while True:
            if (l < x):
                try:
                    if isinstance(my_list[l], int):
                        print("{:d}".format(my_list[l]), end="")
                        count += 1
                except (ValueError, TypeError, IndexError):
                    pass
            l += 1
    finally:
        print()
        return (count)
