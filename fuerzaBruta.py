import time
import itertools

# Lista predefinida de letras minúsculas
letras_minusculas = 'abcdefghijklmnopqrstuvwxyz'

def buscar_palabra(palabra):
    start_time = time.time()  # Marca el inicio de la búsqueda
    
    longitud_palabra = len(palabra)
    
    # Genera todas las combinaciones posibles de letras minúsculas de la longitud de la palabra
    combinaciones = itertools.product(letras_minusculas, repeat=longitud_palabra)
    
    # Itera sobre cada combinación y busca la palabra
    for combinacion in combinaciones:
        palabra_generada = ''.join(combinacion)
        if palabra_generada == palabra:
            end_time = time.time()  # Marca el final de la búsqueda
            tiempo_transcurrido = end_time - start_time
            return tiempo_transcurrido

# Ejemplo de uso
palabra_ingresada = input("Ingrese la palabra o contraseña a buscar: ")
tiempo = buscar_palabra(palabra_ingresada)
print("Tiempo transcurrido:", tiempo, "segundos.")
