#!/usr/bin/python3

def search_replace(my_list, search, replace):
    if (len(my_list) == 0):
        return ([])
    new_list = my_list[:]
    for i in range(len(my_list)):
        if (my_list[i] == search):
            new_list[i] = replace
    return (new_list)
