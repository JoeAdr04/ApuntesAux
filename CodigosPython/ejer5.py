class Servidor:
    def __init__(self, ju1="joel",diamant = 2000):
        self.__jugadores= []
        self.__diamantes = []
        self.__jugadores.append(ju1)
        self.__diamantes.append(diamant)
    
    def agregarJugador(self, jug, diamant):
        self.__jugadores.append(jug)
        self.__diamantes.append(diamant)

    def mostrar(self):
        for j in range(len(self.__jugadores)):
            print(f"Jugador {self.__jugadores[j]}, diamantes: {self.__diamantes[j]}")

class Main():
    s = Servidor()
    s.agregarJugador("Angel",5)
    s.mostrar()