class Persona:
    def __init__(self, nom, ed):
        self.__nombre = nom
        self.__edad = ed

    def saludar(self):
        print(f"hola {self.__nombre}")

    def saludar(self, x):
        print(f"hola {x}")

class Main():

    p = Persona("joel", 25)
    p.saludar()
    p.saludar("luis")