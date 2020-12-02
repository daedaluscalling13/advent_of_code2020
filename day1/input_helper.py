# AOC 2020
# Day 1.1
# Author: Kevin Kibler

def get_input(file_name):

    input_array = list()

    with open(file_name, "r+") as input_file:

        for line in input_file:
            num = line.strip('\n')
            num = int(num)
            input_array.append(num)

    return input_array