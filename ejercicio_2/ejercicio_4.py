#c=capacidad
#p=pasajeros
#sp=subir pasajeros
#cp = cobrar pasaje
#ad = asientos disponibles
#ca = cantidad

class Bus:
    def __init__(self, c):
        self.c = c
        self.p = 0

    def sp(self, ca):
        if self.p + ca <= self.c:
            self.p = self.p + ca
        else:
            print("No hay suficientes asientos")

    def cp(self):
        total = self.p * 1.50
        print("Total a cobrar:", total, "bs")

    def ad(self):
        disponibles = self.c - self.p
        print("Asientos disponibles:", disponibles)

bus1 = Bus(40)

bus1.sp(25)
bus1.cp()
bus1.ad()