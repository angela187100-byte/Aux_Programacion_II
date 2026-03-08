class Servidor:

    def __init__(self):
        self.jugadores = []
        self.diamantes = []

    # para agregar jugadores
    def agregarjugador(self, nombre, cantidaddiamantes):
        if len(self.jugadores) < 10:
            self.jugadores.append(nombre)
            self.diamantes.append(cantidaddiamantes)
        else:
            print("Servidor lleno")

    # stacks de ltodos los diamantes
    def stacks(self):
        for i in range(len(self.jugadores)):
            stacks = self.diamantes[i] // 64
            print(self.jugadores[i], "tiene", stacks, "stacks")

    # el juagodor con mas daiamantes
    def jugadormasdiamantes(self):
        mayor = self.diamantes[0]
        nombre = self.jugadores[0]

        for i in range(len(self.diamantes)):
            if self.diamantes[i] > mayor:
                mayor = self.diamantes[i]
                nombre = self.jugadores[i]

        print("Jugador con mas diamantes:", nombre)

    # para el total de los diamnates
    def totaldiamantes(self):
        total = 0
        for i in range(len(self.diamantes)):
            total = total + self.diamantes[i]

        print("Total de diamantes:", total)

server = Servidor()
server.agregarjugador("corhyn", 120)
server.agregarjugador("angela", 65)
server.agregarjugador("paucara", 30)

server.stacks()
server.jugadormasdiamantes()
server.totaldiamantes()