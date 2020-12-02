# AOC 2020
# Day 1.1
# Author: Kevin Kibler

from input_helper import get_input
from sort_array import sort
from find_pairs import find_pairs
from max_product import max_product

def main():
    input_array = get_input("input.txt")

    sort(input_array)
    print(input_array)

    pairs_list = find_pairs(input_array)
    print(pairs_list)

    product = max_product(pairs_list)
    print(product)

if __name__ == "__main__":
    main()