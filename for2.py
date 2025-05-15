
# carrito=0
# cantprod=0

# while True:
#     op=int(input('''Seleccione una opción
#                  1.- Dar Usuario
#                  2.- Comprar
#                  3.- Mostrar boleta
#                  4.- Salir
#                  '''))
#     match op:
#         case 1:
#             Usuario=str(input("Ingrese su nombre: "))
#         case 2:
#             while True:
#                 prod=int(input('''¿Qué producto desea llevar?:
#                             1.- Arroz 1kg. $2200
#                             2.- Coca Cola 3lts. $2500
#                             3.- 1kg de posta rosada $7500
#                             4.- Agua mineral con gas 1.5lts $700
#                             5.- Trutro de pollo 1kg $3000
#                             6.- Salir
#                                 '''))
#                 match prod:
#                     case 1:
#                         print("Has seleccionado arroz 1kg.")
#                         carrito+=2200
#                         cantprod+=1
#                     case 2:
#                         print("Has seleccionado Coca Cola 3lts.")
#                         carrito+=2500
#                         cantprod+=1
#                     case 3:
#                         print("Has seleccionado posta rosada 1kg.")
#                         carrito+=7500
#                         cantprod+=1
#                     case 4:
#                         print("Has seleccionado agua mineral 1.5lts.")
#                         carrito+=700
#                         cantprod+=1
#                     case 5:
#                         print("Has seleccionado trutro de pollo 1kg.")
#                         carrito+=3000
#                         cantprod+=1
#                     case 6:
#                         if cantprod<3:
#                             print("Debes llevar al menos 3 productos")
#                         else:
#                             print("Saliendo")
#                             break
#                     case _:
#                         print("Has seleccionado una opción inválida")
#         case 3:
#             print(f"Hola {Usuario}, esta es tu boleta")
#             print(f"El total de artuculos es {cantprod}")
#             print(f"El total de su boleta es de ${carrito}")
#             print(f"El total de su boleta más IVA es de ${carrito*1.19}")
#             print(f"Adiós {Usuario}, que estés bien, vuelve pronto")
#         case 4:
#             print("Has apagado el programa")
#             break
#         case _:
#             print("Has seleccionado una opción inválida")
    









# Usuario=str(input("Ingrese su nombre: "))
# carrito=0
# cantprod=0

# while True:
#     prod=int(input('''¿Qué producto desea llevar?:
#                 1.- Arroz 1kg. $2200
#                 2.- Coca Cola 3lts. $2500
#                 3.- 1kg de posta rosada $7500
#                 4.- Agua mineral con gas 1.5lts $700
#                 5.- Trutro de pollo 1kg $3000
#                 6.- Salir
#                     '''))
#     match prod:
#         case 1:
#             print("Has seleccionado arroz 1kg.")
#             carrito+=2200
#             cantprod+=1
#         case 2:
#             print("Has seleccionado Coca Cola 3lts.")
#             carrito+=2500
#             cantprod+=1
#         case 3:
#             print("Has seleccionado posta rosada 1kg.")
#             carrito+=7500
#             cantprod+=1
#         case 4:
#             print("Has seleccionado agua mineral 1.5lts.")
#             carrito+=700
#             cantprod+=1
#         case 5:
#             print("Has seleccionado trutro de pollo 1kg.")
#             carrito+=3000
#             cantprod+=1
#         case 6:
#             if cantprod<3:
#                 print("Debes llevar al menos 3 productos")
#             else:
#                 print("Saliendo")
#                 break
#         case _:
#             print("Has seleccionado una opción inválida")

# print(f"Hola {Usuario}, esta es tu boleta")
# print(f"El total de artuculos es {cantprod}")
# print(f"El total de su boleta es de ${carrito}")
# print(f"El total de su boleta más IVA es de ${carrito*1.19}")
# print(f"Adiós {Usuario}, que estés bien, vuelve pronto")



# cant_alumn=int(input("Ingrese la cantidad de alumnos: "))
# alumn=0
# prom_general=0
# cont_prom_gen=0

# for i in range (cant_alumn):
#     alumn+=1
#     cant_not=int(input(f"Ingrese su cantidad de notas del alumno {alumn} : "))
#     cont_not=0
#     notas=0
#     for i in range (cant_not):
#         cont_not+=1
#         nota=float(input(f"Ingrese la nota n° {cont_not} del alumno {alumn}: "))
#         notas+=nota
#     Prom=notas/cant_not
#     print(f"El promedio del alumno {alumn} es {Prom}")
#     if Prom>=4:
#         print(f"El alumno {alumn} ha aprobado")
#     else:
#         print(f"El alumno {alumn} ha reprobado")
#     cont_prom_gen+=Prom

# prom_general=cont_prom_gen/cant_alumn
# print(f"El promedio general del curso es {prom_general}")



cant_alumn=int(input("Ingrese la cantidad de alumnos: "))

prom_general=0
cont_prom_gen=0

for j in range (cant_alumn):
    cant_not=int(input(f"Ingrese su cantidad de notas del alumno {j+1} : "))
    notas=0
    for i in range (cant_not):
        nota=float(input(f"Ingrese la nota n° {i+1}: "))
        notas+=nota
    Prom=notas/cant_not
    print(f"El promedio del alumno {j+1} es {Prom}")
    if Prom>=4:
        print(f"El alumno {j+1} ha aprobado")
    else:
        print(f"El alumno {j+1} ha reprobado")
    cont_prom_gen+=Prom

prom_general=cont_prom_gen/cant_alumn
print(f"El promedio general del curso es {prom_general}")

