import json
import os

class Etudiante:
    def __init__(self, mat, car, nom):
        self.__matricula = mat
        self.__carnet = car
        self.__nombre =nom

    def toDict(self):
        return {
            "matricula":self.__matricula,
            "carnet": self.__carnet,
            "nombre" :self.__nombre
        }
    
    @staticmethod
    def dicAObj(dic):
        e = Estudiante(dic.get("matricula"), dic.get("carnet"),dic.get("nombre"))
        return e
class ArchEstudiante:
    def __init__(self, ruta:str):
        self.__ruta = ruta
        if(not os.path.exists(self.__ruta)):
            print("archivo creado")
            with open(self.__ruta, "w") as arch:
                json.dump([], arch, ensure_ascii=False, indent=2)
    
    def leer(self):
        with open(self.__ruta, "r") as arch:
            try:
                datos = json.load(arch)
                print(f"datos recuperados de: {self.__ruta}")
            except Exception as e:
                print("ha fallado todo lo que podia fallar al leer", e)
                datos = []
        return datos
    
    def modificar(self, di):
        try:    
            with open(self.__ruta, "w") as arch:
                json.dump(di, arch,ensure_ascii=False, indent=2)
                print(f"Datos modificados en {self.__ruta}")
        except Exception as j:
            print("ha fallado todo lo que podia fallar al modificar", j)

class Main:
    e1 = Etudiante(1, 2, "joel")
    a = ArchEstudiante("estudiantes.json")
    arr = a.leer()
    arr.append(e1.toDict())

    a.modificar(arr)

    print("Datos del archivo: ")
    print(a.leer())