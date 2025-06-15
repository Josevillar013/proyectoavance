def obtener_respuesta(tokens):
    if "hola" in tokens or "buenas" in tokens:
        return "¡Hola! ¿Cómo estás?"
    elif "adiós" in tokens or "hasta" in tokens:
        return "¡Hasta luego! 😊"
    elif "tu nombre" in " ".join(tokens):
        return "Soy un chatbot creado por ti 🚀"
    elif "hora" in tokens:
        from datetime import datetime
        return f"La hora actual es: {datetime.now().strftime('%H:%M:%S')}"
    else:
        return "No entendí eso 🤔. ¿Puedes repetirlo?"
