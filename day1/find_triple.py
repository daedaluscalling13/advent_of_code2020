# AOC 2020
# Day 1.1
# Author: Kevin Kibler

def find_triple(input_array):
    l = 0
    c = len(input_array) - 2
    r = len(input_array) - 1

    triple_list = list()

    for l in range(len(input_array)):
        for c in range(1, len(input_array)):
            for r in range(2, len(input_array)):
                if (input_array[l] + input_array[c] + input_array[r]) == 2020:
                    triple_list.append([input_array[l], input_array[c], input_array[r]])

    return triple_list
            