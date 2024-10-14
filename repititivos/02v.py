import os
os.system ("cls")

def multiplica(n1, n2):
    if n2 == 1 : return n1 
    return multiplica (n1, n2 - 1)
    