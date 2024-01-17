# -*- codigo: utf-16 -*-


def leerEntradaUno() ->list:
    '''función que define la petición de entrada al usuario'''
    return list(input("Dame un byte: "))
def leerEntradaDos() ->list:
    '''función que define la petición de entrada al usuario'''
    return list(input("Dame otro byte: "))

def suma(byteUno,byteDos,acarreo):
    '''función que suma cada bit en cada posición dentro del byte'''
    resultado = [] #lista de resultado
    for n in range(len(byteDos)-1,-1,-1):
        #posición bit 8
        if byteUno[n]==0 and byteDos[n]==1 and acarreo[n]==0:
            resultado.append(1)
        elif byteUno[n]==1 and byteDos[n]==0 and acarreo[n]==0:
            resultado.append(1)
        elif byteUno[n]==1 and byteDos[n]==1 and acarreo[n]==0:
            resultado.append(0) and acarreo.append(1)
        elif byteUno[n]==0 and byteDos[n]==0 and acarreo[n]==0:
            resultado.append(0)
        elif byteUno[n]==1 and byteDos[n]==1 and acarreo[n]==1:
            resultado.append(1) and acarreo.append(1)
        elif byteUno[n]==0 and byteDos[n]==1 and acarreo[n]==1:
            resultado.append(0) and acarreo.append(1)
        elif byteUno[n]==1 and byteDos[n]==0 and acarreo[n]==1:
            resultado.append(0) and acarreo.append(1)
        else:
            return "Cago en to"
        
    return resultado

if __name__=="__main__":

    #entrada
    byteUno = leerEntradaUno()#lista byte primera
    byteDos = leerEntradaDos() #lista byte segundas
    for caracter in range(len(byteUno)):
        byteUno[caracter] = int(byteUno[caracter])
    for caracter in range(len(byteDos)):
        byteDos[caracter] = int(byteDos[caracter])
    acarreo = [0,0,0,0,0,0,0,0,0] #lista de acarreo

    #proceso
    sumaBinario = suma(byteUno,byteDos,acarreo)

    #salida
    print(sumaBinario)