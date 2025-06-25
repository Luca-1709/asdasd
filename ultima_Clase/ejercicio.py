Vehiculos={
    1: "Marca": "BMW"
    "Año": 2019
    "Patente": "tyop29"
    "Tipo": "S"
}

def Ingreso_vehiculos(dic):
    Marca=input("Ingrese la marca del vehículo: ")
    Año=int(input("Ingrese el año del vehículo: "))
    while True:
        Patente=input("Ingrese la patente del vehículo: ")
        if validar_Patente(Patente):
            break
        else

def validar_Patente(Patente):
    minuscula=0
    numeros=0
    while True:
        for palabra in Patente:
            if palabra.isupper():
                minuscula+=1
            if palabra.isdigit():
                numeros+=1
        if minuscula==4 and numeros==2:
            print("La matrícula está bien escrita")
            return True
        else:
            print("La matrícula está mal escrita")
            print("La matrícula debe tener 4 minusculas y 2 numeros")


