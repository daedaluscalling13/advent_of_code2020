# AOC 2020
# Day 4.1
# Kevin Kibler

from passport import Passport

def create_passports(arr):
    
    passport_array = list()

    for data in arr:
        try:
            byr = data['byr']
        except KeyError:
            byr = None

        try:
            iyr = data['iyr']
        except KeyError:
            iyr = None

        try:
            eyr = data['eyr']
        except KeyError:
            eyr = None

        try:
            hgt = data['hgt']
        except KeyError:
            hgt = None

        try:
            hcl = data['hcl']
        except KeyError:
            hcl = None

        try:
            ecl = data['ecl']
        except KeyError:
            ecl = None

        try:
            pid = data['pid']
        except KeyError:
            pid = None

        try:
            cid = data['cid']
        except KeyError:
            cid = None


        new_passport = Passport(byr, iyr, eyr, hgt, hcl, ecl, pid, cid)
        passport_array.append(new_passport)

    return passport_array