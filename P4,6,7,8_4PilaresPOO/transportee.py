from abc import ABC, abstractmethod

# Abstracción: clase base abstracta para vehículos
class Vehiculo(ABC):
    def __init__(self, marca, modelo):
        self._marca = marca              # Encapsulamiento: atributo protegido
        self._modelo = modelo
        self._encendido = False
        self._velocidad = 0

    def encender(self):
        self._encendido = True
        print(f"{self._marca} {self._modelo} ha sido encendido.")

    def apagar(self):
        self._encendido = False
        self._velocidad = 0
        print(f"{self._marca} {self._modelo} ha sido apagado.")

    def estado(self):
        return {
            "marca": self._marca,
            "modelo": self._modelo,
            "encendido": self._encendido,
            "velocidad": self._velocidad
        }

    @abstractmethod
    def acelerar(self):
        pass

# Herencia: clases hijas que extienden la clase base
class Auto(Vehiculo):
    def __init__(self, marca, modelo, puertas):
        super().__init__(marca, modelo)
        self._puertas = puertas

    # Polimorfismo: implementación propia del método abstracto
    def acelerar(self):
        if self._encendido:
            self._velocidad += 10
            print(f"{self._marca} acelerando. Velocidad: {self._velocidad} km/h")
        else:
            print("El auto está apagado.")

class Motocicleta(Vehiculo):
    def __init__(self, marca, modelo, cilindrada):
        super().__init__(marca, modelo)
        self._cilindrada = cilindrada

    def acelerar(self):
        if self._encendido:
            self._velocidad += 20
            print(f"{self._marca} acelerando. Velocidad: {self._velocidad} km/h")
        else:
            print("La motocicleta está apagada.")

# Código cliente
def main():
    auto1 = Auto("Toyota", "Corolla", 4)
    moto1 = Motocicleta("Yamaha", "R3", 321)

    # Prueba de funcionalidad polimórfica
    vehiculos = [auto1, moto1]

    for vehiculo in vehiculos:
        vehiculo.encender()
        vehiculo.acelerar()
        vehiculo.acelerar()
        vehiculo.apagar()
        print(vehiculo.estado())

if __name__ == "__main__":
    main()
