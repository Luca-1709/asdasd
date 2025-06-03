# append(E) -> Agrega un elemento al final de la lista
# pop(int) -> Elimina un elemento de la lista del ID identificado



# lista=[1, "hola", 0.15]
# print(lista[1])

# print(lista)

# lista.append("María")

# print(lista)

# for i in lista:
#     print(i)


from os import system
system("cls")

lista_prod=[]
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





# while True:
#     try:
#         opc = int(input("Ingrese una opción: "))
#         if opc < 1 or opc > 4:
#             print("Error en rango !")
#         break
#     except ValueError:
#         print("ERROR, ingresó otro tipo de dato")

# def validar_numero(minimo,maximo,texto):
#     while True:
#         try:
#             opp=