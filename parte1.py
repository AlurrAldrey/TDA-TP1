from contrato import Contrato, get_inicio_contrato
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
    f = contrato_actual.fin
    i = 1
    res = [contrato_actual]
    loop = False
    contrato_anterior = contrato_actual

    
    while not loop:

        i = i%n
        contrato_actual=contratos[i]

        if i == 0:
            if contrato_anterior.inicio > contrato_anterior.fin or len(res) == 1:
                f = contrato_anterior.fin
            else:
                f = 0
        else:
            f = contrato_anterior.fin

        if contrato_actual.inicio >= f: 
            
            if contrato_actual in res: loop = True
            res.append(contrato_actual)
            contrato_anterior = contrato_actual

        i += 1

    for contrato in res:
        print(contrato.nombre)

    #y ahora deberia identificar el loop para imprimir los verdaderos seleccionados unicamente
main()