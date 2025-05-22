from abc import ABC, abstractmethod

# Abstracción: clase abstracta
class CuentaBancaria(ABC):
    def __init__(self, titular, saldo_inicial=0):
        self._titular = titular                # Encapsulamiento
        self._saldo = saldo_inicial           # Atributo protegido

    def depositar(self, cantidad):
        if cantidad > 0:
            self._saldo += cantidad
            print(f"Depósito exitoso. Nuevo saldo: ${self._saldo}")
        else:
            print("La cantidad debe ser positiva.")

    def consultar_saldo(self):
        return self._saldo

    @abstractmethod
    def retirar(self, cantidad):
        pass


# Cuenta de Ahorro
class CuentaAhorro(CuentaBancaria):
    def __init__(self, titular, saldo_inicial=0, interes=0.02):
        super().__init__(titular, saldo_inicial)
        self._interes = interes

    def aplicar_interes(self):
        self._saldo += self._saldo * self._interes
        print(f"Interés aplicado. Nuevo saldo: ${self._saldo:.2f}")

    # 🧬 Polimorfismo: implementación específica
    def retirar(self, cantidad):
        if 0 < cantidad <= self._saldo:
            self._saldo -= cantidad
            print(f"Retiro exitoso. Saldo restante: ${self._saldo}")
        else:
            print("Fondos insuficientes para el retiro.")


# Cuenta Corriente
class CuentaCorriente(CuentaBancaria):
    def __init__(self, titular, saldo_inicial=0, limite_credito=500):
        super().__init__(titular, saldo_inicial)
        self._limite_credito = limite_credito

    # Polimorfismo: diferente comportamiento de retiro
    def retirar(self, cantidad):
        if cantidad <= self._saldo + self._limite_credito:
            self._saldo -= cantidad
            print(f" Retiro exitoso. Saldo actual: ${self._saldo}")
        else:
            print(" Límite de crédito excedido.")


#  Uso de clases
def main():
    # Creamos cuentas
    ahorro = CuentaAhorro("Ana", 1000)
    corriente = CuentaCorriente("Luis", 500)

    # Operaciones con cuenta de ahorro
    print("\n Cuenta de Ahorro")
    ahorro.depositar(200)
    ahorro.retirar(300)
    ahorro.aplicar_interes()

    # Operaciones con cuenta corriente
    print("\n Cuenta Corriente")
    corriente.retirar(600)  # usa crédito
    corriente.depositar(100)

    # Uso de polimorfismo
    print("\n Operaciones polimórficas:")
    cuentas = [ahorro, corriente]
    for cuenta in cuentas:
        cuenta.retirar(50)

if __name__ == "__main__":
    main()
