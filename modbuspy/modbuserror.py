
class ModbusError(Exception):
    """Erreur Modbus générique"""

class ModbusParameterError(ModbusError):
    """Erreur Modbus Parametre Erroné"""

class ModbusLenghtError(ModbusError):
    """Erreur Modbus Parametre Erroné"""