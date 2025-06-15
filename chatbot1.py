from nlp_utils import limpiar_texto
from responses import obtener_respuesta

def guardar_en_historial(entrada, respuesta):
    with open("historial.txt", "a", encoding="utf-8") as f:
        f.write(f"Tú: {entrada}\n")
        f.write(f"Chatbot: {respuesta}\n\n")

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

        # Guardar la conversación
        guardar_en_historial(entrada, respuesta)

if __name__ == "__main__":
    main()
