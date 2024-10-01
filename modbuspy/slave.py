from typing import Self
from struct import *

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
        InputRegistrerAeraSize: int = 65535,
        HoldingRegisterAeraSize: int = 65535,
        InputCoilsAeraSize: int = 65535,
        CoilsAeraSize: int = 65535,
    ) -> None:
        self.InputRegisterMemory = bytearray(InputRegistrerAeraSize)
        self.HoldingRegisterMemory = bytearray(HoldingRegisterAeraSize)
        self.InputCoilsMemory = bytearray(InputCoilsAeraSize//8+1)
        self.CoilsMemory = bytearray(CoilsAeraSize//8+1)

    @classmethod
    def from_yaml(self) -> Self:
        """Charge un slave a partir d'un yaml"""

    @property 
    def coils(self):
        return list(iter_unpack("?", self.CoilsMemory))
