class Anime:
    def __init__(self, nombre: str, genero: str, nroEpisodios: int):
        self.nombre = nombre
        self.genero = genero
        self.__nroEpisodios = nroEpisodios
        self.__episodios = []
    def __str__(self):
        return f"Anime: {self.nombre}, Género: {self.genero}, Episodios: {self.__nroEpisodios}"
if __name__ == "__main__":
    a1 = Anime("JujutsuKaisen", "Shonen", 60)
    a2 = Anime("Death Note", "Misterio", 37)
    print(a1)
    print(a2)