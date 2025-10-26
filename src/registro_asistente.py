import json
Ruta_json="general.json"

def cargar_datos():
    try: 
        with open(Ruta_json, "r", encoding="utf-8") as f:
            return json.load(f)
    except FileNotFoundError:
        return {"asistentes":{}, "artistas":{}, "eventos":{}}

def guardar_datos(datos):
    with open(Ruta_json, "w", encoding="utf-8") as f:
        json.dump(datos, f, indent=4, ensure_ascii=False)



def registro_asistente():
    datos=cargar_datos()
    print("Registro persona")
    try: 
        id_asistente=int(input("Ingrese su numero de identificacion: "))
    except ValueError:
        print("Se esperaba una serie de numeros de ID")
        return
    
    if str(id_asistente) in datos['asistentes']:
        print("Este numero de ID ya existe")
        return
    nombre=input("Ingrese su nombre completo: ")
    email=input("Ingrese su direccion de correo electronico: ")
    tipo_boleto=input("Seleccione el tipo de boleto (1.VIP, 2.Platino, 3.General): ").lower()
    estado=input("Estado (Confirmado/En espera): ").lower()

    datos["asistentes"][str(id_asistente)]={
        "id_asistente":id_asistente,
        "nombre_completo":nombre,
        "email":email,
        "boleto": tipo_boleto,
        "estado":estado
    }

    guardar_datos(datos)
    print("Se completo el registro. Guardado Correctamente")

