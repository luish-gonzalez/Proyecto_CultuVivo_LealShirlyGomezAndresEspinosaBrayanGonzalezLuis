from menu_asistente import ejecutar_menu_asistente
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
                ejecutar_menu_asistente()
            case "0":
                print("Saliendo del programa")
                break
            case _:
                print("Opcion invalida, ingresa una nueva opcion.")

if __name__ == "__main__":
    main()