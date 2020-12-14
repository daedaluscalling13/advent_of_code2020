# AOC 2020
# Day 4.1
# Author: Kevin Kibler

def is_valid(pass_arr):
    valid_array = list()

    for passport in pass_arr:
        if passport.is_valid():
            valid_array.append(True)
        else:
            valid_array.append(False)

    return valid_array