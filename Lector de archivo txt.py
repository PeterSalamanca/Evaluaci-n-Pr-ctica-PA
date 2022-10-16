from gtts import gTTS

import os

file = open("Texto.txt", "r").read().replace("\n", " ")

language = "es-us"

lector = gTTS(text= str(file), lang= language, slow= False)

lector.save("Texto-prueba.mp3")

os.system("start Texto-prueba.mp3")
