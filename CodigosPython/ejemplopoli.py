class Persona:
    def __init__(self, nom, ed): #comstructor
        self.__nombre = nom
        self.__edad = ed

    def saludar(self): #metodo saludar
        print(f"hola {self.__nombre}")

    def saludar(self, x): #metodo saludar sobreescrito
        print(f"hola {x}")
    
    def text(self):
        return f"{self.__nombre}{self.__edad}"

class Main():

    p = Persona("joel", 25) #instancia de la clase persona
    #p.saludar()
    p.saludar("luis")
    print(p.text())