import registro_asistentes 

def menu_asistente():
        print("1. Registrarse \n2.Ingresar \n3.Regresar al menu principal")
        opcion=input("Seleccione una opcion: ")
        return opcion


def ejecutar_menu_asistente():
    while True:
        opcion = menu_asistente()
        match opcion:
            case "1":
                registro_asistentes.registro_asistente()
            case "2":
                datos=registro_asistentes.cargar_datos()
                id_asistente=input("Ingrese su ID: ")
                if id_asistente not in datos['asistentes']:
                    print("Numero de ID no encontrado. Para ingresar vaya a registrarse")
                else:
                    registro_asistentes.ver_datos()
            case "3":
                print("Regresando al menu de inicio.")
                break
            case _:
                print("Opcion invalida. Por favor intente con una nueva opcion")

if __name__ == "__main__":
    menu_asistente()