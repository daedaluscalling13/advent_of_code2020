# AOC 2020
# Day 1.1
# Author: Kevin Kibler

def max_product(input_pairs_array):
    max_product = -1

    for pair in input_pairs_array:
        product = pair[0] * pair[1]
        if product > max_product:
            max_product = product
    
    return max_product

def max_triple_product(input_triples_array):
    max_product = -1

    for triple in input_triples_array:
        product = triple[0] * triple[1] * triple[2]
        if product > max_product:
            max_product = product
    
    return max_product