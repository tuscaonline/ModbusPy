from typing import Literal, Self, SupportsIndex, Union
from struct import *
from .utils import bytes_to_bools
from .modbuserror import IllegalNumberError, IllegalAdressError, ProtectedAdressError

class MdbMemory(bytearray):
    def __init__(self, size, protectedAera = []) -> None:
        self.protectedAera = protectedAera

        return super().__init__(size)
    def __getitem__(self, key: SupportsIndex | slice, /) -> int: 
        if isinstance(key, slice):
            test = range(*key.indices(len(self)))

            for i in self.protectedAera:
                if isinstance(i, list):
                    if len(i)!=2:
                        raise SyntaxError('The protected Aera parameter can only int or Array of Two int')
                    for j in range(i[0], i[1]+1):
                        if j-1 in test:
                            raise ProtectedAdressError()
                else:
                    if i-1 in test:
                        raise ProtectedAdressError()

        

        return super().__getitem__(key)


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
        protectionAeraIr=[],
        protectionAeraHr=[],
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
        self._InputRegisterMemory = MdbMemory(InputRegistrerAeraSize, protectionAeraIr)
        self._HoldingRegisterMemory = MdbMemory(HoldingRegisterAeraSize, protectionAeraHr)
        self._InputCoilsMemory = MdbMemory(InputCoilsAeraSize // 8)
        self._CoilsMemory = MdbMemory(CoilsAeraSize // 8)
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
            return unpack(
                f"{self._endian}b", self.HoldingRegisterMemory[(adresse - 1):(adresse - 1)+1])[0]
        if memory == "IR":
            return unpack(
                f"{self._endian}b", self.InputRegisterMemory[(adresse - 1):(adresse - 1)+1])[0]
        
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
            return unpack(
                f"{self._endian}B", self.HoldingRegisterMemory[(adresse - 1):(adresse - 1)+1])[0]
        if memory == "IR":
            return unpack(
                f"{self._endian}B", self.InputRegisterMemory[(adresse - 1):(adresse - 1)+1])[0]

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
            return unpack(
                f"{self._endian}h", self.HoldingRegisterMemory[(adresse - 1):(adresse - 1)+2])[0]
        if memory == "IR":
            return unpack(
                f"{self._endian}h", self.InputRegisterMemory[(adresse - 1):(adresse - 1)+2])[0]

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
            return unpack(
                f"{self._endian}H", self.HoldingRegisterMemory[(adresse - 1):(adresse - 1)+2])[0]
        if memory == "IR":
            return unpack(
                f"{self._endian}H", self.InputRegisterMemory[(adresse - 1):(adresse - 1)+2])[0]


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
            return unpack(
                f"{self._endian}i", self.HoldingRegisterMemory[(adresse - 1):(adresse - 1)+4])[0]
        if memory == "IR":
            return unpack(
                f"{self._endian}i", self.InputRegisterMemory[(adresse - 1):(adresse - 1)+4])[0]


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
            return unpack(
                f"{self._endian}I", self.HoldingRegisterMemory[(adresse - 1):(adresse - 1)+4])[0]
        if memory == "IR":
            return unpack(
                f"{self._endian}I", self.InputRegisterMemory[(adresse - 1):(adresse - 1)+4])[0]
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
            return unpack(
                f"{self._endian}q", self.HoldingRegisterMemory[(adresse - 1):(adresse - 1)+8])[0]
        if memory == "IR":
            return unpack(
                f"{self._endian}q", self.InputRegisterMemory[(adresse - 1):(adresse - 1)+8])[0]

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
            return unpack(
                f"{self._endian}Q", self.HoldingRegisterMemory[(adresse - 1):(adresse - 1)+8])[0]
        if memory == "IR":
            return unpack(
                f"{self._endian}Q", self.InputRegisterMemory[(adresse - 1):(adresse - 1)+8])[0]

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
