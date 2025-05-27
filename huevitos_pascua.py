import random, time
noob=0
Master=0
legend=0
top=0

while True:
    try:
        cant_niños=int(input("Ingrese la cantidad de niños que participarán en la búsqueda de huevitos de pascua "))
        while cant_niños<0:
            print("Error, ingrese solo números positivos")
            cant_niños=int(input("Ingrese la cantidad de niños que participarán en la búsqueda de huevitos de pascua "))
        for i in range (cant_niños):
            time.sleep(1)
            print(f"Turno del niño n° {i+1}")
            time.sleep(1)
            cant_huevos=random.randint(3,30)
            print(f"El niño n° {i+1} trajo {cant_huevos}")
            if cant_huevos<12:
                print(f"El niño n° {i+1} es un Noob")
                noob+=1
            elif cant_huevos>=12 and cant_huevos<=24:
                print(f"El niño n° {i+1} es un Master")
                Master+=1
            else:
                print(f"El niño n° {i+1} es un Legend")
                legend+=1
            if cant_huevos>top:
                top=cant_huevos
        time.sleep(1)
        print(f"La cantidad de Noobs es de {noob}")
        print(f"La cantidad de Master es de {Master}")
        print(f"La cantidad de Legend es de {legend}")
        print(f"El mayor n° de huevos encontrados por un niño fue de {top}")
        break
    except Exception:
        print("Solo debe ingresar números enteros")
