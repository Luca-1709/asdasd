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

c=int(input("Ingrese su cantadad de números "))

suma=0
for i in range(c):
    num=int(input("Ingrese un número: "))
    suma=suma+num
print("La suma de todos los números es ", suma)