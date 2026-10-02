from multimethod import multimethod
class LineaTeleferico:
    def __init__(self, col="Rojo", tram="Estación Central, Estación Cementerio, Estación 16 de Julio", nroC="20"):
        self.__color = col
        self.__tramo = tram
        self.__nroCabinas = nroC
        self.__nroEmpleados = 0
        self.__empleados =[]
        self.__edades = []
        self.__sueldos = []
    
    def getColor(self):
        return self.__color
    def agregarEmpleado(self, nom, ap1, ap2, ed, s):
        vec = [nom, ap1, ap2]
        self.__empleados.append(vec)
        self.__edades.append(ed)
        self.__sueldos.append(s)
        self.__nroEmpleados +=1
    
    def eliminar(self, x):
        pos =0
        for e in self.__empleados:
            if(e[1] == x or e[2]== x):
                self.__empleados.pop(pos)
            else:
                pos+=1
    
    def mostrar(self):
        for e in self.__empleados:
            print(e)
            
    def __add__(self, params):
        otro, x = params
        pos =0
        if(isinstance(otro,LineaTeleferico)):
            for e in self.__empleados:
                if(x == e[0]):
                    otro.agregarEmpleado(e[0], e[1], e[2], self.__empleados[pos], self.__sueldos[pos])
                    self.__empleados.pop(pos)
                else:
                    pos+=1
                    
    def mayEdad(self):
        may =0
        for i in range(len(self.__empleados)):
            if(self.__edades[i]>may):
                may =self.__edades[i]
        return may
    
    def maySueldo(self)->float:
        may =0.0
        for i in range(len(self.__empleados)):
            if(self.__sueldos[i]>may):
                may =self.__sueldos[i]           
        return may
    @multimethod    
    def mostrarMay(self, may:int):
        for i in range(len(self.__empleados)):
            if(self.__edades[i]==may):
                print(f"nom:{self.__empleados[i][0]}")
                
    @multimethod            
    def mostrarMay(self, may:float):
        for i in range(len(self.__empleados)):
            if(self.__sueldos[i]==may):
                print(f"nom:{self.__empleados[i][0]}")
class Main():
    t1 = LineaTeleferico()
    t1.agregarEmpleado("Pedro", "Rojas", "Luna", 35, 3500.00)
    t1.agregarEmpleado("Lucy", "Sosa", "Rios",43, 3250.00)
    t1.agregarEmpleado("Ana", "Perez", "Rojas",26,2700.00)
    t1.agregarEmpleado("Saul", "Arce", "Calle",29,2500.00)
    #t1.eliminar("Arce")
    #t1.mostrar()
    
    t2 = LineaTeleferico("azul", "feria", 16)
    t1.mostrar()
    t1+(t2, "Ana")
    print("----------despues--------")
    t1.mostrar()
    print("---otro objeto------")
    t2.mostrar()
    print("------------ultimo---------")
    may = t1.mayEdad()
    #print(may)
    t1.mostrarMay(may)
    print(t1.maySueldo())
    t1.mostrarMay(t1.maySueldo())