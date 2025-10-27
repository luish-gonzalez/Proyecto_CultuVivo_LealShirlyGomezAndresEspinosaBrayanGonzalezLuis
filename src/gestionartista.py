import json
from utils import clear_screen, pause_screen

# --- GESTIÓN DE ARTISTAS ---

def cargar_artistas():
    try:
        with open('artistas.json', 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        return []

def guardar_artistas(artistas):
    with open('data/artistas.json', 'w') as file:
        json.dump(artistas, file, indent=4)

def registrar_artista(artistas):
    clear_screen()
    print("--- Registrar nuevo artista ---")
    nombre = input("Nombre del artista: ")
    if not nombre:
        print("Nombre no puede estar vacío")
        return
    tipo = input("Tipo de presentación: ")
    if not tipo:
        print("Tipo de presentación no puede ser vacío")
        return
    duracion = input("Duración: ")
    if not duracion:
        print("Duración no puede ser vacío")
        return
    contacto = input("Contacto: ")
    if not contacto:
        print("Contacto no puede ser vac")
        return
    artista = {
        "nombre": nombre,
        "tipo_presentacion": tipo,
        "duracion": duracion,
        "contacto": contacto
    }
    artistas.append(artista)
    print("Artista registrado correctamente.")
    pause_screen()

def listar_artistas(artistas):
    clear_screen()
    print("--- Lista de Artistas ---")
    if not artistas:
        print("No hay artistas registrados.")
    for idx, artista in enumerate(artistas):
        print(f"{idx+1}. {artista['nombre']} - {artista['tipo_presentacion']} ({artista['duracion']}) | Contacto: {artista['contacto']}")
    pause_screen()

def editar_artista(artistas):
    clear_screen()
    print("--- Editar artista ---")
    if not artistas:
        print("No hay artistas para editar.")
        pause_screen()
        return
    listar_artistas(artistas)
    idx = int(input("¿Qué artista quieres editar? (número): ")) - 1
    if 0 <= idx < len(artistas):
        artistas[idx]["nombre"] = input("Nuevo nombre: ")
        artistas[idx]["tipo_presentacion"] = input("Nuevo tipo de presentación: ")
        artistas[idx]["duracion"] = input("Nueva duración: ")
        artistas[idx]["contacto"] = input("Nuevo contacto: ")
        print("Artista editado correctamente.")
    else:
        print("Índice no válido.")
    pause_screen()

def eliminar_artista(artistas):
    clear_screen()
    print("--- Eliminar artista ---")
    if not artistas:
        print("No hay artistas para eliminar.")
        pause_screen()
        return
    listar_artistas(artistas)
    idx = int(input("¿Qué artista quieres eliminar? (número): ")) - 1
    if 0 <= idx < len(artistas):
        artistas.pop(idx)
        print("Artista eliminado correctamente.")
    else:
        print("Índice no válido.")
        pause_screen()

def menu_artistas(artistas):
    while True:
        clear_screen()
        print("--- Submenú Artistas ---")
        print("1. Registrar artista")
        print("2. Listar artistas")
        print("3. Editar artista")
        print("4. Eliminar artista")
        print("5. Volver al menú principal")
        opcion = input("Elige una opción: ")
        if opcion == '1':
            registrar_artista(artistas)
        elif opcion == '2':
            listar_artistas(artistas)
        elif opcion == '3':
            editar_artista(artistas)
        elif opcion == '4':
            eliminar_artista(artistas)
        elif opcion == '5':
            break
        else:
            print("Opción inválida")
            pause_screen()
