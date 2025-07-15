
autos = {
    'ABC123': ['Toyota', 2020, 'Gasolina', '1.6L'],
    'DEF456': ['Chevrolet', 2019, 'Diesel', '2.0L'],
    'GHI789': ['Hyundai', 2021, 'Eléctrico', '0.0L'],
    'JKL321': ['Mazda', 2022, 'Gasolina', '2.5L']
}
# stock tiene el medelo del auto para hacer el cruce entre diccionarios
# cada par de datos tiene el modelo y la cantidad de stock y el precio del mismo,
stock = {
    'ABC123': [14, 12500000],
    'DEF456': [0, 10400000],
    'GHI789': [4, 17900000],
    'JKL321': [6, 15500000],
    'ZZZ000': [2, 8900000]  # Este auto no existe en Autos
}

'''
dado los diccionarios anteriores cerar un programa con sl sigueinte menu
1.- Mostrar stock de cada uno 
2.- Buscar precio mas alto 
3.- Actualizar stock 
4.- Borrar un modelo ( considerar borarr el stock tb)
5.- Actualizar datos vehiculo
6.- Salir
'''

def Mostrar(dic):
    for k, v in dic.items():
        print(k, v)

def buscar_precio_masalto(dic):
    auto_precio_mayor=max(dic, key=lambda k: dic[k][1])
    print("El vehículo con el valor más alto es ", auto_precio_mayor," y el valor que tienes es de ", dic[auto_precio_mayor][1])

def actualizar_stock(dic):
    Mostrar(dic)
    vehi_act=input("Seleccione el vehículo a actualizar el stock: ")
    while True:
        if vehi_act in dic:
            print("Selección válida")
            break
        else:
            print("Selección inválida")
            vehi_act=input("Seleccione el vehículo a actualizar el stock: ")
    dato_actualizado=int(input("Ingrese el dato actualizado: "))
    dic[vehi_act][0]=dato_actualizado

def eliminar(dic):
    Mostrar(dic)
    eliminar_vehi=input("Seleccione el vehículo a eliminar: ")
    while True:
        if eliminar_vehi in dic:
            print("Selección válida")
            break
        else:
            print("Selección inválida")
            eliminar_vehi=input("Seleccione el vehículo a eliminar: ")
    del autos[eliminar_vehi]
    del stock[eliminar_vehi]
    
def actualizar_vehi(dic):
    Mostrar(dic)
    vehi_act=input("Seleccione el vehículo a actualizar: ")
    while True:
        if vehi_act in dic:
            print("Selección válida")
            break
        else:
            print("Selección inválida")
            vehi_act=input("Seleccione el vehículo a actualizar: ")
    while True:
        dato_actualizar=int(input('''Seleccione el dato a actualizar: 
                                1.- Marca
                                2.- Año
                                3.- Energía
                                4.- Motor
                                  '''))
        match dato_actualizar:
            case 1:
                dato_actualizado=input("Ingrese la marca actualizada: ")
                dic[vehi_act][0]=dato_actualizado
                break
            case 2:
                dato_actualizado=int(input("Ingrese el año actualizado: "))
                dic[vehi_act][1]=dato_actualizado
                break
            case 3:
                dato_actualizado=input("Ingrese la energía actualizada: ")
                dic[vehi_act][2]=dato_actualizado
                break
            case 4:
                dato_actualizado=input("Ingrese el motor actualizado: ")
                dic[vehi_act][3]=dato_actualizado
                break
            case _:
                print("Selección inválida")


while True:
    op_menu=int(input('''¿A qué menú desea ingresar?
                    1.- Mostrar stock de cada uno
                    2.- Buscar precio más alto
                    3.- Actualizar Stock
                    4.- Borrar modelo
                    5.- Actualizar datos de vehículo
                    6.- Salir
                      '''))
    match op_menu:
        case 1:
            Mostrar(autos)
            Mostrar(stock)
        case 2:
            buscar_precio_masalto(stock)
        case 3:
            actualizar_stock(stock)
        case 4:
            eliminar(autos)
        case 5:
            actualizar_vehi(autos)
        case 6:
            print("Saliendo ...")
            break
        case _:
            print("Selección inválida")