import os
os.system("cls")

edad1= int(input("Primera edad: "))
edad2= int(input("Segunda edad: "))
edad3= int(input("Tercera edad: "))

edad_menor=edad1
edad_mayor=edad1

if edad2<edad_menor:
    edad_menor=edad2
else: 
    edad_menor=edad1

if edad3<edad_menor:
    edad_menor=edad2
    
if edad2>edad_mayor:
    edad_mayor=edad1
    
if edad3<edad_mayor:
    edad_mayor=edad3
    
print(f"La edad menor es: {edad_menor}")
print(f"La edad mayor es: {edad_mayor}")