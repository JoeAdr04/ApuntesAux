import json
import os

class Mascota:
    def __init__(self, nom, due):
        self.__nombre = nom
        self.__duenio = due
    def __str__(self):
        return f"nomnbre:{self.__nombre}, duenio: {self.__duenio}"
    def toDict(self):
        return {
            "nombre": self.__nombre,
            "duenio": self.__duenio
        }
    def getNombre(self):
        return self.__nombre

    def setDuenio(self, d):
        self.__duenio = d

    @staticmethod
    def convertir(algo):
        m = Mascota(algo.get("nombre"), algo.get("duenio"))
        return m

class Archivos:
    def __init__(self, ruta):
        self.__ruta = ruta
        if(not os.path.exists(self.__ruta)):
            print("archivo creado")
            with open(self.__ruta, "w") as arch:
                json.dump([], arch, indent=2)

    def leer(self):
        with open(self.__ruta, "r") as arch:
            try:
                datos = json.load(arch)
                print(f"datos recuperados de: {self.__ruta}")
            except Exception as e:
                print("ha fallado todo lo que podia fallar al leer", e)
                datos = []
        return datos

    def modificar(self, algo):
        try:    
            with open(self.__ruta, "w") as arch:
                json.dump(algo, arch, indent=2)
                print(f"Datos modificados en {self.__ruta}")
        except Exception as j:
            print("ha fallado todo lo que podia fallar al modificar", j)
    
class Main():
    arch = Archivos("Mascotas.json")

    while True:
        print('''Opciones:
        1. llenar datos
        2. leer todo
        3. cambiar duenio
        0. salir
        ''')
        opt = input("Elije una opcion: ").strip()
        if (opt == "1"):
            arr = arch.leer()
            nom = input("Ingresa Nombre mascota: ")
            due = input("ingresa nomnbre duenio")
            masc = Mascota(nom, due)
            arr.append(masc.toDict())
            arch.modificar(arr)
        elif(opt == "2"):
            print(arch.leer())
        
        elif(opt == "3"):
            arr = arch.leer()
            obj = []
            mas = input("NOmbre de la mascota?: ")
            for m in arr:
                obj.append(Mascota.convertir(m))
            
            for m in obj:
                if(m.getNombre() == mas):
                    nuevo = input("nuevo duenio: ")
                    m.setDuenio(nuevo)
            print(obj)
            arr =[]   
            for m in obj:
                arr.append(m.toDict())

        elif(opt == "0"):
            break
        else:
            print("opcon invalida, intenta denuevo")