Notas=[]
from os import system
import time

while True:
    while True:
        try:
            print('''¿A qué menú desea ingresar?
                1.- Ingresar Nota
                2.- Borrar Nota
                3.- Mostrar Notas
                4.- Sacar promedio
                5.- Limpiar todas las notas
                6.- Salir ''')
            op_menu=int(input())
            break
        except Exception:
            print("Error, solo debe ingresar números enteros")
    match op_menu:
        case 1:
            nota=0
            while nota<1 or nota>7:
                try:
                    nota=float(input("Ingrese su nota: "))
                    if nota>=1 and nota<=7:
                        Notas.append(nota)
                        input("Presione enter para continuar")
                        system("cls")
                        break
                    else:
                        print("Nota fuera del rango")
                except Exception:
                    print("Solo debe ingresar números enteros o decimales positvos entre 1 y 7")
        case 2:
            borrar_nota=0
            while nota<1 or nota>7:
                try:
                    borrar_nota=float(input("Ingrese la nota que desea eliminar: "))
                    if nota>=1 and nota<=7:
                        Notas.remove(borrar_nota)
                        input("Presione enter para continuar")
                        system("cls")
                        break
                    else:
                        print("Nota fuera del rango")
                except Exception:
                    print("Solo debe ingresar números enteros o decimales positvos entre 1 y 7")
        case 3:
            print("Mostrando notas ...")
            time.sleep(2)
            if len(Notas)==0:
                print("No hay notas para mostrar")
            else:
                print(Notas)
            input("Presione enter para continuar")
            system("cls")
        case 4:
            print("Calculando promedio ...")
            time.sleep(2)
            promedio=sum(Notas)/len(Notas)
            print(f"El promedio del alumno es de {promedio}")
            input("Presione enter para continuar")
            system("cls")
        case 5:
            print("Eliminando las notas de la lista ...")
            time.sleep(2)
            Notas.clear()
            print("Notas eliminadas")
            input("Presione enter para continuar")
            system("cls")
        case 6:
            print("Saliendo ...")
            break
        case _:
            print("Selección inválida")
            input("Presione enter para continuar")
            system("cls")

