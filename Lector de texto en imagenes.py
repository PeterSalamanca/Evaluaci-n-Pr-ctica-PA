from PIL import Image
from pytesseract import *
import textblob
from textblob import TextBlob

archivo = open("Texto de la Imagen.txt", "w", encoding="utf-8")

pytesseract.tesseract_cmd = r"C:\Users\Peter\AppData\Local\Tesseract-OCR\tesseract.exe"

Img = Image.open("Imagen.JPG")

texto = pytesseract.image_to_string(Img)

archivo.write(texto)

archivo.close()

file= open('Texto de la Imagen.txt')

dataset= file.read()
trad=TextBlob(dataset)
traduccion = trad.translate(from_lang='en',to='es')

print(traduccion)












