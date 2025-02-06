from numpy import array 
import numpy as np 

class ArreglosNP: 
    
    def __init__ (self, v):
        self.arregloNP=np.array(v)
    def insertarNP (self,v):
        self.arregloNP=np.insert(self.arregloNP,i,v)
        print(self.arregloNP)
    def eliminarNP (self,i):
        self.arregloNP= np.delete(self.arregloNP,i)
        print(self.arregloNP)
    def modificarNP (self,i,w):
        self.arregloNP[i]=w
        print(self.arregloNP)

class Lista: 
    def __init__(self,v):
        self.listi=[]
    def insertar (self,v):
        self.listi.append(v)
        print (self.listi)
    def eliminar (self,i):
        self.listi.pop(i)
        print(self.listi)
    def modificar (self,i,w):
        self.listi[i]=w
        print(self.listi)

v=7
i=0
w=8


arreglos= ArreglosNP(v)

arreglos.insertarNP(3)
arreglos.insertarNP(6)
arreglos.insertarNP(9)

arreglos.modificarNP(2,5)
print("eliminar")
arreglos.eliminarNP(0)

print("Listas-----------------------")
listi1= Lista(v)
listi1.insertar(11)
listi1.insertar(12)
listi1.insertar(13)
listi1.insertar(14)
listi1.eliminar(1)
listi1.modificar(1,20)
