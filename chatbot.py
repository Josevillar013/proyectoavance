from nlp_utils import limpiar_texto
from responses import obtener_respuesta

def main():
    print("Chatbot avanzado iniciado. Escribe 'salir' para terminar.")
    while True:
        entrada = input("Tú: ")
        if entrada.lower() == "salir":
            print("Chatbot: ¡Adiós!")
            break
        tokens = limpiar_texto(entrada)
        respuesta = obtener_respuesta(tokens)
        print("Chatbot:", respuesta)

if __name__ == "__main__":
    main()
