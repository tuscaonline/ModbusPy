from modbuspy import bithandler


def test_packbit():
    test = bithandler.bools_to_int([ True, False, False, False, False, True, True, True])
    assert test == b"0\x87"
    pass