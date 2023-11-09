#!/usr/bin/python3

def weight_average(my_list=[]):
    if not my_list:
        return (0)

    x, y = 0, 0
    for score, weight in my_list:
        x += score * weight
        y += weight

    return (x / y)
