'''cifrado ROT-13: rota los caracteres ingresados 13 veces en el ab. ecedario'''
ABC='abcdefghijklmnñopqrstuvwxyzABCDEFGHIJKLMNÑOPQRSTUVWXYZ'
CBA='nñopqrstuvwxyzabcdefghijklmNÑOPQRSTUVWXYZABCDEFGHIJKLM'

def rot13(cifrar:str)->str:
    mapeo = dict(zip(ABC + CBA, CBA + ABC)) #dict: diccionario // zip: para iterar dos listas en paralelo 
    return ''.join(mapeo.get(x, x) for x in cifrar) #join: añade simbolos a la lista,para iterar los valores // get: nos devuelve un valor si existe,sino devuelve none

def descifrarRot13(descifrar:str)->str:
    mapeo = dict(zip(CBA + ABC, ABC + CBA))
    return ''.join(mapeo.get(x, x) for x in descifrar)

if __name__=="__main__":
    #entrada
    cifrar = input("Escribe la frase que quiere cifrar: ")
    descifrar = input("Escribe la frase que quieres descifrar: ")

    #proceso
    cifrado = rot13(cifrar)
    descifrado = descifrarRot13(descifrar)

    #salida
    print("Tu frase cifrada es: " + cifrado)
    print("Tu frase descifrada es :" + descifrado)