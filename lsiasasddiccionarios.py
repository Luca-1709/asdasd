personas={
    1:{"Nombre": "Liam Nesson",
    "Teléfono": 9827358974,
    "EstadoCivil": "Soltero",
    "Ciudadano": True},
    2:{"Nombre": "Christian Balse",
    "Teléfono": 38756467,
    "EstadoCivil": "Soltero",
    "Ciudadano": True},
    3:{"Nombre": "Cristiano Ronaldo",
    "Teléfono": 2353756234,
    "EstadoCivil": "Casado",
    "Ciudadano": False},
    4:{"Nombre": "Vini JR",
    "Teléfono": 98436547,
    "EstadoCivil": "Soltero",
    "Ciudadano": False}
}
while True:
    
        print('''
        1.- Ingresar Persona
        2.- Mostrar listado
        3.- Actualizar persona
        4.- Borrar persona
        5.- Salir''')
        op=int(input("Seleccione una opción: "))
        match op:
            case 1:
                nombre=input("Ingrese el nombre de la persona: ")
                tele=int(input("Ingrese el número telefónico de la persona: "))
                Est_Civ=0
                while Est_Civ<=0 or Est_Civ>=3:
                    Est_Civ=int(input('''Ingrese el estado civil de la persona:
                                      1.- Soltero
                                      2.- Casado'''))
                    match Est_Civ:
                        case 1:
                            Est_Civil="Soltero"
                        case 2:
                            Est_Civil="Casado"
                        case _:
                            print("Selección inválida")
                Ciu=0
                while Ciu<=0 or Ciu>=3:
                    Ciu=int(input('''Ingrese si la persona es cidadana:
                                      1.- Si
                                      2.- No'''))
                    match Ciu:
                        case 1:
                            Ciudadania=True
                        case 2:
                            Ciudadania=False
                        case _:
                            print("Selección inválida")
                Nuevos_Datos={"Nombre": nombre, "Teléfono": tele, "EstadoCivil": Est_Civil, "Ciudadano": Ciudadania}
                personas[len(personas)+1]=Nuevos_Datos
                # personas[lista].update(Nuevos_Datos)
            case 2:
                for n, persona in personas.items():
                    print(n, persona)
            case 3:
                for n, persona in personas.items():
                    print(n, persona)
                act_u=0
                while act_u<1 or act_u>len(personas):
                    act_u=int(input('''¿Qué usuario desea actualizar?:'''))
                act_d=0
                while act_d<1 or act_d>4:
                    act_d=int(input('''¿Qué dato desea actualizar?
                                    1.- Nombre
                                    2.- Teléfono
                                    3.- Estado Civil
                                    4.- Ciudadania'''))
                    match act_d:
                        case 1:
                            Dat_actualizar="Nombre"
                            Actualizacion=input("Ingrese el nombre nuevo: ")
                        case 2:
                            Dat_actualizar="Teléfono"
                            Actualizacion=int(input("Ingrese el número nuevo"))
                        case 3:
                            Dat_actualizar="EstadoCivil"
                            Est_Civ=0
                            while Est_Civ<=0 or Est_Civ>=3:
                                Est_Civ=int(input('''Ingrese el estado civil de la persona:
                                                1.- Soltero
                                                2.- Casado'''))
                                match Est_Civ:
                                    case 1:
                                        Actualizacion="Soltero"
                                    case 2:
                                        Actualizacion="Casado"
                                    case _:
                                        print("Selección inválida")
                        case 4:
                            Dat_actualizar="Ciudadano"
                            Ciu=0
                            while Ciu<=0 or Ciu>=3:
                                Ciu=int(input('''Ingrese si la persona es cidadana:
                                                1.- Si
                                                2.- No'''))
                                match Ciu:
                                    case 1:
                                        Actualizacion=True
                                    case 2:
                                        Actualizacion=False
                                    case _:
                                        print("Selección inválida")
                        case _:
                            print("Selección inválida")
                    personas[act_u][Dat_actualizar]=Actualizacion
            case 4:
                for n, persona in personas.items():
                    print(n, persona)
                del_u=0
                while del_u<1 or del_u>len(personas):
                    del_u=int(input('''¿Qué usuario desea eliminar?:'''))
                # personas.pop(del_u)
                del personas[del_u]
            case 5:
                print("Saliendo ...")
                break
            case _:
                print("Selección inválida")
    # except Exception:
    #     print("Solo")