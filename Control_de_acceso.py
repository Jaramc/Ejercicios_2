# Pide un nombre de usuario y un código numérico.
# Permite el ingreso solo si el usuario no está en la lista restringida y su código 
# cumple al menos una de las siguientes condiciones:
#Es múltiplo de 2.
#Termina en 7.
# Debe mostrar un mensaje distinto según el motivo del rechazo. 
# Elabora un diagrama de flujo que represente la decisión principal.

restringidos = ("Ximena", "yo", "Y no se quien mas")
nombre_usuario = input("Ingrese su nombre de usuario: ").strip()
if not nombre_usuario:
    print("El nombre de usuario no puede estar vacío.")
else:
    if nombre_usuario.lower() in restringidos:
        print("Acceso denegado: el usuario está en la lista restringida.")
    else:
        codigo = input("Ingrese su código numérico: ").strip()
        if not codigo:
            print("El código no puede estar vacío.")
        elif not codigo.isdigit():
            print("El código debe ser numérico.")
        else:
            codigo = int(codigo)
            es_multiplo_2 = (codigo % 2 == 0)
            termina_en_7 = (codigo[-1] == "7")
            if es_multiplo_2 or termina_en_7:
                print("Acceso permitido.")
            else:
                print("Acceso denegado.")

