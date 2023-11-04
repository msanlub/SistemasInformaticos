#calculadora binaria

def id(x):
    return x

def leerEntrada() -> list:
    '''función que da la entrada de byte'''
    return list(map(id,input("Dame un byte: ")))

def soloBinario() ->list:
    '''función que añade 0 ó 1'''
    B = []
    for b in B:
        if b in ("0","1"):
            B.append(b)

if __name__=="__main__":
    print(leerEntrada())

'''
    if len(B) != 8:
        return []
    else:
        print(B)
        '''