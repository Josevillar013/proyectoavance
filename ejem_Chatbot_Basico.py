# Chatbot básico con respuestas predefinidas

print("Chatbot activado. Escribe 'salir' para terminar la conversación.")

while True:
    entrada = input("Tú: ").lower()  # Lee la entrada del usuario y la convierte a minúsculas

    if "hola" in entrada:
        print("Bot: ¡Hola! ¿Cómo estás?")
    elif "como estas" in entrada:
        print("Bot: Muy bien, gracias por preguntar.")
    elif "que haces" in entrada:
        print("Bot: Estoy aprendiendo contigo :)")
    elif "adios" in entrada or "salir" in entrada:
        print("Bot: ¡Hasta luego!")
        break  # Termina el bucle y finaliza la conversación
    else:
        print("Bot: No entendí eso, ¿puedes repetirlo?")
