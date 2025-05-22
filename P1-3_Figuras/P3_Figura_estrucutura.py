import math

# Clase base
class Figura:
    def __init__(self, nombre):
        self.nombre = nombre

    def area(self):
        raise NotImplementedError("Este método debe ser implementado por la subclase.")

# Clases derivadas (Herencia)
class Cuadrado(Figura):
    def __init__(self, lado):
        super().__init__("Cuadrado")
        self.lado = lado

    def area(self):  # Polimorfismo
        return self.lado ** 2

class Circulo(Figura):
    def __init__(self, radio):
        super().__init__("Círculo")
        self.radio = radio

    def area(self):  # Polimorfismo
        return math.pi * self.radio ** 2

class Triangulo(Figura):
    def __init__(self, base, altura):
        super().__init__("Triángulo")
        self.base = base
        self.altura = altura

    def area(self):  # Polimorfismo
        return (self.base * self.altura) / 2

# Función que demuestra el polimorfismo
def mostrar_area(figura):
    print(f"{figura.nombre} - Área: {figura.area():.2f}")

# Prueba
def main():
    figuras = [
        Cuadrado(4),
        Circulo(3),
        Triangulo(5, 2)
    ]

    for figura in figuras:
        mostrar_area(figura)

if __name__ == "__main__":
    main()
