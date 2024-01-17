# -*- codigo: utf-16 -*-

import os
import sys
import platform
import subprocess
import socket

def introducirIp():
    '''El usuario introduce una IP correcto y la divide en octetos.
    
    parameters
    ----------

    Return
    ------
    "La ip introducida es: " más la IP completa.
    '''
    sys_argv_length=len(sys.argv)
    octetos = sys.argv[1].split(".")
    return octetos
    
'''def sistemaOperativo(ip):
    ''
    Descubre el sistema operativo de la ip.

    parameters
    ---------

    returns
    -------
    El tipo de SO y la versión.
    ''
    nombreSO = platform.system()
    versionSO = platform.release()
    print("Nombre del SO y versión: " +  nombreSO + " " + versionSO)'''


def ipCorrecta(ip):
    '''
    Nos aseguramos que la ip es correcta.

    parameter
    ---------
    ip: ip introducida por el usuario.

    returns
    -------
    
    '''
    try:
        if len(ip) == 4:
            for i in ip:
                if not i.isnumeric():
                    raise TypeError
            else:
                if (int(i) <0 or int(i)>255):
                    raise ValueError
    except TypeError:
        print("Debe ser numérico.")
    except ValueError:
        print("Debe estar entre 0 y 255.")

def tipoIp(ip):
    '''
    Comparamos el primer octeto de la ip para saber que tipo es.

    parameters
    ----------
    ip: ip introducida por el usuario

    returns
    -------
    Devuelve el tipo de ip que es.
    '''
    primerOcteto = int(ip[0])

    if 0 <= primerOcteto <= 127:
        print("Es de tipo A.")
    elif 128 <= primerOcteto <= 191:
        print("Es de tipo B.")
    elif 192 <= primerOcteto <= 233:
        print("Es de tipo C.")
    elif 224 <= primerOcteto <= 239:
        print("Es de tipo D.")

#ping

def pingIp(ip):
    '''
    Realiza un ping a la ip introducida.

    parameters
    ----------

    return
    ------
    Realiza un ping a la ip.
    '''
    if platform.system() == "Linux":
        ping = os.system("ping -c 2 "+ sys.argv[1])
        if ping == 0:
            print ('Up.El ping es correcto.')
        else:
            print('Down.La red no está presente.')
    if platform.system() == "Windows":
        ping = os.system("ping -n 2 "+ sys.argv[1])
        if ping == 0:
            print ('Up.El ping es correcto.')
        else:
            print('Down.La red no está presente.')

    #salida = subprocess.run(["ping +, sys.argv[1]"],stdout= subprocess.DEVNULL)
    #if salida.returncode == 1:
     #   print(sys.argv[1], "La red no está presente.")
    #else:
     #   print("El ping es correcto.")

def puertosAbiertos(ip):
    '''comprueba que puertos tiene abiertos la ip introducida'''
    for port in range(65545):
        try:
            serv = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
            serv.bind((sys.argv[1],port))
        except:
            print('[OPEN] Port open:',port)
        serv.close()


def main():
    '''programa principal'''
    ip = introducirIp()
    print("La ip introducida es: ",sys.argv[1])
    ipOk = ipCorrecta(ip)
    tipoIp(ip)
    #sistemaOperativo(ip)
    pingIp(ip)
    puertosAbiertos(ip)

if __name__=="__main__":
    main()

	

