"""
Funciones para mostrar mensajes y cuadrantes en la terminal para
EscribeConUnParpadeo.
"""

import os
from typing import Dict, List
from cuadrantes import *

# ----------------------------------------------------------------------
# Sección 1: Definición de constantes
# ----------------------------------------------------------------------
SANGRIA: int = 20
TXT_MENSAJE: str = (
    "Para escribir, parpadea el número de veces necesarios para seleccionar "
    "la región deseada:\n"
    "Arriba     = 1\n"
    "Derecha    = 2\n"
    "Abajo      = 3\n"
    "Izquierda  = 4\n"
    "Regresar   = 5"
)

mensaje: str = TXT_MENSAJE

# Obtener el ancho de la terminal
terminal_width: int = os.get_terminal_size().columns

# ----------------------------------------------------------------------
# Sección 2: Definición de funciones
# ----------------------------------------------------------------------
def imprimir_mensaje(mensaje: str) -> None:
    """
    Limpia la pantalla y muestra el mensaje ajustado.

    Args:
        mensaje (str): Texto a mostrar.

    Returns:
        None
    """
    limpiar_pantalla()
    ajustar_mensaje(mensaje)

def ajustar_mensaje(mensaje: str) -> None:
    """
    Ajusta el mensaje para mostrar solo las últimas 7 líneas.

    Args:
        mensaje (str): Texto a mostrar.

    Returns:
        None
    """
    lineas: List[str] = mensaje.splitlines()
    ultimas_lineas: List[str] = lineas[-7:]
    print("\nComposición: ")
    print("_" * 80)
    for linea in ultimas_lineas:
        print(linea)
    print("_" * 80, "\n\n")

def limpiar_pantalla() -> None:
    """
    Limpia la pantalla según el sistema operativo.

    Returns:
        None
    """
    os.system('cls' if os.name == 'nt' else 'clear')

def imprime_centrado(texto: str) -> None:
    """
    Imprime un texto centrado en la terminal.

    Args:
        texto (str): Texto a centrar.

    Returns:
        None
    """
    terminal_width: int = os.get_terminal_size().columns
    print(texto.center(terminal_width - 2))

def imprime_izq_der(texto_izq: str, texto_der: str) -> None:
    """
    Imprime un texto alineado a la izquierda y otro a la derecha.

    Args:
        texto_izq (str): Texto alineado a la izquierda.
        texto_der (str): Texto alineado a la derecha.

    Returns:
        None
    """
    if terminal_width < (len(texto_izq) + len(texto_der)):
        print(texto_izq + " " + texto_der)
    else:
        espacio_extra: str = " " * (
            terminal_width - (len(texto_izq) + len(texto_der) + SANGRIA)
        )
        print(
            " " * (SANGRIA // 2) + texto_izq +
            espacio_extra + texto_der + " " * (SANGRIA // 2)
        )

def principal() -> None:
    """
    Imprime los cuadrantes principales.

    Returns:
        None
    """
    for j in range(1, 5):
        imprime_centrado(" ".join(cuadrantes["grupo_1"][f"seccion_{j}"]))
    for j in range(1, 5):
        imprime_izq_der(
            " ".join(cuadrantes["grupo_4"][f"seccion_{j}"]),
            " ".join(cuadrantes["grupo_2"][f"seccion_{j}"])
        )
    for j in range(1, 5):
        imprime_centrado(" ".join(cuadrantes["grupo_3"][f"seccion_{j}"]))

def imprime_sub_cuadrante(sub_cuadrante: Dict[str, List[str]]) -> None:
    """
    Imprime las secciones de un cuadrante.

    Args:
        sub_cuadrante (dict): Diccionario con las secciones.

    Returns:
        None
    """
    imprime_centrado(" ".join(sub_cuadrante["seccion_1"]))
    imprime_izq_der(
        " ".join(sub_cuadrante["seccion_4"]),
        " ".join(sub_cuadrante["seccion_2"])
    )
    imprime_centrado(" ".join(sub_cuadrante["seccion_3"]))

def imprime_elementos(seccion: List[List[str]]) -> None:
    """
    Imprime los elementos de una sección.

    Args:
        seccion (list): Lista con los elementos de la sección.

    Returns:
        None
    """
    imprime_centrado(" ".join(seccion[0]))
    imprime_izq_der(
        " ".join(seccion[3]),
        " ".join(seccion[1])
    )
    imprime_centrado(" ".join(seccion[2]))

if __name__ == "__main__":
    print(
        "Este módulo es parte de EscribeConUnParpadeo y no debe ejecutarse "
        "directamente."
    )