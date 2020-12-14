# AOC 2020
# Day 4.1
# Author: Kevin Kibler

class Passport:

    def __init__(self, byr=None, iyr=None, eyr=None, hgt=None, hcl=None, ecl=None, pid=None, cid=None):
        self.byr = byr
        self.iyr = iyr
        self.eyr = eyr
        self.hgt = hgt
        self.hcl = hcl
        self.ecl = ecl
        self.pid = pid
        self.cid = cid

    def is_valid(self):
        return self.byr_is_valid() and self.iyr_is_valid() and self.eyr_is_valid() and self.hgt_is_valid() and self.hcl_is_valid() and self.ecl_is_valid() and self.pid_is_valid()

    def byr_is_valid(self):
        try:
            return int(self.byr) >= 1920 and int(self.byr) <= 2020
        except TypeError:
            return False

    def iyr_is_valid(self):
        try:
            return int(self.iyr) >= 2010 and int(self.iyr) <= 2020
        except TypeError:
            return False

    def eyr_is_valid(self):
        try:
            return int(self.eyr) >= 2020 and int(self.eyr) <= 2030
        except TypeError:
            return False

    def hgt_is_valid(self):
        try:
            if self.hgt.endswith("cm"):
                hgt = int(self.hgt.strip("cm"))
                return hgt >= 150 and hgt <= 193
            elif self.hgt.endswith("in"):
                hgt = int(self.hgt.strip("in"))
                return hgt >= 59 and hgt <= 76
            else:
                return False
        except AttributeError:
            return False
    
    def hcl_is_valid(self):
        try:
            if len(self.hcl) != 7:
                return False
            if self.hcl[0] != '#':
                return False
            for index in range(1, len(self.hcl)):
                char = self.hcl[index]
                if not((char <= '9' and char >= '0') or (char <='f' and char >= 'a')):
                    return False
            
            return True
        except TypeError:
            return False

    def ecl_is_valid(self):
        valid_colors = ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']
        return self.ecl in valid_colors
    
    def pid_is_valid(self):
        try:
            return len(self.pid) == 9
        except TypeError:
            return False