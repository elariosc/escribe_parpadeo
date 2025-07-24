"""
Sistema de escritura fácil para EscribeConUnParpadeo.

Este módulo permite la selección de caracteres mediante cuadrantes.
Las entradas del usuario determinan la navegación por grupos y secciones,
permitiendo construir mensajes de texto. Incluye funciones para guardar
el mensaje y controlar la transición de estados.

Autor: Eduardo Larios Cruz
Fecha: 2025-07-16
Versión: 1.0
"""

from cuadrantes import cuadrantes
from pantalla import (
    imprimir_mensaje,
    imprime_sub_cuadrante,
    imprime_elementos,
    principal,
)
import datetime

# Estados de navegación
INICIAL: int = 0
ARRIBA: int = 1
DERECHA: int = 2
ABAJO: int = 3
IZQUIERDA: int = 4
REGRESAR: int = 5

GRUPOS: list[str] = ["grupo_1", "grupo_2", "grupo_3", "grupo_4"]
SECCIONES: list[str] = ["seccion_1", "seccion_2", "seccion_3", "seccion_4"]

TXT_REGRESAR_INVALIDO: str = (
    "\nTe encuentras en el menú principal, la opción 'regresar' no es válida"
)
MENU_TXT_PRINCIPAL: str = (
    "\nPor favor proporciona una entrada válida:"
    "\nArriba     = 1"
    "\nDerecha    = 2"
    "\nAbajo      = 3"
    "\nIzquierda  = 4"
)

# Variables globales de estado
estado: int | str = INICIAL
seccion: int | str = INICIAL
inicio_programa: bool = True
mensaje: str = ""


def guardar() -> None:
    """
    Guarda el mensaje en un archivo de texto con la fecha y hora actual.

    Returns:
        None
    """
    fecha_hora_actual: datetime.datetime = datetime.datetime.now()
    nombre_archivo: str = fecha_hora_actual.strftime("%Y-%m-%d_%H-%M-%S.txt")
    try:
        with open(nombre_archivo, 'a', encoding='utf-8') as archivo:
            archivo.write(mensaje + '\n')
        print(f"Texto guardado en {nombre_archivo}")
    except Exception as e:
        print(f"Error al guardar: {e}")


def control_estados(direccion: int) -> None:
    """
    Maneja la transición de estados según la dirección proporcionada.

    Args:
        direccion (int): Dirección seleccionada por el usuario.

    Returns:
        None
    """
    global estado, seccion, mensaje, inicio_programa

    if inicio_programa:
        mensaje = ""
        inicio_programa = False

    if estado == INICIAL:
        if direccion == REGRESAR:
            print(TXT_REGRESAR_INVALIDO)
        else:
            estado = GRUPOS[direccion - 1]
            imprimir_mensaje(mensaje)
            imprime_sub_cuadrante(cuadrantes[estado])
    elif seccion == INICIAL:
        if direccion == REGRESAR:
            imprimir_mensaje(mensaje)
            principal()
            estado = INICIAL
        else:
            seccion = SECCIONES[direccion - 1]
            imprimir_mensaje(mensaje)
            imprime_elementos(cuadrantes[estado][seccion])
    else:
        if direccion == REGRESAR:
            imprimir_mensaje(mensaje)
            imprime_sub_cuadrante(cuadrantes[estado])
            seccion = INICIAL
        else:
            letra: str = cuadrantes[estado][seccion][direccion - 1]
            if letra == "Espacio":
                mensaje += " "
            elif letra == "Borrar":
                mensaje = mensaje[:-1]
            elif letra == "Enter":
                mensaje += "\n"
            elif letra == "Guardar":
                guardar()
                mensaje = ""
            else:
                mensaje += letra
            imprimir_mensaje(mensaje)
            principal()
            estado, seccion = INICIAL, INICIAL


if __name__ == "__main__":
    print(
        "Este módulo es parte de EscribeConUnParpadeo y no debe ejecutarse "
        "directamente."
    )