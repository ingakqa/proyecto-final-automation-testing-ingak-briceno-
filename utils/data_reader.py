import json
import os

def cargar_datos_json(nombre_archivo):
    """Lee y parsea un archivo desde la carpeta test_data."""
    ruta = os.path.join("test_data", nombre_archivo)
    with open(ruta, "r", encoding="utf-8") as f:
        return json.load(f)

