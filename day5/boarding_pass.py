# AOC 2020
# Day 5.1
# Author: Kevin Kibler

class BoardingPass:

    def __init__(self, boarding_string):
        self.boarding_pass = boarding_string

        self.row = self.create_row()
        self.column = self.create_column()
        self.seat_id = self.create_seat_id()

    def create_row(self):
        row_string = [self.boarding_pass[index] for index in range(0, 7)]
        row_bool = string_to_bool(row_string, 'F', 'B')
        return row_bool[0]*64 + row_bool[1]*32 + row_bool[2]*16 + row_bool[3]*8 + row_bool[4]*4 + row_bool[5]*2 + row_bool[6]*1

    def create_column(self):
        column_string = [self.boarding_pass[index] for index in range(7, 10)]
        column_bool = string_to_bool(column_string, 'L', 'R')
        return column_bool[0]*4 + column_bool[1]*2 + column_bool[2]*1

    def create_seat_id(self):
        return self.row * 8 + self.column

def string_to_bool(string, zero_char, one_char):
    return list(map(lambda x: x == one_char, string))