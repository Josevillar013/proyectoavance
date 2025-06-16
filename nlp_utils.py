import re 
from nltk.tokenize import word_tokenize

# Descargar recursos si es necesario
nltk.download('punkt', quiet=True)

def limpiar_texto(texto):
    return re.findall(r'\b\w+\b', texto.lower())
