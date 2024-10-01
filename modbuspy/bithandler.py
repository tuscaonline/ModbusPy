from functools import reduce

def f(a, b):
    return (a << 1) | b

def bools_to_int(arr):
    return reduce(f, arr)