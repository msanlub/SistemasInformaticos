import random

'''tres en raya'''
tablero = [[" "," "," "], 
           [" "," "," "], 
           [" "," "," "]]

USUARIO = "x"
ORDENADOR = "o"
FIN = "fin"

def imprimirTablero(tablero):
    for filas in tablero:
        print(f"{filas} \n")

def comprobarYAñadirPersona(coordenada,tablero):
    try:
        coordenada = coordenada.split(",")
        posicionUno= int(coordenada[0])
        posicionDos= int(coordenada[1])
        if tablero [posicionUno][posicionDos] == " ":
            tablero[posicionUno][posicionDos] = USUARIO
        elif tablero [posicionUno][posicionDos] == USUARIO or tablero [posicionUno][posicionDos] == ORDENADOR:
            main()
        return tablero
    except  IndexError:
        print("Está fuera de rango. vuelve a intentarlo.")
        

def movimientoOrdenador(tablero):
    try:
        posicionUnoOrdenador = random.randint(0,len(tablero)-1) 
        posicionDosOrdenador = random.randint(0,len(tablero)-1)
        if tablero [posicionUnoOrdenador][posicionDosOrdenador] == " ":
            tablero[posicionUnoOrdenador][posicionDosOrdenador] = ORDENADOR
        elif tablero [posicionUnoOrdenador][posicionDosOrdenador] == USUARIO or tablero [posicionUnoOrdenador][posicionDosOrdenador] == ORDENADOR:
            movimientoOrdenador(tablero)
        return tablero
    except : print("")

def comprobarTresEnRayaPorFilas(tablero):
    if tablero[0][0] == USUARIO and tablero [0][1]== USUARIO and tablero[0][2] == USUARIO:
        return "Has ganado"
    if tablero[1][0] == USUARIO and tablero [1][1]== USUARIO and tablero[1][2] == USUARIO:
        return "Has ganado"
    if tablero[2][0] == USUARIO and tablero [2][1]== USUARIO and tablero[2][2] == USUARIO:
        return "Has ganado"
    if tablero[0][0] == USUARIO and tablero [1][0]== USUARIO and tablero[2][0] == USUARIO:
        return "Has ganado"
    if tablero[1][1] == USUARIO and tablero [0][1]== USUARIO and tablero[2][1] == USUARIO:
        return "Has ganado"
    if tablero[0][2] == USUARIO and tablero [1][2]== USUARIO and tablero[2][2] == USUARIO:
        return "Has ganado"
    if tablero[0][0] == ORDENADOR and tablero [0][1]== ORDENADOR and tablero[0][2] == ORDENADOR:
        return "Has perdido"
    if tablero[1][0] == ORDENADOR and tablero [1][1]== ORDENADOR and tablero[1][2] == ORDENADOR:
        return "Has perdido"
    if tablero[2][0] == ORDENADOR and tablero [2][1]== ORDENADOR and tablero[2][2] == ORDENADOR:
        return "Has perdido"
    if tablero[0][0] == ORDENADOR and tablero [1][0]== ORDENADOR and tablero[2][0] == ORDENADOR:
        return "Has perdido"
    if tablero[1][1] == ORDENADOR and tablero [0][1]== ORDENADOR and tablero[2][1] == ORDENADOR:
        return "Has perdido"
    if tablero[0][2] == ORDENADOR and tablero [1][2]== ORDENADOR and tablero[2][2] == ORDENADOR:
        return "Has perdido"
    


def comprobarTresEnRayaDiagonales(tablero):
    if tablero[0][0] == USUARIO and tablero [1][1] == USUARIO and tablero[2][2] == USUARIO:
        return "Has ganado"
    elif tablero[2][0] == USUARIO and tablero[1][1] == USUARIO and tablero[0][2] == USUARIO:
        return "Has ganado"
    elif tablero[0][0] == ORDENADOR and tablero [1][1] == ORDENADOR and tablero[2][2] == ORDENADOR:
        return "Has perdido"
    elif tablero[2][0] == ORDENADOR and tablero[1][1] == ORDENADOR and tablero[0][2] == ORDENADOR:
        return "Has perdido"


def finPartida(entrada,tablero):
    if comprobarTresEnRayaPorFilas(tablero) or comprobarTresEnRayaDiagonales(tablero) == "Has perdido":
        entrada = FIN
        return entrada
    if comprobarTresEnRayaPorFilas(tablero) or comprobarTresEnRayaDiagonales(tablero) == "Has ganado":
        entrada = FIN
        return entrada

def main():
    '''programa principal'''
    entrada = ""

    while entrada != FIN:
        coordenada = input("Indica tu posición (coordenada(x,y)): ")
        comprobarYAñadirPersona(coordenada,tablero)
        imprimirTablero(tablero)
        comprobarTresEnRayaPorFilas(tablero)  
        comprobarTresEnRayaDiagonales(tablero) 
        print("turno del PC.")
        movimientoOrdenador(tablero)
        imprimirTablero(tablero)
        comprobarTresEnRayaPorFilas(tablero) 
        comprobarTresEnRayaDiagonales(tablero)
        entrada = finPartida(entrada,tablero)
    imprimirTablero(tablero)
    print(comprobarTresEnRayaDiagonales(tablero))
    print(comprobarTresEnRayaPorFilas(tablero))
    print("Partida finalizada")

if __name__=="__main__":
    main()