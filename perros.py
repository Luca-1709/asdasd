carrito=0
items=0
Nombre=str(input("Ingrese su nombre: "))
Apellido=str(input("Ingrese su apellido: "))

print(f"Bienvenido a Supermercados Lidl, {Nombre}")
while True:
    while True:
        try:
            op=int(input('''¿Qué desea hacer?
                         1.- Comprar
                         2.- Dar datos de comprador
                         3.- Consultar carrito
                         4.- Pagar y salir
                         '''))
            break
        except Exception:
            print("Solo debe ingresar números enteros.")
    match op:
        case 1:
            print("Menú de compras")
            while True:
                while True:
                    try:
                        op_comprar=int(input('''¿Qué desea llevar?
                                            1.- Coca Cola Zero 3lts. $2.500
                                            2.- Arroz Tucapel 1kg $2.400
                                            3.- Pan 1kg $1.900
                                            4.- Pollo trutro 1kg $3.500
                                            5.- Azucar 1kg $1.500
                                            6.- Volver al menú principal
                                             '''))
                        break
                    except Exception:
                        print("Solo debe ingresar números enteros.")
                match op_comprar:
                    case 1:
                        print("Ha seleccionado Coca Cola zero")
                        carrito+=2500
                        items+=1
                    case 2:
                        print("Ha seleccionado Arroz Tucapel")
                        carrito+=2400
                        items+=1
                    case 3:
                        print("Ha seleccionado Pan")
                        carrito+=1900
                        items+=1
                    case 4:
                        print("Ha seleccionado Pollo trutro")
                        carrito+=3500
                        items+=1
                    case 5:
                        print("Ha seleccionado Azucar")
                        carrito+=1500
                        items+=1
                    case 6:
                        print("Volviendo al menú principal")
                        break
        case 2:
            while True:
                try:
                    Nombre=str(input("Ingrese su nombre: "))
                    Apellido=str(input("Ingrese su apellido: "))
                    rut=int(input("Ingrese su rut, sin puntos ni guiones: "))
                    break
                except Exception:
                    print("Rut inválido, inténtelo de nuevo")
        case 3:
            print("Viendo carrito")
            print(f"En total lleva {items} items, con un total de ${carrito}")
            print(f"El total más iva es de ${carrito*1.19}")
        case 4:
            print(f"El total a pagar es de ${carrito}, por un total de {items} items")
            print(f"El total más iva es de ${carrito*1.19}")
            print(f"Adiós {Nombre} {Apellido}")
            print("Saliendo del sistema")
            break
        case _:
            print("Selección inválida, inténtelo nuevamente")