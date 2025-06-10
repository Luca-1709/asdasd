nombres=[]
apellidos=[]
from os import system
import time

while True:
    print('''
          1.- Insertar nombre y apellido
          2.- Buscar nombre
          3.- Mostrar nombres
          4.- Salir
          ''')
    op=int(input("Seleccione una opción: "))
    match op:
        case 1:
            nom=input("Ingrese un nombre: ")
            nombres.append(nom)
            ape=input("Ingrese un apellido: ")
            apellidos.append(ape)
            print(nombres)
            print(apellidos)
            time.sleep(3)
            system("cls")
        case 2:
            buscar=input("¿Que nombre buscará dentro de la lista? ")
            if buscar in nombres:
                print(f"El nombre {buscar} si se encuentra en la lista")
            else:
                print(f"No se ha encontrado el nombre {buscar} en la lista")
            time.sleep(3)
            system("cls")
        case 3:
            for i in range(len(nombres)):
                print(f"Los nombres completos son {nombres[i]} {apellidos[i]}")
            time.sleep(3)
            system("cls")
        case 4:
            print("Saliendo ....")
            break
        case _:
            print("Opción inválida")
            time.sleep(2)
            system("cls")