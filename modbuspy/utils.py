from itertools import batched
import struct
 
def bools_to_bytes(arr:list[bool])->bytes:
    ret = b""
    for i in batched(reversed(arr), 8):
        octet = 0
        for rang ,j in enumerate(i):
            octet |=  j << rang
        ret += struct.pack(">B", octet)
    return bytes(reversed(ret))


def bytes_to_bools(arr:bytes)->list[bool]:
    ret = []
    for i in (arr):
        octet = 0
        retOct=[]
        for rang in range(7, -1,-1):
            retOct.append((i >> rang) & True)
        ret.extend(retOct)
    
    return (ret)


