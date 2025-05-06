import time

n1=int(input("Ingrese un número: "))
n2=0
while n1>=n2:
    n2=int(input("Ingrese otro número: "))
    if n2<=n1:
        print(f"Error, intentelo de nuevo. Ingrese un número mayor a {n1}")
    
import random
cv=random.randint(n1,n2)
print(cv)
for i in range (cv):
    print("▄")
    time.sleep(1)
