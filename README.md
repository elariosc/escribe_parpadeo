# EscribeConUnParpadeo

**EscribeConUnParpadeo** es un sistema de escritura accesible que permite a los usuarios escribir utilizando parpadeos, detectados mediante un sensor infrarrojo instalado en unos lentes personalizados. Este proyecto está diseñado para personas con movilidad limitada, ofreciéndoles una manera eficiente de comunicarse usando solo el movimiento de los ojos.

## 🚀 Características

- Escritura mediante parpadeos detectados por sensor IR.
- Comunicación entre Arduino y PC.
- Sistema de entrada personalizable con cuadrantes.
- Compatible con diferentes plataformas mediante Python.
- Interfaz adaptable.
- Fácil de usar y expandir.

## 📁 Estructura del proyecto

```
escribe_parpadeo/
├── arduino/
│ └── parpadeo_lentes.ino # Código para Arduino Nano
│
├── docs/ # Documentación (actualmente vacía)
│
├── escribe_parpadeo/
│ ├── config.ini # Configuración del puerto serie (COM)
│ ├── cuadrantes.py # Diccionario de cuadrantes personalizables
│ ├── ejecutar.bat # Archivo ejecutable en windows para lanzar el programa
│ ├── escribir_main.py # Programa principal de escritura
│ ├── instalar_librerias.bat # Archivo ejecutable en windows para instalar las librerias necesarias
│ ├── lectura_serie.py # Script para recibir datos del Arduino
│ ├── maquina_estados.py # Lógica del sistema de escritura
│ ├── pantalla.py # Biblioteca para controlar la impresion de caracteres
│ ├── requirements.txt # Listado de dependencias/librerias necesarias para ejecutar el programa
│ └── start.py # Script para iniciar la aplicación
│
├── modelos_3d/
│ ├── occhiali stenopeici sniper bambu.3mf # Modelo 3D de los lentes
│ └── README.md # Créditos y detalles del modelo
│
├── tests/ # Carpeta para pruebas (actualmente vacía)
│
├── .gitignore # Exclusiones de Git (pycache, etc.)
├── CHANGELOG.md # Registro de cambios del proyecto
├── LICENSE # Licencia MIT (bilingüe)
└── README.md # Documentación principal del proyecto
```

## 🛠️ Requisitos

- Arduino Nano (u otro compatible con teclado HID)
- Sensor Infrarrojo (IR)
- Buzzer (opcional)
- Python 3.10+
- Paquetes: `pyserial`, `keyboard`, `configparser`, `time`

## ⚙️ Instalación
### Opcion 1: Usando linea de comandos

1. Clona el repositorio:
   ```bash
   git clone https://github.com/elariosc/escribe_parpadeo.git
   cd escribe_parpadeo/escribe_parpadeo
   ```

2. Instala las dependencias de Python:
   ```bash
   pip install -r requirements.txt
   ```

3. Conecta el Arduino, carga el código `.ino` y ajusta el puerto en `config.ini`.

4. Ejecuta los scripts:
   ```bash
   python start.py
   ```

### Opcion 2: Entorno de windows

1. En un explorador de internet ve a la pagina:

   https://github.com/elariosc/escribe_parpadeo.git
   
   y descarga el release mas reciente.
   
2. Instala las dependencias de Python:

   Navega por las carpetas y entra en la carpeta `escribe_parpadeo` dos veces hasta
   que veas los archivo con extension `.py`

   Dale doble clic al archivo `instalar_librerias.bat`

   Tambien puedes abrir el cmd en esta ubicacion y ejecutar:
   ```bash
   pip install -r requirements.txt
   ```
   
3. Conecta el Arduino, carga el código `.ino` y ajusta el puerto en `config.ini`.

4. En la misma ubicacion de el punto 3, ejecuta los scripts:
   
   Dale doble clic al archivo `ejecutar.bat`

   Tambien puedes abrir el cmd en esta ubicacion y ejecutar:
   ```bash
   python start.py
   ```
   
## 👓 Créditos del modelo 3D

Los modelos utilizados para los lentes se basan en el diseño publicado por el usuario [Sam Seegmiller](https://makerworld.com/en/u/samseegmiller) en MakerWorld:

**Modelo:**  
[Pinhole Shooting Glasses – MakerWorld](https://makerworld.com/en/models/1039596-pinhole-shooting-glasses#profileId-1024155)

## 📜 Licencia

Este proyecto está licenciado bajo la Licencia MIT.

Consulta el archivo [LICENSE](./LICENSE) para ver los términos completos en inglés y español.
