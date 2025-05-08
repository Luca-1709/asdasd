op=0
arancel=200000
descuento=0

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