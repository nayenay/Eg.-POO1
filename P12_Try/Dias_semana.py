#listar los días de la semana
# Poner valor string a cada día 
#Función donde reciba como parámetro en valor contenido en el enum 
#pring valor correcto -si es igual sino lo es enviar error (comprobar tipo de edad)
# Deimitar el nímero de peticiones a 5
#delimitar el número de peticiones a 5
#comparr el tipo de dato
#is instance

from enum import Enum
from typing import Final
class Dias(Enum):
    Lunes="Lunes"
    Martes="Martes"
    Miercoles="Miércoles"
    Jueves="Jueves"
    VIernes="Viernes"
    Sabado="Sabado"
    Domingo="Domingo"


class Verificador:
    def __init__(self,dia:Dias):
        self.dia=dia
v=Verificador("Martoles")
print(v.dia)
print ("XDXD")

class Intento:
    Max_intento:Final=5


    # try:
    #     if type(Dias.Lunes.value)==type(ValaCom):
    #         print(Dias.Lunes.value)
    #         print("xd")

    # except ZeroDivisionError:
    #     print("No sirve")

    # finally:
    #     print("Error desconocido")

#class y:
    #def__init__(self,valores_comun):

      