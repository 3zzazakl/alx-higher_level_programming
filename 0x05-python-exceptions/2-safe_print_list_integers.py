#!/usr/bin/python3

def safe_print_list_integers(my_list=[], x=0):
    count = 0 
    n = 0
    while (count < x):
        try:
            print("{}".format(my_list[count]), end="")
        except (ValueError, TypeError):
            print(end="")
            n += 1
        else:
            print(end="")
        count += 1
    print("")
    return (count - n)
