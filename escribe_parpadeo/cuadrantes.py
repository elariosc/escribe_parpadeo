"""
Diccionarios de cuadrantes para EscribeConUnParpadeo.

Este módulo define los cuadrantes y sus secciones, que determinan
la disposición y prioridad de los caracteres o comandos accesibles
mediante parpadeos/clics.

Guía para crear tu propio cuadrante:
------------------------------------
Cada sección contiene posiciones que requieren un número diferente de
parpadeos/clics para ser seleccionadas. Las posiciones con números más
pequeños se pueden acceder más rápido.

Prioridad en clics:
cuadrantes = {
    "grupo_1":
        {
        "seccion_1": [3, 4, 5, 6],
        "seccion_2": [4, 5, 6, 7],
        "seccion_3": [5, 6, 7, 8],
        "seccion_4": [6, 7, 8, 9]
        },
    "grupo_2":
        {
        "seccion_1": [4, 5, 6, 7],
        "seccion_2": [5, 6, 7, 8],
        "seccion_3": [6, 7, 8, 9],
        "seccion_4": [7, 8, 9, 10]
        },
    "grupo_3":
        {
        "seccion_1": [5, 6, 7, 8],
        "seccion_2": [6, 7, 8, 9],
        "seccion_3": [7, 8, 9, 10],
        "seccion_4": [8, 9, 10, 11]
        },
    "grupo_4":
        {
        "seccion_1": [6, 7, 8, 9],
        "seccion_2": [7, 8, 9, 10],
        "seccion_3": [8, 9, 10, 11],
        "seccion_4": [9, 10, 11, 12]
        }        
    }

Puedes crear tu propio cuadrante tomando esto como punto de partida.
Asegúrate de que cada sección tenga exactamente 4 elementos para evitar
errores.

Para seleccionar el conjunto de cuadrantes a usar, modifica la variable
CUADRANTE_SELECCIONADO con uno de los siguientes valores:
    - "primera_version"
    - "ia"
    - "optimizado"
"""

from typing import Dict, List

# Cuadrantes de la primera versión
cuadrantes_primera_version: Dict[str, Dict[str, List[str]]] = {
    "grupo_1": {
        "seccion_1": ["Q", "W", "E", "R"],
        "seccion_2": ["T", "Y", "U", "I"],
        "seccion_3": ["O", "", "", ""],
        "seccion_4": ["P", "?", "", ""]
    },
    "grupo_2": {
        "seccion_1": ["A", "S", "D", "F"],
        "seccion_2": ["G", "H", "J", "K"],
        "seccion_3": ["L", "", "", ""],
        "seccion_4": ["Ñ", "", "", ""]
    },
    "grupo_3": {
        "seccion_1": ["Z", "X", "C", "V"],
        "seccion_2": ["B", "N", "M", "Enter"],
        "seccion_3": ["Borrar", "", "", ""],
        "seccion_4": ["Espacio", "", "", ""]
    },
    "grupo_4": {
        "seccion_1": ["1", "2", "3", "4"],
        "seccion_2": ["5", "6", "7", "8"],
        "seccion_3": ["9", "0", "", ""],
        "seccion_4": ["Guardar", "", "", ""]
    }
}

# Cuadrantes proporcionados por IA
cuadrantes_ia: Dict[str, Dict[str, List[str]]] = {
    "grupo_1": {
        "seccion_1": ["E", "A", "O", "S"],
        "seccion_2": ["R", "N", "I", "D"],
        "seccion_3": ["L", "C", "T", "U"],
        "seccion_4": ["M", "P", "Espacio", "."]
    },
    "grupo_2": {
        "seccion_1": ["B", "G", "V", "Y"],
        "seccion_2": ["Q", "H", "F", "Z"],
        "seccion_3": ["J", "Ñ", "X", ","],
        "seccion_4": [":", ";", "\"", "Enter"]
    },
    "grupo_3": {
        "seccion_1": ["¿", "?", "¡", "!"],
        "seccion_2": ["-", "()", "[]", ""],
        "seccion_3": ["{", "}", "/", "*"],
        "seccion_4": ["=", "+", "", "Borrar"]
    },
    "grupo_4": {
        "seccion_1": ["<", ">", "%", ""],
        "seccion_2": ["@", "|", "&", ""],
        "seccion_3": ["_", "#", "$", ""],
        "seccion_4": ["^", "\\", "", ""]
    }
}

# Cuadrantes optimizados por frecuencia de uso (por defecto)
cuadrantes_optimizado: Dict[str, Dict[str, List[str]]] = {
    "grupo_1": {
        "seccion_1": ["Espacio", "E", "L", "Borrar"],
        "seccion_2": ["A", "S", "Enter", "H"],
        "seccion_3": ["N", "I", "G", ";"],
        "seccion_4": ["T", "F", "?", "7"]
    },
    "grupo_2": {
        "seccion_1": ["O", "D", "C", "V"],
        "seccion_2": ["R", "P", "J", "!"],
        "seccion_3": ["M", "Ñ", "(", "8"],
        "seccion_4": ["Z", ")", "9", "&"]
    },
    "grupo_3": {
        "seccion_1": ["U", "Y", "X", "0"],
        "seccion_2": ["Q", "K", "1", "/"],
        "seccion_3": ["W", "2", "*", "_"],
        "seccion_4": ["3", "=", "#", "^"]
    },
    "grupo_4": {
        "seccion_1": ["B", ",", "4", "+"],
        "seccion_2": [".", "5", "-", "$"],
        "seccion_3": ["6", ":", "%", "@"],
        "seccion_4": ["\"", "...", "¿", "Guardar"]
    }
}

CUADRANTE_SELECCIONADO: str = "optimizado"  # Cambia a "primera_version" o "ia"

def obtener_cuadrantes(nombre: str) -> Dict[str, Dict[str, List[str]]]:
    """
    Retorna el diccionario de cuadrantes según el nombre seleccionado.

    Args:
        nombre (str): Nombre del conjunto de cuadrantes a usar.
            Puede ser 'primera_version', 'ia' o 'optimizado'.

    Returns:
        Dict[str, Dict[str, List[str]]]: Diccionario de cuadrantes.
    """
    if nombre == "primera_version":
        return cuadrantes_primera_version
    elif nombre == "ia":
        return cuadrantes_ia
    elif nombre == "optimizado":
        return cuadrantes_optimizado
    else:
        raise ValueError(
            f"Nombre de cuadrante '{nombre}' no válido. "
            "Usa 'primera_version', 'ia' o 'optimizado'."
        )

cuadrantes: Dict[str, Dict[str, List[str]]] = obtener_cuadrantes(
    CUADRANTE_SELECCIONADO
)

if __name__ == "__main__":
    print(
        "Este módulo solo define los cuadrantes y no debe ejecutarse "
        "directamente."
    )