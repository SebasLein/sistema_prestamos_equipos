# Sistema de Préstamos de Equipos

## Descripción

Este proyecto corresponde al **Proyecto de clase - Sistema de Préstamos de Equipos**, desarrollado como parte del proceso de formación en **Python Avanzado**.

El objetivo del proyecto es desarrollar una aplicación de consola que permita gestionar el inventario de equipos de cómputo, registrar préstamos, realizar devoluciones y consultar el historial de préstamos.

La solución integra conceptos de **Programación Orientada a Objetos (POO)**, junto con el uso de **listas, tuplas y diccionarios**, aplicando también principios básicos de encapsulación y organización modular del código.

---

## Objetivos

El proyecto tiene como objetivos principales:

- Aplicar los conceptos de clases y objetos en Python.
- Implementar encapsulación mediante atributos privados y propiedades.
- Crear clases independientes para representar los elementos principales del sistema.
- Utilizar diccionarios para gestionar el inventario de equipos.
- Utilizar listas para almacenar el historial de préstamos.
- Utilizar tuplas para registrar la información de cada préstamo.
- Implementar un menú interactivo para facilitar el uso del sistema.
- Aplicar validaciones para evitar operaciones incorrectas.
- Organizar el código en diferentes módulos según la responsabilidad de cada clase.

---

## Funcionalidades

El sistema cuenta con las siguientes funcionalidades:

1. **Ver equipos**
   - Permite consultar todos los equipos registrados.
   - Muestra si cada equipo se encuentra disponible o prestado.

2. **Registrar préstamo**
   - Permite seleccionar un equipo disponible.
   - Solicita el nombre del usuario.
   - Registra el préstamo junto con la fecha.
   - Cambia el estado del equipo a prestado.
   - Impide prestar un equipo que ya se encuentre ocupado.

3. **Devolver equipo**
   - Permite seleccionar un equipo prestado.
   - Cambia nuevamente su estado a disponible.
   - Valida que el equipo exista y que se encuentre prestado.

4. **Ver historial**
   - Muestra el historial de préstamos de cada equipo.
   - Indica el usuario y la fecha de cada préstamo.
   - Informa cuando un equipo no tiene préstamos registrados.

5. **Agregar equipo**
   - Permite registrar nuevos equipos en el inventario.
   - Verifica que el equipo no exista previamente.

6. **Salir**
   - Permite finalizar la ejecución del programa.

---

## Diseño de clases

El proyecto está compuesto por tres clases principales y una clase encargada de administrar la lógica general del sistema.

### Clase `Equipo`

Representa cada equipo disponible dentro del inventario.

Sus principales elementos son:

- `nombre`: identifica el equipo.
- `__disponible`: atributo encapsulado que controla si el equipo está disponible.
- `__historial`: lista privada que almacena los préstamos realizados.

Entre sus métodos se encuentran:

- `prestar()`
- `devolver()`
- `agregar_prestamo()`

También utiliza propiedades para consultar el estado de disponibilidad y el historial.

---

### Clase `Usuario`

Representa a la persona que realiza un préstamo.

Cuenta con:

- `__nombre`: atributo privado que almacena el nombre del usuario.
- `nombre`: propiedad utilizada para consultar el nombre.
- `__str__()`: permite representar el usuario como texto.

---

### Clase `Prestamo`

Representa un préstamo realizado por un usuario.

La clase almacena:

- El usuario que realiza el préstamo.
- La fecha en la que se registra.

El método `obtener_registro()` permite convertir la información del préstamo en una tupla con el formato:

```text
(usuario, fecha)
```

Esto permite cumplir con el requisito de utilizar tuplas para almacenar los registros del historial.

---

### Clase `Sistema`

Es la clase encargada de administrar las operaciones generales del programa.

Contiene un diccionario de equipos y proporciona métodos para:

- Mostrar equipos.
- Registrar préstamos.
- Devolver equipos.
- Consultar el historial.
- Agregar nuevos equipos.

El diccionario utiliza el nombre del equipo como clave y un objeto de la clase `Equipo` como valor.

---

## Aplicación de listas, tuplas y diccionarios

Uno de los objetivos principales del proyecto es integrar las estructuras de datos estudiadas durante el curso.

### Listas

Se utilizan para almacenar el historial de préstamos de cada equipo.

Ejemplo:

```python
self.__historial = []
```

Cada nuevo préstamo se agrega a esta lista.

### Tuplas

Cada préstamo se registra mediante una tupla que contiene el usuario y la fecha:

```python
(usuario, fecha)
```

Las tuplas permiten mantener estos datos como un registro inmutable.

### Diccionarios

El inventario general se administra mediante un diccionario:

```python
self.equipos = {}
```

Cada equipo se almacena utilizando su nombre como clave y un objeto `Equipo` como valor.

---

## Encapsulación

La encapsulación se aplica principalmente en la clase `Equipo`.

Los atributos relacionados con el estado del equipo y su historial son privados:

```python
self.__disponible
self.__historial
```

De esta manera, otras partes del programa no modifican directamente estos valores.

El cambio del estado se realiza mediante métodos como:

```python
prestar()
devolver()
```

También se utilizan propiedades (`@property`) para permitir la consulta controlada de determinados atributos.

Esto permite mantener una separación entre los datos internos de los objetos y las operaciones que pueden realizarse sobre ellos.

---

## Estructura del proyecto

```text
sistema_prestamos_equipos/
│
├── images/
│   ├── menu.png
│   ├── equipos.png
│   ├── prestamo.png
│   ├── estado_prestado.png
│   ├── historial.png
│   └── devolucion.png
│
├── equipo.py
├── usuario.py
├── prestamo.py
├── sistema.py
├── main.py
├── README.md
└── .gitignore
```

### Descripción de los archivos

- **`equipo.py`**: contiene la clase `Equipo`.
- **`usuario.py`**: contiene la clase `Usuario`.
- **`prestamo.py`**: contiene la clase `Prestamo`.
- **`sistema.py`**: contiene la clase `Sistema` y la lógica principal de gestión.
- **`main.py`**: contiene el menú interactivo y punto de entrada del programa.
- **`images/`**: contiene las capturas de pantalla utilizadas como evidencia de funcionamiento.
- **`README.md`**: documentación general del proyecto.
- **`.gitignore`**: contiene archivos y elementos que no deben ser incluidos en el repositorio.

## Validaciones implementadas

El programa cuenta con diferentes validaciones para mantener un funcionamiento adecuado:

- Verifica que el equipo exista antes de realizar un préstamo.
- Impide registrar un préstamo de un equipo que ya está prestado.
- Verifica que el equipo exista antes de realizar una devolución.
- Impide devolver un equipo que ya se encuentra disponible.
- Verifica que un equipo nuevo no esté registrado previamente.
- Valida las opciones seleccionadas en el menú principal.

Estas validaciones permiten evitar operaciones incorrectas y proporcionan mensajes claros al usuario.

---

## Tecnologías utilizadas

- **Python 3**
- **Visual Studio Code**
- **Git**
- **GitHub**

El proyecto utiliza únicamente herramientas y funcionalidades necesarias para desarrollar los conceptos trabajados durante la formación.

---

## Reflexión sobre el aprendizaje

El desarrollo de este proyecto permitió reforzar los conocimientos relacionados con la Programación Orientada a Objetos en Python. Uno de los principales aprendizajes fue comprender que las clases permiten representar elementos del mundo real dentro de un programa y que cada clase puede tener una responsabilidad específica.

También fue importante aplicar el concepto de encapsulación, especialmente mediante atributos privados y propiedades, ya que esto permite controlar la forma en que se consulta y modifica la información interna de los objetos.

Otro aprendizaje importante fue la integración de diferentes estructuras de datos. Las listas se utilizaron para almacenar los historiales de préstamos, las tuplas para representar los registros individuales de cada préstamo y los diccionarios para administrar el inventario de equipos.

Durante el desarrollo también fue necesario realizar diferentes pruebas en consola para verificar que los préstamos, devoluciones, consultas y registros funcionaran correctamente. Esto permitió identificar errores en la forma de utilizar el programa y mejorar los mensajes mostrados al usuario.

Finalmente, la organización del proyecto en diferentes archivos y clases permitió comprender mejor la importancia de separar responsabilidades dentro de una aplicación. El uso de Git y GitHub también permitió llevar un control organizado de los cambios realizados durante el desarrollo.

---

## Autor

**Sebastian Lein Castro Grajales**

Proyecto académico desarrollado como parte del proceso de formación en **Python Avanzado - SENA**.
