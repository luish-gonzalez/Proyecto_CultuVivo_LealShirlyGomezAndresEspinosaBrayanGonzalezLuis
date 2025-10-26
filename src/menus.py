
from gestionadministrador import cargar_eventos,crear_evento, listar_eventos, editar_evento,eliminar_evento, asignar_artista_a_evento, guardar_eventos
from gestionartista import menu_artistas, cargar_artistas, guardar_artistas
from gestionasistente import cargar_eventos, registro_asistente, mostrarEventosRegistrados
from utils import clear_screen, pause_screen

ruta_archivo = "data/eventos.json"




def main():
    while True:
        print("===== CULTUVIVO=====")
        print("1. Iniciar como Administrador")
        print("2. Iniciar como Asistente")
        print("0. Salir")
        opcion = input("Opción: ")

        match opcion:
            case "1":
                menu_administrador()
            case "2": 
                menu_asistente()
            case "0":
                print("Saliendo del programa")
                break
            case _:
                print("Opcion invalida, ingresa una nueva opcion.")






def menu_administrador():
    eventos = cargar_eventos(ruta_archivo)
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

def menu_asistente():
    print("--- Menú de Asistente ---")
    print("1. Registrarse como asistente")
    print("2. Listar eventos disponibles")
    print("3. Ver eventos registrados")
    print("4. Regresar al menú principal")
    opcion = input("Seleccione una opción: ")
    if opcion == '1':
        nombre, id_asistente = registro_asistente()
        print(f"Registro exitoso. Nombre: {nombre}, ID: {id_asistente}")
        pause_screen()
    elif opcion == '2':
        eventos = cargar_eventos(ruta_archivo)
        listar_eventos(eventos)
        pause_screen()
    elif opcion == '3':
        eventos = cargar_eventos(ruta_archivo)
        eventos_registrados = []  
        mostrarEventosRegistrados(eventos, eventos_registrados)
        pause_screen()
    elif opcion == '4':
        print("Regresando al menú principal.")
        pause_screen()
    else:
        print("Opción inválida. Por favor intente de nuevo.")
        pause_screen()