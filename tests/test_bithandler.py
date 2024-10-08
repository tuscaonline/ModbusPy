from modbuspy import utils
import bitarray


 
def test_packbit():
    bits = bitarray.bitarray() 
    bits.frombytes(b"\xcF\xf3\xc1\xf2")
    test = utils.bools_to_bytes(list(bits))
    assert test == bitarray.bitarray( bits).tobytes()
    # pass

def test_unpackbit():
    octet = b"\xa1\x32\x21"
    bits = bitarray.bitarray() 
    bits.frombytes(octet)
    test = utils.bytes_to_bools(octet)
    assert test == list(bitarray.bitarray( bits))
    pass