comuna=0
cont=0
arancel=200000

while comuna!=1 and comuna!=2 and comuna!=3 and comuna!=4 and comuna!=5:
    comuna=int(input("indique de que comuna es" \
    "                 1.- la florida " \
    "                 2.- la pinatana" \
    "                 3.- la granja" \
    "                 4.- san joaquin"
    "                 5.- otra comuna" \
    "                 "))

    if comuna==1:
        print("su descuento es del 20%")
        cont+=0.20
    
    elif comuna==2:
        print("su descuento es del 30%")
        cont+=0.30
    
    elif comuna==3:
        print("su descuentos es del 25%")
        cont+=0.25
    
    elif comuna==4:
        print("su descuento es del 15%")
        cont+=0.15
    elif comuna==5:
        print("no tiene descuento")

    
gp=0

while gp!=1 and gp!=2 and gp!=3:
    gp=int(input("indique con cuantas personas vive"
 "              1.- 1 persona"
 "              2.- 2 a 4 personas"
 "              3.- 5 o mas personas"))

    if gp==1:
        print("su descuento es del 2%")
        cont+=0.02

    elif gp==2:
        print("su descuento es del 3%")
        cont+=0.03

    elif gp==3:
        print("su descuento es del 4%")
        cont+=0.04

    elif gp==4:
        print("usted no tiene descuento")


print(f"su descuento es de {cont*100}%")

cont=1-cont
arancel*=cont
 
print(f"El total de su arancel es $ {arancel}")