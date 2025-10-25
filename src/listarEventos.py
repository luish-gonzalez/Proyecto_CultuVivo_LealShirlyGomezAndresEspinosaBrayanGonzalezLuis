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
    
    for evento in eventos:
        nombre = evento.get('nombre', 'Desconocido')
        fecha = evento.get('fecha', 'Desconocida')
        ubicacion = evento.get('lugar', 'Desconocida')
        hora = evento.get('hora', 'Desconocida')
        artistas = evento.get('artistas', [])
        capacidad = evento.get('maxcap', 'Desconocida')
        print(f"Evento: {nombre}\nFecha: {fecha}\nUbicación: {ubicacion}\nHora: {hora}\nArtistas: {', '.join(artistas)}\nCapacidad Máxima: {capacidad}\n{'-'*40}")

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
            print(f"Evento: {nombre}\nFecha: {fecha}\nUbicación: {ubicacion}\n{'-'40}")