ci=0
credito=0
while ci!=1 and ci!=2 and ci!=3 :
    print("Indique su nivel de ingreso")
    ci=int(input("1.-$500.000 a $1.000.000 "
                 "2.-$1.000.001 a 1.500.000 " \
                 "3.-1.500.001 o más: "))
    if ci==1:
        credito+=300000
        
    elif ci==2:
        credito+=650000
        
    elif ci==3:
        credito+=1000000
        
    else:
        print("Respuesta invalida")

ne=0
while ne!=1 and ne!=2 and ne!=3 :
    print("Indique su nivel educacional")
    ne=int(input("1.-Básico "
                 "2.-Media "  \
                 "3.-Superior: "))
    if ne==1:
        credito*=1
        
    elif ne==2:
        credito*=1.3
        
    elif ne==3:
        credito*=1.5
        
    else:
        print("Respuesta invalida")

na=0
while na!=1 and na!=2 :
    print("Indique su nacionalidad")
    na=int(input("1.-Chilena "
                 "2.-Extranjera: "))
    if na==1:
        credito+=300000
        
    elif na==2:
        credito=credito
        
    else:
        print("Respuesta invalida")

print(f"Su credito será de {int(credito)}")
