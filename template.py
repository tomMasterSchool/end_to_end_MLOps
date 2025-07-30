"""
Este script automatiza la creación de la estructura base para un proyecto de Machine Learning.

Lo que hace:
- Define una lista de rutas de archivos y carpetas que forman parte de la arquitectura del proyecto.
- Crea cada carpeta si no existe.
- Crea archivos vacíos si no existen o si están vacíos.
- Registra mensajes en consola informando cada acción (creación de carpetas, archivos, o detección de que ya existen).

Es útil para estandarizar el inicio de nuevos proyectos, asegurando que todos los módulos, paquetes y archivos de configuración estén presentes desde el comienzo.
"""




# Importa módulos para manejar el sistema de archivos y logging
import os
from pathlib import Path
import logging

# Configura el sistema de logging para mostrar mensajes de nivel INFO con formato de timestamp
logging.basicConfig(level=logging.INFO, format='[%(asctime)s]: %(message)s:')

# Nombre del proyecto base (se usará para crear la estructura del código fuente)
project_name = "mlProject"

# Lista con las rutas de archivos/carpetas que se crearán en el proyecto
list_of_files = [
    ".github/workflows/.gitkeep",  # Para mantener el directorio en control de versiones aunque esté vacío
    f"src/{project_name}/__init__.py",  # Inicializa el paquete principal del proyecto
    f"src/{project_name}/components/__init__.py",  # Inicializa el subpaquete components
    f"src/{project_name}/utils/__init__.py",  # Inicializa el subpaquete utils
    f"src/{project_name}/config/common.py",  # Módulo para configuraciones compartidas
    f"src/{project_name}/config/__init__.py",  # Inicializa el subpaquete config
    f"src/{project_name}/config/configuration.py",  # Módulo principal de configuración
    f"src/{project_name}/pipeline/__init__.py",  # Inicializa el subpaquete pipeline
    f"src/{project_name}/entity/__init__.py",  # Inicializa el subpaquete entity
    f"src/{project_name}/entity/config_entity.py",  # Módulo con clases de configuración (nombre corregido)
    f"src/{project_name}/constant/__init__.py",  # Inicializa el subpaquete constant
    "config/config.yaml",  # Archivo YAML para configuración general (nombre corregido)
    "schema.yaml",  # Archivo para definir el esquema de datos
    "params.yaml",  # Archivo con parámetros del modelo o del pipeline
    "main.py",  # Script principal del proyecto
    "Dockerfile",  # Definición del contenedor Docker
    "requirements.txt",  # Lista de dependencias del proyecto (nombre corregido)
    "setup.py",  # Script de instalación del paquete
    "research/trials.ipynb",  # Notebook para pruebas o prototipos
    "templates/index.html",
    "test.py"  # Página HTML de plantilla (posible para apps web)
]


# Itera sobre cada archivo definido en la lista
for filepath in list_of_files:
    filepath = Path(filepath)  # Convierte la ruta a un objeto Path (más robusto que string)
    filedir, filename = os.path.split(filepath)  # Separa la ruta en directorio y nombre de archivo

    if filedir != "":
        os.makedirs(filedir, exist_ok=True)  # Crea el directorio si no existe; evita error si ya existe
        logging.info(f"Creating directory: {filedir} for the file: {filename}")  # Log de creación de directorio

    # Si el archivo no existe o está vacío
    if (not os.path.exists(filepath)) or (os.path.getsize(filepath) == 0):
        with open(filepath, "w") as f:  # Crea un archivo vacío
            pass
        logging.info(f"Creating empty file: {filepath}")  # Log de creación de archivo vacío
    else:
        logging.info(f"{filename} already exists and is not empty")  # Log si el archivo ya existe y no está vacío

