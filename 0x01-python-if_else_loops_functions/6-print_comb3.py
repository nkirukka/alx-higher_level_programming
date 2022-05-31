#!/usr/bin/python3
for row in range(10):
    for col in range(row + 1, 10):
        if row == 8 and col == 9:
            print("{:d}{:d}".format(row, col))
        else:
            print("{:d}{:d}".format(row, col), end=", ")
