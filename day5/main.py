# AOC 2020
# Day 5.1
# Author: Kevin Kibler

from input_helper import get_input
from make_passes import make_passes
from get_max import get_max
from find_seat import find_seat

def main():
    input_arr = get_input("input.txt")

    pass_arr = make_passes(input_arr)

    max_seat_id = get_max(pass_arr)
    print(max_seat_id)

    remaining_seats = find_seat(pass_arr)
    print(remaining_seats)

if __name__ == "__main__":
    main()
