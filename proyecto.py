from agente import Agente
Agente_ia=Agente()
print("Chatbot documental")
print("Escribe 'salir' para terminar")

# 2. Bucle de conversación
while True:
    pregunta = input("Pregunta: ")
    
    if pregunta.lower() == 'salir':
        break
    
    # 3. El agente procesa y responde
    respuesta = Agente_ia.respuesta(pregunta)
    print(f"Agente: {respuesta}")