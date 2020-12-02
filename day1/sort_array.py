# AOC 2020
# Day 1.1
# Author: Kevin Kibler

def sort(input_array):
    mergesort(input_array)

def mergesort(input_array):
    if len(input_array) > 0:
        left_array = input_array[:len(input_array//2)]
        right_array = input_array[len(input_array)//2:]

        mergesort(left_array)
        mergesort(right_array)

        i = 0
        j = 0
        k = 0

        while i<len(left_array) and j<len(right_array):
            if left_array[i] < right_array[j]:
                input_array[k] = left_array[i]
                i += 1
                k += 1
            else:
                input_array[k] = right_array[j]
                j += 1
                k += 1
            
        while i<len(left_array):
            input_array[k] = left_array[i]
            i += 1
            k += 1

        while j<len(right_array):
            input_array[k] = right_array[j]
            j += 1
            k += 1