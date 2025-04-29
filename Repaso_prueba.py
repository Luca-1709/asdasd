# a=int(input())
# for i in range (1,10001):
#     print(f"{i} x {a} = {i*a}")

# a=int(input())
# for i in range (a):
#     for e in range(101):
#         print(f"{i} x {e} = {i*e}")

# edad=-1

# while(edad<0 or edad>100):
#     edad=int(input("Ingrese su edad: "))
#     if (edad<0 or edad>100):
#         print("Error, fuera de rango")

# print("Ha ingresado exitosamente")
# print(edad)

# term=int(input("Ingrese un número: "))
# p=0
# ip=0

# for i in range (1,term+1):
#     if i % 2 == 0:
#         print(f"{i} es Par")
#         p+=1
#     else:
#         print(f"{i} es impar")
#         ip+=1

# a=0
# cont=0 
# suma=0
# r="so"
# while r!="salir":
#     r=input("¿Desea salir? ")
#     if r=="no":
#         a=int(input("Ingrese un número o salga del sistema: "))
#         suma+=a
#         cont+=1

# print("Ha salido del sistema")
# # print(f"La sumatoria total de los {cont} números es de {suma}")

# opc=0
# cont=0
# total=0

# while opc != 2:
#     print("1.- Agregar un número")
#     print("2.- Salir")
#     opc=int(input())
#     if opc == 1:
#         num=int(input("Ingrese un número: "))
#         cont+=1
#         total+=num

# print(f"La cantidad de números que ha ingresado es de {cont}")
# print(f"La sumatoria de los números ingresados es de {total}")
# num=0
# tot=0
# a=0

# while tot<50:
#     num=int(input("Ingrese un número: "))
#     import random
#     a=random.randint(2,8)
#     tot=num*a
#     print(tot)
#     if tot>50:
#         print("Logró la meta")
#     else:
#         print("Intente nuevamente")


# n=-1

# while n<0:
#     n=int(input("Ingrese un número positivo: "))
#     if n<0:
#         print("Ha ingresado un número negativo, intentelo de nuevo")

# n*=5
# n-=8
# n+=3
# n/=2
# print(f"El valor final es de {n}")

import random
a=random.randint(1,50)