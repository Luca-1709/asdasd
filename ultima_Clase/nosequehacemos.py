Juegos={
        1:  {"Nombre": "Kirby",
            "Precio": 70000,
            "Code": "KirB5613"}
}

def mostrar_juegos(dic):
    for j, datos in dic.items():
        print(j , datos)

def valida_code(code):
    mayusculas=0
    minusculas=0
    numero=0
    for palabra in code:
        if palabra.isupper():
            mayusculas+=1
        if palabra.islower():
            minusculas+=1
        if palabra.isdigit():
            numero+=1
    if mayusculas==2 and minusculas==2 and numero==4:
        print("El código está bien escrito")
        return True
    else:
        print("El código está mal escrito")

def valida_nombre(nombre):
    palabras=nombre.split()
    return len(palabras)==2

def valida_precio(precio):
    if precio>=70000 and precio<=100000:
        return True
    else: 
        return False

def agregar_juego(dic):
    ultima=list(dic.keys())[-1]
    while True:
        nombre=input("Ingrese el nombre del juego: ")
        if valida_nombre(nombre):
            print("El nombre contiene 2 palabras")
            break
        else:
            print("El nombre no fue ingresado")
            print("El nombre debe contener 2 palabras")
    while True:
        precio=int(input("Ingrese el precio del juego: "))
        if valida_precio(precio):
            print("El precio está dentro del rango")
            break
        else:
            print("El precio está fuera del rango establecido")
    while True:
        code=input("Ingrese el codigo del juego: ")
        if valida_code(code):
            dic[ultima+1]={
                        "Nombre": nombre,
                        "Precio": precio,
                        "Code": code
            }
            print("Juego ingresado con exito")
            break
        else:
            print("El juego no fue ingresado")
            print("El código debe tener 2 mayúsculas, 2 minúsculas y 4 dígitos")
    
def elimnar_juego(dic):
    mostrar_juegos(dic)
    Del_J=0
    ultima=list(dic.keys())[-1]
    while Del_J<1 or Del_J>ultima:
        Del_J=int(input("¿Qué Juego desea eliminar? "))
    del dic[Del_J]

def actualizar_juego(dic):
    mostrar_juegos(dic)
    act_juego=0
    ultima=list(dic.keys())[-1]
    while act_juego<1 or act_juego>ultima:
        act_juego=int(input("¿Que juego desea actualizar? "))
    act_dat=0
    while act_dat<1 or act_dat>3:
        act_dat=int(input('''Seleccione el dato que desea actualizar
                          1.- Nombre
                          2.- Precio
                          3.- Codigo
                          4.- Salir
                          '''))
        match act_dat:
            case 1:
                dato_actualizado=input("Ingrese el nuevo nombre: ")
                Juegos[act_juego]["Nombre"]=dato_actualizado
            case 2:
                dato_actualizado=int(input("Ingrese el nuevo precio: "))
                Juegos[act_juego]["Precio"]=dato_actualizado
            case 3:
                while True:
                    dato_actualizado=input("Ingrese el nuevo código: ")
                    if valida_code(dato_actualizado):
                        print("Código ingresado correctamente")
                        Juegos[act_juego]["Code"]=dato_actualizado
                        break
                    else:
                        print("Codigo inválido")
                        print("El código debe tener 2 mayúsculas, 2 minúsculas y 4 dígitos")

while True:
    print('''
          1.- Agregar juegos
          2.- Mostrar juegos
          3.- Actualizar juegos
          4.- Borrar juegos
          5.- Salir''')
    op=int(input("Seleccione una opción: "))
    match op:
        case 1:
            agregar_juego(Juegos)
        case 2:
            mostrar_juegos(Juegos)
        case 3:
            actualizar_juego(Juegos)
        case 4:
            elimnar_juego(Juegos)
        case 5:
            break