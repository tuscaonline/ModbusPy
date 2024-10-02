from functools import reduce
from itertools import batched
import struct

def f(a, b):
    return (a << 1) | b

def bools_to_bytes(arr:list[bool])->bytes:
    ret = bytes()
    for i in batched(reversed(arr), 8):
        octet = 0
        for rang ,j in enumerate(i):
            octet |=  j << rang
        ret += struct.pack(">B", octet)
    return bytes(reversed(ret))

def bytes_to_bool(payload:bytes)-> list[bool]:
    """"""
    ret = []
    for octet in payload:
        for i in range(7,-1, -1):
           ret.append(((octet >> i) & 1)==True)
        pass
    return ret