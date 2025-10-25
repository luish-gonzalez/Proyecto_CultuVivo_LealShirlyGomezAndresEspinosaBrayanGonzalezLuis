import json

rutaArchivos = "data/eventos.json"

def cargar_eventos(ruta_archivo):
    try:
        with open(ruta_archivo, 'r', encoding='utf-8') as archivo:
            eventos = json.load(archivo)
        return eventos
    except FileNotFoundError:
        print(f"Error: El archivo {ruta_archivo} no se encontró.")
        return []
    except json.JSONDecodeError:
        print(f"Error: El archivo {ruta_archivo} no es un JSON válido.")
        return []

def listar_eventos(eventos):
    if not eventos:
        print("No hay eventos para mostrar.")
        return