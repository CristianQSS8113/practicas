import os
os.system("Cls")

gigabytes= float(input("Capacidad del disco duro en gigabytes: "))

megabytes = gigabytes * 1000
kilobytes = megabytes * 1000
bytes = kilobytes * 1000

print(f"Capacidad en Megabytes : {megabytes} MB")
print(f"Capacidad en Kilobytes : {kilobytes} KB")
print(f"Capacidad en Bytes : {bytes} Bytes")