import nltk
from nltk.tokenize import word_tokenize

# Descargar recursos si es necesario
nltk.download('punkt', quiet=True)

def limpiar_texto(texto):
    return word_tokenize(texto.lower())
