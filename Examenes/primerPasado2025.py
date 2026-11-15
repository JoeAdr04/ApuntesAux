from multimethod import multimethod
class Parqueo:
    
    def __init__(self, nro, tar):
        self.__nroVehiculos = nro
        self.__tarifaHora = tar
        self.__vehiculos = [["123axd", "luis jairo"],
                            ["123axd", "luis jairo"],
                            ["123axd", "luis jairo"]]
        self.__tiempo = [[2, 5],
                         [9,12],
                         [1,3]]
    
    def __add__(self, otro):
        pos = 0
        for v in self.__vehiculos:
            if(v[0] == otro):
                self.__vehiculos.pop(pos)
                self.__tiempo.pop(pos)
            else:
                pos+=1
                
    @multimethod
    def calcularIngreso(self):
        sum = 0
        for t in self.__tiempo:
            sum = ((t[1]- t[0])*self.__tarifaHora)+ sum
        return(sum)
    
    @multimethod
    def calcularIngreso(self, k:int):
        sum = 0
        for t in self.__tiempo:
            time = (t[1]- t[0])
            if(time == k):
                sum = (time*self.__tarifaHora)+ sum
                
        print(f"tarifa de los vehiculos que estuvieron {k} horas es de: {sum}")
            
class Negocio:
    def __init__(self, cap , nom, due):
        self._capital = cap
        self._nombre = nom
        self._duenio = due
        
    def compara(self, otro:"Negocio"):
        if(self._capital == otro._capital or self._duenio == otro._duenio):
            return True
        
    def getCapital(self):
        return self._capital
        
    def __str__(self):
        return f"capital {self._capital}, nombre {self._nombre}"
        
        
class Peluqueria(Negocio):
    def __init__(self, cap=0, nom="asdf", due= "asdf", ubi= "asdf", hora= 5):
        super().__init__(cap, nom, due)
        self.__ubicacion = ubi
        self.__horarioAtencion = hora
        self.__cortes = []
        
class Saltenieria(Negocio):
    def __init__(self, cap, nom, due, hora):
        super().__init__(cap, nom, due)
        self.__horarioAtencion = hora
        self.__pedidos = []
        self.__menu = []
    
class Panaderia(Negocio):
    def __init__(self, cap= "12", nom = "qwer", due = "qwer", mat= "qwer", ub= "qwer"):
        super().__init__(cap, nom, due)
        self.__materiales = mat
        self.__ubicacion = ub
        self.__pedidos = []
        



class Main():

    p = Parqueo(20, 3) #instancia
    p+"1234axd"
    print(f"tarigfatotal {p.calcularIngreso()}")
    p.calcularIngreso(3)
    
    pel1 = Peluqueria()
    pel2 = Peluqueria(65, "xd", "lol", "calle falsa", 13)
    
    sal = Saltenieria(13, "aasdf", "qwerty", 14)
    
    pan1 = Panaderia()
    pan2 = Panaderia(321, "lkjlkj","asdfasdg", "harina", "calle verdadera" )
    
    pan1.compara(sal)
    
    negocios =[pel1, pel2, sal, pan1, pan2]
    may = 0
    for n in negocios:
        if(n.getCapital() >may):
            may = n.getCapital()
    for n in negocios:
        if(n.getCapital() == may):
            print(n)