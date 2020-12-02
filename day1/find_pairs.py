# AOC 2020
# Day 1.1
# Author: Kevin Kibler

def find_pairs(input_array):
    l = 0
    r = len(input_array) - 1

    pair_list = list()

    while l < r:
        if (l + r) == 2020:
            pair_list.append([l, r])
        elif (l + r) > 2020:
            r -= 1
        else:
            l += 1

    return pair_list
            