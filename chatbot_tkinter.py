import tkinter as tk
from nlp_utils import limpiar_texto
from responses import obtener_respuesta

def enviar_mensaje():
    entrada_usuario = entrada.get()
    if entrada_usuario.strip() == "":
        return

    tokens = limpiar_texto(entrada_usuario)
    respuesta = obtener_respuesta(tokens)

    chat.insert(tk.END, f"Tú: {entrada_usuario}\n")
    chat.insert(tk.END, f"Chatbot: {respuesta}\n\n")
    entrada.delete(0, tk.END)

# Crear ventana
ventana = tk.Tk()
ventana.title("Chatbot con Tkinter")
ventana.geometry("400x400")

# Área de conversación
chat = tk.Text(ventana, height=20, width=50)
chat.pack(pady=10)

# Campo de entrada
entrada = tk.Entry(ventana, width=40)
entrada.pack(side=tk.LEFT, padx=10)

# Botón de enviar
boton = tk.Button(ventana, text="Enviar", command=enviar_mensaje)
boton.pack(side=tk.LEFT)

# Ejecutar la interfaz
ventana.mainloop()
