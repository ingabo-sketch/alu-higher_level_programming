#!/usr/bin/python3
def weight_average(my_list=[]):
    if not my_list:
        return 0
    total = 0
    weight = 0
    for score, item_weight in my_list:
        total += score * item_weight
        weight += item_weight
    if weight == 0:
        return 0
    return total / weight
