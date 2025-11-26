#Simula un inicio de sesión con usuario y contraseña predefinidos. 
# Permite hasta tres intentos. Si ambos campos están vacíos, el intento no cuenta. 
# Finaliza al alcanzar el máximo o lograr acceso exitoso. Evalúa cada combinación con 
# operadores lógicos y muestra el motivo del fallo.


contrasena = "xm2508"
usuario = "ximena jaramc"
intentos = 3
print("=====Inicio de sesion=====")

while intentos != 0:
    inicio_usuario = input("Ingrese su usuario: ")
    inicio_contrasena = input("Ingrese la contrasena: ")
    if not inicio_usuario:
        print("El campu usuario no puede estar vacio")
    if inicio_usuario == usuario:
        print("Usuario correcto.")
    else:
        print("Usuario incorrecta")
        intentos -= 1
    if not inicio_contrasena:
        print("El campo contrasena no puede estar vacio")
    if inicio_contrasena == contrasena:
        print("Contrasena correcta")
    else:
        print("Contrasena incorrecta")
        intentos -= 1
        
        #print("los campos estan vacios.")
        #if inicio_contrasena == contrasena:
        #    print("Contrasena correcta.")
        #else:
         #   print("Contrasena incorrecta:")
        #    intentos -= 1
        #if inicio_usuario == usuario:
         #   print("Usuario correcto.")
        #else:
         #   print("Usuario incorrecto.")
          #  intentos -= 1
        
    
