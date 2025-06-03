from os import system
listaNotas=[]
sum_Not=0
cont_nota=0

while True:
    print("Presione 1 para ingresar su nota")
    print("Ingrese 2 para salir")
    op=int(input("Seleccione una opción: "))
    match op:
        case 1:
            try:
                nota=float(input("Ingrese su nota: "))
                if nota!=0:
                    listaNotas.append(nota)
                    sum_Not+=nota
                    cont_nota+=1
                    print(f"Sus notas cargadas son {listaNotas}")
                    print(F"En total lleva {sum_Not} notas")
                    print(f"Hasta ahora su promedio es de {sum_Not/cont_nota}")
                else:
                    print("Volviendo al menú principal")
                    break
            except Exception:
                print("Solo debe ingresar números enteros o decimales")
        case 2:
            print(f"Su promedio final es de: {sum(listaNotas)/len(listaNotas)}")
            print("Saliendo del sistema")
            break
    