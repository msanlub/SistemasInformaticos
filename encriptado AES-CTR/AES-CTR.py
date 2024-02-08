from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes

def generar_clave():
    return get_random_bytes(16)  # Generar una clave de 128 bits (16 bytes)

def encriptar(texto_plano, clave):
    nonce = get_random_bytes(16)  # Generar un nonce de 128 bits (16 bytes)
    print("Longitud del nonce:", len(nonce))  # Verificar la longitud del nonce
    cipher = AES.new(clave, AES.MODE_CTR, nonce=nonce)  # Crear un objeto Cipher en modo CTR
    texto_cifrado = cipher.encrypt(texto_plano) # Encriptar el texto plano
    return nonce + texto_cifrado  # Devolver el nonce concatenado con el texto cifrado

def desencriptar(texto_cifrado, clave):
    nonce = texto_cifrado[:16]  # Extraer el nonce del texto cifrado
    ciphertext = texto_cifrado[16:]  # Extraer el texto cifrado sin el nonce
    cipher = AES.new(clave, AES.MODE_CTR, nonce=nonce)  # Crear un objeto Cipher en modo CTR
    texto_plano = cipher.decrypt(ciphertext)  # Desencriptar el texto cifrado
    return texto_plano

def main():
    clave = generar_clave()  # Generar una clave aleatoria
    mensaje = b'Este es un mensaje secreto.'  # Definir el mensaje a encriptar
    
    mensaje_encriptado = encriptar(mensaje, clave)  # Encriptar el mensaje
    print("Mensaje Encriptado:", mensaje_encriptado)

    mensaje_desencriptado = desencriptar(mensaje_encriptado, clave)  # Desencriptar el mensaje
    print("Mensaje Desencriptado:", mensaje_desencriptado.decode('utf-8'))

if __name__ == "__main__":
    main()
