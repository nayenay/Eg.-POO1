#P13 Conjuntos (es solo una parte de la práctica 13
# P13 incluye arreglos, listas, conjuntos y diccionarios
#Crear un conjunto de 5 elementos 
#   agregar un calor que no existe en el conjunto
#   eliminar un valor que existe 
#   eliminar un valor que no existe
#   verificar si existe un valor 
#   agregar un valor repetido 



c={0,2,3,6,7}
c.add(4)
c.remove(2)   #error si no se encuentra
c.discard(5)  #no hay error si no se encuentra
print(1 in c) #True/false
print(3 in c)
c.add(7)
print(c)

print("-----------------------------------------------------------------------------")

A={0,1,2,3,4,5}
B={0,2,4,6,8,10}

#sintaxis de union
U=B.union(A)
print(U)
Uu=B|A
print(A)

#Intersección 
I=B.intersection(A)
print(I)
Ii=A&B
print(Ii)

#diferencia 
D=A.difference(B)
print(D)
Dd=A-B #ese no es el símbolo de diferencia de conjuntos, lit lo está restando, no diferenciando
print(Dd)


SD=A.symmetric_difference(B)
print("SD",SD)
#SDd= A ∧ B 

#Un conjunto pertenece a otro conjunto?
print(A.issuperset(B)) #B pertenece a A?
print(B.issuperset(A)) #A pertenece a B?
Aa={0,1,2}
print(A.issuperset(Aa)) #Aa pertenece a A

print(A.issubset(B))    #A pertencea a B?

#contar elemnentos dentro de un conjunto
print(len(A))
E=A.copy()
print(E)
A.clear()
print(len(A))

print(E.isdisjoint(B)) #que rayos hace esto?????


