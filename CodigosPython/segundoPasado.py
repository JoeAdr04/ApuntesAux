class Anuncio:
    def __init__(self, num=0, pre=0.1):
        self.__numero = num
        self.__precio = pre

class Artista:
    def __init__(self, nom, car, anios):
        self.__nombre = nom
        self.__ci = car
        self.__aniosExp = anios

    def getAnios(self):
        return self.__aniosExp

class Obra:
    
    def __init__(self, titulo, material, nom1, car1, anio1, nom2, car2, anio2):
        self._titulo = titulo 
        self._material = material
        self._artista1 = Artista(nom1, car1, anio1)
        self._artista2 = Artista(nom2, car2, anio2)
        self._anuncio = None

    def agregarAnuncio(self, anun):
        self._anuncio = anun

    def getArt1(self):
        return self._artista1

class Pintura(Obra):
    def __init__(self, titulo:str, material:str, nom1, car1, anio1, nom2, car2, anio2, gen):
        super().__init__(titulo, material, nom1, car1, anio1, nom2, car2, anio2)
        self.__genero = gen
        


class Main():
    a1 = Anuncio() #instancia
    a2 = Anuncio(2, 2.3)
    #art1 = Artista()

    #inciso a
    p1 = Pintura("monalisa", "oleo", "davinci", 123, 20, "joel", 321, 1, "intriga")
    
    p2 = Pintura("monalisa", "oleo", "davinci", 123, 20, "adrian", 444, 4, "cuatro")

    p2.agregarAnuncio(a1)

    #aux = p1.getArt1()
    print(type((p1.getArt1()).getAnios()))
    #print(type(aux))
