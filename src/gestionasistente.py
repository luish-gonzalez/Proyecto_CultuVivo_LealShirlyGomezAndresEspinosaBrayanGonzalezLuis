import json 

def menu_asistente():
        print("1. Registrarse \n2.Ingresar \n3.Regresar al menu principal")
        opcion=input("Seleccione una opcion: ")
        return opcion

ruta_archivo = "data/eventos.json"

def ejecutar_menu_asistente():
    while True:
        opcion = menu_asistente()
        match opcion:
            case "1":
                registro_asistente.cargar_eventos()
            case "2":
                datos=registro_asistente.cargar_eventos()
                id_asistente=input("Ingrese su ID: ")
                if id_asistente not in datos['asistentes']:
                    print("Numero de ID no encontrado. Para ingresar vaya a registrarse")
                else:
                    registro_asistente.cargar_eventos()
            case "3":
                print("Regresando al menu de inicio.")
                break
            case _:
                print("Opcion invalida. Por favor intente con una nueva opcion")


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



def regisrarseEnEvento(eventos, nombre_evento):
    for evento in eventos:
        if evento.get('nombre') == nombre_evento:
            print(f"Te has registrado exitosamente en el evento: {nombre_evento}")
            return
    print(f"El evento '{nombre_evento}' no se encontró.")

def mostrarEventosRegistrados(eventos, eventos_registrados):
    if not eventos_registrados:
        print("No estás registrado en ningún evento.")
        return
    
    print("Eventos en los que estás registrado:")
    for evento in eventos:
        if evento.get('nombre') in eventos_registrados:
            nombre = evento.get('nombre', 'Desconocido')
            fecha = evento.get('fecha', 'Desconocida')
            ubicacion = evento.get('ubicacion', 'Desconocida')
            print(f"Evento: {nombre}\nFecha: {fecha}\nUbicación: {ubicacion}\n{'-'*40}")

import os
import json

RUTA_ASISTENTES = 'data/asistentes.json'

def cargar_asistentes():
    try:
        with open(RUTA_ASISTENTES, 'r', encoding='utf-8') as file:
            return json.load(file)
    except FileNotFoundError:
        return []
    except json.JSONDecodeError:
        print(f"Error: El archivo {RUTA_ASISTENTES} tiene JSON inválido.")
        return []

def guardar_asistentes(asistentes):
    carpeta = os.path.dirname(RUTA_ASISTENTES)
    if not os.path.exists(carpeta):
        os.makedirs(carpeta)
    with open(RUTA_ASISTENTES, 'w', encoding='utf-8') as file:
        json.dump(asistentes, file, indent=4, ensure_ascii=False)

def registro_asistente():
    nombre = input("Ingrese su nombre: ").strip()
    id_asistente = input("Ingrese su ID: ").strip()
    return nombre, id_asistente

def agregar_asistente(nombre, id_asistente):
    asistentes = cargar_asistentes()
    asistentes.append({
        "nombre": nombre,
        "id_asistente": id_asistente
    })
    guardar_asistentes(asistentes)
    print(f"Asistente {nombre} registrado correctamente.")
