# Clase base
class Empleado:
    def __init__(self, nombre):
        self.nombre = nombre

    def calcular_pago(self):
        raise NotImplementedError("Este método debe ser implementado por la subclase.")

# Clases derivadas (Herencia)
class EmpleadoPorHora(Empleado):
    def __init__(self, nombre, horas_trabajadas, tarifa_por_hora):
        super().__init__(nombre)
        self.horas_trabajadas = horas_trabajadas
        self.tarifa_por_hora = tarifa_por_hora

    def calcular_pago(self):  # Polimorfismo
        return self.horas_trabajadas * self.tarifa_por_hora

class EmpleadoAsalariado(Empleado):
    def __init__(self, nombre, salario_mensual):
        super().__init__(nombre)
        self.salario_mensual = salario_mensual

    def calcular_pago(self):  # Polimorfismo
        return self.salario_mensual

class EmpleadoPorComision(Empleado):
    def __init__(self, nombre, ventas_realizadas, porcentaje_comision):
        super().__init__(nombre)
        self.ventas_realizadas = ventas_realizadas
        self.porcentaje_comision = porcentaje_comision

    def calcular_pago(self):  # Polimorfismo
        return self.ventas_realizadas * self.porcentaje_comision

# Función que demuestra polimorfismo
def mostrar_pago(empleado):
    print(f"{empleado.nombre} - Pago: ${empleado.calcular_pago():.2f}")

# Prueba
def main():
    empleados = [
        EmpleadoPorHora("Carlos", 40, 120),
        EmpleadoAsalariado("Ana", 15000),
        EmpleadoPorComision("Luis", 50000, 0.10)
    ]

    for empleado in empleados:
        mostrar_pago(empleado)

if __name__ == "__main__":
    main()
