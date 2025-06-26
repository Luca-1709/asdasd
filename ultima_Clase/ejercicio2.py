datos_trabajadores={
    1:{"Nombre": "Lucas Canales",
       "Edad": 21,
       "ID": "LBCL17",
       "Cargo": "Ing Informatico"}
}

trabajadores=1

def agregar_trab(dic):
    while True:
        Nombre=input("Ingrese el Nombre del trabajador: ")
        if validar_Nombre(Nombre):
            print("El nombre cumple con las condiciones y se agregó al sistema")
            break
        else:
            print("El nombre no cumple con las condiciones de tener nombre y apellido del trabajador o 2 palabras")
            print("Nombre no ingresado")
    while True:
        Edad=input("Ingrese la edad del trabajador: ")
        if validar_edad(Edad):
            print("Edad ingresada con éxito")
            break
        else:
            print("La edad debe tener 2 dígitos")
    while True:
        ID=input("Ingrese el Identificador del trabajador: ")
        if validar_ID(ID):
            print("Identificador ingresado con éxito")
            break
        else:
            print("El identificador debe tener 4 mayusculas y 2 dígitos")
    while True:
        op_cargo=int(input('''Ingrese el cargo del trabajador: 
                           1.- Desarrollador
                           2.- Diseñador
                           3.- Finanzas
                           ''')) # type: ignore
        match op_cargo:
            case 1:
                Cargo="Desarrollador"
                break
            case 2:
                Cargo="Diseñador"
                break
            case 3:
                Cargo="Finanzas"
                break
            case _:
                print("Selección inválida")
    ultimo=list(dic.keys())[-1]
    dic[ultimo+1]={"Nombre": Nombre,
                 "Edad": Edad,
                 "Identificador": ID,
                 "Cargo": Cargo}
    trabajadores+=1

def validar_Nombre(Nombre):
    palabras=Nombre.split()
    return len(palabras)==2

def validar_edad(edad):
    digitos=0
    for numeros in edad:
        if numeros.isdigit():
            digitos+=1
    if digitos==2:
        return True
    else:
        print("Edad mal ingresada")

def validar_ID(ID):
    mayusculas=0
    digitos=0
    for identificador in ID:
        if identificador.isupper():
            mayusculas+=1
        if identificador.isdigit():
            digitos+=1
    if mayusculas==4 and digitos==2:
        return True
    else:
        print("Identificador mal ingresado")

def mostrar_trabajadores(dic):
    for k, valor in dic.items():
        print(k, valor)

def actualizar_trabajador(dic):
    mostrar_trabajadores(dic)
    act_trab=int(input("¿Qué trabajador desea actualizar? "))
    ultimo=list(dic.keys())[-1]
    while act_trab<1 or act_trab>ultimo:
        print("Trabajador no encontrado, inténtelo de nuevo")
        act_trab=int(input("¿Qué trabajador desea actualizar? "))
    while True:
        act_dato=int(input('''¿Qué dato desea actualizar?
                           1.- Nombre
                           2.- Edad
                           3.- Identidicador
                           4.- Cargo
                           5.- Salir
                           '''))
        match act_dato:
            case 1:
                while True:
                    dato_actualizado=input("Ingrese el nuevo nombre del trabajador: ")
                    if validar_Nombre(dato_actualizado):
                        print("El nombre cumple con los requisitos y fue actualizado")
                        dic[act_trab]["Nombre"]=dato_actualizado
                        break
                    else:
                        print("El nombre no cumple con los requisitos; nombre y apellido o 2 palabras")  
            case 2:
                while True:
                    dato_actualizado=input("Ingrese la nueva edad del trabajador: ")
                    if validar_edad(dato_actualizado):
                        print("Edad actualizada")
                        dic[act_trab]["Edad"]=dato_actualizado
                        break
                    else:
                        print("La edad debe contener 2 dígitos")
            case 3:
                while True:
                    dato_actualizado=input("Ingrese el nuevo identificador del trabajador: ")
                    if validar_ID(dato_actualizado):
                        print("Identificador actualizado")
                        dic[act_trab]["ID"]=dato_actualizado
                        break
                    else:
                        print("El identificador debe contener 4 mayusculas y 2 dígitos")
            case 4:
                while True:
                    op_cargo=int(input('''Ingrese el cargo del trabajador: 
                                    1.- Desarrollador
                                    2.- Diseñador
                                    3.- Finanzas
                                    ''')) # type: ignore
                    match op_cargo:
                        case 1:
                            dato_actualizado="Desarrollador"
                            dic[act_trab]["Cargo"]=dato_actualizado
                            break
                        case 2:
                            dato_actualizado="Diseñador"
                            dic[act_trab]["Cargo"]=dato_actualizado
                            break
                        case 3:
                            dato_actualizado="Finanzas"
                            dic[act_trab]["Cargo"]=dato_actualizado
                            break
                        case _:
                            print("Selección inválida")
            case 5:
                print("Saliendo")
                break
            case _:
                print("Selección inválida")

def eliminar_trabajadores(dic):
    mostrar_trabajadores(dic)
    del_trab=int(input("¿Qué trabajador desea borrar del sistema?: "))
    ultimo=list(dic.keys())[-1]
    while del_trab<1 or del_trab>ultimo:
        print("Trabajador no encontrado, inténtelo de nuevo")
        del_trab=int(input("¿Qué trabajador desea borrar del sistema?: "))
    del dic[del_trab]
    trabajadores-=1

def mostrar_estadisticas(dic):
    ultimo=list(dic.keys())[-1]
    print("El último trabajador ingresado fue ",ultimo, dic[ultimo])
    print(f"La cantidad de trabajadores que hay es de {trabajadores}")


while True:
    op_menu=int(input('''¿Qué desea hacer?:
                      1.- Agregar Trabajador
                      2.- Mostrar Trabajadores
                      3.- Actualizar Trabajador
                      4.- Eliminar Trabajador
                      5.- Mostrar estadísticas; último ingreso y cantidad de trabajadores
                      '''))
    match op_menu:
        case 1:
            agregar_trab(datos_trabajadores)
        case 2:
            mostrar_trabajadores(datos_trabajadores)
        case 3:
            actualizar_trabajador(datos_trabajadores)
        case 4:
            eliminar_trabajadores(datos_trabajadores)
        case 5:
            mostrar_estadisticas(datos_trabajadores)
        case 6:
            print("Saliendo...")
            break
        case _:
            print("Selección inválida")