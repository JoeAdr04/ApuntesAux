import json
import os
class Archivos:
    def __init__(self, ruta):
        self.__ruta = ruta
        if(not os.path.exists(self.__ruta)):
            print("archivo creado")
            with open(self.__ruta, "w") as arch:
                json.dump([], arch, indent=2)
    
class Main():
    a = Archivos("prueba1.json")
