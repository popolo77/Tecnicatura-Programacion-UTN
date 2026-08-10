# 📚 Módulo 1: Introducción a Java

Este módulo abarca los fundamentos de la plataforma Java, la configuración del entorno de desarrollo, la sintaxis básica del lenguaje, el manejo de datos en memoria, los operadores aritméticos/lógicos y las herramientas esenciales de depuración y lectura de datos.

---

## 1. ⚙️ Entorno de Desarrollo y Arquitectura de Java

Java es un lenguaje compilado e interpretado bajo el principio *"Write Once, Run Anywhere"* (Escribe una vez, ejecútalo en cualquier lugar).

### Componentes Clave de la Plataforma
* **JDK (Java Development Kit):** Es el kit de desarrollo completo. Contiene el compilador (`javac`), las librerías estándar y la plataforma de ejecución (`JRE`). Es indispensable para escribir y compilar programas.
* **JRE (Java Runtime Environment):** Es el entorno necesario únicamente para ejecutar aplicaciones Java precompiladas. Contiene la JVM y las bibliotecas de tiempo de ejecución.
* **JVM (Java Virtual Machine):** Máquina virtual que ejecuta el **Bytecode** (`.class`). Traduce el código intermedio a instrucciones de máquina según el sistema operativo hospedador.
* **Bytecode:** Código de bajo nivel independiente de la plataforma generado por el compilador de Java.

### Flujo de Compilación
```text
[Código Fuente .java] -> (Compilador javac) -> [Bytecode .class] -> (JVM) -> [Código Máquina]

```

### Gestión de Proyectos en NetBeans

* **Creación de proyectos:** File → New Project → Java Application.
* **Exportar entrega:** File → Export Project → To ZIP.
* **Importar proyecto:** File → Import Project → From ZIP *(nunca descomprimir manualmente antes de importar)*.

---

## 2. 🏗️ Estructura Básica de un Programa en Java

En Java, todo código debe residir dentro de una clase, y el punto de entrada principal para la ejecución es el método `main`.

### Estructura Jerárquica

1. **Paquete (`package`):** Ubicación lógica de la clase dentro del proyecto.
2. **Importaciones (`import`):** Clases externas necesarias (ej. `import java.util.Scanner;`).
3. **Clase (`public class`):** Debe coincidir exactamente con el nombre del archivo `.java`.
4. **Método Principal (`main`):** `public static void main(String[] args)`.

### Ejemplo de Estructura

```java
package com.utn.modulo1;

import java.util.Scanner;

public class MiPrograma {
    public static void main(String[] args) {
        System.out.println("¡Hola, Programación II!");
    }
}

```

### Convención de Nombres

* **Clases:** `PascalCase` (ejemplo: `GestionClientes`, `Ejercicio_01`).
* **Variables y Métodos:** `camelCase` (ejemplo: `edadUsuario`, `calcularPromedio()`).
* **Paquetes:** Todo en minúsculas (ejemplo: `com.utn.modelo`).
* **Constantes:** `SNAKE_CASE_UPPER` (ejemplo: `VALOR_MAXIMO`, `IMPUESTO_IVA`).

---

## 3. 🧠 Memoria, Variables y Tipos de Datos

Java es un lenguaje de **tipado estático y fuerte**: toda variable debe declarar su tipo antes de ser utilizada. Se gestiona en dos áreas de memoria: **Stack** y **Heap**.

### A. Tipos Primitivos (Stack)

Almacenan directamente el valor asignado dentro de la memoria Stack.

* **byte:** Entero de 8 bits (rango: -128 a 127).
* **short:** Entero de 16 bits (rango: -32,768 a 32,767).
* **int:** Entero de 32 bits (estándar por defecto).
* **long:** Entero de 64 bits (requiere sufijo `L`, ej: `5000000000L`).
* **float:** Decimal de 32 bits (requiere sufijo `f`, ej: `3.14f`).
* **double:** Decimal de 64 bits (estándar por defecto para decimales).
* **char:** Carácter Unicode de 16 bits (delimitado por comillas simples `'A'`).
* **boolean:** Valor lógico de 1 bit (`true` o `false`).

### B. Tipos de Referencia / Objetos (Heap)

Las variables almacenan en el Stack una dirección de memoria (referencia) que apunta al objeto real ubicado en el Heap.

* **String:** Cadena de texto inmutable delimitada por comillas dobles (`"Texto"`).
* **Objetos y Arreglos:** Instancias creadas con la palabra reservada `new`.

### C. Declaración, Inicialización y Constantes

* **Declaración:** Reserve de espacio en memoria (`int edad;`).
* **Inicialización:** Primera asignación de valor (`edad = 25;`).
* **Constantes (`final`):** Asignación inmutable (`final double PI = 3.14159;`).

---

## 4. ⚖️ Operadores y Precedencia Matemática

### Operadores

* **Aritméticos:** `+`, `-`, `*`, `/`, `%` (módulo o resto).
* **Relacionales:** `==`, `!=`, `>`, `<`, `>=`, `<=` (devuelven `boolean`).
* **Lógicos:** `&&` (AND), `||` (OR), `!` (NOT).
* **Incremento / Decremento:** `++`, `--`

### Orden de Precedencia (Prioridad de Ejecución)

1. Paréntesis: `()`
2. Incremento / Decremento: `++`, `--`
3. Multiplicación, División y Módulo: `*`, `/`, `%`
4. Suma y Resta: `+`, `-`
5. Operadores Relacionales e Igualdad: `>`, `<`, `==`, `!=`
6. Operadores Lógicos: `&&`, `||`
7. Asignación: `=`, `+=`, `-=`, `*=`, `/=`

### Conversión de Tipos (Casting)

* **Conversión Implícita (Promoción):** Automática de un tipo menor a uno mayor sin pérdida de datos (ej. `int` a `double`).
* **Conversión Explícita (Casting):** Forzada mediante `(tipo)` cuando se pasa de un rango mayor a menor (ej. `int precio = (int) 99.99;`).

---

## 5. 📥 Entradas/Salidas y Estándar de Cátedra (`Scanner`)

### Salida por Consola

* `System.out.println()`: Imprime y realiza salto de línea.
* `System.out.print()`: Imprime sin salto de línea.
* `System.out.printf()`: Salida formateada (`%d` enteros, `%f` flotantes, `%s` cadenas).

### Estándar Obligatorio para `Scanner`

Para evitar el error del **"Salto de Línea Fantasma"** (que ocurre al combinar `nextInt()` o `nextDouble()` con `nextLine()`), la cátedra establece como norma estricta:

> **Regla de Cátedra:** Leer **SIEMPRE** con `sc.nextLine()` y realizar el parseo manual a los tipos numéricos requeridos.

### Métodos de Parseo

* **int:** `Integer.parseInt(sc.nextLine())`
* **double:** `Double.parseDouble(sc.nextLine())`
* **long:** `Long.parseLong(sc.nextLine())`
* **boolean:** `Boolean.parseBoolean(sc.nextLine())`

---

## 6. 🔍 Depuración de Código (Debugging)

Proceso sistemático para identificar, aislar y corregir errores lógicos o de ejecución.

### Clasificación de Errores

1. **Errores de Compilación (Sintaxis):** Detectados por el IDE/compilador antes de ejecutar (falta de `;`, nombres mal escritos).
2. **Errores de Ejecución (Runtime):** Ocurren en tiempo de ejecución interrumpiendo el programa (`ArithmeticException`, `NullPointerException`).
3. **Errores Lógicos:** El programa compila y ejecuta sin fallas, pero produce resultados incorrectos por lógica defectuosa.

### Herramientas de Depuración en NetBeans

* **Breakpoint (Punto de Interrupción):** Marca en el margen izquierdo donde la ejecución se pausa.
* **Step Over (F8):** Ejecuta la línea actual y pasa a la siguiente.
* **Step Into (F7):** Entra dentro del método de la línea actual.
* **Step Out (Ctrl+F7):** Sale del método actual y vuelve al llamador.
* **Watch / Variables:** Panel de inspección de variables en tiempo real.
* **Prueba de Escritorio:** Simulación manual en papel leyendo línea por línea y registrando el valor de cada variable en una tabla.

```

```