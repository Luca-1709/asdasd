# Listas, Diccionarios y Reflexiones.

# Listas
# Uso y explicación

# # #     -6 -5 -4 -3  -2 -1
# lista=[5, 7, 2, 9, 10, 2]
# #      0  1  2  3  4   5     índices de los objetos dentro de la lista

# # print(lista[-4])    #acceso al valor por índice negativo
# # print(lista[0])    #acceso al valor por índice positivo
# # # Llamará al obejto según su ID de la lista

# # # Mostar toda la lista
# print(lista)

# for num in lista:           #Para mostrar cada uno de los valores individualmente
#     print(num)

# Hacer una lista con 5 notas
# luego sacar promedio
# las notas deben ser valores int
# # ej; 55, 67 ,34

# notas=[55,66,70,20,32]
# sum_not=0
# cont_not=0

# for num in notas:
#     print(num)
#     if num<=40:
#         print("Esta nota es un rojo")
#     else:
#         print("Esta nota es un azul")
#     sum_not+=num
#     cont_not+=10

# promedio=sum_not/cont_not
# print(f"El promedio es de {promedio}")

nombres=["Robin","Noelia","Coni"]
apellidos=["Hood","Maldonado","Chan"]

print(len(nombres))

for i in range(len(nombres)):
    print(f"Su nombre es {nombres[i]} {apellidos[i]}")

frutas=["Sandia","Melón","Chirimoya"]

for fruta in frutas:
    print(f"La {fruta} tiene {len(fruta)} carácteres")

# autos=["Audi","BMW","Toyota","KIA","Mercedes"]

# for auto in autos:
#     print(auto)
#     if "a" in auto.lower:
#         print(f"{auto} contiene al menos una a")
#     else:
#         print("Ni una a encontrada")
