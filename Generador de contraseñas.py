archivo = open("Genrador de contraseñas.txt", "w")

import random

minus = "abcdefghijklmñopqrstuvwxyz"
mayus = minus.upper()
numeros = "0123456789"
simbolos = "@[]{}()*,;/\-¡?¿!$%&=+_:."

aleatorio = minus+mayus+numeros+simbolos
longitud = 10

for _ in range(10):
    muestra = random.sample(aleatorio, longitud)
    password = "".join(muestra)
    # print(password)
    archivo.write(password)
    archivo.write("\n")
archivo.close()