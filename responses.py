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

    elif "gracias" in tokens or "agradecido" in tokens:
        return "¡De nada! Estoy aquí para ayudarte 😊"

    elif "precio" in tokens or "cuesta" in tokens:
        return "Nuestros precios varían según el servicio. ¿Puedes darme más detalles?"

    elif "servicios" in tokens or "ofrecen" in tokens:
        return "Ofrecemos diagnóstico, reparación y mantenimiento de autos."

    elif "horario" in tokens or "abren" in tokens or "cierran" in tokens:
        return "Nuestro horario es de lunes a viernes de 9 a.m. a 6 p.m."

    elif "ubicación" in tokens or "dónde están" in " ".join(tokens):
        return "Estamos ubicados en el centro de la ciudad, cerca del parque principal."

    elif "ayuda" in tokens or "necesito" in tokens:
        return "¡Claro! ¿Con qué necesitas ayuda?"

    elif "clima" in tokens:
        return "Lo siento, aún no tengo acceso al clima en tiempo real 🌦️"

    elif "chiste" in tokens:
        return "¿Por qué los programadores confunden Halloween con Navidad? Porque OCT 31 == DEC 25 🎃🎄"

    else:
        return "No entendí eso 🤔. ¿Puedes repetirlo?"
