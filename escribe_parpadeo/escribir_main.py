"""
Módulo principal para la interacción por parpadeo en EscribeConUnParpadeo.

Este script gestiona la entrada del usuario mediante el teclado, simulando
la selección por parpadeo. Utiliza un temporizador para determinar la acción
a ejecutar según el número de pulsaciones de Enter. Permite navegar por
cuadrantes y ejecutar comandos definidos en la máquina de estados.

Asegúrate de tener configurados los cuadrantes y la máquina de estados
antes de ejecutar este módulo.
"""

import threading
import time
from typing import Any
from pynput import keyboard
from maquina_estados import *

TIEMPO_EJECUCION: int = 1

MENU_TXT: str = (
    "\nOpción inválida, por favor proporciona una entrada válida:"
    "\nArriba     = 1\nDerecha    = 2\nAbajo      = 3\nIzquierda  = 4"
    "\nRegresar   = 5"
)

TXT_CONTADOR: list[str] = [
    "Arriba    ", "Derecha   ", "Abajo     ", "Izquierda", "Regresar "
]

# Variables de control
temporizador = 0  # Tiempo transcurrido
temporizador_activo = False  # Estado del temporizador
contador_enter = 0  # Cuenta las pulsaciones de Enter
contar = True  # Controla si se sigue contando

def incrementar_temporizador() -> None:
    """
    Ejecuta la acción correspondiente cuando el temporizador expira.

    Returns:
        None
    """
    global temporizador, temporizador_activo, contador_enter
    while temporizador_activo:
        if temporizador > TIEMPO_EJECUCION:
            temporizador_activo = False
            if contador_enter in [ARRIBA, DERECHA, ABAJO, IZQUIERDA, REGRESAR]:
                control_estados(contador_enter)
            else:
                print(MENU_TXT)
            contador_enter = 0
        time.sleep(0.8)
        temporizador += 1

def on_key_press(key: Any) -> None:
    """
    Maneja el evento cuando una tecla es presionada.

    Args:
        key (Any): Tecla presionada.

    Returns:
        None
    """
    global contar, contador_enter, temporizador_activo, temporizador
    try:
        if contar:
            if key == keyboard.Key.enter:
                contar = False
                contador_enter += 1
                if contador_enter <= len(TXT_CONTADOR):
                    print(
                        f"\rSelección: {TXT_CONTADOR[contador_enter-1]}",
                        end="", flush=True
                    )
                else:
                    print(f"\nContador Enter: {contador_enter}")
                temporizador_activo = False
                temporizador = 0
            elif key == keyboard.Key.esc:
                print("Saliendo del programa...")
                # Detiene el oyente de teclado lanzando StopException
                raise keyboard.Listener.StopException()
    except AttributeError:
        pass

def on_key_release(key: Any) -> None:
    """
    Maneja el evento cuando una tecla es liberada.

    Args:
        key (Any): Tecla liberada.

    Returns:
        None
    """
    global contar, temporizador_activo, temporizador
    try:
        if key == keyboard.Key.enter:
            contar = True
            temporizador_activo = True
            threading.Thread(target=incrementar_temporizador).start()
            temporizador = 0
    except AttributeError:
        pass

def main() -> None:
    """
    Función principal que inicia el programa y los oyentes de teclado.

    Returns:
        None
    """
    imprimir_mensaje(mensaje)
    principal()
    with keyboard.Listener(
        on_press=on_key_press,
        on_release=on_key_release
    ) as listener:
        listener.join()

if __name__ == "__main__":
    main()