# AOC 2020
# Day 3.1
# Author: Kevin Kibler

def tree_count(arr, right, down):
    row = 0
    count = 0

    for col in range(0, len(arr), down):
        if(arr[col][row % len(arr[0])] == '#'):
            count += 1
        
        row += right

    return count
        