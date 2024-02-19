import time
import itertools

# Lista predefinida de lenguaje
l1 = 'abcdefghijklmnñopqrstuvwxyzABCDEFGHIJKLMNÑOPQRSTUVWXYZ123456789*+-_/?¿'


def buscar_palabra(palabra):
    longitud_palabra = len(palabra)
    
    # Genera todas las combinaciones posibles de lenguaje de la longitud de la palabra
    combinaciones = itertools.product(l1, repeat=longitud_palabra)
    
    # Itera sobre cada combinación y busca la palabra
    start_time = time.time()  # Marca el inicio de la búsqueda
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
