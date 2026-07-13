
```markdown
# 🪓 Machete de Sintaxis Rápida - Python

La hoja de trucos definitiva para copiar y pegar estructuras comunes de código. Sin vueltas.

---

## 🕒 1. Entrada, Salida y Conversiones (Casting)
```python
# Leer texto
texto = input("Texto: ")

# Leer números enteros y flotantes
entero = int(input("Entero: "))
flotante = float(input("Decimal: "))

# Mostrar con formato rápido (f-strings)
print(f"Texto: {texto} | Número: {entero} | Decimal con 2 dígitos: {flotante:.2f}")

```

---

## 🛣️ 2. Condicionales (`if-elif-else`)

```python
if condicion_1:
    # Código si se cumple 1
elif condicion_2:
    # Código si se cumple 2 (Opcional, podés meter los que quieras)
else:
    # Código si no se cumple ninguna de las anteriores (Opcional)

```

**Operadores Lógicos:** `and` (Y), `or` (O), `not` (Negación).

**Operadores de Comparación:** `==` (Igual), `!=` (Distinto), `>`, `<`, `>=`, `<=`.

---

## 🔄 3. Bucles y Repeticiones

### Bucle `while` (Por condición/Validación)

```python
# Validar que un dato sea correcto
dato = int(input("Ingrese número positivo: "))
while dato <= 0:
    print("Error.")
    dato = int(input("Reingrese: "))

```

### Bucle `for` (Por rangos o colecciones)

```python
# range(inicio, fin_exclusivo, paso)
for i in range(0, 10, 2): 
    print(i) # Imprime de 0 a 8 yendo de 2 en 2

# Recorrer un string o lista directamente
for elemento in coleccion:
    print(elemento)

```

---

## 📊 4. Listas (Estructura Mutable)

```python
lista = ["a", "b", "c"]

lista.append("d")        # Agrega al final -> ['a', 'b', 'c', 'd']
lista.insert(1, "x")     # Inserta en índice 1 -> ['a', 'x', 'b', 'c', 'd']
lista.remove("b")        # Borra por valor exacto
elemento = lista.pop(0)  # Borra por índice y lo guarda en la variable (remueve 'a')
largo = len(lista)       # Cuántos elementos tiene la lista

# Recorrer obteniendo el índice y el valor al mismo tiempo
for idx, val in enumerate(lista):
    print(f"En el índice {idx} está el valor {val}")

```

---

## 🧩 5. Funciones (Bloques reutilizables)

```python
def mi_funcion(parametro1, parametro2="Por defecto"):
    # Tu lógica acá
    resultado = parametro1 + 2
    return resultado # Devuelve el valor al programa principal

# Invocación
salida = mi_funcion(10)

```

---

## 🗃️ 6. Estructuras Complejas (Tuplas, Diccionarios, Sets)

### Tuplas (Inmutables - No cambian)

```python
mi_tuple = (10, 20, 30)
x = mi_tuple[0] # Lectura directa

```

### Diccionarios (Clave-Valor)

```python
# Declaración
usuario = {"id": 123, "nombre": "Mariano", "rol": "Admin"}

# Acceso y Modificación
usuario["nombre"] = "Mariano K." # Cambia el valor
usuario["edad"] = 43             # Agrega una clave nueva si no existía

# Recorrer claves y valores juntos
for clave, valor in usuario.items():
    print(f"{clave} -> {valor}")

```

### Sets / Conjuntos (Valores únicos sin orden)

```python
mi_set = {1, 2, 3, 3, 3} # Guarda solo {1, 2, 3}

```

---

## 🛡️ 7. Manejo de Errores (`try-except`)

```python
try:
    numero = int(input("Número: "))
    calculo = 10 / numero
except ValueError:
    print("No ingresaste un número válido.")
except ZeroDivisionError:
    print("No se puede dividir por cero.")
except Exception as e:
    print(f"Error inesperado: {e}")

```

---

## 📁 8. Archivos Planos (`with open`)

```python
# ESCRITURA ('w' borra todo, 'a' agrega al final)
with open("datos.txt", "w", encoding="utf-8") as file:
    file.write("Línea de texto\n")

# LECTURA LÍNEA POR LÍNEA
with open("datos.txt", "r", encoding="utf-8") as file:
    for linea in file:
        print(linea.strip()) # .strip() saca el salto de línea oculto

```

---

## 🧬 9. Algoritmos Obligatorios (Burbuja y Búsqueda Binaria)

### Ordenamiento Burbuja

```python
def ordenar_burbuja(lista):
    n = len(lista)
    for i in range(n):
        for j in range(0, n - i - 1):
            if lista[j] > lista[j + 1]:
                lista[j], lista[j + 1] = lista[j + 1], lista[j] # Intercambio
    return lista

```

### Búsqueda Binaria (Requiere lista previamente ordenada)

```python
def busqueda_binaria(lista, buscado):
    izq, der = 0, len(lista) - 1
    while izq <= der:
        medio = (izq + der) // 2
        if lista[medio] == buscado:
            return medio # Devuelve el índice encontrado
        elif lista[medio] > buscado:
            der = medio - 1
        else:
            izq = medio + 1
    return -1 # No encontrado

```