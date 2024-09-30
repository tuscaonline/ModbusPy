class ModbusDataModel:
    """Describe the slave mapping
    We can have :
    - Dicretes Input, Single bit, Read-Only
    - Coils, Single bit, Read-Write
    - Input Registers, 16-bit word, Read-Only
    - Holding Registers, 16-bit word, Read-Write
The MODBUS application protocol defines precisely PDU addressing rules. 
In a MODBUS PDU each data is addressed from 0 to 65535.
It also defines clearly a MODBUS data model composed of 4 blocks that comprises several 
elements numbered from 1 to n
    """

class Coil:
    """Represent a read only bit"""
    adress:int
    value:bool

class InputRegister:
    """Represent a read-write bit"""
    adress:int
    value:bool

class  DiscreteInput:
    """Represent a read only word (16bit)"""
    adress:int
    value:bytes

class HoldingRegister:
    """Represent a read only word (16bit)"""
    adress:int
    value:bytes