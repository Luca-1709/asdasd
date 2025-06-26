Vehiculos={
    1:{"Marca": "BMW",
    "Año": 2019,
    "Patente": "tyop29",
    "Tipo": "Sedan"}
}

def mostrar_vehículo(dic):
    for key, vehiculo in dic.items():
        print(key, vehiculo)

def validar_año(año):
    numeros=0
    while True:
        for numero in año:
            if numero.isdigit():
                numeros+=1
        if numeros==4:
            print("Año ingresado correctamente")
            return True
        else:
            print("Año ingresado incorrectamente")
            print("Deben ser 4 números")
            return False

def Ingreso_vehiculos(dic):
    Marca=input("Ingrese la marca del vehículo: ")
    while True:
        Año=input("Ingrese el año del vehículo: ")
        if validar_año(Año):
            break
        else:
            print("Año no ingresado")
    while True:
        Patente=input("Ingrese la patente del vehículo: ")
        if validar_Patente(Patente):
            break
        else:
            print("Matricula no ingresada")
    while True:
        op_tipo_v=int(input('''Seleccione el tipo de vehiculo:
                            1.- Sedan
                            2.- Camioneta
                            3.- Moto
                            '''))
        match op_tipo_v:
            case 1:
                Tipo="Sedan"
                break
            case 2:
                Tipo="Camioneta"
                break
            case 3:
                Tipo="Moto"
                break
            case _:
                print("Selección inválida") 
    Ultimo=list(dic.keys())[-1]
    dic[Ultimo+1]={"Marca": Marca,
                         "Año": Año,
                         "Patente": Patente,
                         "Tipo": Tipo}
            
def validar_Patente(Patente):
    minuscula=0
    numeros=0
    while True:
        for palabra in Patente:
            if palabra.islower():
                minuscula+=1
            if palabra.isdigit():
                numeros+=1
        if minuscula==4 and numeros==2:
            print("La matrícula está bien escrita")
            return True
        else:
            print("La matrícula está mal escrita")
            print("La matrícula debe tener 4 minusculas y 2 numeros")
            return False
        
def actualizar_vehiculo(dic):
    mostrar_vehículo(dic)
    act_v=int(input('''Qué vehículo desea actualizar: '''))
    ultimo=list(dic.keys())[-1]
    while act_v<1 or act_v>ultimo:
        print("Vehículo no encontrado, inténtelo nuevamente")
        act_v=int(input('''Qué vehículo desea actualizar: '''))
    while True:
        act_dato=int(input('''Qué dato desea actualizar:
                           1.- Marca
                           2.- Año
                           3.- Patente
                           4.- Tipo
                           5.- Salir
                           '''))
        match act_dato:
            case 1:
                act_marca=input("Ingrese la nueva marca: ")
                dic[act_v]["Marca"]=act_marca
            case 2:
                while True:
                    act_año=input("Ingrese el nuevo año del vehículo: ")
                    if validar_año(act_año):
                        dic[act_v]["Año"]=act_año
                        break
                    else:
                        print("Año no ingresado")
            case 3:
                while True:
                    act_Patente=input("Ingrese la nueva patente del vehículo: ")
                    if validar_Patente(act_Patente):
                        dic[act_v]["Patente"]=act_Patente
                        break
                    else:
                        print("Matricula no ingresada")
            case 4:
                while True:
                    act_tipo=int(input('''Seleccione el nuevo tipo de vehiculo:
                                        1.- Sedan
                                        2.- Camioneta
                                        3.- Moto
                                        '''))
                    match act_tipo:
                        case 1:
                            Tipo="Sedan"
                            break
                        case 2:
                            Tipo="Camioneta"
                            break
                        case 3:
                            Tipo="Moto"
                            break
                        case _:
                            print("Selección inválida") 
                dic[act_v]["Tipo"]=Tipo
            case 5:
                break
            case _:
                print("Selección inválida")
    
def borrar_vehiculo(dic):
    mostrar_vehículo(dic)
    borrar=int(input("Ingrese el Vehículo que desea borrar: "))
    ultimo=list(dic.keys())[-1]
    while borrar<1 or borrar>ultimo:
        print("Vehículo inválido")
        borrar=int(input("Ingrese el Vehículo que desea borrar: "))
    del dic[borrar]

def mostrar_ultimo_v(dic):
    ultimo=list(dic.keys())[-1]
    print(f"El último vehículo ingresado fue {ultimo}, {dic[ultimo]}")

def mostrar_cant_vehiculos(cant):
    print(f"La cantidad de vehiculos dentro es de {cant}")

cant_vehiculos=1

while True:
    op_Menu=int(input('''Seleccione que desea hacer:
                      1.- Ingresar vehículo
                      2.- Mostrar Vehículos
                      3.- Actualizar vehículo
                      4.- Borrar vehículo
                      5.- Mostrar estadísticas: último ingresado y total en garage
                      6.- Salir
                      '''))
    match op_Menu:
        case 1:
            Ingreso_vehiculos(Vehiculos)
            cant_vehiculos+=1
        case 2:
            mostrar_vehículo(Vehiculos)
        case 3:
            actualizar_vehiculo(Vehiculos)
        case 4:
            borrar_vehiculo(Vehiculos)
            cant_vehiculos-=1
        case 5:
            mostrar_ultimo_v(Vehiculos)
            mostrar_cant_vehiculos(cant_vehiculos)
        case 6:
            break
        case _:
            print("Selección inválida")