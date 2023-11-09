#!/usr/bin/python3

def complex_delete(a_dictionary, value):
    deleted = [key for key, val in a_dictionary.items() if val == value]
    for key in deleted:
        a_dictionary.pop(key)
    return (a_dictionary)
