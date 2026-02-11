# 🎮 Tetris

Una implementación completa del clásico juego **Tetris** desarrollada en Python con interfaz de consola usando **curses**. El proyecto incluye gestión de puntuaciones, sistema de niveles dinámicos y almacenamiento persistente de récords.

## 📋 Tabla de Contenidos

- [Descripción](#descripción)
- [Características](#características)
- [Requisitos Previos](#requisitos-previos)
- [Instalación](#instalación)
- [Uso](#uso)
- [Controles](#controles)
- [Estructura del Proyecto](#estructura-del-proyecto)
- [Mecánicas del Juego](#mecánicas-del-juego)
- [Tecnologías](#tecnologías)
- [Contribuciones](#contribuciones)
- [Licencia](#licencia)
- [Autor](#autor)

---

## 📝 Descripción

Este proyecto implementa el famoso juego Tetris con todas sus mecánicas clásicas:
- Caída automática de piezas (Tetrominós)
- Detección de colisiones y bloqueos
- Eliminación de filas completas
- Sistema de puntuación progresivo
- Aumento dinámico de velocidad con el nivel
- Almacenamiento de puntuaciones de jugadores
- Interfaz visual en la consola con emojis coloridos

El juego ha sido desarrollado como proyecto educativo para practicar conceptos de programación estructurada, gestión de estado y persistencia de datos.

## ✨ Características

✅ **Mecánicas de Juego Completas**
- 7 tipos de piezas diferentes (Tetrominós estándar)
- Rotación de piezas con 4 estados
- Detección de colisiones en tiempo real
- Sistema de scoring con multiplicadores por filas eliminadas
- Velocidad progresiva (aumenta cada 5 puntos)

✅ **Interfaz Visual**
- Tablero de 10×15 bloques
- Logo ASCII art en colores
- Información de puntuación y velocidad en pantalla
- Bordes decorativos con caracteres Unicode
- Emojis para diferenciación de piezas

✅ **Sistema de Puntuaciones**
- Persistencia de récords en base de datos
- Tabla de puntuaciones visible al perder
- Validación de nombres de jugador (mín. 3 caracteres)
- Almacenamiento y recuperación de datos

✅ **Controles Intuitivos**
- Movimientos fluidos con teclas de flecha
- Rotación con barra espaciadora
- Salida rápida con 'q'

## 🔧 Requisitos Previos

- **Python 3.8+**
- Sistema operativo: Linux, macOS o Windows (con terminal compatible)
- Terminal con soporte para caracteres Unicode y emojis

## 📦 Instalación

1. **Clona el repositorio:**
   ```bash
   git clone https://github.com/MiguelViHe/Tetris.git
   cd Tetris
   ```
2. **Crea un entorno virtual:**
   ```bash
   python -m venv venv
   source venv/bin/activate  # En Windows: venv\Scripts\activate
   ```
3. **Instala las dependencias (si son necesarias):**
   ```bash
   pip install -r requirements.txt
   ```
   Nota: Este proyecto usa curses, que es parte de la librería estándar de Python en Linux/macOS. En Windows, puede requerir instalación adicional o el uso de WSL.

## 🚀 Uso
Ejecuta el juego desde la línea de comandos:

```bash
python -m src.tetris
```
El juego se iniciará en tu terminal. Asegúrate de que tu ventana de terminal sea lo suficientemente grande para mostrar el tablero (mín. 20×30 caracteres).

## 🎮 Controles

| Acción            | Tecla                |
|------------------|----------------------|
| Mover Izquierda  | ⬅️ Flecha izquierda  |
| Mover Derecha    | ➡️ Flecha derecha    |
| Descender Rápido | ⬇️ Flecha abajo      |
| Girar Pieza      | Barra espaciadora    |
| Salir del Juego  | q                    |


## Mecánicas
- Caída Automática: Las piezas caen automáticamente según la velocidad actual (comienza en 1.0s y disminuye)
- Detección Automática de Game Over: El juego termina cuando una pieza nueva no puede colocarse en la parte superior del tablero
- Eliminación de Filas: Cuando completas una fila horizontal, se elimina y las filas superiores caen
- Puntuación: Ganas puntos según el número de filas eliminadas en un movimiento

## 📁 Estructura del Proyecto
```Code
Tetris/
├── src/
│   ├── __init__.py           # Inicializador del paquete
│   ├── tetris.py             # Función principal del juego
│   ├── pieces.py             # Definición de piezas (Tetrominós)
│   ├── piece_actions.py      # Lógica de movimiento y rotación
│   ├── checkers.py           # Detección de colisiones
│   ├── constants.py          # Constantes y enumeraciones
│   ├── printer.py            # Renderizado en consola
│   ├── gameover.py           # Pantalla de game over
│   ├── score.py              # Lógica de puntuación
│   └── speed.py              # Cálculo de velocidad
├── persistence/
│   └── repository/           # Gestión de persistencia (BD)
├── data/                     # Almacenamiento de datos
├── requirements.txt          # Dependencias del proyecto
├── .gitignore                # Archivos ignorados por Git
├── .python-version           # Versión recomendada de Python
└── README.md                 # Este archivo
```

## Archivos Principales
| Archivo               | Descripción                                                   |
|------------------------|---------------------------------------------------------------|
| src/tetris.py          | Punto de entrada del juego y bucle principal                 |
| src/pieces.py          | Definición de las 7 piezas Tetris con sus rotaciones         |
| src/piece_actions.py   | Movimiento, rotación, bloqueo y eliminación de filas         |
| src/checkers.py        | Validación de colisiones y límites del tablero               |
| src/constants.py       | Dimensiones del tablero, velocidad inicial, logo             |
| src/printer.py         | Renderizado visual del juego en consola                      |
| src/gameover.py        | Interfaz de fin de juego y captura de nombre                 |
| src/score.py           | Cálculo y almacenamiento de puntuaciones                     |
| src/speed.py           | Función para aumentar la velocidad con los puntos            |


## 🎲 Mecánicas del Juego
Sistema de Piezas
Las 7 piezas Tetris estándar (Tetrominós):

 ⬛ I (Negro): Línea recta  
 🟦 J (Azul): Forma de L invertida  
 🟧 L (Naranja): Forma de L  
 🟨 O (Amarillo): Cuadrado  
 🟥 Z (Rojo): Escalera izquierda  
 🟪 T (Púrpura): Forma de T  
 🟩 S (Verde): Escalera derecha  


Sistema de Puntuación
- 1 fila completa = 1 punto
- 2 filas completas = 2.5 puntos
- 3 filas completas = 4.5 puntos
- 4 filas completas = 7 puntos
Velocidad Progresiva

La velocidad aumenta conforme acumulas puntos:

- Comenzar: 1.0 segundos entre caídas
- Aumenta según la fórmula: velocidad = 1.0 - (puntos * 0.05)
- Velocidad mínima: 0.2 segundos (muy rápido)

El juego valida:

- Límites laterales del tablero
- Bloqueo en el suelo
- Colisión con piezas anteriores
- Rotaciones válidas

## 🛠️ Tecnologías
- Lenguaje: Python 3.8+
- Librería de Consola: curses (estándar en Python)
- Persistencia: Base de datos para puntuaciones (SQLite)
- Estructura: Programación orientada a objetos y funcional

Futuras Mejoras
- Agregar sonidos
- Implementar modo multijugador
- Crear interfaz gráfica (Pygame)
- Sistema de logros/medallas

## 👤 Autor
MiguelViHe
GitHub: @MiguelViHe

## 🙋 Soporte
Si encuentras problemas o tienes sugerencias:

- Abre un issue en GitHub
- Describe el problema con la máxima claridad posible
- Incluye pasos para reproducir el error (si aplica)
¡Gracias por jugar Tetris! 🎮
