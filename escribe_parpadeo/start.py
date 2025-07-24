"""
Script para iniciar los módulos de EscribeConUnParpadeo.
Ejecuta lectura_serie.py minimizado y escribir_main.py en una terminal visible.
"""

import os
import sys
import subprocess
import time

def get_base_path() -> str:
    """
    Obtiene la ruta base del programa, considerando si está empaquetado.

    Returns:
        str: Ruta base del programa.
    """
    if getattr(sys, 'frozen', False):
        return sys._MEIPASS  # PyInstaller extrae los archivos aquí
    return os.path.dirname(os.path.abspath(__file__))

def run_script(script_path: str, minimized: bool = False) -> None:
    """
    Ejecuta un script Python en una terminal de Windows.

    Args:
        script_path (str): Ruta al script Python.
        minimized (bool): Si True, ejecuta la terminal minimizada.

    Returns:
        None
    """
    if minimized:
        cmd = f'start /min python "{script_path}"'
    else:
        cmd = f'start cmd /k python "{script_path}" 2> nul'
    try:
        subprocess.Popen(cmd, shell=True)
    except Exception as e:
        print(f"Error al ejecutar {script_path}: {e}")

def main() -> None:
    """
    Función principal para iniciar los módulos del sistema.

    Returns:
        None
    """
    base_path = get_base_path()
    lectura_serie = os.path.join(base_path, "lectura_serie.py")
    escribir_main = os.path.join(base_path, "escribir_main.py")

    # Ejecutar lectura_serie.py minimizado
    run_script(lectura_serie, minimized=True)

    # Esperar para asegurar que lectura_serie.py está en ejecución
    time.sleep(2)

    # Ejecutar escribir_main.py en terminal visible
    run_script(escribir_main, minimized=False)

if __name__ == "__main__":
    main()