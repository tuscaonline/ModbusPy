from modbuspy import bithandler
import bitarray


bits= [ True, True, False, False, False, True, False, True]

def test_packbit():
    test = bithandler.bools_to_int(bits)
    assert test == b"\xc5"
    pass

def test_bitsarray():
    a= bitarray.bitarray( bits)
    assert a