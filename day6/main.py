# AOC 2020
# Day 6.1
# Author: Kevin Kibler

from input_helper import get_input
from get_counts import get_counts
from get_counts import get_counts2
from get_sum import get_sum

def main():
    input_arr = get_input("input.txt")
    count_arr = get_counts(input_arr)
    count_sum = get_sum(count_arr)
    print(count_sum)

    count_arr2 = get_counts2(input_arr)
    count_sum2 = get_sum(count_arr2)
    print(count_sum2)

if __name__ == "__main__":
    main()