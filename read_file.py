"""
Clase read_file
Permite que el chatbot lea los documentos
"""

try:
    with open("documento.txt", "r", encoding="utf-8") as archivo:
        contenido = archivo.read()
except FileNotFoundError:
    print(f"No se encuentra el archivo.")
else:
    print(contenido)