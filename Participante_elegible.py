#Solicita la edad, si tiene licencia de conducción y si posee vehículo propio.
# Determina si la persona puede participar en una competencia, aplicando las 
# siguientes condiciones:
# Edad mínima de 18 años.
#Licencia vigente.
#Vehículo propio o préstamo autorizado.
#Evalúa con combinaciones de and y or para determinar si es Apto o No apto.

edad = int(input ("Ingrese su edad: "))
licencia = input ("Tiene licencia de conduccion? (si/no)")
vehiculo = ("El vehiculo es propio? (si/no)")

if vehiculo == "no":
    prestamo = input("Cuenta con permiso autorizado? (si/no)")
if edad >= 18 and licencia == "si" and vehiculo == "si":
    print("Puedes participar en la competencia")
if edad >= 18 and licencia == "si" and prestamo == "si":
    print ("Puedes participar en la competencia")
if (edad <= 18 and licencia == "si" and vehiculo == "si") or (edad >= 18 and licencia == "no" and vehiculo == "si") or (edad >=18 and licencia == "si" and prestamo == "no" ): 
    print ("No puedes competir")