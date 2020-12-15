# AOC 2020
# Day 6.1
# Author: Kevin Kibler

def get_input(input_name_string):
    input_arr = list()

    with open(input_name_string, "r+") as input_file:
        group_arr = list()

        for line in input_file:
            if line == '\n':
                input_arr.append(group_arr)
                group_arr = list()
            else:
                line = line.strip('\n')
                group_arr.append(line)

        input_arr.append(group_arr)

    return input_arr

if __name__ == "__main__":
    print(get_input("input.txt"))