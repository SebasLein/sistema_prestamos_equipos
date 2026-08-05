class Usuario:
    """
    Clase que representa a un usuario del sistema de préstamos.
    """

    def __init__(self, nombre):
        """
        Constructor de la clase.

        Args:
            nombre (str): Nombre del usuario.
        """

        self.__nombre = nombre

    @property
    def nombre(self):
        """
        Devuelve el nombre del usuario.
        """
        return self.__nombre

    def __str__(self):
        """
        Devuelve una representación en texto del usuario.
        """
        return self.__nombre