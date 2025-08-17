import random
import string


class MaterialBiblioteca:
    def __init__(self, titulo, autor):
        self.__titulo = titulo.title()
        self.__autor = autor.title()
        self.__codigo = self.__generar_codigo()
        self.__estado = "Disponible"

    def __generar_codigo(self):
        return ''.join(random.choices(string.ascii_uppercase + string.digits, k=8))

    # Getters
    def get_titulo(self): return self.__titulo
    def get_autor(self): return self.__autor
    def get_codigo(self): return self.__codigo
    def get_estado(self): return self.__estado

    # Setter
    def set_estado(self, nuevo_estado): self.__estado = nuevo_estado

    # Métodos
    def prestar(self):
        if self.__estado == "Disponible":
            self.__estado = "Prestado"
            print(f"El libros '{self.__titulo}' ha sido prestado.")
        else:
            print(f"El libro '{self.__titulo}' ya está prestado.")
            return False

    def devolver(self):
        if self.__estado == "Prestado":
            self.__estado = "Disponible"
            print(f"El libros '{self.__titulo}' ha sido devuelto.")
        else:
            print(f"El libros '{self.__titulo}' no estaba prestado.")
            return False

    def mostrar_info(self):
        print("\n Información del libro ")
        print(f"Título: {self.__titulo}")
        print(f"Autor: {self.__autor}")
        print(f"Código: {self.__codigo}")
        print(f"Estado: {self.__estado}")



# Clases 

class LibroFisico(MaterialBiblioteca):
    MAX_DIAS = 7
    
    def __init__(self, titulo, autor, numero_ejemplar):
        super().__init__(titulo, autor)
        self.__numero_ejemplar = numero_ejemplar

    def mostrar_info(self):
        super().mostrar_info()
        print(f"Número de ejemplar: {self.__numero_ejemplar}")
        print(f"Préstamo máximo: {self.MAX_DIAS} días")


class LibroDigital(MaterialBiblioteca):
    MAX_DIAS = 3
    
    def __init__(self, titulo, autor, tamano_archivo):
        super().__init__(titulo, autor)
        self.__tamano_archivo = tamano_archivo

    def mostrar_info(self):
        super().mostrar_info()
        print(f"Tamaño del archivo: {self.__tamano_archivo} MB")
        print(f"Préstamo máximo: {self.MAX_DIAS} días")



def buscar_libro(codigo, registros):
    return next((libro for libro in registros if libro.get_codigo() == codigo), None)



#menu
def menu():
    registros = []

    while True:
        print("\n=== Biblioteca ===")
        print("1. Registrar libros")
        print("2. Prestar libros")
        print("3. Devolver libro")
        print("4. Consultar libros")
        print("5. Salir\n")

        opcion = input("Seleccione una opción: ").strip()

        if opcion == "1":
            print("\n-- Registro de libro --")
            tipo = input("1. Libro físico  o  2. Libro digital: ").strip()
            titulo = input("Ingrese el título: ").title()
            autor = input("Ingrese el autor: ").title()

            if tipo == "1":
                try:
                    numero = int(input("Número de ejemplar: "))
                    registros.append(LibroFisico(titulo, autor, numero))
                    print("\nLibro físico registrado con éxito.\n")
                except ValueError:
                    print("\nIngrese un número válido.\n")

            elif tipo == "2":
                try:
                    tamano = float(input("Tamaño del archivo (MB): "))
                    if tamano <= 0:
                        raise ValueError
                    registros.append(LibroDigital(titulo, autor, tamano))
                    print("\nLibro digital registrado con éxito.\n")
                except ValueError:
                    print("\nIngrese un valor válido.\n")

            else:
                print("\nTipo no válido.\n")

        elif opcion == "2":
            disponibles = [libro for libro in registros if libro.get_estado() == "Disponible"]
            if disponibles:
                print("\n=== Libros disponibles para prestar ===")
                for libro in disponibles:
                    print(f"Código: {libro.get_codigo()} | Título: {libro.get_titulo()}")
            else:
                print("\nNo hay libros disponibles para prestar.\n")
                continue
            codigo = input("\nIngrese el código del libro a prestar: ").upper()
            libro = buscar_libro(codigo, registros)
            if libro and libro.get_estado() == "Disponible":
                libro.prestar()
                print("")  
            else:
                print("\n No se encontró un libro disponible con ese código.\n")

        elif opcion == "3":
            prestados = [libro for libro in registros if libro.get_estado() == "Prestado"]
            if prestados:
                print("\n Libros prestados para devolver ")
                for libro in prestados:
                    print(f"Código: {libro.get_codigo()} | Título: {libro.get_titulo()}")
            else:
                print("\nNo hay libros prestados para devolver.\n")
                continue
            codigo = input("\nIngrese el código del libro a devolver: ").upper()
            libro = buscar_libro(codigo, registros)
            if libro and libro.get_estado() == "Prestado":
                libro.devolver()
                print("")  
            else:
                print("\nNo se encontró el libro.\n")

        elif opcion == "4":
            if registros:
                print("\n=== Lista de libros registrados ===\n")
                for libro in registros:
                    libro.mostrar_info()
                    print("\n--------------------\n")
            else:
                print("\nNo hay libros registrados.\n")

        elif opcion == "5":
            print("\nSaliendo del sistema...\n")
            break

        else:
            print("\nOpción no válida. Intente de nuevo.\n")
    registros = []

    while True:
        print("Biblioteca")
        print("1. Registrar libros")
        print("2. Prestar libros")
        print("3. Devolver libro")
        print("4. Consultar libros")
        print("5. Salir")

        opcion = input("Seleccione una opción: ").strip()

        if opcion == "1":
            print("Registro de libro ")
            tipo = input("1. Libro físico  o  2. Libro digital  ").strip()
            titulo = input("Ingrese el título: ").title()
            autor = input("Ingrese el autor: ").title()

            if tipo == "1":
                try:
                    numero = int(input("Número de ejemplar: "))
                    registros.append(LibroFisico(titulo, autor, numero))
                    print("Libro físico registrado con éxito.")
                    print("")
                except ValueError:
                    print("Ingrese un número válido")
                    print("")

            elif tipo == "2":
                try:
                    tamano = float(input("Tamaño del archivo (MB): "))
                    if tamano <= 0:
                        raise ValueError
                    registros.append(LibroDigital(titulo, autor, tamano))
                    print("Libro digital registrado con éxito.")
                    print("")
                except ValueError:
                    print("Ingrese un valor valido")
                    print("")

            else:
                print("Tipo no válido.")

        elif opcion == "2":
            codigo = input("Ingrese el código del libro a prestar: ").upper()
            libro = buscar_libro(codigo, registros)
            if libro:
                libro.prestar()
            else:
                print("No se encontró un libro con ese código.")

        elif opcion == "3":
            codigo = input("Ingrese el código del libro a devolver: ").upper()
            libro = buscar_libro(codigo, registros)
            if libro:
                libro.devolver()
            else:
                print("No se encontró un libro con ese código.")
                print("")

        elif opcion == "4":
            if registros:
                print("Lista de libros registrados:")
                for libro in registros:
                    libro.mostrar_info()
                    print("--------------------")
            else:
                print("No hay libros registrados.")
                print("")

        elif opcion == "5":
            print("Saliendo del sistema")
            print("")
            break

        else:
            print("Opción no válida. Intente de nuevo.")
    registros = []

    while True:
        print("Biblioteca")
        print("1. Registrar libros")
        print("2. Prestar libros")
        print("3. Devolver libro")
        print("4. Consultar libros")
        print("5. Salir")

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            print("\n-- Registro de libro --")
            tipo = input("1. Libro físico  2. Libro digital  ").upper()
            titulo = input("Ingrese el título: ")
            autor = input("Ingrese el autor: ")

            if tipo == "1":
                numero = input("Número de ejemplar: ")
                libro = LibroFisico(titulo, autor, numero)
                libros.append(libro)
                print("Libro físico registrado con éxito.")

            elif tipo == "2":
                tamano = float(input("Tamaño del archivo (MB): "))
                libro = LibroDigital(titulo, autor, tamano)
                libros.append(libro)
                print("Libro digital registrado con éxito.")

            else:
                print("Tipo no válido.")

        elif opcion == "2":
            codigo = input("Ingrese el código del libros a prestar: ")
            libro = buscar_libro(codigo, libros)
            if libros:
                libros.prestar()
            else:
                print("No se encontró un libro con ese código.")

        elif opcion == "3":
            codigo = input("Ingrese el código del libros a devolver: ")
            libros = libros(codigo, libros)
            if libros:
                libros.devolver()
            else:
                print("No se encontró un libros con ese código.")

        elif opcion == "4":
            if libros:
                print("\n Lista de libros registrados ")
                for m in libros:
                    m.mostrar_info()
                    print("--------------------")
            else:
                print("No hay libros registrados.")

        elif opcion == "5":
            print("Saliendo del sistema")
            break

        else:
            print("Intente de nuevo.")



if __name__ == "__main__":
    menu()
