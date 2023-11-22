import os
import sys
import platform

sys_argv_length=len(sys.argv)
octetos = sys.argv[1].split(".")
print("La ip introducida es: ",sys.argv[1])

#ip correcta
try:
    if len(octetos) == 4:
        for i in octetos:
            if not i.isnumeric():
                raise TypeError
        else:
            if (int(i) <0 or int(i)>255):
                raise ValueError
except TypeError:
    print("Debe ser numérico.")
except ValueError:
    print("Debe estar entre 0 y 255.")

#tipo de ip
primerOcteto = int(octetos[0])

if 0 <= primerOcteto <= 127:
    print("Es de tipo A.")
elif 128 <= primerOcteto <= 191:
    print("Es de tipo B.")
elif 192 <= primerOcteto <= 233:
    print("Es de tipo C.")
elif 224 <= primerOcteto <= 239:
    print("Es de tipo D.")

#ping
    print("Nombre del SO y versión: " +  platform.system() + " " + platform.release()
    print(sistemaOperativo)

salida = subprocess.run(["ping", sys.argv[1]],stdout=subprocess.DEVNULL)



	

