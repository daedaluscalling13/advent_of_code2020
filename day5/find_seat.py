# AOC 2020
# Day 5.2
# Author: Kevin Kibler

def find_seat(pass_arr):
    seat_list = [i for i in range(1024)]
    for b_pass in pass_arr:
        seat_list.remove(b_pass.seat_id)

    return seat_list