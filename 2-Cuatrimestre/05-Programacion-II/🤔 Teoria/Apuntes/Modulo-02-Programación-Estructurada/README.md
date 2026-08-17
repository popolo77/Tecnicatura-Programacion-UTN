# 📚 Módulo 2: Programación Estructurada

Este módulo aborda los fundamentos del **Paradigma Estructurado en Java**, el control de flujo algorítmico mediante **estructuras condicionales** y **estructuras de repetición (bucles)**, modularización mediante **funciones y métodos**, **ámbito de variables (scope)**, **recursividad**, técnicas de **programación defensiva** y **depuración (debugging)**.

---

## 1. 🏛️ Teorema del Programa Estructurado (Böhm y Jacopini)

Demostrado matemáticamente en los años 60 por Corrado Böhm y Giuseppe Jacopini[cite: 1252], este teorema establece que **cualquier algoritmo computable** puede desarrollarse combinando únicamente tres construcciones lógicas fundamentales, eliminando la necesidad de saltos incondicionales (`goto`):


```

```
                   ESTRUCTURAS FUNDAMENTALES
                               │
     ┌─────────────────────────┼─────────────────────────┐
     ▼                         ▼                         ▼

```

1. SECUENCIA              2. SELECCIÓN              3. ITERACIÓN
(Paso a paso lineal)      (if, else, switch)       (for, while, do-while)

```

1. **Secuencia:** Ejecución consecutiva y lineal de instrucciones en el orden en que están escritas.
2. **Selección (Bifurcación):** Toma de decisiones que deriva el flujo de ejecución por diferentes caminos según el resultado de una condición booleana (`if`, `else`, `switch`)[cite: 973, 1029].
3. **Iteración (Repetición):** Ejecución reiterada de un bloque de código mientras se cumpla una condición lógica predeterminada (`while`, `do-while`, `for`).

---

## 2. ⚖️ Operadores Relacionales y Lógicos

### A. Operadores Relacionales (Comparación)
Comparan dos operandos y devuelven siempre un valor de verdad de tipo `boolean` (`true` o `false`)[cite: 975]:

| Operador | Descripción | Ejemplo | Resultado |
| :---: | :--- | :---: | :---: |
| `==` | Igual a | `5 == 5` | `true` [cite: 976] |
| `!=` | Distinto de | `5 != 3` | `true` [cite: 976] |
| `>` | Mayor que | `7 > 2` | `true` [cite: 976] |
| `<` | Menor que | `4 < 6` | `true` [cite: 976] |
| `>=` | Mayor o igual que *(sin espacios intermedios)* [cite: 1084] | `5 >= 5` | `true` [cite: 976] |
| `<=` | Menor o igual que *(sin espacios intermedios)* [cite: 1084] | `3 <= 8` | `true` [cite: 976] |

> ⚠️ **Regla Crítica con `String`:** El operador `==` en objetos compara **posiciones de memoria (referencias)** y no el texto real[cite: 979, 982]. Para comparar el contenido de dos cadenas se debe utilizar siempre `.equals()` o `.equalsIgnoreCase()`[cite: 979, 982]:
> ```java
> String nombre1 = "Juan";
> String nombre2 = "Juan";
> System.out.println(nombre1 == nombre2);        // Puede ser true o false (compara referencias)
> System.out.println(nombre1.equals(nombre2)); // Siempre true (compara contenido real)
> ```
[cite: 980, 981, 982]

### B. Operadores Lógicos (Combinación Booleana)
Permiten conectar y evaluar múltiples condiciones simultáneamente[cite: 984]:

* **`&&` (AND Lógico):** Retorna `true` solo si **ambas** expresiones son verdaderas[cite: 985]. Posee *evaluación de cortocircuito* (si la primera condición es falsa, descarta evaluar el resto).
* **`||` (OR Lógico):** Retorna `true` si **al menos una** de las expresiones evaluadas es verdadera[cite: 985]. También aplica *cortocircuito* (si la primera es verdadera, no evalúa la segunda).
* **`!` (NOT / Negación):** Invierte el valor de verdad de la expresión[cite: 985].

```java
int edad = 20;
boolean tieneEntrada = true;

if (edad >= 18 && tieneEntrada) {
    System.out.println("Puede ingresar al evento.");
} else {
    System.out.println("No puede ingresar.");
}

```

---

## 3. 🔀 Estructuras de Control Condicional

### 1. Condicional `if` / `else if` / `else`

Evalúa expresiones booleanas secuenciales de arriba hacia abajo para tomar decisiones mutuamente excluyentes:

```java
int nota = 75;

if (nota >= 90) {
    System.out.println("Excelente");
} else if (nota >= 60) {
    System.out.println("Aprobado");
} else {
    System.out.println("Desaprobado");
}

```

### 2. Operador Ternario (`? :`)

Alternativa compacta en una sola línea para asignaciones condicionales simples:

```java
// Sintaxis: condición ? valor_si_true : valor_si_false;
int numero = 8;
String resultado = (numero % 2 == 0) ? "Par" : "Impar";
System.out.println(resultado); // "Par"

```

### 3. Estructura `switch` (Clásico vs. Rule Switch)

Especialmente útil cuando una misma variable puede tomar múltiples valores fijos discretos (`int`, `char`, `String`, etc.):

* **Switch Tradicional:** Requiere la instrucción `break` para evitar la caída en cascada (*fall-through*) hacia los casos siguientes:


```java
int dia = 3;
switch (dia) {
    case 1:
        System.out.println("Lunes");
        break;
    case 2:
        System.out.println("Martes");
        break;
    case 3:
        System.out.println("Miércoles");
        break;
    default:
        System.out.println("Día no válido");
}

```



* **Rule Switch (Java 12+ / Sintaxis con Flecha `->`):** Más conciso, elimina el riesgo de olvidar un `break`:


```java
switch (dia) {
    case 1 -> System.out.println("Lunes");
    case 2 -> System.out.println("Martes");
    case 3 -> System.out.println("Miércoles");
    default -> System.out.println("Día no válido");
}

```




---

## 4. 🔁 Estructuras de Repetición (Bucles)

| Estructura | Evaluación de Condición | Ejecuciones Mínimas | Uso Principal Recomendado |
| --- | --- | --- | --- |
| **`while`** | **Al inicio** (Pre-prueba) | 0 veces | Cuando **no** se conoce de antemano cuántas veces se repetirá el ciclo o para validación de datos por centinela. |
| **`do-while`** | **Al final** (Post-prueba) | 1 vez garantizada | Menús de opciones y validaciones donde el usuario debe interactuar al menos una vez. |
| **`for`** | **Al inicio** (Por contador) | 0 veces | Cuando **se conoce la cantidad exacta de iteraciones** o recorridos secuenciales. |

### A. Bucle `while` (Control por condición)

```java
int contador = 1;
while (contador <= 5) {
    System.out.println("Número: " + contador);
    contador++; // Modificación del estado para evitar bucle infinito
}

```

### B. Bucle `do-while` (Garantía de primera ejecución)

```java
int numero = 0;
do {
    System.out.println("Número: " + numero);
    numero++;
} while (numero < 3); // Imprime 0, 1, 2

```

### C. Bucle `for` (Control por contador)

```java
// for (inicialización; condición_de_corte; incremento_o_decremento)
for (int i = 1; i <= 5; i++) {
    System.out.println("Número: " + i);
}

```

---

## 5. 🧮 Mecánicas Clave en Iteraciones

### Contadores vs. Acumuladores

* **Contador:** Variable entera que se modifica en una cantidad **constante** (generalmente `+1` o `-1`) para contar repeticiones o eventos.
* **Acumulador:** Variable numérica que acumula cantidades **variables** en cada iteración mediante sumas o restas sucesivas (`suma += valor`).

```java
int suma = 0;     // Acumulador
int contador = 0; // Contador

for (int i = 1; i <= 5; i++) {
    suma += i;
    contador++;
}
System.out.println("Suma total: " + suma);       // 15
System.out.println("Total números: " + contador); // 5

```

### Control Interno: `break` vs. `continue`

* **`break`:** Corta y finaliza de inmediato la ejecución del bucle, pasando el control a la primera instrucción fuera del ciclo.
* **`continue`:** Interrumpe únicamente la iteración actual y salta de inmediato a la siguiente evaluación/incremento del ciclo.

---

## 6. 🔲 Ciclos Anidados y Pensamiento Matricial

Un ciclo anidado es un bucle dentro de otro bucle. Constituye la base para el recorrido de filas y columnas (espacios bidimensionales, tablas, grillas y matrices).

### Analogía del Reloj

Por cada avance de **1 unidad** en el ciclo externo (la aguja de las horas / variable `i`), el ciclo interno (el minutero / variable `j`) debe **completar todas sus vueltas desde el inicio hasta el final**.

```java
// Generación de tablas de multiplicar (Filas y Columnas)
for (int i = 1; i <= 3; i++) {
    for (int j = 1; j <= 3; j++) {
        System.out.println(i + " x " + j + " = " + (i * j));
    }
}

```

---

## 7. 🧩 Funciones, Métodos y Modularización

### Principio "Divide y Vencerás"

Consiste en descomponer un problema complejo en subproblemas más pequeños, manejables e independientes mediante funciones o métodos reutilizables.

### Anatomía de un Método Estático en Java

```java
public static int sumar(int a, int b) {
    int resultado = a + b;
    return resultado; // Retorna un valor compatible con el tipo declarado
}

```

* **`public static`:** Modificadores de acceso y contexto. `static` permite invocar el método directamente sin instanciar la clase contenedora.
* **Tipo de retorno:** Tipo de dato devuelto por la función (`int`, `double`, `String`, `boolean`). Si no retorna ningún dato, se utiliza `void` (procedimiento).
* **Parámetros:** Variables locales que reciben los valores enviados como argumentos al invocar la función.

### Paso de Parámetros por Valor en Java

En Java, **todos los parámetros se pasan estrictamente por valor**:

* **Tipos Primitivos:** Se envía una copia exacta del dato. Las modificaciones que sufra la variable dentro del método no alteran a la variable original externa.
* **Tipos Referencia (Objetos y Arreglos):** Se envía una copia de la referencia (puntero de memoria). Las modificaciones en el contenido del objeto se reflejan externamente, pero reasignar la variable dentro del método no cambia el puntero original.

### Ámbito de Variables (Scope)

El alcance o ciclo de vida de una variable está delimitado estrictamente por el bloque de llaves `{}` donde fue declarada. Al finalizar la ejecución del bloque, la variable se destruye y se libera de la memoria Stack.

---

## 8. 🔄 Recursividad

### Definición y Pilares Fundamentales

Técnica algorítmica donde un método se invoca a sí mismo para resolver una instancia más simple del mismo problema.

Toda función recursiva debe contar obligatoriamente con dos elementos:

1. **Caso Base (Condición de corte):** Condición terminal que devuelve un valor directo sin realizar auto-llamadas. Previene la recursión infinita.
2. **Caso Recursivo (Paso inductivo):** Invocación al mismo método con parámetros que reducen el tamaño del problema acercándolo progresivamente al caso base.

### La Pila de Llamadas (*Call Stack*) y `StackOverflowError`

Cada llamada recursiva reserva un marco (*stack frame*) en la memoria Stack. Si el caso base no se alcanza o el número de llamadas recursivas excede la memoria disponible, Java lanza la excepción crítica `java.lang.StackOverflowError`.

```java
// Factorial de un número entero positivo: n! = n * (n - 1)!
public static int factorial(int n) {
    // 1. Caso Base
    if (n <= 1) {
        return 1;
    }
    // 2. Caso Recursivo
    return n * factorial(n - 1);
}

```

---

## 9. 🛡️ Errores Críticos y Programación Defensiva

```
                          ERRORES COMUNES EN JAVA
                                     │
         ┌───────────────────────────┼───────────────────────────┐
         ▼                           ▼                           ▼
1. SINTAXIS SEPARADA        2. ASIGNACIÓN EN IF         3. CRASH EN TIEMPO
 (Ej: > = o < =)              (Ej: if (a = true))          DE EJECUCIÓN
  Falla en compilación         Compila con bug lógico      (División por cero)

```

### 1. El Error del Espacio en Operadores Compuestos

* **Incorrecto:** `if (a > = b)` ❌ *(El compilador lee dos tokens separados e impide compilar)*.


* **Correcto:** `if (a >= b)` ✔️ *(Debe escribirse como un token único e indivisible)*.



### 2. El Bug Silencioso: Asignación (`=`) vs. Comparación (`==`)

* **Peligro:** Escribir `if (activo = true)` asigna el valor en lugar de comparar. En tipos booleanos, compila sin advertencias pero **fuerza la condición a ser siempre verdadera**, generando un fallo lógico crítico en el sistema.


* **Forma Segura:** Usar `if (activo == true)` o directamente `if (activo)`.



### 3. Programación Defensiva: Prevención de División por Cero

Una división entre enteros por cero no es detectada al compilar, pero causa el colapso (*crash*) inmediato del programa al lanzar una excepción `ArithmeticException`.

```java
int numerador = 10;
int divisor = 0;

// Validación previa con programación defensiva
if (divisor != 0) {
    int resultado = numerador / divisor;
    System.out.println("Resultado: " + resultado);
} else {
    System.out.println("Error: División por cero no permitida.");
}

```

---

## 10. 🔍 Técnicas de Auditoría y Debugging

* **Prueba de Escritorio (Traza Manual):** Tabla manual donde se audita línea por línea la evolución de las variables a medida que avanzan las iteraciones de un ciclo o llamadas recursivas.
* **Breakpoint (Punto de Interrupción):** Marca colocada en el IDE para pausar la ejecución del programa y evaluar el estado de la memoria en tiempo real.
* **Step Over (`F8`):** Ejecuta la línea seleccionada en cámara lenta y avanza a la siguiente instrucción sin ingresar a métodos secundarios.

