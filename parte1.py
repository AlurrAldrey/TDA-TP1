from contrato import Contrato
from contrato import get_fin_contrato

def main():

    print("ingrese el nombre del archivo de contratos:")
    filename = input()
    file = open(filename,"r")
    contratos = []

    #recorro el archivo y meto cada contrato en la lista de contratos y obtengo la cantidad de elementos
    n = 0
    for line in file:
        datos = line.split(",")
        c = Contrato(datos[0],int(datos[1]),int(datos[2]))
        contratos.append(c)
        n += 1

    #ordeno por fin de contrato en orden ascendente
    contratos.sort(key=get_fin_contrato)

    #imprimo el primer elemento de contratos ya que es seleccionado automáticamente y la variable f con la fecha 
    #de finalización del contrato
    contrato_actual = contratos[0]
    print(contrato_actual.nombre)
    f = contrato_actual.fin
    i = 1

    #recorro la lista de contratos a partir del segundo elemento e imprimo los nombres de los contratos que son
    #compatibles con el anterior
    while i < n:
        contrato_actual=contratos[i]

        if contrato_actual.inicio >= f:
            print(contrato_actual.nombre)
            f = contrato_actual.fin
        
        i += 1

main()