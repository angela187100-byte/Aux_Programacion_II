class Instrumento:
    def __init__(self, nombre, material, tipo):
        self.nombre = nombre
        self.material = material
        self.tipo = tipo

    def __str__(self):
        return f"{self.nombre} - {self.material} - {self.tipo}"


inst1 = Instrumento("Guitarra", "Madera", "Cuerda")
inst2 = Instrumento("Flauta", "Metal", "Aire")

print(inst1)
print(inst2)