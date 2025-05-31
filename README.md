# Generador de Correos Institucionales 🏫✉️

## Descripción 📄
Herramienta modular en Python para procesar datos de estudiantes y generar:
- Correos electrónicos institucionales (formato: `l[numero_control]@pachuca.tecnm.mx`)
- Listados de números de control (formato separado por `OR`)
- Todo esto para poder automatizar y facilitar la creación de los correos sin antes recibirlos para poder crear filtros en GMAIL, separandolos de otra lista con datos inecesarios

## Características principales ✨
- **Extracción automática** de números de control desde archivos TXT
- **Múltiples formatos** de salida configurables
- **Arquitectura modular** fácil de extender
- **Validación integrada** de datos
- **Interfaz interactiva** paso a paso

## Estructura del código 🧱
```bash
.
├── Generador_Correos.py   # Programa principal
├── sample_data.txt        # Ejemplo de datos de entrada
├── correos_ejemplo.txt    # Ejemplo de salida (correos)
└── numeros_ejemplo.txt    # Ejemplo de salida (números)