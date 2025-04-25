import json
import os

ARCHIVOS = {
    "usuarios": "data/usuarios.json"
}

def cargar_datos():
    datos = {}
    for key, path in ARCHIVOS.items():
        if os.path.exists(path):
            with open(path, "r") as f:
                datos[key] = json.load(f)
        else:
            datos[key] = {}
    return datos

def guardar_datos(datos):
    for key, path in ARCHIVOS.items():
        with open(path, "w") as f:
            json.dump(datos.get(key, {}), f)
