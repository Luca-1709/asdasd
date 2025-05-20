# try:
    
#     n1=int(input("ingrese un num: "))
#     n2=int(input("ingrese un num: "))
#     print(f"La división es {n1/n2}")

# except ZeroDivisionError as nombre_de_excepción:
#     # Código para manejar la excepción
#     print(f"Se produjo una excepción: {nombre_de_excepción}")


while True:
    try:
        op=int(input("Ingrese un N°: "))
        break
    except Exception:
        print("Debe ingresar solo números")

    