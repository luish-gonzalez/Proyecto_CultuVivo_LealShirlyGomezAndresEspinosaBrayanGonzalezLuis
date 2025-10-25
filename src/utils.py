import os

def pause_screen():
    input("presione enter para continuar:")

def clear_screen():
    os.system('cls' if os.name=='nt' else 'clear')

    