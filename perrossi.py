while True:
    try:
        perros=int(input("Ingrese cuántos perros participarán en la caza: "))
        cuota=int(input("Ingrese cuantos conejos deberá traer cada perro: "))
        break
    except Exception:
        print("Ingrese solo números enteros")
import random, time
si_cuota=0
no_cuota=0

for p in range (perros):
    time.sleep(1)
    print(f"El perro n° {p+1} salió a cazar")
    time.sleep(2)
    conejos_cazados=random.randint(0,cuota*2)
    print(f"El perro n° {p+1} ha vuelto y trajo {conejos_cazados} conejos")
    time.sleep(1)
    if conejos_cazados>=cuota:
        print(f"El perro n° {p+1} cumplió con la cuota y podrá comer filete")
        si_cuota+=1
    else:
        print(f"El perro n° {p+1} no cumplió con la cuota y no comerá filete")
        no_cuota+=1

time.sleep(1)
print(f"En total {si_cuota} perros lograron la cuota y {no_cuota} no la lograron")