# hpj1=50
# hpj2=50
# import random
# turno=random.randint(1,2)
# import time

# while hpj1>0 and hpj2>0:
#     if turno % 2==0:
#         ataque=random.randint(3,15)
#         ataquecrit=ataque*2
#         probac=random.randint(1,5)
#         if probac==1:
#             print("Turno del jugador 1")
#             time.sleep(1)
#             print("Jugador 1 ha atacado")
#             print(f"Ataque crítico, {ataquecrit} de daño")
#             hpj2-=ataquecrit
#             print(f"La vida del jugaror 2 bajado a bajado a {hpj2}")
#             time.sleep(1)
#         else:
#             print("Turno del jugador 1")
#             time.sleep(1)
#             print("Jugador 1 ha atacado")
#             print(f"Ataque normal, {ataque} de daño")
#             hpj2-=ataque
#             print(f"La vida del jugaror 1 bajado a bajado a {hpj2}")
#             time.sleep(1)
#     else:
#         ataque=random.randint(3,15)
#         ataquecrit=ataque*2
#         probac=random.randint(1,5)
#         if probac==1:
#             print("Turno del jugador 2")
#             time.sleep(1)
#             print("Jugador 2 ha atacado")
#             print(f"Ataque crítico, {ataquecrit} de daño")
#             hpj1-=ataquecrit
#             print(f"La vida del jugaror 2 bajado a bajado a {hpj1}")
#             time.sleep(1)
#         else:
#             print("Turno del jugador 2")
#             time.sleep(1)
#             print("Jugador 2 ha atacado")
#             print(f"Ataque normal, {ataque} de daño")
#             hpj1-=ataque
#             print(f"La vida del jugaror 1 bajado a bajado a {hpj1}")
#             time.sleep(1)

#     turno+=1

# if hpj1>hpj2:
#     print("El ganador es el Jugador 1")
# else:
#     print("El ganador es el Jugador 2")

n1=int(input("Ingrese un número: "))
n2=0

while n2<=n1:
    n2=int(input("Ingrese otro número que sea mayor al primero: "))
    if n2<=n1:
        print("Dato invalido, vuelva a intentarlo")

import random
nrand=random.randint(n1,n2)
print(f"El número aleatorio entre {n1} y {n2} es {nrand}")

for i in range (nrand):
    print("Hola")