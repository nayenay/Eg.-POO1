#clase del 27 de marzo del 2025 POO1 en python 
#crear lista de 5 valores mixtos
# Crear listas de 5 valores del mismmo tipo con umpy
# listas anteriores convertirlas a tuplas y conjuntos 
# crear un diccionario de 5 elementos con valores de distintos tipos

import numpy as np
from numpy import array
listilla1=np.array([2,3,4,5,6])
listilla2=[21,22,23,24,25]
listilla3=list([30,31,32,33,34])
tuplita1=tuple(map(int, listilla1))
conjuntillo1=set(map(float,listilla1))
conjuntillo2=set(listilla2)
diccionario1={"a":88,"b":"bb"}


print(listilla1)
print(tuplita1)
print(conjuntillo1) 
print(conjuntillo2)  
print(diccionario1)

listilla2.append(99)
print(listilla2)
listilla2.insert(1,98)
print(listilla2)
listilla2.extend([2,"hola"])
print(listilla2)
listilla2.index()
print(listilla2)
listilla2.count()
print(listilla2)
