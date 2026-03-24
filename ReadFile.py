def ReadFile(ruta):
    try:
        with open(ruta, "r", encoding="utf-8") as archivo:
            contenido = archivo.read()
    except FileNotFoundError:
        print(f"No se encuentra el archivo.")
    else:
        print(contenido)