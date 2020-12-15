# AOC 2020
# Day 5.1
# Author: Kevin Kibler

def get_input(input_name_string):

    input_arr = list()

    with open(input_name_string, "r+") as input_file:

        for line in input_file:
            line = line.strip('\n')
            input_arr.append(line)

    return input_arr