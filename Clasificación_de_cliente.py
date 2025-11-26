#Pide el valor total de una compra y el tipo de membresía. Clasifica al cliente como:
#Premium → monto alto y membresía activa.
#Frecuente → monto medio o membresía temporal.
#Regular → cualquier otro caso.
#Si el monto es inválido, muestra un mensaje de error.

monto = input("Ingresa el valor total de la compra: ")
membresia = input("Ingresa el tipo de membresía (1:activa / 2:temporal / 3:ninguna): ")
try:
    monto = float(monto)
    if monto < 0:
        print("Error: el monto no puede ser negativo.")
        exit()
except ValueError:
    print("Error: el monto ingresado no es válido.")
    exit()
try:
    membresia = int(membresia)
    if membresia not in (1, 2, 3):
        print("Error: el tipo de membresía no es válido.")
        exit()
except ValueError:
    print("Error: el tipo de membresía debe ser un número (1, 2 o 3).")
    exit()
if monto >= 1000 and membresia == 1:
    categoria = "Premium"
elif (500 <= monto < 1000) or (membresia == 2):
    categoria = "Frecuente"
else:
    categoria = "Regular"

print(f"El cliente ha sido clasificado como: {categoria}")
