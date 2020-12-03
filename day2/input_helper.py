# AOC 2020
# Day 2.1
# Author: Kevin Kibler

from password import Password

def get_input(file_name):

    password_input_array = list()

    with open(file_name, "r+") as input_file:

        for line in input_file:
            line = line.strip('\n')
            line = line.split()
            frequencies = line[0].split('-')
            freq_char = line[1].strip(':')
            password = line[2]

            pass_to_add = Password(int(frequencies[0]), int(frequencies[1]), freq_char, password)
            password_input_array.append(pass_to_add)

    return password_input_array

if __name__ == "__main__":
    print(get_input('input.txt'))