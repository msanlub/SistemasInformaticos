import Crypto
from Crypto.Cipher import AES

obj = AES.new('Esta es una clave123', AES.MODE_CBC, 'Esto es un IV456')
mensaje = "Maldito seas Jose"
texto_cifrado = obj.encrypt(mensaje)
texto_cifrado
'\xd6\x83\x8dd!VT\x92\xaa`A\x05\xe0\x9b\x8b\xf1'
obj2 = AES.new('Esta es una clave123', AES.MODE_CBC, 'Esto es un IV456')
obj2.decrypt(texto_cifrado)
'Maldito seas Jose'