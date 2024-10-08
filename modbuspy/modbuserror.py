
class ModbusError(Exception):
    """Erreur Modbus générique"""

class ModbusParameterError(ModbusError):
    """Erreur Modbus Parametre Erroné"""

class ModbusLenghtError(ModbusError):
    """Erreur Modbus Parametre Erroné"""

class IllegalNumberError(ModbusError):
    """Erreur de conversion de type"""

class IllegalAdressError(ModbusError):
    """Erreur de conversion de type"""
