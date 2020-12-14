# AOC 2020
# Day 4.1
# Author: Kevin Kibler

def get_input(input_name_string):
    input_arr = list()

    with open(input_name_string, "r+") as input_file:
        input_fields = dict()

        for line in input_file:
            if line == '\n':
                input_arr.append(input_fields)
                input_fields = dict()
            else:
                line = line.strip('\n')
                line = line.split()
                
                for field in line:
                    field = field.split(":")
                    input_fields[field[0]] = field[1]

        input_arr.append(input_fields)

    return input_arr

if __name__ == "__main__":
    arr = get_input("input2.txt")
    for passport in arr:
        print(passport)