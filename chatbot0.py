def responder(mensaje):
    mensaje = mensaje.lower()
    if "hola" in mensaje:
        return "¡Hola! ¿En qué puedo ayudarte?"
    elif "adiós" in mensaje:
        return "¡Hasta luego! Que tengas un buen día."
    else:
        return "Lo siento, no entendí eso."

def main():
    print("Chatbot simple iniciado. Escribe 'salir' para terminar.")
    while True:
        entrada = input("Tú: ")
        if entrada.lower() == "salir":
            print("Chatbot: ¡Adiós!")
            break
        respuesta = responder(entrada)
        print("Chatbot:", respuesta)

if __name__ == "__main__":
    main()
