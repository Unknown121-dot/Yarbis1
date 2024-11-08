# matematicas.py
import re

def es_expresion_valida(expresion):
    """
    Verifica si la expresión matemática es válida.
    Solo permite operaciones básicas como +, -, *, /, y números.
    """
    # Expresión regular para validar una operación matemática simple
    patron = r'^[\d\+\-\*/\(\)\.\s]+$'
    return bool(re.match(patron, expresion))

def evaluar_expresion(expresion):
    """
    Evalúa una expresión matemática dada y devuelve el resultado.
    """
    try:
        # Usamos eval de forma segura con la validación previa
        if es_expresion_valida(expresion):
            resultado = eval(expresion)
            return resultado
        else:
            return "La expresión no es válida."
    except Exception as e:
        return f"Error al evaluar la expresión: {str(e)}"
