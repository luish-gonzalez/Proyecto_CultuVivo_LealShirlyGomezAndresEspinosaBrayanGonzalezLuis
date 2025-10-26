from utils import pause_screen, clear_screen
import json

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
        print("Hora no puede ser vacía")
        return
    capacidad = int(input("Capacidad máxima: "))
    if not capacidad:
        print("Capacidad no puede ser vacía")
        return
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
    for idx, evento in enumerate(eventos):
        print(f"{idx+1}. {evento['nombre']} ({evento['fecha']} - {evento['hora']})")
    pause_screen()

def editar_evento(eventos):
    clear_screen()
    print("--- Editar evento ---")
    if not eventos:
        print("No hay eventos para editar.")
        pause_screen()
        return
    listar_eventos(eventos)
    idx = int(input("¿Qué evento quieres editar? (número): ")) - 1
    if 0 <= idx < len(eventos):
        eventos[idx]["nombre"] = input("Nuevo nombre: ")
        if not ["nombre"]:
            print("Nombre no puede estar vacio")
            return
        eventos[idx]["fecha"] = input("Nueva fecha (YYYY-MM-DD): ")
        eventos[idx]["hora"] = input("Nueva hora (HH:MM): ")
        eventos[idx]["lugar"] = input("Nuevo lugar: ")
        eventos[idx]["capacidad_maxima"] = int(input("Nueva capacidad: "))
        eventos[idx]["descripcion"] = input("Nueva descripción: ")
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