
from gestionadministrador import cargar_eventos, cargar_artistas,crear_evento, listar_eventos, editar_evento,eliminar_evento, asignar_artista_a_evento, guardar_eventos, guardar_artistas
from gestionartista import menu_artistas
from utils import clear_screen, pause_screen



def menu_administrador():
    eventos = cargar_eventos()
    artistas = cargar_artistas()
    while True:
        clear_screen()
        print("--- Gestión de Eventos Culturales ---")
        print("1. Crear evento")
        print("2. Listar eventos")
        print("3. Editar evento")
        print("4. Eliminar evento")
        print("5. Asignar artista a evento")
        print("6. Artistas")
        print("7. Salir")
        opcion = input("Elige una opción: ")
        if opcion == '1':
            crear_evento(eventos)
        elif opcion == '2':
            listar_eventos(eventos)
        elif opcion == '3':
            editar_evento(eventos)
        elif opcion == '4':
            eliminar_evento(eventos)
        elif opcion == '5':
            asignar_artista_a_evento(eventos)
        elif opcion == '6':
            menu_artistas(artistas)
        elif opcion == '7':
            guardar_eventos(eventos)
            guardar_artistas(artistas)
            print("Datos guardados. ¡Hasta luego!")
            pause_screen()
            break
        else:
            print("Opción inválida")
            pause_screen()

