#!/usr/bin/env python3
"""
Script de configuración para el proyecto de análisis de Netflix
Ejecuta este script para configurar automáticamente el entorno del proyecto
"""

import os
import sys
import subprocess
from pathlib import Path


def run_command(command, description):
    """Ejecuta un comando y muestra el resultado"""
    print(f"🔄 {description}...")
    try:
        subprocess.run(command, shell=True, check=True, capture_output=True, text=True)
        print(f"✅ {description} completado")
        return True
    except subprocess.CalledProcessError as e:
        print(f"❌ Error en {description}: {e}")
        print(f"Output: {e.output}")
        return False


def check_python_version():
    """Verifica que la versión de Python sea compatible"""
    version = sys.version_info
    if version.major == 3 and version.minor >= 9:
        print(f"✅ Python {version.major}.{version.minor}.{version.micro} detectado")
        return True
    else:
        print(
            f"❌ Python 3.9+ requerido. Versión actual: {version.major}.{version.minor}.{version.micro}"
        )
        return False


def setup_virtual_environment():
    """Configura el entorno virtual"""
    venv_path = Path(".venv")

    if venv_path.exists():
        print("✅ Entorno virtual ya existe")
        return True

    return run_command("python -m venv .venv", "Creando entorno virtual")


def install_requirements():
    """Instala las dependencias del requirements.txt"""
    requirements_path = Path("requirements.txt")

    if not requirements_path.exists():
        print("❌ Archivo requirements.txt no encontrado")
        return False

    # Detectar el sistema operativo para usar el activador correcto
    if os.name == "nt":  # Windows
        pip_cmd = ".venv\\Scripts\\pip"
    else:  # Unix/Linux/MacOS
        pip_cmd = ".venv/bin/pip"

    return run_command(
        f"{pip_cmd} install -r requirements.txt", "Instalando dependencias"
    )


def check_datasets():
    """Verifica la existencia del dataset principal y archivos opcionales"""
    main_dataset = "data/netflix_dataset.csv"

    if not Path(main_dataset).exists():
        print(f"⚠️  Dataset principal faltante: {main_dataset}")
        print("\nPor favor, coloca el archivo netflix_dataset.csv en la carpeta data/.")
        return False
    else:
        print("✅ Dataset principal encontrado: data/netflix_dataset.csv")

    # Verificar archivos opcionales de IMDb
    optional_files = ["data/imdb-ratings.csv", "data/imdb-movies.csv"]
    for file in optional_files:
        if Path(file).exists():
            print(f"✅ Archivo opcional encontrado: {file}")
        else:
            print(f"ℹ️  Archivo opcional no encontrado: {file} (no es requerido)")

    return True


def create_data_directory():
    """Crea directorios para organizar mejor los datos"""
    directories = ["data", "outputs", "models"]

    for directory in directories:
        Path(directory).mkdir(exist_ok=True)
        print(f"✅ Directorio '{directory}' creado/verificado")


def main():
    """Función principal del script de configuración"""
    print("🎬 Configuración del Proyecto de Análisis de Netflix")
    print("=" * 50)

    # Verificar versión de Python
    if not check_python_version():
        return

    # Configurar entorno virtual
    if not setup_virtual_environment():
        return

    # Instalar dependencias
    if not install_requirements():
        return

    # Crear directorios
    create_data_directory()

    # Verificar datasets
    check_datasets()

    print("\n🎉 Configuración completada!")
    print("\nPara activar el entorno virtual:")
    if os.name == "nt":
        print("   .venv\\Scripts\\activate")
    else:
        print("   source .venv/bin/activate")

    print("\nPara ejecutar Jupyter:")
    print("   jupyter notebook practica-9.ipynb")


if __name__ == "__main__":
    main()
