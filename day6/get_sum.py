# AOC 2020
# Day 6.1
# Author: Kevin Kibler

def get_sum(count_arr):
    count_sum = 0

    for group in count_arr:
        count_sum += len(group)

    return count_sum