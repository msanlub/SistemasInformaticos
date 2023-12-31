'''cifrado ROT-13: rota los caracteres ingresados 13 veces en el ab. ecedario'''
ABC='abcdefghijklmnñopqrstuvwxyzABCDEFGHIJKLMNÑOPQRSTUVWXYZ'
CBA='nñopqrstuvwxyzabcdefghijklmNÑOPQRSTUVWXYZABCDEFGHIJKLM'

def rot13(cifrar:str)->str:
    mapeo = dict(zip(ABC , CBA)) #dict: diccionario // zip: para iterar dos listas en paralelo 
    return ''.join(mapeo.get(x, x) for x in cifrar) #join: añade simbolos a la lista,para iterar los valores // get: nos devuelve un valor si existe,sino devuelve none

def descifrarRot13(descifrar:str)->str:
    mapeo = dict(zip(CBA , ABC))
    return ''.join(mapeo.get(x, x) for x in descifrar)

if __name__=="__main__":
    #entrada
    menu = input("¿Qué quiere,cifrar o descifrar una frase? -> ").lower()

    #proceso y salida
    if menu == "cifrar":
        cifrar = input("Escribe la frase que quiere cifrar: \n")
        cifrado = rot13(cifrar)
        print("Tu frase cifrada es: " + cifrado)
    elif menu == "descifrar":
        descifrar = input("Escribe la frase que quieres descifrar: \n")
        descifrado = descifrarRot13(descifrar)
        print("Tu frase descifrada es :" + descifrado)
    else:
        print("Esa opción no es correcta.")
    
    