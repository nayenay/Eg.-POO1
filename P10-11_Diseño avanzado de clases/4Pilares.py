# 1. Encapsulamiento: Restringe el acceso a los atributos de un objeto. y permite su modificación solo a través de métodos controlados.
#         expone solo lo necesario a través de métodos públicos

print("1-------------------------------------------------------------------------------------------")
class Persona:
    def __init__(self, nombre, edad):#inicializa doblem método, esta inicializando los atribytos y métodos, eso es un constructor. init toma en cuenta que se puede acceder directamente o que es privado 
        self.__nombre = nombre  # Atributo privado
        self.__edad = edad  # Atributo privado
    
    def get_nombre(self):  # Método público para acceder a __nombre
        return self.__nombre
    
    def set_edad(self, nueva_edad):  # Método público para modificar __edad
        if nueva_edad > 0:
            self.__edad = nueva_edad

# Uso de encapsulamiento
persona = Persona("Juan", 25)
print(persona.get_nombre())  # Se accede al nombre a través de un método público
print("2-------------------------------------------------------------------------------------------")
# 2. Herencia: Permite que una clase herede atributos y métodos de otra.
class Animal:
    def __init__(self, nombre,raza):
        self.nombre = nombre
        self.raza= raza
    
    def hacer_sonido(self):
        return "Sonido genérico"

class Perro(Animal):  # Perro hereda de Animal
    def hacer_sonido(self):
        return "Guau guau"

# Uso de herencia
perrito = Perro("Firulais","Doberman")
print(perrito.nombre)  # Accede al atributo heredado
print(perrito.hacer_sonido())  # Método sobreescrito
print(perrito.raza)

print("3-------------------------------------------------------------------------------------------")

# 3. Polimorfismo: Permite que diferentes clases tengan métodos con el mismo nombre pero con diferente comportamiento.
def hacer_sonar(animal):
    print(animal.hacer_sonido())

gato = Animal("Michi")
perro = Perro("Rex")

hacer_sonar(gato)  # Llama al método de Animal
hacer_sonar(perro)  # Llama al método sobreescrito en Perro

print("4-------------------------------------------------------------------------------------------")

# 4. Abstracción: Oculta detalles de implementación y muestra solo lo esencial.
from abc import ABC, abstractmethod

class Figura(ABC):  # Clase abstracta
    @abstractmethod
    def area(self):
        pass  # Método abstracto, debe ser implementado en las subclases
                #pass pasa a la siguiente linea de código sin retornar nada 
class Cuadrado(Figura):
    def __init__(self, lado):
        self.lado = lado
    
    def area(self):
        return self.lado * self.lado

# Uso de abstracción
cuadrado = Cuadrado(4)
print(cuadrado.area())  # Implementación concreta del método abstracto
