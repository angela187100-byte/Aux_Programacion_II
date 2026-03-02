class Televisor:
    def __init__(self, marca: str = "", resolucion: int = 0, tipo: str = ""):
        self.__marca = marca
        self.__resolucion = resolucion
        self.__tipo = tipo

    def __str__(self):
        return f"Marca: {self.__marca}, Resolución: {self.__resolucion}p, Tipo: {self.__tipo}"
if __name__ == "__main__":
    tv1 = Televisor("Samsung", 1080, "OLED")
    tv2 = Televisor("LG", 4, "OLED")

    print(tv1)
    print(tv2)