# ##### Perros de caza
# while True:
#     try:
#         c_perros=int(input("Ingrese la cantidad de perros que cazaran: "))
#         while c_perros<1:
#             print("Debe ingresar un número entero positivo")
#             c_perros=int(input("Ingrese la cantidad de perros que cazaran: "))
        
#         cuota=int(input("Ingrese la cantidad de conejos mínima que debe traer cada perro: "))
#         while cuota<1:
#             print("Debe ingresar un número entero positivo")
#             cuota=int(input("Ingrese la cantidad de conejos mínima que debe traer cada perro: "))
#         break
#     except Exception:
#         print("Debe ingresar solo número enteros")



# import random
# si=0
# no=0

# for i in range (c_perros):
#     conejos_cazados=random.randint(0,6)
#     print(f"El perro n° {i+1} trajo {conejos_cazados} conejos")
#     if conejos_cazados>=cuota:
#         print(f"El perro n° {i+1} cumplió con la cuota y le corresponde un filete")
#         si+=1
#     else:
#         print(f"El perro n° {i+1} no cumplió con la cuota y no podrá comer filete")
#         no+=1

# print(f"En total {si} perros lograron la cuota y {no} no lo lograron")


# # rojos=int(input("¿Cuantos rojos hay en el curso? "))
# # decimas=0

# # for i in range (4):
# #     asistencia_Taller=str(input(f"Asistió al taller n° {i+1}: "))
# #     if asistencia_Taller=="si" or asistencia_Taller=="s" or asistencia_Taller=="Si" or asistencia_Taller=="SI":
# #         print("Obtiene 3 decimas")
# #         decimas+=0.3
# #     else:
# #         print("No tiene decimas por este taller")

# # if decimas>=1:
# #     print("Tiene la bendición del profesor")
# # else:
# #     print("No se le puede ayudar")

# # nota_final=float(input("Ingrese su nota final: "))
# # nota_final+=decimas

# # print(f"Su nota final es {nota_final}")

# # if nota_final>=4:
# #     print("Ha aprovado")
# # else:
# #     print("Ha reprobado")



# # while True:
# #     decimas=0
# #     asistencia=int(input('''A cuantos talleres ha asistido?
# #                          1.- Un solo taller
# #                          2.- Dos talleres
# #                          3.- Tres talleres
# #                          4.- Cuatro talleres
# #                          5.- Ningún taller
# #                          6.- Salir
# #                          '''))
# #     match asistencia:
# #         case 1:
# #             print("Le corresponden 3 decimas")
# #             decimas+=0.3
# #             if decimas>=1:
# #                 print("Tiene la bendición del profesor")
# #             else:
# #                 print("No se le puede ayudar")

# #             nota_final=float(input("Ingrese su nota final: "))
# #             nota_final+=decimas

# #             print(f"Su nota final es {nota_final}")

# #             if nota_final>=4:
# #                 print("Ha aprovado")
# #             else:
# #                 print("Ha reprobado")
# #         case 2:
# #             print("Le corresponden 6 decimas")
# #             decimas+=0.6
# #             if decimas>=1:
# #                 print("Tiene la bendición del profesor")
# #             else:
# #                 print("No se le puede ayudar")

# #             nota_final=float(input("Ingrese su nota final: "))
# #             nota_final+=decimas

# #             print(f"Su nota final es {nota_final}")

# #             if nota_final>=4:
# #                 print("Ha aprovado")
# #             else:
# #                 print("Ha reprobado")
# #         case 3:
# #             print("Le corresponden 9 decimas")
# #             decimas+=0.9
# #             if decimas>=1:
# #                 print("Tiene la bendición del profesor")
# #             else:
# #                 print("No se le puede ayudar")

# #             nota_final=float(input("Ingrese su nota final: "))
# #             nota_final+=decimas

# #             print(f"Su nota final es {nota_final}")

# #             if nota_final>=4:
# #                 print("Ha aprovado")
# #             else:
# #                 print("Ha reprobado")
# #         case 4:
# #             print("Le corresponden 12 decimas")
# #             decimas+=1.2
# #             if decimas>=1:
# #                 print("Tiene la bendición del profesor")
# #             else:
# #                 print("No se le puede ayudar")

# #             nota_final=float(input("Ingrese su nota final: "))
# #             nota_final+=decimas

# #             print(f"Su nota final es {nota_final}")

# #             if nota_final>=4:
# #                 print("Ha aprovado")
# #             else:
# #                 print("Ha reprobado")
# #         case 5:
# #             print("Le corresponden 0 decimas")
# #             decimas+=0
# #             if decimas>=1:
# #                 print("Tiene la bendición del profesor")
# #             else:
# #                 print("No se le puede ayudar")

# #             nota_final=float(input("Ingrese su nota final: "))
# #             nota_final+=decimas

# #             print(f"Su nota final es {nota_final}")

# #             if nota_final>=4:
# #                 print("Ha aprovado")
# #             else:
# #                 print("Ha reprobado")
# #         case 6:
# #             print("Saliendo")
# #             break

# # # if decimas>=1:
# # #     print("Tiene la bendición del profesor")
# # # else:
# # #     print("No se le puede ayudar")

# # # nota_final=float(input("Ingrese su nota final: "))
# # # nota_final+=decimas

# # # print(f"Su nota final es {nota_final}")

# # # if nota_final>=4:
# # #     print("Ha aprovado")
# # # else:
# # #     print("Ha reprobado")
total=0
cant_aut=0
cant_lav_full=0
cant_lav_stand=0
cant_lav_bas=0

while True:
    try:
        op=int(input('''A que programa desea acceder: 
                     1.- Cursar pago del lavado
                     2.- Ver ventas diarias
                     3.- Salir
                     '''))
    except Exception:
        print("Debe ingresar solo números enteros")
    match op:
        case 1:
            print("Curso de pagos")
            while True:
                try:
                    op_lav=int(input('''¿Qué tipo de lavado realizó?
                                    1.- Básico $7.000
                                    2.- Standard $10.000
                                    3.- Full $15.000
                                    4.- Salir
                                     '''))
                except Exception:
                    print("Debe ingresar solo números enteros")
                match op_lav:
                    case 1:
                        print("Lavado básico")
                        total+=7000
                        cant_aut+=1
                        cant_lav_bas+=1
                    case 2:
                        print("Lavado Standard")
                        total+=10000
                        cant_aut+=1
                        cant_lav_stand+=1
                    case 3:
                        print("Lavado Full")
                        total+=15000
                        cant_aut+=1
                        cant_lav_full+=1
                    case 4:
                        print("Volviendo al menú principal")
                        break
                    case _:
                        print("Selección inválida, vuelva a intentarlo")
        case 2:
            print("Viendo ventas totales")
            print(f"Durante el día se han lavado {cant_aut} y se ha recaudado ${total}")
        case 3:
            print("Saliendo del programa")
            if cant_lav_full>=1:
                print("El monto mayor recaudado de un lavado es $15.000")
            elif cant_lav_stand>=1:
                print("El monto mayor recaudado de un lavado es $10.000")
            elif cant_lav_bas>=1:
                print("El monto mayor recaudado de un lavado es $7.000")
            else:
                print("No se ha lavado ningún auto hoy")
            break
        case _:
            print("Selección inválida, inténtelo nuevamente")