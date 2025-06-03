
from os import system
system("cls")

lista_prod=["agua", "bebida"]
while True:
    print("")
    print("1.- Agregar producto")
    print("2.- Eliminar un producto")
    print("3.- Listar los productos")
    print("4.- Salir del sistema")
    op= int(input("-> "))
    match op:
        case 1:
            producto= input(" Ingrese el producto que desea agregar: ")
            lista_prod.append(producto)
            print(f"El producto {producto} agregado existosamente")
            system("cls")
        case 2:
            cont = 1
            for i in lista_prod:
                print(f"{cont}.-{i}")
                cont+=1
            aux =int(input("eliminar -> "))-1
            print(f"Producto {lista_prod[aux]} eliminado exitosamente")
            lista_prod.pop(aux)
            input("Presiones enter para continuar")
            system("cls")
        case 3:
            cont = 1
            for i in lista_prod:
                print(f"{cont}.-{i}")
                cont+=1
            print("Presiones enter para continuar")
            system("cls")
        case 4:
            print("Saliendo del sistema")
            break
        case _:
            print("Selección inválida, chúpalo")
