import setuptools  # Asegúrate de tener esta importación al principio

# Abre el archivo README.md con codificación UTF-8 y lee su contenido para usarlo como descripción larga del paquete
with open("README.md", "r", encoding="utf-8") as f:
    long_description = f.read()

# Versión actual del paquete (se puede actualizar con cada release)
__version__ = "0.0.0"

# Nombre del repositorio en GitHub (usado como referencia en el setup)
REPO_NAME = "end_to_end_MLOps"

# Nombre de usuario del autor en GitHub
AUTHOR_USER_NAME = "tomMasterSchool"

# Nombre del paquete fuente
SRC_REPO = "mlProject"

# Correo del autor
AUTHOR_EMAIL = "tomasvbg@gmail.com"

# Configuración del paquete usando setuptools
setuptools.setup(
    name=SRC_REPO,
    version=__version__,
    author=AUTHOR_USER_NAME,
    author_email=AUTHOR_EMAIL,
    description="A small python package for ML app",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url=f"https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}",
    project_urls={
        "Bug Tracker": f"https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}/issues",
    },
    package_dir={"": "src"},
    packages=setuptools.find_packages(where="src"),
)
