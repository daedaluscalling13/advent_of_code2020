# AOC 2020
# Day 1.1
# Author: Kevin Kibler

def find_pairs(input_array):
    l = 0
    r = len(input_array) - 1

    pair_list = list()

    while l < r:
        if (input_array[l] + input_array[r]) == 2020:
            pair_list.append([input_array[l], input_array[r]])
            r -= 1
            l += 1
        elif (input_array[l] + input_array[r]) > 2020:
            r -= 1
        else:
            l += 1

    return pair_list
            