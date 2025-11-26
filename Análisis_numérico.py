#Solicita tres números enteros y determina:
#Si los tres son positivos.
#Si al menos uno es negativo.
#Si exactamente uno es cero.
# Debe analizar todas las combinaciones mediante condiciones encadenadas.

numero1 = input("Ingrese un numero: ")
numero2 = input("Ingresa un segundo numero: ")
numero3 = input("Ingresa un tercer numero: ")

if numero1 >= 1 and numero2 >= 1 and numero3 >= 1:
    print("Los tres numeros son positivos")
    
    if numero1 <= 0 or numero2 <= 0 or numero3 <= 0:
        print("Uno de los numeros es negativo")
        
        if (numero1 == 0 and numero2 !=0 and numero3 !=0) or (numero1 !=0 and numero2 == 0 and numero3 !=0) or (numero1 != 0 and numero2 != 0 and numero3 == 0):
            print("Uno de los numeros es 0")