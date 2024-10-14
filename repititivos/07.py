import os 
os.system("cls")

def factorial (n):
    factorial = 1
    while n > 1 :
        n -=1

    return factorial

def  factorial_r (n):
    if n == 1 : return n 
    return n * factorial_r (n - 1)

numero= int(input("Numero: "))

print(f"Factorial = {factorial_r(numero)}")