from sistema import Sistema


def menu():

    sistema = Sistema()

    while True:

        print("\n==============================")
        print(" SISTEMA DE PRÉSTAMOS")
        print("==============================")
        print("1. Ver equipos")
        print("2. Registrar préstamo")
        print("3. Devolver equipo")
        print("4. Ver historial")
        print("5. Agregar equipo")
        print("6. Salir")

        opcion = input("\nSeleccione una opción: ")

        if opcion == "1":
            sistema.mostrar_equipos()

        elif opcion == "2":
            sistema.registrar_prestamo()

        elif opcion == "3":
            sistema.devolver_equipo()

        elif opcion == "4":
            sistema.ver_historial()

        elif opcion == "5":
            sistema.agregar_equipo()

        elif opcion == "6":
            print("\nGracias por utilizar el sistema.")
            break

        else:
            print("\nOpción no válida.")


if __name__ == "__main__":
    menu()