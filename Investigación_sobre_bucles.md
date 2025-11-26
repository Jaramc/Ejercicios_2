Crea un archivo llamado investigacion_bucles.md donde respondas:

Diferencias entre un bucle controlado por contador y un bucle controlado por condición.
Ejemplos cotidianos que representen el uso de cada tipo de bucle.
Cuándo es más apropiado usar while en lugar de for.
Qué es un bucle infinito, cómo prevenirlo y cómo detectarlo durante la ejecución.
Qué función cumplen las sentencias break y continue dentro de un ciclo.
Explica el error lógico más común al usar while y cómo evitarlo.
El archivo debe incluir títulos, subtítulos y ejemplos descriptivos en formato Markdown.

# Bucles en programación: guía rápida en Markdown

## 1. Bucle controlado por contador vs bucle controlado por condición

### 1.1 Bucle controlado por contador

Un bucle está controlado por contador cuando:

* Se repite un número conocido de veces.
* Existe una variable contador que:

  * Se inicializa antes del bucle.
  * Se incrementa o decrementa en cada iteración.
  * Se compara con un límite (inicio/fin).

Ejemplo típico en código (similar a C/Java):

```c
for (int i = 0; i < 10; i++) {
    // Se ejecuta exactamente 10 veces
}
```

### Ejemplos cotidianos (contador)

1. Hacer 20 abdominales

   * Contador: número de abdominales realizadas.
   * Límite: 20.
   * Sabes de antemano cuántas repeticiones harás.

2. Repartir exactamente 5 volantes a las primeras 5 personas

   * Entregas un volante y sumas 1 al contador.
   * Cuando llegas a 5, paras.

3. Leer 10 páginas de un libro

   * Página actual como contador.
   * Parar cuando hayas leído 10 páginas más.

---

### 1.2 Bucle controlado por condición

Un bucle está controlado por condición cuando:

* No sabes cuántas veces se repetirá.
* El criterio de parada depende de una condición lógica que puede cambiar mientras se ejecuta el programa (entrada de usuario, estado del sistema, sensores, etc.).

Ejemplo típico en código:

```python
respuesta = ""
while respuesta != "salir":
    respuesta = input("Escribe un comando o 'salir': ")
```

### Ejemplos cotidianos (condición)

1. Esperar a que llegue el bus

   * Condición: “el bus ha llegado”.
   * No sabes cuántos minutos esperarás.

2. Regar una planta hasta que la tierra esté húmeda

   * Condición: humedad de la tierra “suficiente”.
   * No sabes cuántos segundos o minutos regarás.

3. Hablar por teléfono hasta que la otra persona cuelgue

   * Condición: “la llamada sigue activa”.

---

## 2. Cuándo es más apropiado usar while en lugar de for

En términos generales:

* for: cuando conoces el número de iteraciones (o puedes expresarlo claramente como un recorrido sobre una colección, rango, lista, etc.).
* while: cuando la cantidad de iteraciones no es conocida y depende de una condición que puede cambiar de forma impredecible.

### Casos típicos para while

1. Leer datos hasta fin de archivo o hasta que el usuario escriba “salir”:

```python
linea = input("Escribe algo (o 'salir'): ")
while linea != "salir":
    print("Leí:", linea)
    linea = input("Escribe algo (o 'salir'): ")
```

2. Esperar a que se cumpla un evento externo:

* Esperar a que un servidor responda.
* Esperar a que un sensor indique un valor específico.

3. Procesos de “reintento”:

```python
intentos = 0
max_intentos = 3
exito = False

while intentos < max_intentos and not exito:
    # intentar operación
    intentos += 1
    # actualizar exito según el resultado
```

---

## 3. Bucle infinito: qué es, cómo prevenirlo y cómo detectarlo

### 3.1 Qué es un bucle infinito

Un bucle infinito es un ciclo que:

* Nunca cumple la condición de salida.
* Por lo tanto, no termina por sí mismo.

Ejemplo típico en while:

```python
while True:
    print("Esto nunca termina por sí solo")
```

O menos obvio:

```python
i = 0
while i < 10:
    print(i)
    # i nunca cambia → condición siempre verdadera
```

### 3.2 Cómo prevenir bucles infinitos

1. Asegurarse de que la condición pueda volverse falsa:

   * Actualizar correctamente las variables que intervienen en la condición.
   * Evitar condiciones que son siempre verdaderas por diseño (por ejemplo, `while True` sin break controlado).

2. Diseñar el bucle con un “plan de salida” claro:

   * Identificar qué tiene que suceder para que el bucle termine.
   * Verificar que ese evento es alcanzable.

3. Añadir límites de seguridad:

```python
i = 0
while condicion and i < 1000:
    # ...
    i += 1
```

### 3.3 Cómo detectar un bucle infinito durante la ejecución

* El programa:

  * No responde (se “congela”).
  * Consume CPU constantemente.
  * No pasa de cierta parte del código (los mensajes de depuración se repiten sin parar).

Formas prácticas de detectarlo:

1. Usar mensajes de depuración:

```python
i = 0
while condicion:
    print("Iteración:", i)
    i += 1
```

2. Usar un depurador (debugger):

   * Colocar puntos de ruptura dentro del bucle.
   * Ver cómo cambian las variables en cada iteración.

3. Observar la salida:

   * Si ves la misma línea repetida miles de veces, probablemente hay un bucle infinito o casi infinito.

---

## 4. Sentencias break y continue dentro de un ciclo

### 4.1 Sentencia break

* Sale inmediatamente del bucle más interno.
* Se usa cuando se cumple una condición que hace innecesario continuar iterando.

Ejemplo:

```python
while True:
    comando = input("Comando: ")
    if comando == "salir":
        break  # rompe el while
    print("Procesando comando:", comando)
```

Ejemplo cotidiano:

* Estás buscando una llave en cajones; cuando la encuentras, dejas de revisar más cajones.

### 4.2 Sentencia continue

* Salta directamente a la siguiente iteración del bucle.
* Omite el resto del código en la iteración actual.

Ejemplo:

```python
for i in range(10):
    if i % 2 == 0:
        continue  # salta el código que está debajo si i es par
    print("Impar:", i)
```

Ejemplo cotidiano:

* Revisar una lista de correos:

  * Si el asunto está vacío, lo saltas y pasas al siguiente (continue).
  * Si encuentras un correo urgente y con eso es suficiente, dejas de revisar el resto (break).

---

## 5. Error lógico más común al usar while y cómo evitarlo

### 5.1 Error típico: no actualizar la condición (o actualizarla mal)

El error lógico más frecuente con while es:

* Olvidar modificar la variable que forma parte de la condición.
* O modificarla de forma incorrecta, de modo que la condición nunca deja de ser verdadera (o se vuelve verdadera otra vez).

Ejemplo con error:

```python
i = 0
while i < 5:
    print(i)
    # Falta i += 1 → bucle infinito
```

Otro ejemplo sutil:

```python
i = 0
while i <= 5:
    print(i)
    i += 2
```

Aquí no es infinito, pero quizá se esperaba imprimir exactamente hasta 5 y el salto de 2 puede saltarse valores, causando una lógica incorrecta según el objetivo.

### 5.2 Cómo evitar este tipo de errores

1. Revisar el “ciclo de vida” de la variable de control:

   * Inicializarla correctamente antes del while.
   * Modificarla siempre dentro del cuerpo del bucle.
   * Confirmar que esa modificación se hace en todas las rutas posibles (if, else, etc.).

2. Pensar el bucle en lenguaje natural:

   * “Mientras i sea menor que 5, imprime i y luego súmale 1.”
   * Comparar esa frase con el código para ver si coincide.

3. Empezar por un for cuando sea posible:

   * Si el bucle realmente es de contador conocido, un for reduce la probabilidad de error:

```python
for i in range(5):
    print(i)
```

4. Usar pruebas rápidas:

   * Probar con valores pequeños.
   * Añadir prints para ver cuántas veces se repite y cómo cambian las variables.

---

## 6. Resumen final

* Un bucle controlado por contador se usa cuando sabemos cuántas veces se repetirá; un bucle controlado por condición se usa cuando el número de iteraciones depende de un estado o evento.
* for suele ser más apropiado para recorridos con número de iteraciones conocido; while se prefiere cuando la condición de parada es más compleja o desconocida.
* Un bucle infinito nunca termina porque la condición nunca se vuelve falsa; se previene diseñando bien la condición, actualizando la variable de control y usando límites de seguridad.
* break sirve para salir del bucle; continue salta a la siguiente iteración sin ejecutar el resto del cuerpo en la actual.
* El error lógico más común con while es olvidar actualizar la variable de control o hacerlo mal; se evita revisando la lógica, probando con casos simples y usando for cuando el problema es de conteo claro.
