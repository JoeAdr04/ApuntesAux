class Servidor:
    def __init__(self, ju1="joel",diamant = 2000):
        self.__jugadores= []
        self.__diamantes = []
        self.__jugadores.append(ju1)
        self.__diamantes.append(diamant)
    
    def agregarJugador(self, jug, diamant):
        self.__jugadores.append(jug)
        self.__diamantes.append(diamant)

    def verificarStacks(self):
        for i in range(len(self.__jugadores)):
            cantidad = self.__diamantes[i]//64
            print(f"Jugador: {self.__jugadores[i]} tiene {cantidad} de stacks de diamante")
            
    def masDiamantes(self):
        pos = 0
        may = 0
        for i in range(len(self.__jugadores)):
            if(self.__diamantes[i]>=may):
                may = self.__diamantes[i]
                pos = i
        print(f"Jugador con mas diamantes: {self.__jugadores[pos]}, tiene: {self.__diamantes[pos]} diamantes")
        
    def totalDiamantes(self):
        sum =0
        for d in self.__diamantes: #d tomara cada valor del arreglo [200, 239, 78]
            sum +=d
        print(f"Diamantes conseguidos en el servidor: {sum}")
            
    def mostrar(self):
        for j in range(len(self.__jugadores)):
            print(f"Jugador {self.__jugadores[j]}, diamantes: {self.__diamantes[j]}")

class Main():
    s = Servidor()
    #funcione spara el inciso a)
    s.agregarJugador("Angel",129)
    s.agregarJugador("Mari",78)
    s.mostrar()
    #funcion para el incisio b)
    s.verificarStacks()
    #funcion para el inciso c)
    s.masDiamantes()
    #funcion para el inciso d)
    s.totalDiamantes()