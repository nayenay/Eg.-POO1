from enum import Enum

# Definir un Enum con los días de la semana
class Dias(Enum):
    LUNES = "Lunes"
    MARTES = "Martes"
    MIERCOLES = "Miércoles"
    JUEVES = "Jueves"
    VIERNES = "Viernes"
    SABADO = "Sábado"
    DOMINGO = "Domingo"

# Función que valida si el día ingresado está en el Enum
def verificar_dia(dia):
    try:
        if not isinstance(dia, str):
            raise TypeError("Se esperaba un valor de tipo string.")

        dia = dia.capitalize()  # Normalizar el formato

        if dia in [d.value for d in Dias]:  # Verificar si está en el Enum
            print(f"Día válido: {dia}")
        else:
            raise ValueError("El día ingresado no es válido. Debe ser un día de la semana.")

    except TypeError as e:
        print(f"Error de tipo: {e}")
    except ValueError as e:
        print(f"Error: {e}")
    finally:
        print("Ejecución finalizada.")

# Pruebas
verificar_dia("Lunes")     # Día válido
verificar_dia("domingo")   # Día válido
verificar_dia("Feriado")   # Error: Día no válido
verificar_dia(123)         # Error de tipo