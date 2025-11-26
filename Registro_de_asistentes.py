# Crea un ciclo que solicite nombres hasta que se escriba “FIN”. 
# Al finalizar, muestra:
# - El total de nombres ingresados.
# - Si hay nombres repetidos.
# El programa debe ignorar entradas vacías y evitar usar TRY/EXCEPTION.

nombre = []     
contador = []    
ingreso_nombre = input('Ingrese un nombre, o escriba "FIN" para finalizar: ')
ingreso_nombre = ingreso_nombre.strip()

while ingreso_nombre.upper() != "FIN":
    if not ingreso_nombre:
        print("El nombre no puede estar vacío.")
    else:
        if ingreso_nombre in nombre and ingreso_nombre not in contador:
            contador.append(ingreso_nombre)
        nombre.append(ingreso_nombre)
    ingreso_nombre = input('Ingrese un nombre, o escriba "FIN" para finalizar: ')
    ingreso_nombre = ingreso_nombre.strip()
print(f"El total de nombres ingresados fue: {len(nombre)}")
if contador:
    print("Hay nombres repetidos.")
    print("Nombres repetidos:", contador)
else:
    print("No hay nombres repetidos.")
