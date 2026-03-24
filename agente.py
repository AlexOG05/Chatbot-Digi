import ollama
from ReadFile import Lector
class Agente:
    def __init__(self):
        #Cuando instancias al agente este primero crea un  objeto (lector) que permite leer documentos
        #Esta es la fuente de información
        self.Fuente=Lector("documento.txt")
    def respuesta(self, pregunta):
        #El agente lee la fuente de información(lee el texto) y guarda su contenido en la variable documento
        documento=self.Fuente.leer()
        #Le das s instrucciones a ollama de como tiene que responder(es como un prompt de IA)
        #Esto es como si fueras a la ia e hicieras tu mismo la pregunta
        instrucciones = f"Usa este texto: '{documento}' para responder brevemente a: {pregunta}"
        #ollama.chat(tiene dos argumentos)
        #model que es el motor de ia que se va a usar
        #messages es una lista de los mensajes que le quieres hacer a la ia
        # messages=[{message1},{message2}]
        #el contenido de cada mensaje tiene dos etiquetas el rol(quien habla) y el contenido(que dice)
        respuesta = ollama.chat(model='llama3.2', messages=[{'role': 'user', 'content': instrucciones}])
        #Hacemos que devuelva la respuesta de la ia
        #de la variable message coge el contenido/valor que hay/tiene la clave 'content' del diccionario message1
        return respuesta['message']['content']