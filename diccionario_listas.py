# Vero=[ 
#             [3,4]
#             [8,9,64,8]
#                 ]
# print(Vero[1][1])


# dic={
#     "Nombre": "Alan Grant",
#     "Número": 986372881,
#     "Casado": True
# }
# print(dic)
# dic["Nombre"]="Alan Grant Brito"
# print(dic)
# dic["Ciudad"]="Vélez"
# print(dic)

# frutas={
#     "Naranja": 400,
#     "Manzana": 500,
#     "Pera": 700
# }
# print(frutas)
# frutas["Granada"]= 1000

# print(frutas)

# for key, value in frutas.items():
#     print(key, value)

# # productos=[
#     {"nombre":"portamina", "precio": 400}, 
#     {"nombre":"goma", "precio": 200},
#     {"nombre":"estuche", "precio": 1600}
# ]
# print(productos[2]["precio"])

# artículos=[
#     {"Nombre": "Pala" , "Precio": 20000}
# ]
# aseo=[
#     {"Nombre": "cloro", "Precio":1500}
# ]
# def Ennumerar_diccionario(lista):
#     for num, articulo in enumerate(lista):
#         print(num+1,".- ", articulo["Nombre"], articulo["Precio"])

# def agregar_articulo(lista):
#     art=input("Ingrese el artículo que desea agregar: ")
#     precio=int(input("¿Cuál es el valor del producto?: "))
#     lista.append({"Nombre": art, "Precio": precio})

# def eliminar_articulo(lista):
#     Ennumerar_diccionario(lista)
#     borrar=input("Ingrese el artículo que desea eliminar: ")
#     lista.pop(borrar-1)

# def actualizar_art(lista):
#     Ennumerar_diccionario(lista)
#     act=int(input("¿Qué producto desea actualizar? "))
#     art=input("Ingrese el artículo que desea actualizar: ")
#     precio=int(input("¿Cuál es el nuevo valor del producto?: "))
#     artículos[act-1]["Nombre"]=art
#     artículos[act-1]["Precio"]=precio

# from os import system
# import time

# def menu_Compra():
#     while True:
#         print('''¿Qué desea hacer?:
#             1.- Agregar artículo
#             2.- Borrar artículo
#             3.- Actualizar artículo
#             4.- Mostrar listado de artículos
#             5.- Salir''')
#         op=int(input())
#         match op:
#             case 1:
#                 agregar_articulo(artículos)
#                 print("Agregando artículo ... ")
#                 time.sleep(2)
#                 input("Presione enter")
#                 system("cls")
#             case 2:
#                 eliminar_articulo(artículos)
#                 print("Eliminando producto ...")
#                 time.sleep(2)
#                 input("Presione enter")
#                 system("cls")
#             case 3:
#                 actualizar_art(artículos)
#                 print("Actualizando productos ...")
#                 time.sleep(2)
#                 input("Presione enter")
#                 system("cls")
#             case 4:
#                 time.sleep(2)
#                 Ennumerar_diccionario(artículos)
#                 input("Presione enter para continuar")
#                 system("cls")
#             case 5:
#                 print("Saliendo ...")
#                 time.sleep(2)
#                 break
#             case _:
#                 print("Selección inválida")

# menu_Compra()

personas={
    1:{"Nombre": "Liam Nesson",
       "Teléfono": 87528424,
       "EstadoCivil": "Soltero",
       "Ciudadano": True},
    
    2:{"Nombre": "Christian Bale",
       "Teléfono": 234531258,
       "EstadoCivil": "Soltero",
       "Ciudadano": False}
}
print(personas[2]["Nombre"])