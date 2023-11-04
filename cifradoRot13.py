'''cifrado ROT-13: rota los caracteres ingresados 13 veces en el abecedario'''
ABC='abcdefghijklmnopqrstuvwxyzñABCDEFGHIJKLMNOPQRSTUVWXYZÑ'
CBA='nopqrstuvwxyzabcdefghijklmñNOPQRSTUVWXYZABCDEFGHIJKLMÑ'

def rot13(frase:str)->str:
    mapeo = dict(zip(ABC + CBA, CBA + ABC)) #dict: diccionario // zip: para iterar dos listas en paralelo 
    return ''.join(mapeo.get(x, x) for x in frase) #join: añade simbolos a la lista,para iterar los valores // get: nos devuelve un valor si existe,sino devuelve none

if __name__=="__main__":
    #entrada
    frase = input("Escribe la frase que quiere cifrar: ")

    #proceso
    cifrado = rot13(frase)

    #salida
    print(cifrado)

