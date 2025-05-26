ventas_diarias=0
cant_autos=0
cant_lav_f=0
cant_lav_s=0
cant_lav_b=0

while True:
    while True:
        try:
            op_menu1=int(input('''¿A qué programa desea acceder?
                               1.- Curso de lavado de autos
                               2.- Ver las ventas del día
                               3.- Salir
                               '''))
            match op_menu1:
                case 1:
                    while True:
                        op_lavado=int(input('''¿Qué lavado desea?
                                            1.- Full $15.000
                                            2.- Standard $10.000
                                            3.- Básico $7.000
                                            4.- Volver al menú principal
                                            '''))
                        match op_lavado:
                            case 1:
                                print("Lavado full")
                                ventas_diarias+=15000
                                cant_autos+=1
                                cant_lav_f+=1
                            case 2:
                                print("Lavado Standard")
                                ventas_diarias+=10000
                                cant_autos+=1
                                cant_lav_s+=1
                            case 3:
                                print("Lavado Básico")
                                ventas_diarias+=7000
                                cant_autos+=1
                                cant_lav_b+=1
                            case 4:
                                print("Volviendo al menú principal")
                                break
                            case _:
                                print("Selección inválida, inténtelo de nuevo")
                case 2:
                    print("Viendo las ventas diarias")
                    print(f"En total durante el día se ha recaudado ${ventas_diarias} y se han lavado {cant_autos} autos")
                case 3:
                    if cant_lav_f>0:
                        print("El monto mayor recaudado por un lavado fue de $15.000")
                    elif cant_lav_s>0:
                        print("El monto mayor recaudado por un lavado fue de $10.000")
                    elif cant_lav_b>0:
                        print("El monto mayor recaudado por un lavado fue de $7.000")
                    else:
                        print("No se realizó ningún lavado hoy")
                    print("Saliendo del programa")
                    break
            break
        except Exception:
            print("Ingrese solo números enteros")