# AOC 2020
# Day 4.1
# Author: Kevin Kibler

def get_valid_num(valid_arr):
    count = 0

    for b in valid_arr:
        if b:
            count += 1

    return count