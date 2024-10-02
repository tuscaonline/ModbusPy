from modbuspy import slave

def test_slave():
    test = slave.Slave()
    assert len(test.HoldingRegisterMemory) == 65536
    assert len(test.InputRegisterMemory) == 65536
    assert len(test.InputCoilsMemory) == 8192
    assert len(test.CoilsMemory) == 8192
    assert len(test.coils) == 65536
    assert len(test.inputCoils) == 65536

def test_type():
    type UINT16 = int
    assert isinstance( 15 ,UINT16)