# Uso y expliación de Match

def suma2(n1,n2):
    print(f"La suma es {n1+n2}")

def suma():
    n1=int(input("Ingrese un número:   "))
    n2=int(input("Ingrese otro número: "))
    print("El resultado de la suma es", n1+n2)

def resta():
    n1=int(input("Ingrese un número: "))
    n2=int(input("Ingrese otro número: "))
    print("El resultado de la resta es", n1-n2)

def multiplicación():
    n1=int(input("Ingrese un número: "))
    n2=int(input("Ingrese otro número: "))
    print("El resultado de la multiplicación es", n1*n2)

def división():
    n1=int(input("Ingrese un número: "))
    n2=int(input("Ingrese otro número: "))
    print("El resultado de la división es", n1/n2)


def calculadora():
    while True:
        op=int(input('''Selecciones una opcion:
                    1.- Suma
                    2.- Resta
                    3.- Multiplicación
                    4.- División
                    5.- Salir
                    '''))

        match op:
            case 1:
                print("Suma")
                suma()
            case 2:
                print("Resta")
                resta()
            case 3:
                print("Multiplicación")
                multiplicación()
            case 4:
                print("División")
                división()
            case 5:
                print("Salir")
                break
            case _:
                print("Opción invalida")

# calculadora()


# # menu recursivo
# debe tener 3 programas creados anteriormente
# el menu debe llamar a estos programas
#  y ejecutarlos d manera correcta
# debe tener la opcion e salir
# y la opcion por defecto



def descuento_arancel():
   op=0
   descuento=0
   arancel=200000
   while op!=1 and op!=2 and op!=3 and op!=4 and op!=5:
    op=int(input("""Indique a que comuna corresponde: 
                     1.- La Florida
                     2.- La Pintana
                     3.- Puente Alto
                     4.- San Joaquín
                     5.- Ninguna de las anteriores
                    """))
    if op==1:
        print("Ha seleccionado a La Florida como su comuna")
        descuento+=0.2
    elif op==2:
        print("Ha seleccionado a La Pintana como su comuna")
        descuento+=0.3
    elif op==3:
        print("Ha seleccionado a Puente Alto como su comuna")
        descuento+=0.25
    elif op==4:
        print("Ha seleccionado a San Joaquín como su comuna")
        descuento+=0.15
    elif op==5:
        print("No pertenece a ninguna de las anteriores comunas")
        descuento+=0
    else:
        print("Seleccion invalida, intentelo de nuevo")

    gf=0
    while gf<=0:
        gf=int(input("Indique cuantas personas viven en su hogar: "))
        if gf==1:
            descuento+=0.02
        elif gf>=2 and gf<=4:
            descuento+=0.03
        elif gf>=5:
            descuento+=0.04
        else:
            print("Seleccion invalida, intentelo de nuevo")

    print(f"El descuento total es de {round(descuento*100)}%")

    descuento=1-descuento
    arancel*=descuento

    print(f"El total a pagar del arancel es de ${arancel}")

def carrito_compras():
    CantP=int(input("¿Cuántos productos llevará? "))
    carrito=0

    for i in range(CantP):
        print("¿Qué produto llevará? ")
        print("1.- Coca-Cola 3lt. $2.700")
        print("2.- Galletas $700")
        print("3.- Helado $2000")
        print("4.- Truto de pollo 1kg. $3200")
        prod=int(input("Ingrese el producto: "))
        if prod==1:
            print("Ha selecionado Coca-Cola 3lt. con un costo de $2700")
            carrito+=2700
        elif prod==2:
            print("Ha selecionado Galletas con un costo de $700")
            carrito+=700
        elif prod==3:
            print("Ha selecionado Helado con un costo de $2000")
            carrito+=2000
        elif prod==4:
            print("Ha selecionado Truto de pollo 1kg. con un costo de $3200")
            carrito+=3200
        else:
            print("Ha seleccionado una opción invalida")

    print(f"El total de su compra es de ${carrito}")
    print(f"El total de su compra + IVA es de ${carrito*1.19}")

def juego_street():
    hpj1=50
    hpj2=50
    import random
    turno=random.randint(1,2)
    import time

    while hpj1>0 and hpj2>0:
        if turno % 2==0:
            ataque=random.randint(3,15)
            ataquecrit=ataque*2
            probac=random.randint(1,5)
            if probac==1:
                time.sleep(1)
                print("Turno del jugador 1")
                time.sleep(1)
                print("Jugador 1 ha atacado")
                print(f"Ataque crítico, {ataquecrit} de daño")
                hpj2-=ataquecrit
                time.sleep(1)
                print(f"La vida del jugaror 2 bajado a bajado a {hpj2}")
                time.sleep(1)
            else:
                time.sleep(1)
                print("Turno del jugador 1")
                time.sleep(1)
                print("Jugador 1 ha atacado")
                print(f"Ataque normal, {ataque} de daño")
                hpj2-=ataque
                time.sleep(1)
                print(f"La vida del jugaror 1 bajado a bajado a {hpj2}")
                time.sleep(1)
        else:
            ataque=random.randint(3,15)
            ataquecrit=ataque*2
            probac=random.randint(1,5)
            if probac==1:
                time.sleep(1)
                print("Turno del jugador 2")
                time.sleep(1)
                print("Jugador 2 ha atacado")
                print(f"Ataque crítico, {ataquecrit} de daño")
                hpj1-=ataquecrit
                time.sleep(1)
                print(f"La vida del jugaror 2 bajado a bajado a {hpj1}")
                time.sleep(1)
            else:
                time.sleep(1)
                print("Turno del jugador 2")
                time.sleep(1)
                print("Jugador 2 ha atacado")
                print(f"Ataque normal, {ataque} de daño")
                hpj1-=ataque
                time.sleep(1)
                print(f"La vida del jugaror 1 bajado a bajado a {hpj1}")
                time.sleep(1)

        turno+=1

    if hpj1>hpj2:
        print("El ganador es el Jugador 1")
    else:
        print("El ganador es el Jugador 2")

def menu():
    while True:
        op=int(input('''Seleccione un programa:
                    1.- Descuento de aranceles
                    2.- Carrito de compras
                    3.- Juego Street
                    4.- Salir
                    '''))

        match op:
            case 1:
                print("Seleccionó el programa de Descuento de aranceles")
                descuento_arancel()
            case 2:
                print("Seleccionó el programa de Carrito de compras")
                carrito_compras()
            case 3:
                print("Seleccionó el programa de Juego Street")
                juego_street()
            case 4:
                print("Salir")
                break
            case _:
                print("Opción invalida")

menu()
