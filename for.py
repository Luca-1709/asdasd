# Conoceremos la estructura y eso de for

# a=int(input("Ingrese un número: "))
# print("Esta es la tabla del", a)
# for i in range(11):
#     print(a, "x", i, "=", a*i)

# nombre=input("Ingrese su nombre")

# for i in range(3):
#     print("Hola", nombre)

# c=int(input("Ingrese su cantadad de notas "))

# notas=0
# for i in range(c):
#     nota=float(input("Ingrese su nota: "))
#     notas=notas+nota
# promedio=float(notas/c)
# print("Su promedio es: ", round(promedio))

# c=int(input("Ingrese su cantadad de números "))

# suma=0
# for i in range(c):
# #     num=int(input("Ingrese un número: "))
# #     suma=suma+num
# # print("La suma de todos los números es ", suma)

# c1="Jessie"
# c2="Jammes"
# vc1=0
# vc2=0

# cvot=int(input("¿Cuántas personas votarán? "))

# for i in range (cvot):
#     print("¿Por quíen votará?: 1.- ", c1, " o 2.-", c2)
#     print(f"¿Por quíen votará?: 1.- {c1}, 2.- {c2}")
#     voto=int(input())
#     if voto==1:
#         print("Ha votado por ", c1)
#         vc1=+1
#     elif voto==2:
#         print("Ha votado por ", c2)
#         vc2=+1
#     else:
#         print("Voto invalido")

# if vc1>vc2:
#     print("El ganador es ", c1)
# elif vc2>vc1:
#     print("El ganador es ", c2)
# else:
#     print("Empate")

palabra=str(input("Ingrese una palabra: "))

for i in "aeiou":
    if i in palabra:
        print(i)

# palabra=str(input("Ingrese una palabra: "))
# vocales="aeiou"
# palabrav=palabra.find(vocales)
# for i in palabrav:
#     print(i)

