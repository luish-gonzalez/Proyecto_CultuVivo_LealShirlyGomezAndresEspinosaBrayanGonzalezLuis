from utils import pause_screen, clear_screen
import json
import os

def cargar_eventos():
    try:
        with open('data/eventos.json', 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        return []

def guardar_eventos(eventos):
    ruta = 'data/eventos.json'
    carpeta = os.path.dirname(ruta)
    if not os.path.exists(carpeta):
        os.makedirs(carpeta)
    with open(ruta, 'w', encoding='utf-8') as file:
        json.dump(eventos, file, indent=4)


def crear_evento(eventos):
    clear_screen()
    print("--- Crear nuevo evento ---")
    nombre = input("Nombre del evento: ").strip()
    if not nombre: 
        print("nombre no puede estar vacio:")
        return
    fecha = input("Fecha (YYYY-MM-DD): ").strip()
    if not fecha: 
        print("Fecha no puede ser vacío")
        return    
    hora = input("Hora (HH:MM): ").strip()
    if not hora:
        print("Hora no puede ser vacía")
        return
    lugar = input("Lugar: ").strip()
    if not lugar:
        print("Lugar no puede ser vacía")
        return
    while True:
        try:
            capacidad = int(input("Capacidad máxima: "))
            if capacidad <= 0:
                print("Capacidad debe ser mayor que 0.")
                continue
            break
        except ValueError:
            print("Debe ingresar un número válido para capacidad.")
    descripcion = input("Descripción: ")
    if not descripcion:
        print("Descripción no puede ser vacia")
        return
    evento = {
        "nombre": nombre,
        "fecha": fecha,
        "hora": hora,
        "lugar": lugar,
        "capacidad_maxima": capacidad,
        "descripcion": descripcion,
        "artistas": []
    }
    eventos.append(evento)
    print("Evento creado correctamente.")
    pause_screen()

def listar_eventos(eventos):
    clear_screen()
    print("--- Lista de Eventos ---")
    if not eventos:
        print("No hay eventos registrados.")
    else:
        for idx, evento in enumerate(eventos, 1):
            nombre = evento.get('nombre', 'Sin nombre')
            fecha = evento.get('fecha', 'Sin fecha')
            hora = evento.get('hora', 'Sin hora')
            print(f"{idx}. {nombre} ({fecha} - {hora})")
    pause_screen()



def editar_evento(eventos):
    clear_screen()
    print("--- Editar evento ---")
    if not eventos:
        print("No hay eventos para editar.")
        pause_screen()
        return
    listar_eventos(eventos)
    try:
        idx = int(input("¿Qué evento quieres editar? (número): ")) - 1
    except ValueError:
        print("Entrada inválida. Debe ingresar un número.")
        pause_screen()
        return
    if 0 <= idx < len(eventos):
        evento = eventos[idx]

        # Editar cada campo, manteniendo el anterior si el usuario deja vacío
        nuevo_nombre = input(f"Nuevo nombre [{evento['nombre']}]: ").strip()
        if nuevo_nombre:
            evento["nombre"] = nuevo_nombre

        nueva_fecha = input(f"Nueva fecha (YYYY-MM-DD) [{evento['fecha']}]: ").strip()
        if nueva_fecha:
            evento["fecha"] = nueva_fecha

        nueva_hora = input(f"Nueva hora (HH:MM) [{evento['hora']}]: ").strip()
        if nueva_hora:
            evento["hora"] = nueva_hora

        nuevo_lugar = input(f"Nuevo lugar [{evento['lugar']}]: ").strip()
        if nuevo_lugar:
            evento["lugar"] = nuevo_lugar

        while True:
            capacidad_str = input(f"Nueva capacidad [{evento['capacidad_maxima']}]: ").strip()
            if capacidad_str == "":
                break  # Mantiene la anterior
            try:
                capacidad = int(capacidad_str)
                if capacidad <= 0:
                    print("La capacidad debe ser un número positivo.")
                    continue
                evento["capacidad_maxima"] = capacidad
                break
            except ValueError:
                print("Por favor, ingrese un número válido.")

        nueva_descripcion = input(f"Nueva descripción [{evento['descripcion']}]: ").strip()
        if nueva_descripcion:
            evento["descripcion"] = nueva_descripcion

        print("Evento editado correctamente.")
    else:
        print("Índice no válido.")
    pause_screen()

def eliminar_evento(eventos):
    clear_screen()
    print("--- Eliminar evento ---")
    if not eventos:
        print("No hay eventos para eliminar.")
        pause_screen()
        return
    listar_eventos(eventos)
    idx = int(input("¿Qué evento quieres eliminar? (número): ")) - 1
    if 0 <= idx < len(eventos):
        eventos.pop(idx)
        print("Evento eliminado correctamente.")
    else:
        print("Índice no válido.")
    pause_screen()



# --asignar artista a evento--

def asignar_artista_a_evento(eventos):
    clear_screen()
    print("--- Asignar artista a evento ---")
    if not eventos:
        print("No hay eventos disponibles.")
        pause_screen()
        return
    listar_eventos(eventos)
    idx_evento = int(input("¿A qué evento desea asignar un artista? (número): ")) - 1
    if 0 <= idx_evento < len(eventos):
        nombre_artista = input("Nombre del artista: ")
        tipo_presentacion = input("Tipo de presentación (ej: música, danza): ")
        duracion = input("Duración de la presentación (ej: 60 minutos): ")
        artista = {
            "nombre": nombre_artista,
            "tipo_presentacion": tipo_presentacion,
            "duracion": duracion
        }
        eventos[idx_evento]["artistas"].append(artista)
        print("Artista asignado correctamente al evento.")
    else:
        print("Índice no válido.")
    pause_screen()