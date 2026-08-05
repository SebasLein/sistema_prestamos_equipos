from equipo import Equipo
from usuario import Usuario
from prestamo import Prestamo


class Sistema:
    """
    Clase principal que administra el sistema de préstamos.
    """

    def __init__(self):
        """
        Inicializa el inventario con algunos equipos.
        """

        self.equipos = {
            "Portátil Dell": Equipo("Portátil Dell"),
            "HP ProBook": Equipo("HP ProBook"),
            "MacBook Air": Equipo("MacBook Air")
        }

    def mostrar_equipos(self):
        """
        Muestra todos los equipos y su disponibilidad.
        """

        print("\n===== EQUIPOS =====")

        for equipo in self.equipos.values():

            estado = "Disponible" if equipo.disponible else "Prestado"

            print(f"{equipo.nombre} - {estado}")

    def agregar_equipo(self):
        """
        Agrega un nuevo equipo al inventario.
        """

        nombre = input("Ingrese el nombre del nuevo equipo: ")

        if nombre in self.equipos:
            print("Ese equipo ya existe.")
            return

        self.equipos[nombre] = Equipo(nombre)

        print("Equipo agregado correctamente.")

    def registrar_prestamo(self):
        """
        Registra el préstamo de un equipo.
        """

        self.mostrar_equipos()

        nombre_equipo = input("\nEscriba el nombre exacto del equipo a prestar: ")

        if nombre_equipo not in self.equipos:
            print("Ese equipo no existe.")
            return

        equipo = self.equipos[nombre_equipo]

        if not equipo.disponible:
            print("Ese equipo ya se encuentra prestado.")
            return

        nombre_usuario = input("Nombre del usuario: ")

        usuario = Usuario(nombre_usuario)

        prestamo = Prestamo(usuario)

        equipo.agregar_prestamo(prestamo.obtener_registro())

        equipo.prestar()

        print("Préstamo registrado correctamente.")

    def devolver_equipo(self):
        """
        Marca un equipo como devuelto.
        """

        nombre_equipo = input("Equipo a devolver: ")

        if nombre_equipo not in self.equipos:
            print("Ese equipo no existe.")
            return

        equipo = self.equipos[nombre_equipo]

        if equipo.devolver():
            print("Equipo devuelto correctamente.")
        else:
            print("El equipo ya estaba disponible.")

    def ver_historial(self):
        """
        Muestra el historial de préstamos.
        """

        print("\n===== HISTORIAL =====")

        for equipo in self.equipos.values():

            print(f"\n{equipo.nombre}")

            if not equipo.historial:
                print("Sin préstamos registrados.")
                continue

            for usuario, fecha in equipo.historial:
                print(f"- {usuario} ({fecha})")