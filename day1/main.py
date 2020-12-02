# AOC 2020
# Day 1.1
# Author: Kevin Kibler

from input_helper import get_input
from sort_array import sort
from find_pairs import find_pairs
from find_triple import find_triple
from max_product import max_product, max_triple_product

def main():
    input_array = get_input("input.txt")
    sort(input_array)
    pairs_list = find_pairs(input_array)
    product = max_product(pairs_list)
    print(product)

    triples_list = find_triple(input_array)
    product2 = max_triple_product(triples_list)
    print(product2)

if __name__ == "__main__":
    main()