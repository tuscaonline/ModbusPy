from modbuspy import modbustype, modbuserror
import pytest

def test_register():
    trame = modbustype.TrameRegister(3,1 , 4)

    assert trame.adress == 1
    assert trame.functionCode == 3
    assert len(trame.trame) == 4
    assert trame.trame == b'\x00\x00\x00\x00'
    pass


def test_register_wrong_len():
    with pytest.raises(modbuserror.ModbusLenghtError):
        trame = modbustype.TrameRegister(3,1 , 4, b'\x00\x00\x00')

def test_register_wrong_datatype():
    with pytest.raises(modbuserror.ModbusParameterError):
        trame = modbustype.TrameRegister(3,1 , 4, '00')

def test_register_good_datatype():
    trame = modbustype.TrameRegister(3,1 , 4,b'\x01\x02\x03\x04')
    assert trame.trame == b'\x01\x02\x03\x04'
    assert isinstance(trame.trame, bytearray)

    pass