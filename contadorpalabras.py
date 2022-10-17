archivo = "Punto 2.txt"

try:
    with open(archivo) as f_obj:
        contenido = f_obj.read()
        # print(contenido)
except FileNotFoundError:
    mensaje = "El archivo no existe"
else:
    # Contador de palabras del archivo
    palabras = contenido.split()
    # split crea una lista con las palabras encontradas
    num_palabras = len(palabras)
    # print("El archivo contiene "+str(num_palabras)+" palabras")

    file = open("Resultado.txt", "w")
    file.write("El archivo contiene "+str(num_palabras)+" palabras")
    file.close()


