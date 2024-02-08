import base64
import os
import Crypto
from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP


'''
Se compone de una clave pública de dos numeros y otra privada de otros dos numeros. El mensaje primero se cifra utilizando la clave pública ( s econvierte el mensaje en un formato de numeros y luego se le aplica una operación matemática) y luego se descifra utilizando la clave privada correspondiente.
En resumen, la clave pública se utiliza para cifrar el mensaje, mientras que la clave privada se utiliza para descifrarlo.
'''
def credenciales(pk, msj):
    with open('credenciales_crypto.txt','wb') as f:
        f.write(pk.exportKey(format='PEM'))
        f.write(base64.b64encode(msj))

def encriptar_mensaje(mensaje):
    random_generator = Crypto.Random.new().read

    private_key = RSA.generate(1024, random_generator)
    public_key = private_key.publickey()

    mensaje = mensaje.encode()

    cipher = PKCS1_OAEP.new(public_key)
    encrypted_message  = cipher.encrypt(mensaje)

    credenciales(private_key, encrypted_message)
    return private_key, encrypted_message


def abrir_credenciales():
    with open('credenciales_crypto.txt', 'rb') as f:
        data = f.read()
        pk, msj = data.split(b"-----END RSA PRIVATE KEY-----", maxsplit=1)
        pk = pk + b"-----END RSA PRIVATE KEY-----"
        msj = base64.b64decode(msj)
        return pk, msj

def desencriptar_mensaje():
    clave_privada, mensaje_a_desencriptar = abrir_credenciales()
    pk = RSA.importKey(clave_privada)
    cipher = PKCS1_OAEP.new(pk)
    return cipher.decrypt(mensaje_a_desencriptar)

pk, msg = encriptar_mensaje('C0nTraseÑ@ S3guRa_')
print(desencriptar_mensaje())