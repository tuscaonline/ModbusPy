from modbuspy import bithandler
import bitarray


bits=[1, 1, 0, 0, 0, 1, 0, 1, 1, 1, 0, 0, 0, 1, 0, 0, 1, 0, 1, 0, 0, 0, 0, 1]

def test_packbit():
    a= bitarray.bitarray( bits)
    test = bithandler.bools_to_bytes(bits)
    assert test == a.tobytes()
    pass

def test_unpackbit():
    ""
    a= bitarray.bitarray( bits)
    # a.frombytes(b"\x01")
    res = bithandler.bytes_to_bool(a.tobytes())
    assert res == bits
