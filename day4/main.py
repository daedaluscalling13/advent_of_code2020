# AOC 2020
# Day 4.1
# Author: Kevin Kibler

from input_helper import get_input
from create_passports import create_passports
from valid_passports import is_valid
from valid_num import get_valid_num

def main():
    arr = get_input("input.txt")
    p_arr = create_passports(arr)
    print(type(p_arr[0].byr), type(p_arr[0].iyr), type(p_arr[0].eyr), type(p_arr[0].hgt), type(p_arr[0].hcl), type(p_arr[0].ecl), type(p_arr[0].pid), type(p_arr[0].cid))
    for passport in p_arr:
        print(passport.byr, passport.iyr, passport.eyr, passport.hgt, passport.hcl, passport.ecl, passport.pid, passport.cid)
    v_arr = is_valid(p_arr)
    v_num = get_valid_num(v_arr)
    print(v_num)

if __name__ == "__main__":
    main()