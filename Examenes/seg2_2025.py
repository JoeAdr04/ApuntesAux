class Persona:
    def __init__(self, nom= "", ed=0, pes=0):
        self.__nombre = nom
        self.__edad = ed
        self.__peso = pes
        
    def getPeso(self):
        return self.__peso
    
    def getEdad(self):
        return self.__edad
        
class Cabina:
    def __init__(self, nro):
        self.__nroCabina = nro
        self.__personasAbordo = []
        
    def getNro(self):
        return self.__nroCabina
        
    def agregarPersona(self, per:Persona):
        self.__personasAbordo.append(per)
        
    def cumpleNorma(self):
        sum =0
        for p in self.__personasAbordo:
            sum =sum+p.getPeso()
        if(sum >=850 or len(self.__personasAbordo) >=10):
            return False
        return True
    
    def getPersonasAbordo(self):
        return self.__personasAbordo
        
class Linea:
    #declaro los atributos fuera 
    #ArrayList<Cabina> cabinas = new ArrayList<>();
    def __init__(self, col): ##cosntructor
        self.__color = col
        self.__filaPersonas = []
        self.__cabinas = []
        # (java) ArrayList<Cabina> cabinas = new ArrayList<>();
        self.__cantidadCabinas =0
        self.__cabinas.append(Cabina(1))
        self.__cabinas.append(Cabina(2))
        self.__cabinas.append(Cabina(3))
    
    def llenarFila(self, per):
        self.__filaPersonas.append(per)    
    
    def getColor(self):
        return self.__color
    
    def agregarCabina(self, cab):
        self.__cabinas.append(cab)
        
    def getCabinas(self):
        return self.__cabinas
    
    def sacarPrimeraPersona(self):
        per = self.__filaPersonas[0]
        self.__filaPersonas.pop(0)
        return per
    
    def calcularIngresosTarRegular(self):
        sum = 0
        for c in self.__cabinas:
            for p in c.getPersonasAbordo():
                if(p.getEdad()>25 or p.getEdad() <60):
                    sum = sum + 3
                #else:
                    #sum = sum + 1.5
        return sum


class MiTeleferico:
    def __init__(self):
        self.__lineas = []
        self.__cantidadIngresos = 0.0
        self.__lineas.append(Linea("Roja".upper()))
        self.__lineas.append(Linea("Amarilla".upper()))
        self.__lineas.append(Linea("Verde".upper()))
        
    def agregarLinea(self, lin):
        self.__lineas.append(lin)
        
    def llenarFila(self, per ,color):
        for l in self.__lineas:
            if(l.getColor().upper() == color.upper()):
                l.llenarFila(per)
    #inciso a    
    def agregarPersonaFila(self, colorLinea, cabx):
        for l in self.__lineas:
            if(colorLinea.upper() == l.getColor().upper()):
                for c in l.getCabinas():
                    if (c.getNro() == cabx):
                        if (c.cumpleNorma() == True):
                            c.agregarPersona((l.sacarPrimeraPersona()))
    
    #inciso b
    def verificarReglas(self):
        for l in self.__lineas:
            for c in l.getCabinas():
                if (c.cumpleNorma() == True):
                    print(f"Cabina {c.getNro()}, de la linea {l.getColor()} cumple las normas establecidas por mi telferico")
    
    def calculaIngreso(self):
        for l in self.__lineas:
            for c in l.getCabinas():
                for p in c.getPersonasAbordo():
                    if(p.getEdad()>25 or p.getEdad() <60):
                        self.__cantidadIngresos = self.__cantidadIngresos + 3
                    else:
                        self.__cantidadIngresos = self.__cantidadIngresos + 1.5
        print(f"Ingresos Totales: {self.__cantidadIngresos}")
        
    def mayorIngreso(self):
        may =0
        for l in self.__lineas:
            if(l.calcularIngresosTarRegular() > may):
                may = l.calcularIngresosTarRegular()
                
        for l in self.__lineas:
            if(l.calcularIngresosTarRegular() == may):
                print(f"linea con mayor ingreso en tarifa regular {l.getColor()}")
        
        
class Main():
    tel = MiTeleferico()
    tel.llenarFila(Persona("juan", 25, 80), "Roja")
    tel.llenarFila(Persona("MARIA", 20, 60), "Amarilla")
    tel.llenarFila(Persona("luis", 43, 80), "Verde")
    tel.llenarFila(Persona("joel", 12, 100), "Roja")
    tel.llenarFila(Persona("andrea", 21, 50), "Amarilla")
    tel.llenarFila(Persona("clara", 90, 50), "Verde")
    #ALT + SHIFT + FLECHAABAJO(DUPLICAR LINEA DE CODIGO)
        
    #inciso a
    tel.agregarPersonaFila("Roja",2)
    tel.agregarPersonaFila("Roja",2)
    tel.agregarPersonaFila("Amarilla",1)
    
    #inciso b
    tel.verificarReglas()
    
    #inciso c
    tel.calculaIngreso()
    
    #inciso d:
    tel.mayorIngreso()
    