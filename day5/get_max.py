# AOC 2020
# Day 5.1
# Author: Kevin Kibler

def get_max(pass_arr):
    max_id = 0
    for b_pass in pass_arr:
        max_id = max(max_id, b_pass.seat_id)

    return max_id