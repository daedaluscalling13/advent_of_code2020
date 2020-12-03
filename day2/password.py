# AOC 2020
# Day 2.1
# Author: Kevin Kibler

class Password:

    def __init__(self, min_freq, max_freq, freq_char, password):
        self.min_freq = min_freq
        self.max_freq = max_freq
        self.freq_char = freq_char
        self.password = password
        self.valid = False
        self.valid2 = False

    def set_valid(self):
        count = 0
        for char in self.password:
            if char == self.freq_char:
                count += 1
        
        if count <= self.max_freq and count >= self.min_freq:
            self.valid = True

    def set_valid2(self):
        try:
            if self.password[self.min_freq - 1] == self.freq_char:
                self.valid2 = True
        except(IndexError):
                pass

        try:
            if self.password[self.max_freq - 1] == self.freq_char:
                if self.valid2:
                    self.valid2 = False
                else:
                    self.valid2 = True
        except(IndexError):
            pass