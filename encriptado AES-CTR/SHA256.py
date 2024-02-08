import hashlib

'''
Genera un hash que se añade al codigo.
¡¡¡OJO!!!-->la encriptación es un proceso reversible (puedes obtener la información original a partir de los datos encriptados utilizando una clave), el hashing es un proceso irreversible (una vez que se calcula el hash, no se puede obtener la información original a partir de él).
'''

def calcular_sha256(texto):
    # Codifica la cadena de texto en bytes antes de calcular el hash
    texto_codificado = texto.encode('utf-8')
    # Calcula el hash SHA-256
    hash_sha256 = hashlib.sha256(texto_codificado)
    # Devuelve el valor hash en formato hexadecimal
    return hash_sha256.hexdigest()

def main():
    texto = input("Introduce el texto a encriptar: ")
    hash_sha256 = calcular_sha256(texto)
    print("El hash SHA-256 del texto es:", hash_sha256)

if __name__ == "__main__":
    main()
