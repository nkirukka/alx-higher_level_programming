#!/usr/bin/python3
def pow(a, b):
    ex = 0
    if a >= 0 and b >= 0:
        ex = a ** b
    elif a < 0 and b > 0:
        ex = (a) ** b
    return ex
