from os import system
productos=[]
precios=[]
carrito=[]
valor_carrito=0

while True:
    print(''' 
          1.- Ingresar productos
          2.- Comprar
          3.- Crear boleta
          4.- Salir''')
    op=int(input("A qué menú desea ingresar: "))
    match op:
        case 1:
            prod=input("Ingrese el pructo que desea agregar a la lista: ")
            productos.append(prod)
            precio=int(input("Ingrese el precio del producto: "))
            precios.append(precio)
            print(productos)
            print(precios)
            input("Presione enter para continuar")
            system("cls")
        case 2:
            if len(productos)>0:
                for i in range(len(productos)):
                    print(f"El producto {productos[i]} tiene un valor de ${precios[i]}")
                    agre=0
                    while agre<1 or agre>2:
                        agre=int(input('''¿Desea agregar el producto al carrito?
                                    1.- Si
                                    2.- No
                                       '''))
                        match agre:
                            case 1:
                                print(f"Agregando al carrito el producto {productos[i]}")
                                valor_carrito+=precios[i]
                                carrito.append(productos[i])
                                input("Presione enter para continuar")
                                system("cls")
                            case 2:
                                print("No se ha agregado el producto al carrito")
                                input("Presione enter para continuar")
                                system("cls")
                            case _:
                                print("Selección inválida")
                                input("Presione enter para continuar")
                                system("cls")
            else:
                print("Aún no hay productos en la lista")
                input("Presione enter para continuar")
                system("cls")
        case 3:
            total=0
            print("Mostrando boleta....")
            print("-------0-------")
            for i in range(len(carrito)):
                print( productos[i], "-----$", precios[i])
                total+=precios[i]
            print(f"Lleva los siguientes productos {carrito}")
            print(f"El valor neto del carrito es de ${valor_carrito}")
            print(f"El valor + IVA del carrito es de ${valor_carrito*1.19}")
            print("-------0-------")
            input("Presione enter para continuar")
            system("cls")
        case 4:
            print("Saliendo ...")
            break
        case _:
            print("Selección inválida")
            input("Presione enter para continuar")
            system("cls")