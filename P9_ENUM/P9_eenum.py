#P9
#Enum
from enum import Enum
class Consecutive(Enum):
    Lunes=1
    Martes=2
    Miercoles=3

print(Consecutive.Lunes) 

print(Consecutive.Lunes.value)

print(type(Consecutive.Lunes))

print(type(Consecutive.Lunes.value))
