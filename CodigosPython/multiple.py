class Animal:
    def __init__(self, gen, col):
        self._genero = gen
        self._color = col
    
    def __str__(self):
        return f"genero: {self._genero}, color: {self._color}"

    def getDuenio(self):
        return self._duenio

class Mamifero(Animal):
    def __init__(self, gen, col, ed):
        Animal.__init__(self, gen, col)
        self._edad =ed
    def __str__(self):
        return f"{super().__str__()}, edad:{self._edad} (mammifero)"
        
class Mascota(Animal):
    def __init__(self, gen, col, due):
        Animal.__init__(self,gen, col)
        self._duenio = due

    def __str__(self):
        return f"{super().__str__()}, duenio:{self._duenio} (mascota)"

    


class Perro(Mascota, Mamifero):
    def __init__(self, gen, col, ed, due, nom):
        Mamifero.__init__(self, gen, col, ed)
        Mascota.__init__(self, gen, col, due)
        self.__nombre = nom
    
    def __str__(self):
        return f"{super().__str__()}"

    
class Main():
    p = Perro("macho", "cafe", 4, "joel", "boby")


    print(p)
    print(p.getDuenio())