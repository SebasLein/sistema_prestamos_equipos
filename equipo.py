class Equipo:
    """
    Clase que representa un equipo disponible para préstamo.
    """

    def __init__(self, nombre):
        """
        Constructor de la clase.

        Args:
            nombre (str): Nombre del equipo.
        """

        self.nombre = nombre
        self.__disponible = True
        self.__historial = []

    @property
    def disponible(self):
        """
        Devuelve el estado actual del equipo.
        """
        return self.__disponible

    def prestar(self):
        """
        Marca el equipo como prestado si está disponible.

        Returns:
            bool: True si el préstamo fue exitoso, False en caso contrario.
        """

        if self.__disponible:
            self.__disponible = False
            return True

        return False

    def devolver(self):
        """
        Marca el equipo como disponible nuevamente.

        Returns:
            bool: True si la devolución fue exitosa, False en caso contrario.
        """

        if not self.__disponible:
            self.__disponible = True
            return True

        return False

    def agregar_prestamo(self, prestamo):
        """
        Agrega un préstamo al historial del equipo.

        Args:
            prestamo (tuple): Tupla con el usuario y la fecha.
        """

        self.__historial.append(prestamo)

    @property
    def historial(self):
        """
        Devuelve el historial de préstamos.
        """
        return self.__historial