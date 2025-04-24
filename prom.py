
# c=int(input("Ingrese su cantadad de notas "))
# naz=0
# notas=0
# for i in range(c):
#     nota=float(input("Ingrese su nota: "))
#     if nota>=4:
#         naz+=1
#     notas=notas+nota

# promedio=float(notas/c)

# print("Su promedio es: ", round(promedio))
# print(f"Obtuvo {naz} notas azules")

# if round(promedio)>=4:
#     print("Ha aprovado")
# else:
#     print("Ha reprobado")


# nombre=input("Ingrese su nombre ")
# edad=input("Ingrese su edad ")

# print(f"Bienvenido {nombre}, su edad es {edad}")

# nombre=input("Ingrese su nombre: ")

# for i in nombre:
# #     print(i)

# frase=str(input("Ingrese una frase: "))
# frasese=frase.replace(" ","")
# caract=0

# for i in frasese:
#      caract+=+1
#     # caract=caract+1


# print(f"La frase contiene {caract} caracteres")

# CantP=int(input("¿Cuántos productos llevará? "))
# carrito=0

# for i in range(CantP):
#     print("¿Qué produto llevará? ")
#     print("1.- Coca-Cola 3lt. $2.700")
#     print("2.- Galletas $700")
#     print("3.- Helado $2000")
#     print("4.- Truto de pollo 1kg. $3200")
#     prod=int(input("Ingrese el producto: "))
#     if prod==1:
#         print("Ha selecionado Coca-Cola 3lt. con un costo de $2700")
#         carrito+=2700
#     elif prod==2:
#         print("Ha selecionado Galletas con un costo de $700")
#         carrito+=700
#     elif prod==3:
#         print("Ha selecionado Helado con un costo de $2000")
#         carrito+=2000
#     elif prod==4:
#         print("Ha selecionado Truto de pollo 1kg. con un costo de $3200")
#         carrito+=3200
#     else:
#         print("Ha seleccionado una opción invalida")

# print(f"El total de su compra es de ${carrito}")
# print(f"El total de su compra + IVA es de ${carrito*1.19}")

frase=input("Ingrese su frase: ")

# for i in frase:
#     print(i)

# caract=0
# for i in frase:
#     caract+=1

# print(f"La frase contiente {caract} carácteres")
vocal=0
# for i in "aeiou":
#     if i in frase:
#         print(i)
#         vocal+=1
# print(f"La frase contiene {vocal} vocales")
cons=0
e=0
for i in frase:
    if i.lower() in "aeiouáéíóú":
        vocal+=1
    elif i==" ":
        e+=1
    else:
        cons+=1

print(f"La frase contiene {vocal} vocales")
print(f"La frase contiene {cons} consonantes")