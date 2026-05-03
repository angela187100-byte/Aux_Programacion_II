class Mueble:
    def __init__(self, tipo, material):
        self.tipo = tipo
        self.material = material

class Habitacion:
    def __init__(self, nombre, tamanio):
        self.nombre = nombre
        self.tamanio = tamanio
        self.muebles = []
    def agregar_mueble(self, mueble):
        self.muebles.append(mueble)
    def cant_muebles(self):
        return len(self.muebles)

class Departamento:
    def __init__(self, nro_puerta, nro_piso):
        self.nro_puerta = nro_puerta
        self.nro_piso = nro_piso
        self.habitaciones = []
    def agregar_habitacion(self, habitacion):
        self.habitaciones.append(habitacion)
    def nro_hab(self):
        return len(self.habitaciones)
    def total_muebles(self):
        total = 0
        for h in self.habitaciones:
            total += h.cant_muebles()
        return total

class Parqueo:
    def __init__(self, capacidad, precio_h):
        self.capacidad = capacidad
        self.cant_auto = 0
        self.parqueo = []
        self.precio_h = precio_h

    def agregar_auto(self, placa):
        if self.cant_auto < self.capacidad:
            self.parqueo.append(placa)
            self.cant_auto += 1
            print("Auto agregado correctamente:", placa)
        else:
            print("No hay capacidad disponible en el parqueo")

class Edificio:
    def __init__(self, nombre, superficie):
        self.nombre = nombre
        self.superficie = superficie
        self.deps = []
        self.parqueo = None

    def adicionar_parqueo(self, parqueo):
        self.parqueo = parqueo

    def agregar_departamento(self, departamento):
        self.deps.append(departamento)

    def departamento_mas_habitaciones_piso(self, piso):
        mayor = -1

        for d in self.deps:
            if d.nro_piso == piso:
                if d.nro_hab() > mayor:
                    mayor = d.nro_hab()

        for d in self.deps:
            if d.nro_piso == piso and d.nro_hab() == mayor:
                print("Departamento:", d.nro_puerta)

    def agregar_mueble_departamento(self, nro_puerta, piso, mueble):
        for d in self.deps:
            if d.nro_puerta == nro_puerta and d.nro_piso == piso:
                if len(d.habitaciones) > 0:
                    d.habitaciones[0].agregar_mueble(mueble)
                    print("Mueble agregado")
                    return

        print("Departamento no encontrado")

    def departamento_mas_muebles(self):
        mayor = -1

        for d in self.deps:
            if d.total_muebles() > mayor:
                mayor = d.total_muebles()

        for d in self.deps:
            if d.total_muebles() == mayor:
                print("Departamento:", d.nro_puerta)

    def habitacion_mas_muebles_piso(self, piso):
        mayor = -1

        for d in self.deps:
            if d.nro_piso == piso:
                for h in d.habitaciones:
                    if h.cant_muebles() > mayor:
                        mayor = h.cant_muebles()

        for d in self.deps:
            if d.nro_piso == piso:
                for h in d.habitaciones:
                    if h.cant_muebles() == mayor:
                        print("Habitacion:", h.nombre)

    def es_primo(self, n):
        if n < 2:
            return False

        for i in range(2, n):
            if n % i == 0:
                return False

        return True

    def eliminar_departamentos_hab_prima(self):
        nueva_lista = []

        for d in self.deps:
            if not self.es_primo(d.nro_hab()):
                nueva_lista.append(d)

        self.deps = nueva_lista

ed = Edificio("Edificio Central", 500.0)

p = Parqueo(2, 5.0)
ed.adicionar_parqueo(p)
d1 = Departamento(101, 1)
d2 = Departamento(102, 1)
d3 = Departamento(201, 2)
h1 = Habitacion("Dormitorioo", 20.0)
h2 = Habitacion("Cocina", 12.0)
h3 = Habitacion("Sala", 25.0)
h1.agregar_mueble(Mueble("Cama", "Madera"))
h1.agregar_mueble(Mueble("Ropero", "Madera"))
h2.agregar_mueble(Mueble("Mesa", "Vidrio"))
h3.agregar_mueble(Mueble("Sofa", "Cuero"))
d1.agregar_habitacion(h1)
d1.agregar_habitacion(h2)
d2.agregar_habitacion(h3)
ed.agregar_departamento(d1)
ed.agregar_departamento(d2)
ed.agregar_departamento(d3)

print("b) Departamento con más habitaciones del piso 1:")
ed.departamento_mas_habitaciones_piso(1)
print("c) Agregar mueble al departamento puerta 102 piso 1:")
ed.agregar_mueble_departamento(102, 1, Mueble("Silla", "Metal"))
print("d) Departamento con más muebles:")
ed.departamento_mas_muebles()
print("e) Habitación con más muebles del piso 1:")
ed.habitacion_mas_muebles_piso(1)
print("f) Eliminar departamentos con cantidad prima de habitaciones:")
ed.eliminar_departamentos_hab_prima()
print("Agregar autos al parqueo:")
ed.parqueo.agregar_auto("123ABC")
ed.parqueo.agregar_auto("456DEF")
ed.parqueo.agregar_auto("789GHI")