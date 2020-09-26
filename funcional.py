class Edo:
    def __init__(self,nombre,padre):
        self.nombre = nombre
        self.padre = padre

def miembro(edo,lista):
    resp = False
    for nodo in lista:
        if nodo.nombre == edo:
            resp = True
            break
    return resp

def getHijos(edo,proble):
    return proble[edo]

def expandir(edo,proble,Abiertos,Cerrados):
    hijos=getHijos(edo,proble)
    for hijo in hijos :
        if not miembro(hijo,Abiertos)and not miembro (hijo,Cerrados) :
            Abiertos.append(Edo(hijo,edo))
    return Abiertos

def sigue_ampl(Abiertos):
    resp = Abiertos[0]
    del Abiertos[0]
    return Abiertos,resp

def sigue_prof(Abiertos):
    resp = Abiertos[-1]
    del Abiertos[-1]
    return Abiertos,resp

def getOrden(Cerrados):
    resp =[]
    for nodo in Cerrados :
        resp.append(nodo.nombre)
    return resp

def getCamino(ini,Cerrados):
    resp=[]
    edo = Cerrados[-1].nombre
    listo = False
    while not listo :
        if edo == ini:
            listo = True
            resp.insert (0,edo)
        else:
            for nodo in Cerrados:
                if nodo.nombre == edo:
                    resp.insert (0,nodo.nombre)
                    edo = nodo.padre
                    break
    return resp

def primAmp(ini,meta,proble):
    Abiertos =[Edo(ini,ini)]
    Cerrados =[]
    listo = False
    while not listo:
        Abiertos,actual=sigue_ampl(Abiertos)
        if actual.nombre == meta:
            listo = True
            Cerrados.append(actual)
        else:
            Abiertos = expandir ( actual.nombre,proble,Abiertos,Cerrados)
            Cerrados.append(actual)
    return Cerrados

def primProf(ini,meta,proble):
    Abiertos = [Edo (ini,ini)]
    Cerrados = []
    listo = False
    while not listo:
        Abiertos,actual = sigue_prof(Abiertos)
        if actual.nombre == meta:
            listo = True
            Cerrados.append(actual)
        else:
            Abiertos = expandir(actual.nombre,proble,Abiertos,Cerrados)
            Cerrados.append(actual)
    return Cerrados

def main(ini,meta):
    
    proble={ 
        'A':['B','D','E'], 
        'B':['A','C','F'], 
        'C':['B','D','F','G'], 
        'D':['A','C','E','G'], 
        'E':['A','D','G'], 
        'F':['B','C','G','H'],
        'G':['C','D','E','F'],
        'H':['F']
    }
    
    Cerrados = primAmp(ini,meta,proble)
    orden = getOrden(Cerrados)
    print("Orden de visita segun primero en amplitud: ")
    print(orden)
    Cerrados = primProf(ini,meta,proble)
    camino = getCamino(ini,Cerrados)
    print("Camino segun primero en profundidad :")
    print(camino)


    

if __name__ == "__main__":
    print("En que nodo quieres iniciar?")
    nodo1= input()
    print("En que nodo quieres terminar?")
    nodo2= input()
    main(nodo1,nodo2)