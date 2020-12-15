# AOC 2020
# Day 5.1
# Author: Kevin Kibler

from boarding_pass import BoardingPass

def make_passes(input_arr):
    pass_arr = list()
    for entry in input_arr:
        pass_arr.append(BoardingPass(entry))

    return pass_arr