class Persona:
    def __init__(self, nom, car, ed):
        self._nombre = nom
        self._carnet = car
        self._edad = ed
    
    def mostrar(self):
        return f"nombre{self._nombre}"
    def __str__(self):
        return f"nombre: {self._nombre}, carnet:{self._carnet}, edad: {self._edad}(clase padre)"

class Estudiante(Persona):
    def __init__(self, nom, ed, car, mat, carr):
        super().__init__(nom, car, ed)
        self.__matricula = mat
        self.__carrera = carr

    def mostrar(self):
        return f"{super().mostrar()}, matricula: {self.__matricula}, carnet:{self._carnet}"
    def __str__(self):
        #super().__str__() hereda el metododo __str__ de la clase padre
        return f"{super().__str__()} matricula: {self.__matricula}, carrera: {self.__carrera}"

class Docente(Persona):
    def __init__(self, nom, ed, car,ant, suel):
        super.__init__(nom, ed, car)
        self.__antiguedad = ant
        self.__sueldo = suel

    def __str__(self):
        #tambien puedo jalar el atributo protegio
        return f"nombre: {self._nombre}, carnet: {self._carnet}, edad: {self._edad}"

class Main():
    p = Persona("joel", 1234, 25)
    print(p.mostrar())
    e = Estudiante("luis", 4321, 21, 5555, "Informatica")
    print(e.mostrar())
    print(e)