from typing import Self
from struct import *
from modbuspy import bithandler
from typing import overload

class Slave:
    """L'idée est de représenter l'état interne de l'esclave Modbus
    Zone IR
    Zone HR
    Zone Coils
    Zone Input Coils

    Il faut qu'on puisse interdire des zones
    """

    IR: bytearray

    def __init__(
        self,
        InputRegistrerAeraSize: int = 65536,
        HoldingRegisterAeraSize: int = 65536,
        InputCoilsAeraSize: int = 65536,
        CoilsAeraSize: int = 65536,
    ) -> None:
        self.InputRegisterMemory = bytearray(InputRegistrerAeraSize)
        self.HoldingRegisterMemory = bytearray(HoldingRegisterAeraSize)
        self.InputCoilsMemory = bytearray((InputCoilsAeraSize//8))
        self.CoilsMemory = bytearray((CoilsAeraSize//8))

    @classmethod
    def from_yaml(self) -> Self:
        """Charge un slave a partir d'un yaml"""

    @property 
    def coils(self)->list[bool]:
        """Les coils sous formes de list de bool"""
        return bithandler.bytes_to_bool(self.CoilsMemory)

    @property 
    def inputCoils(self)->list[bool]:
        """Les InputCoils sous formes de list de bool"""
        return bithandler.bytes_to_bool(self.CoilsMemory)

    @overload
    def set_input_register(self):
        ...
