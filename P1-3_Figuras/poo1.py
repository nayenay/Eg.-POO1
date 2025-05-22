#Calcular figuras geométricas
#comentario
from math import pi, tan, sqrt
print ("SI")
NL=int(input("Cuántos lados tiene la figura?"))
L= int(input("Cuánto mide cada lado?"))

class Figura: 
    def perimetro(NL,L):
        p = NL * L
        return print("Perimetro= ",p)
    def a3(L):
        a=L*(sqrt((L**2)-((L/2)**2)))/2
        return print("Área del triángulo= ",a)   
    def a4(L):
        a=L*L 
        return print("Área del cuadrado= ",a) 
    def poly(NL,L):
        a=((NL*L*L)/(4*(tan(pi/NL))))
        return print("Área del polígono= ",a) 
    
    

Figura.perimetro(NL,L)
#if (NL==3):
#    Figura.a3(L)
#if (NL==4):
#    Figura.a4(L)   
#if (NL>4):
    
    
Figura.poly(NL,L)