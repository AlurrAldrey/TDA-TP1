#definición de la clase contrato para simplificar las operaciones del algoritmo
class Contrato:
    
    def __init__(self,nombre,inicio,fin):
        self.nombre = nombre
        self.inicio = inicio
        self.fin = fin

def get_fin_contrato(c):
    return c.fin
          
            