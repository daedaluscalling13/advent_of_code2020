# AOC 2020
# Day 2.1
# Kevin Kibler

from input_helper import get_input
from password import Password
from get_valid_passwords import get_valid_passwords, get_valid_passwords2

def main():
    password_array = get_input('input.txt')

    valid_password_array = get_valid_passwords(password_array)
    valid2_password_array = get_valid_passwords2(password_array)

    print(len(valid_password_array))
    print(len(valid2_password_array))

if __name__ == "__main__":
    main()