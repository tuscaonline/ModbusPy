from modbuspy import slave, modbuserror
import pytest


def test_slave():
    test = slave.Slave()
    assert len(test._HoldingRegisterMemory) == 65536
    assert len(test._InputRegisterMemory) == 65536
    assert len(test._InputCoilsMemory) == 8192
    assert len(test._CoilsMemory) == 8192
    assert len(test.coils) == 65536
    assert len(test.inputCoils) == 65536



def test_slave_checkAdressMaxHr():
    maxRegister = 2580
    test = slave.Slave(HoldingRegisterAeraSize=maxRegister)
    with pytest.raises(modbuserror.IllegalAdressError, match=r"Illegal address \(\d+\)"):
        test.set_int8(maxRegister+2, 12, "HR")
    with pytest.raises(modbuserror.IllegalAdressError, match=r"Illegal address \(\d+\)"):
        test.set_int8(0, 12, "HR")

def test_slave_checkAdressMaxIr():
    maxRegister = 2580
    test = slave.Slave(InputRegistrerAeraSize=maxRegister)
    with pytest.raises(modbuserror.IllegalAdressError, match=r"Illegal address \(\d+\)"):
        test.set_int8(maxRegister+2, 12, "IR")
    with pytest.raises(modbuserror.IllegalAdressError, match=r"Illegal address \(\d+\)"):
        test.set_int8(0, 12, "IR")

def test_slave_int8_checksize():
    test = slave.Slave()
    with pytest.raises(
        modbuserror.IllegalNumberError, match=r"Illegal value \(\d+\) for int 8"
    ):
        test.set_int8(1, 244, "HR")
    with pytest.raises(
        modbuserror.IllegalNumberError, match=r"Illegal value \(-\d+\) for int 8"
    ):
        test.set_int8(1, -130, "HR")

def test_getset_int8_HR():
    number = 127
    test = slave.Slave(endianness="Little")
    test.set_int8(1, number, "HR")
    assert test._HoldingRegisterMemory[0:1] == b"\x7f"
    assert test.get_int8(1, 'HR') == number


def test_set_int8_IR():
    number =-128
    test = slave.Slave(endianness="Little")
    test.set_int8(1, number, "IR")
    assert test.get_int8(1, 'IR') == number


def test_slave_uint8_checksize():
    test = slave.Slave()
    with pytest.raises(
        modbuserror.IllegalNumberError, match=r"Illegal value \(\d+\) for uint8"
    ):
        test.set_uint8(1, 256, "HR")
    with pytest.raises(
        modbuserror.IllegalNumberError, match=r"Illegal value \(-\d+\) for uint8"
    ):
        test.set_uint8(1, -1, "HR")

def test_getset_uint8_HR():
    number = 245
    test = slave.Slave(endianness="Little")
    test.set_uint8(1, number, "HR")
    assert test.get_uint8(1, 'HR') == number


def test_set_uint8_IR():
    number =244
    test = slave.Slave(endianness="Little")
    test.set_uint8(1, number, "IR")
    assert test.get_uint8(1, 'IR') == number


#16 BIT

def test_slave_int16_checksize():
    test = slave.Slave()
    with pytest.raises(
        modbuserror.IllegalNumberError, match=r"Illegal value \(\d+\) for int16"
    ):
        test.set_int16(1, 32769, "HR")
    with pytest.raises(
        modbuserror.IllegalNumberError, match=r"Illegal value \(-\d+\) for int16"
    ):
        test.set_int16(1, -32769, "HR")

def test_getset_int16_HR():
    number = 24520
    test = slave.Slave(endianness="Little")
    test.set_int16(1, number, "HR")
    assert test.get_int16(1, 'HR') == number


def test_set_int16_IR():
    number =-24521
    test = slave.Slave(endianness="Little")
    test.set_int16(1, number, "IR")
    assert test.get_int16(1, 'IR') == number


def test_slave_uint16_checksize():
    test = slave.Slave()
    with pytest.raises(
        modbuserror.IllegalNumberError, match=r"Illegal value \(\d+\) for uint16"
    ):
        test.set_uint16(1, 65536, "HR")
    with pytest.raises(
        modbuserror.IllegalNumberError, match=r"Illegal value \(-\d+\) for uint16"
    ):
        test.set_uint16(1, -1, "HR")

def test_getset_uint16_HR():
    number = 65500
    test = slave.Slave(endianness="Little")
    test.set_uint16(1, number, "HR")
    assert test.get_uint16(1, 'HR') == number


def test_set_uint16_IR():
    number =655
    test = slave.Slave(endianness="Little")
    test.set_uint16(1, number, "IR")
    assert test.get_uint16(1, 'IR') == number


#32 BIT

def test_slave_int32checksize():
    test = slave.Slave()
    with pytest.raises(
        modbuserror.IllegalNumberError, match=r"Illegal value \(\d+\) for int32"
    ):
        test.set_int32(1, 2_147_483_648, "HR")
    with pytest.raises(
        modbuserror.IllegalNumberError, match=r"Illegal value \(-\d+\) for int32"
    ):
        test.set_int32(1,	-2_147_483_649, "HR")

def test_getset_int32_HR():
    number = 2_147_450_648
    test = slave.Slave(endianness="Little")
    test.set_int32(1, number, "HR")
    assert test.get_int32(1, 'HR') == number


def test_set_int32_IR():
    number =-2_147_450_648
    test = slave.Slave(endianness="Little")
    test.set_int32(1, number, "IR")
    assert test.get_int32(1, 'IR') == number


def test_slave_uint32_checksize():
    test = slave.Slave()
    with pytest.raises(
        modbuserror.IllegalNumberError, match=r"Illegal value \(\d+\) for uint32"
    ):
        test.set_uint32(1, 4_294_967_297, "HR")
    with pytest.raises(
        modbuserror.IllegalNumberError, match=r"Illegal value \(-\d+\) for uint32"
    ):
        test.set_uint32(1, -1, "HR")

def test_getset_uint32_HR():
    number = 4_294_967_287
    test = slave.Slave(endianness="Little")
    test.set_uint32(1, number, "HR")
    assert test.get_uint32(1, 'HR') == number


def test_set_uint32_IR():
    number =4_294_867_287
    test = slave.Slave(endianness="Little")
    test.set_uint32(1, number, "IR")
    assert test.get_uint32(1, 'IR') == number



#64 BIT

def test_slave_int64checksize():
    test = slave.Slave()
    with pytest.raises(
        modbuserror.IllegalNumberError, match=r"Illegal value \(\d+\) for int64"
    ):
        test.set_int64(1, 9_223_372_036_854_775_808, "HR")
    with pytest.raises(
        modbuserror.IllegalNumberError, match=r"Illegal value \(-\d+\) for int64"
    ):
        test.set_int64(1,	-9_223_372_036_854_775_809, "HR")

def test_getset_int64_HR():
    number =  9_223_372_036_854_775_790
    test = slave.Slave(endianness="Little")
    test.set_int64(1, number, "HR")
    assert test.get_int64(1, 'HR') == number


def test_set_int64_IR():
    number = -9_223_372_036_854_775_800
    test = slave.Slave(endianness="Little")
    test.set_int64(1, number, "IR")
    assert test.get_int64(1, 'IR') == number


def test_slave_uint64_checksize():
    test = slave.Slave()
    with pytest.raises(
        modbuserror.IllegalNumberError, match=r"Illegal value \(\d+\) for uint64"
    ):
        test.set_uint64(1, 18_446_744_073_709_551_616, "HR")
    with pytest.raises(
        modbuserror.IllegalNumberError, match=r"Illegal value \(-\d+\) for uint64"
    ):
        test.set_uint64(1, -1, "HR")

def test_getset_uint64_HR():
    number = 18_446_744_063_709_551_616
    test = slave.Slave(endianness="Little")
    test.set_uint64(1, number, "HR")
    assert test.get_uint64(1, 'HR') == number


def test_set_uint64_IR():
    number =18_446_744_053_709_551_616
    test = slave.Slave(endianness="Little")
    test.set_uint64(1, number, "IR")
    assert test.get_uint64(1, 'IR') == number


