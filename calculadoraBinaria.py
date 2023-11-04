def id(x):
    return x

def leerEntradaUno() ->list:
    '''función que define la petición de entrada al usuario'''
    return list(map(id,input("Dame un byte: ")))
def leerEntradaDos() ->list:
    '''función que define la petición de entrada al usuario'''
    return list(map(id,input("Dame otro byte: ")))

def suma(byteUno,byteDos,ac,r):
    '''función que suma cada bit en cada posición dentro del byte'''
    for n in range[len(byteDos)-1,-1,-1]:
        #posición bit 8
        if byteUno[n]==0 and byteDos[n]==1 and ac[-1]==0:
            return r[n]==1
        elif byteUno[-1]==1 and byteDos[-1]==0 and ac[-1]==0:
            return r[-1]==1
        elif byteUno[-1]==1 and byteDos[-1]==1 and ac[-1]==0:
            return r[-1]==0 and ac[-2]==1
        elif byteUno[-1]==0 and byteDos[-1]==0 and ac[-1]==0:
            return r[-1]==0
        elif byteUno[-1]==1 and byteDos[-1]==1 and ac[-1]==1:
            return r[-1]==1 and ac[-2]==1
        elif byteUno[-1]==0 and byteDos[-1]==1 and ac[-1]==1:
            return r[-1]==0 and ac[-2]==1
        elif byteUno[-1]==1 and byteDos[-1]==0 and ac[-1]==1:
            return r[-1]==0 and ac[-2]==1
    
        
if __name__=="__main__":

    #entrada
    byteUno = leerEntradaUno()#lista byte primera
    byteDos = leerEntradaDos() #lista byte segunda

    #proceso
    ac = [0,0,0,0,0,0,0,0,0] #lista de acarreo
    r = [0,0,0,0,0,0,0,0,0] #lista de resultado
    sumaBinario = suma(byteUno,byteDos,ac,r)

    #salida
    print(sumaBinario)