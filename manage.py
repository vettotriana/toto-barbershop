#!/usr/bin/env python
"""Utilidad de línea de comandos de Django para tareas administrativas."""

import os
import sys

def main():
    # Establece el módulo de configuración predeterminado para el proyecto Django.
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'ebarber.settings')
    
    try:
        # Intenta importar la función para ejecutar comandos de Django desde la línea de comandos.
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        # Levanta un error si Django no se puede importar, lo cual puede ocurrir si Django
        # no está instalado o si el entorno virtual no está activado.
        raise ImportError(
            "No se pudo importar Django. ¿Estás seguro de que está instalado"
            " y disponible en tu variable de entorno PYTHONPATH?"
            "¿Olvidaste activar un entorno virtual?"
        ) from exc
    # Ejecuta el comando proporcionado en la línea de comandos.
    execute_from_command_line(sys.argv)

if __name__ == '__main__':
    # Punto de entrada del script. Ejecuta la función principal si este script
    # se ejecuta como un programa principal.
    main()
