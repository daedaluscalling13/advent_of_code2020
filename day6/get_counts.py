# AOC 2020
# Day 6.1
# Author: Kevin Kibler

def get_counts(groups_arr):
    count_arr = list()
    for group in groups_arr:
        count_set = set()

        for person in group:
            for answer in person:
                count_set = count_set.union(answer)
        
        count_arr.append(count_set)
    return count_arr

def get_counts2(groups_arr):
    count_arr = list()
    for group in groups_arr:
        group_count = set().union(group[0])

        for person in group:
            group_count = set(group_count).intersection(person)

        count_arr.append(group_count)
    return count_arr