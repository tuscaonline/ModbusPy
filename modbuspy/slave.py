from typing import Literal, Self, Union
from struct import *
from .utils import bytes_to_bools
from .modbuserror import IllegalNumberError, IllegalAdressError


class Slave:
    """L'idée est de représenter l'état interne de l'esclave Modbus
    Zone IR
    Zone HR
    Zone Coils
    Zone Input Coils

    Il faut qu'on puisse interdire des zones
    """

    

    def __init__(
        self,
        InputRegistrerAeraSize: int = 65536,
        HoldingRegisterAeraSize: int = 65536,
        InputCoilsAeraSize: int = 65536,
        CoilsAeraSize: int = 65536,
        
        endianness: Literal["Big", "Little", "Native"] = "Native",
    ) -> None:
        self.InputRegistrerAeraSize = InputRegistrerAeraSize
        self.HoldingRegisterAeraSize = HoldingRegisterAeraSize
        self.InputCoilsAeraSize = InputCoilsAeraSize
        self.CoilsAeraSize = CoilsAeraSize
        self._InputRegisterMemory = bytearray(InputRegistrerAeraSize)
        self._HoldingRegisterMemory = bytearray(HoldingRegisterAeraSize)
        self._InputCoilsMemory = bytearray(InputCoilsAeraSize // 8)
        self._CoilsMemory = bytearray(CoilsAeraSize // 8)
        self.endienness = endianness
        match endianness:
            case "Big":
                self._endian = ">"
            case "Little":
                self._endian = "<"
            case "Native":
                self._endian = "@"
            case _:
                self._endian = "@"
    @property
    def InputRegisterMemory(self):
        return self._InputRegisterMemory;

    @property
    def HoldingRegisterMemory(self):
        return self._HoldingRegisterMemory;   

    @property
    def InputCoilsMemory(self):
        return self._InputCoilsMemory;   
    @property
    def CoilsMemory(self):
        return self._CoilsMemory;   

    @classmethod
    def from_yaml(self) -> Self:
        """Charge un slave a partir d'un yaml"""

    @property
    def coils(self):
        return bytes_to_bools(self._CoilsMemory)

    @property
    def inputCoils(self):
        return bytes_to_bools(self._InputCoilsMemory)

    ## 8 bit
    def set_int8(self, adresse: int, value: int, memory: Literal["HR", "IR"]):
        if not (-128 <= value <= 127):
            raise IllegalNumberError(f"Illegal value ({value}) for int 8")
        self.checkAdressRegister(adresse, memory)
        if memory == "HR":
            pack_into(
                f"{self._endian}b", self._HoldingRegisterMemory, adresse - 1, value
            )
        if memory == "IR":
            pack_into(f"{self._endian}b", self._InputRegisterMemory, adresse - 1, value)

    def get_int8(self, adresse: int, memory: Literal["HR", "IR"]):
        self.checkAdressRegister(adresse, memory)
        if memory == "HR":
            return unpack_from(
                f"{self._endian}b", self._HoldingRegisterMemory, adresse - 1
            )[0]
        if memory == "IR":
            return unpack_from(
                f"{self._endian}b", self._InputRegisterMemory, adresse - 1
            )[0]

    def set_uint8(self, adresse: int, value: int, memory: Literal["HR", "IR"]):
        if not (0 <= value <= 255):
            raise IllegalNumberError(f"Illegal value ({value}) for uint8")
        self.checkAdressRegister(adresse, memory)
        if memory == "HR":
            pack_into(
                f"{self._endian}B", self._HoldingRegisterMemory, adresse - 1, value
            )
        if memory == "IR":
            pack_into(f"{self._endian}B", self._InputRegisterMemory, adresse - 1, value)

    def get_uint8(self, adresse: int, memory: Literal["HR", "IR"]):
        self.checkAdressRegister(adresse, memory)
        if memory == "HR":
            return unpack_from(
                f"{self._endian}B", self._HoldingRegisterMemory, adresse - 1
            )[0]
        if memory == "IR":
            return unpack_from(
                f"{self._endian}B", self._InputRegisterMemory, adresse - 1
            )[0]

    # 16 BIT
    def set_int16(self, adresse: int, value: int, memory: Literal["HR", "IR"]):
        if not (-32768 <= value <= 32767):
            raise IllegalNumberError(f"Illegal value ({value}) for int16")
        self.checkAdressRegister(adresse, memory)
        if memory == "HR":
            pack_into(
                f"{self._endian}h", self._HoldingRegisterMemory, adresse - 1, value
            )
        if memory == "IR":
            pack_into(f"{self._endian}h", self._InputRegisterMemory, adresse - 1, value)

    def get_int16(self, adresse: int, memory: Literal["HR", "IR"]):
        self.checkAdressRegister(adresse, memory)
        if memory == "HR":
            return unpack_from(
                f"{self._endian}h", self._HoldingRegisterMemory, adresse - 1
            )[0]
        if memory == "IR":
            return unpack_from(
                f"{self._endian}h", self._InputRegisterMemory, adresse - 1
            )[0]

    def set_uint16(self, adresse: int, value: int, memory: Literal["HR", "IR"]):
        if not (0 <= value <= 65535):
            raise IllegalNumberError(f"Illegal value ({value}) for uint16")
        self.checkAdressRegister(adresse, memory)
        if memory == "HR":
            pack_into(
                f"{self._endian}H", self._HoldingRegisterMemory, adresse - 1, value
            )
        if memory == "IR":
            pack_into(f"{self._endian}H", self._InputRegisterMemory, adresse - 1, value)

    def get_uint16(self, adresse: int, memory: Literal["HR", "IR"]):
        self.checkAdressRegister(adresse, memory)
        if memory == "HR":
            return unpack_from(
                f"{self._endian}H", self._HoldingRegisterMemory, adresse - 1
            )[0]
        if memory == "IR":
            return unpack_from(
                f"{self._endian}H", self._InputRegisterMemory, adresse - 1
            )[0]

    # 32 BIT
    def set_int32(self, adresse: int, value: int, memory: Literal["HR", "IR"]):
        if not (-2147483648 <= value <= 2147483647):
            raise IllegalNumberError(f"Illegal value ({value}) for int32")
        self.checkAdressRegister(adresse, memory)
        if memory == "HR":
            pack_into(
                f"{self._endian}i", self._HoldingRegisterMemory, adresse - 1, value
            )
        if memory == "IR":
            pack_into(f"{self._endian}i", self._InputRegisterMemory, adresse - 1, value)

    def get_int32(self, adresse: int, memory: Literal["HR", "IR"]):
        self.checkAdressRegister(adresse, memory)
        if memory == "HR":
            return unpack_from(
                f"{self._endian}i", self._HoldingRegisterMemory, adresse - 1
            )[0]
        if memory == "IR":
            return unpack_from(
                f"{self._endian}i", self._InputRegisterMemory, adresse - 1
            )[0]

    def set_uint32(self, adresse: int, value: int, memory: Literal["HR", "IR"]):
        if not (0 <= value <= 4_294_967_295):
            raise IllegalNumberError(f"Illegal value ({value}) for uint32")
        self.checkAdressRegister(adresse, memory)
        if memory == "HR":
            pack_into(
                f"{self._endian}I", self._HoldingRegisterMemory, adresse - 1, value
            )
        if memory == "IR":
            pack_into(f"{self._endian}I", self._InputRegisterMemory, adresse - 1, value)

    def get_uint32(self, adresse: int, memory: Literal["HR", "IR"]):
        self.checkAdressRegister(adresse, memory)
        if memory == "HR":
            return unpack_from(
                f"{self._endian}I", self._HoldingRegisterMemory, adresse - 1
            )[0]
        if memory == "IR":
            return unpack_from(
                f"{self._endian}I", self._InputRegisterMemory, adresse - 1
            )[0]

    # 64 BIT
    def set_int64(self, adresse: int, value: int, memory: Literal["HR", "IR"]):
        if not (-9_223_372_036_854_775_808 <= value <= 9_223_372_036_854_775_807):
            raise IllegalNumberError(f"Illegal value ({value}) for int64")
        self.checkAdressRegister(adresse, memory)
        if memory == "HR":
            pack_into(
                f"{self._endian}q", self._HoldingRegisterMemory, adresse - 1, value
            )
        if memory == "IR":
            pack_into(f"{self._endian}q", self._InputRegisterMemory, adresse - 1, value)

    def get_int64(self, adresse: int, memory: Literal["HR", "IR"]):
        self.checkAdressRegister(adresse, memory)
        if memory == "HR":
            return unpack_from(
                f"{self._endian}q", self._HoldingRegisterMemory, adresse - 1
            )[0]
        if memory == "IR":
            return unpack_from(
                f"{self._endian}q", self._InputRegisterMemory, adresse - 1
            )[0]

    def set_uint64(self, adresse: int, value: int, memory: Literal["HR", "IR"]):
        if not (0 <= value <= 18_446_744_073_709_551_615):
            raise IllegalNumberError(f"Illegal value ({value}) for uint64")
        self.checkAdressRegister(adresse, memory)
        if memory == "HR":
            pack_into(
                f"{self._endian}Q", self._HoldingRegisterMemory, adresse - 1, value
            )
        if memory == "IR":
            pack_into(f"{self._endian}Q", self._InputRegisterMemory, adresse - 1, value)

    def get_uint64(self, adresse: int, memory: Literal["HR", "IR"]):
        self.checkAdressRegister(adresse, memory)
        if memory == "HR":
            return unpack_from(
                f"{self._endian}Q", self._HoldingRegisterMemory, adresse - 1
            )[0]
        if memory == "IR":
            return unpack_from(
                f"{self._endian}Q", self._InputRegisterMemory, adresse - 1
            )[0]

    def checkAdressRegister(self, adress: int, memory: Literal["HR", "IR"]) -> bool:
        """Raise an error if the adress is oustide range"""
        if not (
            1
            <= adress
            <= (
                self.InputRegistrerAeraSize
                if memory == "IR"
                else self.HoldingRegisterAeraSize
            )
        ):
            raise IllegalAdressError(f"Illegal address ({adress})")
        return True
