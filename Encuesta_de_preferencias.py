# Solicita edad y respuesta a la pregunta: “¿Te gusta programar?” (sí/no). 
# El programa debe repetirse mientras la edad ingresada sea mayor a cero.
# Al finalizar, muestra cuántas respuestas fueron afirmativas y cuántas negativas. 
# Controla respuestas vacías o incorrectas dentro del ciclo.

edad = 1
contador_si = 0
contador_no = 0

while edad > 0:
    texto_edad = input("Ingrese su edad: ")

    if not texto_edad:
        print("El campo edad no puede estar vacio")
    else:
        edad = int(texto_edad)

        if edad > 0:
            programador = input("¿Te gusta programar? (si/no): ")
            if not programador:
                print("El campo '¿Te gusta programar?' no puede estar vacío")
            elif programador == "si":
                contador_si += 1
            elif programador == "no":
                contador_no += 1
            else:
                print("Respuesta inválida. Debes responder 'si' o 'no'.")

print(f"Las respuestas positivas fueron {contador_si}")
print(f"Las respuestas negativas fueron {contador_no}")
