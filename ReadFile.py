class Lector:
#permite que el chatbot lea los documentos
    def __init__(self, ruta_archivo):
        self.ruta=ruta_archivo
    def leer(self):
        try:
            with open(self.ruta, "r", encoding="utf-8") as archivo:
               return archivo.read()
        except FileNotFoundError:
            print(f"No se encuentra el archivo.")
        else:
            print(contenido)