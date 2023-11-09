#!/usr/bin/python3

def complex_delete(a_dictionary, value):
    deleted = [key for key, value in a_dictionary.items() if key == value]
    for key in deleted:
        a_dictionary.pop(key)
    return (a_dictionary)
