#Práctica 14 
#Json
import json 
import requests 

class GestorJson:
    def __init__(self, arch):
        self.arch=arch

    def leerJson(self):
        try: 
            with open(self.arch,'r') as f: #falta 'r'después de self.arch
                return json.load(f)
        except FileNotFoundError:
            print("Archivo no existe")
        except json.JSONDecodeError:
            print("El archivo no es json")
            return{}
        
    def escribirJson(self,datos):
        try: 
            with open(self.arch,'w') as f: 
                return json.dump(datos,f,indent=4)
        except FileNotFoundError:
            print("Archivo no existe")
        except json.JSONDecodeError:
            print("El archivo no es json")
            return{}
            
    def modificarJson(self,llave,valor):
        datos=self.leerJson()
        datos[llave]=valor
        self.escribirJson(datos)

    def obtenerPokemon(self,pokemon): 
        try:
            URL = f"https://pokeapi.co/api/v2/pokemon/{pokemon}"
            response=requests.get(URL)
            response.raise_for_status()
            data=response.json()
            self.escribirJson(data)
        except requests.exceptions.HTTPError:
            print("el enlace no existe")
        except requests.exceptions.RequestException:
            print("No se puede realizar la petición")

gjson=GestorJson("pokemon.json")
gjson.obtenerPokemon("Pikachu")
pokemoninfo=gjson.leerJson()
#print(pokemoninfo)
jalarpokemon= gjson.modificarJson("abilities", 2)
print(jalarpokemon)



