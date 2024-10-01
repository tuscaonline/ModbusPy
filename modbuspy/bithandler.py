from functools import reduce
from itertools import batched
import struct

def f(a, b):
    return (a << 1) | b

def bools_to_int(arr:list[bool])->bytearray:
    ret = b""
    for i in batched(reversed(arr), 16):
        octet = 0
        for rang ,j in enumerate(i):
            octet |=  j << rang
        ret += struct.pack(">B", octet)
    return ret
