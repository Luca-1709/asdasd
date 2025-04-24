# # #Expliacion y uso de while

# # num=0

# # while num<5:
# #     print("hola")
# #     num+=1
# import time
# num=10
# while num>0:
#     print(num)
#     time.sleep(1)
#     num-=1

# clave=3344
# password=int(input("Ingrese su clave: "))
# intento=3

# while clave!=password or intento==0:
#     print("Clave incorrecta, le quedan ", intento, " intentos")
#     password=int(input("Ingrese su clave: "))
#     intento=intento-1
#     if intento<=0:
#         break

# if intento>=1:
#     print("Clave correcta, bienvenido al sistema")
# else:
#     print("Clave incorrecta, sistema bloqueado")

nsum=int(input("Ingrese un número: "))
suma=0

while nsum!=0:
    suma+=nsum
    print(suma)
    nsum=int(input("Ingrese un número: "))


print("Ha salido del programa")
print(f"La sumatoria total es de {suma}")