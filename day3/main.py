# AOC 2020
# Day 3.1
# Author: Kevin Kibler

from input_helper import get_input
from tree_count import tree_count

def main():
    arr = get_input("input.txt")

    count11 = tree_count(arr, 1, 1)
    count31 = tree_count(arr, 3, 1)
    count51 = tree_count(arr, 5, 1)
    count71 = tree_count(arr, 7, 1)
    count12 = tree_count(arr, 1, 2)

    print(count11 * count31 * count51 * count71 * count12)

if __name__ == "__main__":
    main()