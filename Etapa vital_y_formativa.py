#Solicita la edad y el nivel educativo de una persona. Clasifica su etapa según las siguientes reglas:

#Menor de 6 años → Infante
#Entre 6 y 17 años y estudia → Estudiante escolar
#Entre 18 y 25 años y estudia → Universitario
#Mayor de 25 años y trabaja → Adulto activo
#Mayor de 60 años y no trabaja → Adulto mayor jubilado
#En cualquier otro caso → No determinado
#Valida que la edad sea coherente y utiliza condiciones encadenadas con operadores lógicos.

etapa = "No determinado"

edad = input("Ingresa tu edad: ")
edad= edad.strip()

if not edad:
    print("La edad no puede estar vacía.")
if not edad.isdigit():
    print("La edad debe ser un número entero positivo.")
else:
    edad = int(edad)
    if edad <= 0 or edad > 120:
        print("La edad ingresada no es coherente.")
    else:
        nivel = input("Ingresa tu nivel educativo (ninguno, escolar, universitario): ")
        nivel = nivel.strip().lower()
        if not nivel:
            print("El nivel educativo no puede estar vacío.")
        else:
            estudia = (nivel == "escolar") or (nivel == "universitario")
            trabaja = input("¿Trabajas actualmente? (si/no): ")
            trabaja = trabaja.strip().lower()
            if trabaja == "si":
                trabaja = True
            elif trabaja == "no":
                trabaja = False
            else:
                print("Respuesta sobre trabajo no válida, se asumirá que no trabaja.")
                trabaja = False
            if edad < 6:
                etapa = "Infante"
            elif edad >= 6 and edad <= 17 and estudia:
                etapa = "Estudiante escolar"
            elif edad >= 18 and edad <= 25 and estudia:
                etapa = "Universitario"
            elif edad > 60 and (not trabaja):
                etapa = "Adulto mayor jubilado"
            elif edad > 25 and trabaja:
                etapa = "Adulto activo"
            else:
                etapa = "No determinado"
            print("Etapa:", etapa)
