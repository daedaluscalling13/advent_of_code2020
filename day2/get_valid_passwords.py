# AOC
# Day 2.1
# Author: Kevin Kibler

def get_valid_passwords(password_array):
    results_array = list()

    for password in password_array:
        password.set_valid()
        if password.valid:
            results_array.append(password)
    
    return results_array

def get_valid_passwords2(password_array):
    results_array = list()

    for password in password_array:
        password.set_valid2()

        if password.valid2:
            results_array.append(password)
    
    return results_array