class Animal:
    def __init__(self, nombre, edad, nombreDueno):
        self.nombre = nombre
        self.edad = edad
        self.nombreDueno = nombreDueno

class Perro(Animal):
    def __init__(self, nombre, edad, nombreDueno, requiereBosal, ladraFuerte):
        super().__init__(nombre, edad, nombreDueno)
        self.requiereBosal = requiereBosal
        self.ladraFuerte = ladraFuerte

class Gato(Animal):
    def __init__(self, nombre, edad, nombreDueno, cazaRatones, tomaLeche):
        super().__init__(nombre, edad, nombreDueno)
        self.cazaRatones = cazaRatones
        self.tomaLeche = tomaLeche

class CentroVeterinario:
    def __init__(self, nombre):
        self.nombre = nombre
        self.perros = []
        self.gatos = []

    def agregarperro(self, perro):
        if len(self.perros) < 100:
            self.perros.append(perro)

    def agregar_gato(self, gato):
        if len(self.gatos) < 100:
            self.gatos.append(gato)

    def ordenarperros(self):
        n = len(self.perros)
        for i in range(n):
            for j in range(0, n - i - 1):
                p1 = self.perros[j]
                p2 = self.perros[j + 1]

                cambiar = False
                if p1.edad > p2.edad:
                    cambiar = True
                elif p1.edad == p2.edad:
                    if p1.nombreDueno > p2.nombreDueno:
                        cambiar = True
                    elif p1.nombreDueno == p2.nombreDueno:
                        if p1.nombre > p2.nombre:
                            cambiar = True
                if cambiar:
                    self.perros[j], self.perros[j + 1] = self.perros[j + 1], self.perros[j]

    def ordenargatos(self):
        n = len(self.gatos)
        for i in range(n):
            for j in range(0, n - i - 1):
                g1 = self.gatos[j]
                g2 = self.gatos[j + 1]

                cambiar = False

                # 1. primero los que toman leche (True primero)
                if g1.tomaLeche < g2.tomaLeche:
                    cambiar = True
                elif g1.tomaLeche == g2.tomaLeche:
                    # 2. edad descendente
                    if g1.edad < g2.edad:
                        cambiar = True
                    elif g1.edad == g2.edad:
                        # 3. nombre ascendente
                        if g1.nombre > g2.nombre:
                            cambiar = True
    def verificarduenos(self):
        conteo = {}

        for p in self.perros:
            conteo[p.nombreDueno] = conteo.get(p.nombreDueno, 0) + 1

        for g in self.gatos:
            conteo[g.nombreDueno] = conteo.get(g.nombreDueno, 0) + 1

        for dueno, cantidad in conteo.items():
            if cantidad > 1:
                print(f"{dueno} tiene {cantidad} animales")

cv1 = CentroVeterinario("Vet Norte")
cv2 = CentroVeterinario("Vet Sur")

cv1.agregarperro(Perro("Rex", 5, "Carlos", True, True))
cv1.agregarperro(Perro("Max", 3, "Carlos", False, True))

cv1.agregar_gato(Gato("Michi", 2, "Ana", True, True))
cv1.agregar_gato(Gato("Luna", 4, "Carlos", False, False))

cv1.ordenarperros()
cv1.ordenargatos()

print("\nDueños con más de un animal:")
cv1.verificarduenos()