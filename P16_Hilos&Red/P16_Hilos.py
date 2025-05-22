import threading 
import time

class hilo(threading.Thread):
    def __init__(self,nombre,intervalo):
        super().__init__()
        self.nombre = nombre
        self.intervalo = intervalo

    def run(self):
        print (f"El hilo {self.nombre} ha comenzado")
        for i in range(5): 
            print(f"El hilo >> {self.nombre} << se encuentra en iteración {i} ")
            time.sleep (self.intervalo)
        print(f"El hilo >> {self.nombre} << ha finalizado")
               

hilo1=hilo("hilo1",2)
hilo2=hilo("hilo2",4)
hilo1.start()
hilo2.start()
hilo1.join()
hilo2.join()
