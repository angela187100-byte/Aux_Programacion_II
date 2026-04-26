class Libro:
    def __init__(self, nombre, autor, anio):
        self.nombre = nombre
        self.autor = autor
        self.anio = anio

    def mostrar(self):
        print(f"Libro: {self.nombre}, Autor: {self.autor}, Año: {self.anio}")


class Biblioteca:
    def __init__(self, nombre):
        self.nombre = nombre
        self.libros = []

    def agregar_libro(self, libro):
        if len(self.libros) < 100:
            self.libros.append(libro)

    def buscar_libro(self, nombre):
        for libro in self.libros:
            if libro.nombre == nombre:
                libro.mostrar()
                return True
        return False

    def cantidad_libros(self):
        return len(self.libros)

    def mostrar(self):
        print(f"Biblioteca: {self.nombre} ({len(self.libros)} libros)")
        for libro in self.libros:
            libro.mostrar()

b1 = Biblioteca("Central")
b2 = Biblioteca("Zona Sur")

b1.agregar_libro(Libro("Libro 1", "Angela", 2020))
b1.agregar_libro(Libro("Libro 2", "Corhyn", 2018))

b2.agregar_libro(Libro("Libro 3", "Paucara", 2015))
b2.agregar_libro(Libro("Libro 4", "Machicado", 2021))

print("\nBuscar libro 'Python':")
b1.buscar_libro("Libro 1")

print("\nBiblioteca(s) con más libros:")
max_libros = max(b1.cantidad_libros(), b2.cantidad_libros())

if b1.cantidad_libros() == max_libros:
    b1.mostrar()
if b2.cantidad_libros() == max_libros:
    b2.mostrar()