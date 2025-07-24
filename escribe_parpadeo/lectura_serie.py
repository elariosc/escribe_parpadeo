"""
Este script permite la comunicación entre un Arduino y la computadora
a través del puerto serie. Lee señales enviadas por el Arduino y simula
la pulsación de la tecla "Enter" en el sistema operativo cuando recibe
la instrucción correspondiente. El puerto serie se configura mediante
el archivo config.ini. El script maneja errores de conexión y asegura
el cierre seguro del puerto al finalizar la ejecución.

Uso principal:
- Detectar señales de parpadeo desde Arduino.
- Simular la pulsación de "Enter" en la computadora.
- Configuración flexible del puerto serie.
"""

import serial
import pyautogui
import configparser

def obtener_puerto() -> str:
    """
    Obtiene el puerto serie desde el archivo de configuración.

    Returns:
        str: Puerto serie configurado o 'COM3' por defecto.
    """
    config: configparser.ConfigParser = configparser.ConfigParser()
    config.read("config.ini")
    return config.get("Settings", "COM_PORT", fallback="COM3")

def main() -> None:
    """
    Función principal para la comunicación con Arduino y simulación
    de la tecla Enter.

    Returns:
        None
    """
    puerto: str = obtener_puerto()
    try:
        arduino: serial.Serial = serial.Serial(puerto, 9600, timeout=1)
        print(f"Conectado a {puerto}")

        while True:
            linea: str = arduino.readline().decode().strip()
            if linea == "ENTER":
                pyautogui.keyDown("enter")  # Simula tecla presionada
                print("Enter presionado")
            elif linea == "RELEASE":
                pyautogui.keyUp("enter")  # Simula tecla liberada
                print("Enter liberado")
    except serial.SerialException:
        print(f"No se pudo conectar al puerto {puerto}")
    except KeyboardInterrupt:
        print("\nPrograma terminado por el usuario")
    finally:
        if 'arduino' in locals():
            arduino.close()  # Cierra la conexión con el puerto serie

if __name__ == "__main__":
    main()