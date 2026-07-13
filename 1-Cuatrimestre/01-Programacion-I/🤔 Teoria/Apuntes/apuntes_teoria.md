
```markdown
# 🧠 Manual de Consulta y Apuntes Teóricos - Programación I (UTN)

Este documento sirve como bitácora oficial de teoría, sintaxis y buenas prácticas para las 10 unidades de la materia del plan de estudios de la Tecnicatura Universitaria en Programación.

---

## 🔹 Unidad 1: Estructuras Secuenciales

El paradigma imperativo se basa en el flujo lineal de instrucciones. Un algoritmo secuencial ejecuta una acción matemática o lógica estrictamente detrás de la otra.

### Conceptos Fundamentales
* **Variables:** Espacios reservados en la memoria RAM. Python utiliza **tipado dinámico** (no hace falta declarar si es texto o número, el intérprete lo deduce) y **fuertemente tipado** (no podés sumar un texto con un número directamente).
* **Buenas Prácticas de Estilo (PEP 8):** Los nombres de las variables deben ser descriptivos y usar `snake_case` (letras minúsculas separadas por guiones bajos).

### Operadores Aritméticos y Prioridad
1. Énfasis/Paréntesis `()`
2. Potencia `**`
3. Multiplicación `*`, División flotante `/`, División entera `//`, Módulo (resto) `%`
4. Suma `+`, Resta `-`

```python
# Demostración de tipos de datos y operaciones secuenciales
nombre_usuario = input("Ingrese el nombre del estudiante: ") # Retorna un str
horas_practica = int(input("Ingrese horas de programación semanales: ")) # Casting a int

# Cálculo de proyección mensual (4 semanas) con división flotante y entera
total_horas_mensual = horas_practica * 4
promedio_diario_flotante = total_horas_mensual / 30
promedio_diario_entero = total_horas_mensual // 30
resto_horas = total_horas_mensual % 30

print(f"Estudiante: {nombre_usuario}")
print(f"Proyección mensual: {total_horas_mensual} horas.")
print(f"Promedio diario exacto: {promedio_diario_flotante:.2f} horas.")
print(f"Cociente entero diario: {promedio_diario_entero} horas. Resto: {resto_horas}")

```

---

## 🔹 Unidad 2: Estructuras Condicionales

Las estructuras condicionales controlan el flujo del programa evaluando expresiones lógicas mediante operadores relacionales (`>`, `<`, `==`, `!=`, `>=`, `<=`) y lógicos (`and`, `or`, `not`).

### Tipos de Bifurcaciones

| Estructura | Palabras Clave | Dinámica de Ejecución |
| --- | --- | --- |
| **Simple** | `if` | Evalúa una condición. Si es verdadera, ejecuta el bloque indentado. |
| **Compuesta** | `if / else` | Ofrece un camino alternativo obligatorio si la condición principal es falsa. |
| **Múltiple** | `if / elif / else` | Evalúa en cascada. En el momento que una condición es verdadera, ejecuta y rompe la estructura. |

```python
# Sistema de control de asistencia y calificaciones
nota_final = float(input("Ingrese la nota definitiva (1-10): "))
porcentaje_asistencia = int(input("Ingrese el porcentaje de asistencia (0-100): "))

if porcentaje_asistencia < 75:
    print("Estado: Libre por inasistencias 🔴")
else:
    # Condicionales anidados para determinar la condición académica
    if nota_final >= 7:
        print("Estado: Promocionado 🟢 ¡Felicitaciones!")
    elif nota_final >= 4:
        print("Estado: Regularizado 🟡 (Rinde examen final)")
    else:
        print("Estado: Libre por insuficiencia académica 🔴 (Va a recuperatorio)")

```

---

## 🔹 Unidad 3: Estructuras Repetitivas

Los bucles permiten la ejecución reiterada de un bloque de código. La elección del bucle depende de si el número de iteraciones está determinado o indeterminado.

### `while` (Bucle Condicional)

Se ejecuta mientras una condición booleana sea verdadera. Es propenso a bucles infinitos si no se altera la variable de control dentro del bloque. Ideal para validaciones de datos de entrada.

### `for` (Bucle Iterativo)

Itera sobre una secuencia (una lista, una tupla, un diccionario o un rango numérico generado por `range()`).

```python
# 1. Ejemplo de validación con 'while' (Garantiza que el dato sea correcto)
edad = int(input("Ingrese su edad (debe ser entre 18 y 100 años): "))
while edad < 18 or edad > 100:
    print("Error: Edad fuera del rango permitido.")
    edad = int(input("Por favor, reingrese una edad válida: "))

print(f"Edad registrada exitosamente: {edad}")

print("-" * 30)

# 2. Ejemplo de procesamiento con 'for' y acumuladores
print("Listado de números pares en un rango definido:")
suma_pares = 0
# range(inicio, fin_exclusivo, paso)
for numero in range(2, 11, 2):
    print(f"-> Número par detectado: {numero}")
    suma_pares += numero  # Acumulador

print(f"La sumatoria total de los números pares impresos es: {suma_pares}")

```

---

## 🔹 Unidad 4: Trabajo Colaborativo (Git & GitHub)

El control de versiones es el pilar del desarrollo profesional. Permite registrar el historial de cambios, volver atrás en el tiempo y fusionar código desarrollado en equipo.

### Flujo de Trabajo Esencial (Git Workflow)

1. **Directorio de Trabajo (Working Directory):** Archivos modificados en tu PC que aún no guardaste en el historial.
2. **Área de Preparación (Staging Area):** Zona temporal donde seleccionás los cambios que van a formar parte de tu próxima "foto".
3. **Repositorio Local (.git):** El historial definitivo guardado localmente en tu máquina.
4. **Repositorio Remoto (GitHub):** Servidor en la nube para respaldar y compartir el código.

### Comandos Críticos de Consola

* `git init`: Inicializa un repositorio Git local en la carpeta actual.
* `git status`: Diagnóstica qué archivos fueron modificados, cuáles están en el Staging y cuáles no están siendo rastreados.
* `git add <archivo>` (o `git add .` para todo): Mueve los cambios del directorio de trabajo al Staging Area.
* `git commit -m "Mensaje descriptivo"`: Guarda de forma permanente los cambios que estaban en el Staging Area en el historial local.
* `git remote add origin <URL>`: Vincula tu repositorio local con el repositorio remoto en GitHub.
* `git push -u origin main`: Sube tus commits locales a la rama principal de GitHub.

---

## 🔹 Unidad 5: Listas

Las listas en Python son colecciones secuenciales de elementos, **ordenadas** (mantienen el índice posicional comenzando en `0`) y **mutables** (pueden cambiar, agregarse o borrarse elementos en tiempo de ejecución).

### Métodos de Manipulación Estructurada

```python
# Inicialización de una lista de lenguajes
lenguajes = ["Python", "C", "C++"]

# Agregar elementos
lenguajes.append("Java")          # Inserta al final: ['Python', 'C', 'C++', 'Java']
lenguajes.insert(1, "JavaScript") # Inserta en índice 1: ['Python', 'JavaScript', 'C', 'C++', 'Java']

# Modificación directa por índice
lenguajes[2] = "C lúdico"

# Eliminación de elementos
lenguajes.remove("C++")           # Busca el valor exacto y lo elimina. Lanza error si no existe.
elemento_eliminado = lenguajes.pop(0) # Elimina por índice y retorna el valor (remueve 'Python')

print(f"Lista final: {lenguajes}")
print(f"Elemento extraído con pop(0): {elemento_eliminado}")

# Recorrido avanzado de listas obteniendo índice y valor simultáneamente
for indice, lenguaje in enumerate(lenguajes):
    print(f"Índice {indice}: {lenguaje}")

```

---

## 🔹 Unidad 6: Funciones y Modularización

Una función es un bloque de código organizado y reutilizable que se invoca para realizar una única tarea específica. Sigue el principio arquitectónico de **alta cohesión y bajo acoplamiento**.

### Conceptos Clave

* **Parámetros:** Variables declaradas en la definición de la función.
* **Argumentos:** Los valores reales que se le pasan a la función cuando se la invoca.
* **Ámbito de las Variables (Scope):** Las variables definidas dentro de una función son de alcance **local**. No existen en el programa principal a menos que se devuelvan explícitamente mediante un `return`.

```python
def calcular_impuesto_tecnologico(precio_base, tasa_porcentaje=21):
    """
    Docstring: Calcula el costo de un impuesto tecnológico.
    Tiene un parámetro por defecto (tasa_porcentaje = 21).
    """
    if precio_base <= 0:
        return 0.0 # El return interrumpe la ejecución inmediatamente
    
    monto_impuesto = precio_base * (tasa_porcentaje / 100)
    precio_final = precio_base + monto_impuesto
    return precio_final

# Invocación pasando argumentos posicionales y por palabra clave (keyword arguments)
computadora_precio = 150000
total_a_pagar = calcular_impuesto_tecnologico(computadora_precio)
total_con_tasa_especial = calcular_impuesto_tecnologico(computadora_precio, tasa_porcentaje=35)

print(f"Costo estándar: ${total_a_pagar}")
print(f"Costo tasa especial: ${total_con_tasa_especial}")

```

---

## 🔹 Unidad 7: Datos Complejos

Python provee estructuras avanzadas nativas optimizadas para diferentes necesidades de almacenamiento y velocidad algorítmica.

### Tuplas (`tuple`)

Colecciones ordenadas pero **inmutables**. Una vez creadas, no pueden modificarse, agregarse ni eliminarse sus elementos. Son seguras para datos constantes (coordenadas, configuraciones).

```python
coordenadas_utn = (-34.6181, -58.4201)

```

### Diccionarios (`dict`)

Estructuras indexadas por **pares Clave-Valor**. Las claves deben ser únicas e inmutables (como cadenas o enteros). No tienen un orden posicional, pero su velocidad de búsqueda es extremadamente rápida (complejidad constante en términos informáticos).

```python
# Estructura compleja combinando diccionarios y listas
profesor = {
    "nombre": "Alejandro",
    "catedra": "Programación I",
    "comisiones": [101, 102, 103],
    "activo": True
}
# Acceso y modificación
profesor["comisiones"].append(104)
print(f"Comisiones del profesor: {profesor['comisiones']}")

```

### Conjuntos (`set`)

Colecciones de elementos **únicos** y **no ordenados**. No permiten duplicados. Son ideales para operaciones matemáticas de conjuntos (uniones, intersecciones) y para limpiar duplicados de una lista.

```python
numeros_duplicados = [1, 2, 2, 3, 4, 4, 4, 5]
numeros_unicos = list(set(numeros_duplicados)) # Resultado: [1, 2, 3, 4, 5]

```

---

## 🔹 Unidad 8: Manejo de Errores y Excepciones

Los errores en un programa se dividen en errores de sintaxis (detectados antes de ejecutar) y errores en tiempo de ejecución (excepciones). El manejo de excepciones intercepta estos eventos para evitar que el software se interrumpa abruptamente.

### Estructura Completa `try / except / else / finally`

```python
try:
    # Código propenso a fallar
    dividendo = int(input("Ingrese el numerador: "))
    divisor = int(input("Ingrese el denominador: "))
    resultado = dividendo / divisor
except ValueError:
    print("Error Crítico: Debe ingresar estrictamente números enteros.")
except ZeroDivisionError:
    print("Error Crítico: La división por cero es indeterminada en matemáticas.")
except Exception as e:
    print(f"Ocurrió un error inesperado no contemplado: {e}")
else:
    # Se ejecuta SOLO si el bloque try no arrojó ninguna excepción
    print(f"Operación exitosa. El resultado es: {resultado}")
finally:
    # Se ejecuta SIEMPRE, haya o no haya error. Ideal para liberar recursos del sistema.
    print("Cierre de la operación de cálculo.")

```

---

## 🔹 Unidad 9: Manejo de Archivos

La persistencia de datos permite guardar el estado de una aplicación en el disco duro para que no se pierda al apagar la computadora o cerrar el programa.

### Modos Fundamentales de Apertura

* `'r'`: Lectura (Read). El archivo debe existir, de lo contrario lanza `FileNotFoundError`.
* `'w'`: Escritura (Write). Crea el archivo si no existe. Si ya existe, **borra todo su contenido** antes de escribir.
* `'a'`: Anexo (Append). Abre el archivo para agregar datos al final sin destruir lo existente.

### Uso de Context Managers (`with`)

Es la norma profesional en Python. Asegura que el archivo se cierre correctamente y libere los descriptores de archivos del sistema operativo, incluso si el programa falla en medio de la lectura o escritura.

```python
# 1. Escritura segura de un archivo de texto lineal
lista_alumnos = ["Mariano Kastelic", "Ana Pérez", "Juan Gómez"]

with open("estudiantes_prog1.txt", "w", encoding="utf-8") as archivo:
    for alumno in lista_alumnos:
        archivo.write(f"{alumno}\n") # Escribe cada nombre con un salto de línea

print("Archivo guardado con éxito.")

print("-" * 30)

# 2. Lectura y procesamiento línea por línea
print("Leyendo base de datos de alumnos:")
try:
    with open("estudiantes_prog1.txt", "r", encoding="utf-8") as archivo:
        for nro_linea, linea in enumerate(archivo, 1):
            # .strip() remueve los espacios en blanco y saltos de línea '\n' de los extremos
            print(f"Registro N° {nro_linea}: {linea.strip()}")
except FileNotFoundError:
    print("El archivo solicitado no se encuentra en el directorio.")

```

---

## 🔹 Unidad 10: Recursividad y Algoritmos Básicos

Esta unidad une la lógica abstracta avanzada con la optimización de algoritmos de procesamiento de datos.

### Recursividad

Técnica de programación donde una función se invoca a sí misma para resolver una versión más pequeña del problema original. Para evitar un desborde de memoria (*Stack Overflow*), requiere dos componentes obligatorios:

1. **Caso Base:** La condición de salida que detiene las llamadas recursivas.
2. **Caso Recursivo:** La llamada a la función pasando un subproblema modificado que se acerque progresivamente al caso base.

```python
def cuenta_regresiva_recursiva(numero):
    if numero == 0: # Caso Base
        print("🚀 ¡Despegue!")
    else:           # Caso Recursivo
        print(f"Tiempo restante: {numero}...")
        cuenta_regresiva_recursiva(numero - 1)

cuenta_regresiva_recursiva(3)

```

### Algoritmo de Ordenamiento: Burbuja (*Bubble Sort*)

Compara pares de elementos adyacentes en una lista y los intercambia si están en el orden incorrecto. Repite este proceso recorriendo la lista múltiples veces hasta que no se requieran más intercambios.

```python
def ordenar_burbuja(lista):
    n = len(lista)
    # Bucle externo recorre toda la lista
    for i in range(n):
        # Bucle interno hace las comparaciones adyacentes (los últimos i elementos ya están ordenados)
        for j in range(0, n - i - 1):
            if lista[j] > lista[j + 1]:
                # Intercambio posicional nativo en Python (Swapping)
                lista[j], lista[j + 1] = lista[j + 1], lista[j]
    return lista

datos = [64, 34, 25, 12, 22, 11, 90]
print(f"Lista ordenada por Burbuja: {ordenar_burbuja(datos)}")

```

### Algoritmos de Búsqueda

#### Búsqueda Secuencial

Revisa los elementos de la lista uno por uno de principio a fin. Funciona en listas desordenadas, pero es ineficiente en colecciones masivas.

#### Búsqueda Binaria

Algoritmo de alta velocidad. Divide repetidamente a la mitad el espacio de búsqueda donde podría estar el elemento. **Es requisito obligatorio e indispensable que la lista esté estrictamente ordenada.**

```python
def busqueda_binaria(lista_ordenada, elemento_buscado):
    izquierda = 0
    derecha = len(lista_ordenada) - 1

    while izquierda <= derecha:
        medio = (izquierda + derecha) // 2
        
        # Caso de éxito
        if lista_ordenada[medio] == elemento_buscado:
            return medio # Retorna el índice donde se encontró
        
        # Si el elemento es menor, descarto la mitad derecha
        elif lista_ordenada[medio] > elemento_buscado:
            derecha = medio - 1
        
        # Si el elemento es mayor, descarto la mitad izquierda
        else:
            izquierda = medio + 1
            
    return -1 # Retorna -1 si el elemento no existe en la lista

lista_test = [11, 12, 22, 25, 34, 64, 90] # Lista ordenada previamente
posicion = busqueda_binaria(lista_test, 25)
print(f"El elemento 25 se encuentra en el índice: {posicion}")

```
