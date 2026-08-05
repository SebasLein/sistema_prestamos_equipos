from datetime import datetime


class Prestamo:
    """
    Clase que representa el préstamo de un equipo.
    """

    def __init__(self, usuario):
        """
        Constructor de la clase.

        Args:
            usuario (Usuario): Usuario que realiza el préstamo.
        """

        self.__usuario = usuario
        self.__fecha = datetime.now().strftime("%d/%m/%Y")

    @property
    def usuario(self):
        """
        Devuelve el usuario del préstamo.
        """
        return self.__usuario

    @property
    def fecha(self):
        """
        Devuelve la fecha del préstamo.
        """
        return self.__fecha

    def obtener_registro(self):
        """
        Devuelve el préstamo como una tupla (usuario, fecha).
        """
        return (self.__usuario.nombre, self.__fecha)