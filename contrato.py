class Contrato:
    
    def __init__(self,nombre,inicio,fin):
        self.nombre = nombre
        self.inicio = inicio
        self.fin = fin

    def __str__(self):
        return (self.nombre + "," + self.inicio + "," + self.fin)

def get_fin_contrato(c):
    return c.fin
          
            