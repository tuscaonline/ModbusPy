from modbuspy import slave

def test_slave():
    test = slave.Slave()
    assert len(test.HoldingRegisterMemory) == 65535
    assert len(test.InputRegisterMemory) == 65535
    assert len(test.InputCoilsMemory) == 8192
    assert len(test.CoilsMemory) == 8192
    assert len(test.coils) == 65535