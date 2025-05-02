from typing import Final

class Usuario:
    Max_usuario:Final=1000


    try:
        a=(3/0)
        print(a)

    except ZeroDivisionError:
        print("No sirve")

    finally:
        print("Error desconocido")