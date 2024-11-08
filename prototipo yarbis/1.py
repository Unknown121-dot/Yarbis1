# chatbot.py
from matematicas import es_expresion_valida, evaluar_expresion

def responder_pregunta(pregunta):
    pregunta = pregunta.lower().strip()
    
    if es_expresion_valida(pregunta):
        resultado = evaluar_expresion(pregunta)
        return f"El resultado es: {resultado}"
    else:
        return "Lo siento, no puedo procesar esa pregunta."

def iniciar_chat():
    print("Hola, ¿en qué te puedo ayudar hoy? (Escribe 'adiós' para salir)")
    
    while True:
        entrada = input("Tú: ")
        
        if entrada.lower() == "adiós":
            print("Adiós, ¡que tengas un buen día!")
            break
        
        respuesta = responder_pregunta(entrada)
        print("Yarbis:", respuesta)

if __name__ == "__main__":
    iniciar_chat()
