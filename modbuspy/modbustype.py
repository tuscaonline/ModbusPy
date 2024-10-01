from .modbuserror import ModbusParameterError, ModbusLenghtError

class TrameRegister:
    """Representation d'une trame (Fct 3 ou 4)"""

    def __init__(
        self, functionCode: int, start: int, lenght: int, data: None | bytearray | bytes = None 
    ) -> None:
        """Création de la trame

        Args:
            functionCode (int) : Code fonction
            start (int): adresse de départ
            lenght (int): longueur
            data (None | bytearray) : donnée d'initialisation éventuelle
        """
        
        self.adress = start
        self.functionCode = functionCode

        if data is None:
            self.trame = bytearray(lenght)
        else:
            if not( isinstance(data, bytearray) or   isinstance(data, bytes) ):
                raise ModbusParameterError('Data parameter can be only bytearray or bytes')
            if not (len(data)==lenght):
                raise ModbusLenghtError('Data parameter has wrong len')
            self.trame = bytearray(data)

    
    def __repr__(self) -> str:
        return f"Trame {self.functionCode}, adresse {self.adress}, contenu 0x{self.trame.hex()}"
