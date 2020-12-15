# AOC Day 3
# Day 3.1
# Author: Kevin Kibler
# Description: Input helper

def get_input(input_file_string):

    input_array = list()

    with open(input_file_string, "r+") as input_file:
        for line in input_file:
            input_row = list()
            line = line.strip('\n')
            for char in line:
                input_row.append(char)
        
            input_array.append(input_row)

    return input_array

if __name__ == "__main__":
    arr = get_input("input.txt")
    for line in arr:
        print(line)