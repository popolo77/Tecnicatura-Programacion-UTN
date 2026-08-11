# 💻 Práctica Módulo 1: Introducción a Java

Este repositorio contiene la resolución completa de la guía de trabajos prácticos correspondiente al **Módulo 1** de Programación II (UTN). Todos los ejercicios están implementados bajo los estándares de desarrollo exigidos por la cátedra (uso de `Scanner` con `nextLine()` y parseo manual).

---

## 📌 Lista de Ejercicios

### 🔹 Ejercicio 01: Hola Mundo
* **Consigna:** Crear un programa básico que imprima por consola el mensaje de bienvenida `"¡Hola, Mundo!"`.
* **Conceptos clave:** Estructura de clase, método `main`, `System.out.println()`.

```java
package modulo_01;

/**
 * Ejercicio 01: Mensaje de bienvenida por consola.
 * @author Mariano Popolo
 */
public class Ejercicio_01 {

    public static void main(String[] args) {
        System.out.println("¡Hola, Mundo!");
    }
}

```

---

### 🔹 Ejercicio 02: Variables y Tipos de Datos

* **Consigna:** Declarar e inicializar variables de distintos tipos primitivos y referencias (`String`, `int`, `double`, `boolean`) e imprimir sus valores de forma clara y etiqueta por etiqueta.
* **Conceptos clave:** Tipado estático, memoria Stack, inicialización.

```java
package modulo_01;

/**
 * Ejercicio 02: Declaración e impresión de variables con etiquetas.
 * @author Mariano Popolo
 */
public class Ejercicio_02 {

    public static void main(String[] args) {
        String nombre = "Mariano";
        int edad = 43;
        double altura = 1.74; // Expresado en metros
        boolean estudiante = true;
        
        System.out.println("Nombre: " + nombre);
        System.out.println("Edad: " + edad);
        System.out.println("Altura: " + altura + " m");
        System.out.println("Es estudiante: " + estudiante);
    }
}

```

---

### 🔹 Ejercicio 03: Lectura de Datos con Scanner

* **Consigna:** Solicitar al usuario su nombre y edad desde la consola utilizando la clase `Scanner` e imprimir un mensaje de saludo.
* **Estándar de cátedra:** Evitar el "salto de línea fantasma" leyendo siempre con `nextLine()` y parseando a `int` con `Integer.parseInt()`.

```java
package modulo_01;

import java.util.Scanner;

/**
 * Ejercicio 03: Lectura por consola aplicando el estándar obligatorio de lectura.
 * @author Mariano Popolo
 */
public class Ejercicio_03 {

    public static void main(String[] args) {
        Scanner input = new Scanner(System.in);
        
        System.out.print("Ingrese su nombre: ");
        String nombre = input.nextLine();
        
        System.out.print("Ingrese su edad: ");
        int edad = Integer.parseInt(input.nextLine());
        
        System.out.println("Hola " + nombre);
        System.out.println("Tienes " + edad + " años");
        
        input.close();
    }
}

```

---

### 🔹 Ejercicio 04: Operaciones Aritméticas Básicas

* **Consigna:** Leer dos números enteros ingresados por el usuario y calcular su suma, resta, multiplicación y división.
* **Conceptos clave:** Operadores aritméticos, casting explícito `(double)` para conservar decimales en la división.

```java
package modulo_01;

import java.util.Scanner;

/**
 * Ejercicio 04: Calculadora de operaciones aritméticas básicas.
 * @author Mariano Popolo
 */
public class Ejercicio_04 {

    public static void main(String[] args) {
        Scanner input = new Scanner(System.in);
        
        System.out.print("Ingrese un número entero: ");
        int n_1 = Integer.parseInt(input.nextLine());
        
        System.out.print("Ingrese otro número entero: ");
        int n_2 = Integer.parseInt(input.nextLine());
        
        int suma = n_1 + n_2;
        int resta = n_1 - n_2;
        int multi = n_1 * n_2;
        double divi = (double) n_1 / n_2; // Casting a double
        
        System.out.println("La suma es " + suma);
        System.out.println("La resta es " + resta);
        System.out.println("La multiplicación es " + multi);
        System.out.println("La división es " + divi);
        
        input.close();
    }
}

```

---

### 🔹 Ejercicio 05: Caracteres de Escape

* **Consigna:** Mostrar un mensaje formateado en una sola instrucción/cadena utilizando secuencias de escape (`\n` para salto de línea y `\"` para comillas dobles).

```java
package modulo_01;

/**
 * Ejercicio 05: Uso de caracteres de escape para formateo de texto.
 * @author Mariano Popolo
 */
public class Ejercicio_05 {

    public static void main(String[] args) {
        System.out.println("Nombre: Juan Pérez\nEdad: 30 años\nDirección: \"Calle Falsa 123\"");
    }
}

```

---

### 🔹 Ejercicio 06: División Entera vs. División Real

* **Consigna:** Comparar el comportamiento de la división entre dos enteros (`int`) frente a la división con números decimales (`double`).
* **Conceptos clave:** Truncado de decimales en división entera.

```java
package modulo_01;

import java.util.Scanner;

/**
 * Ejercicio 06: Comparación de precisión en división entera vs real.
 * @author Mariano Popolo
 */
public class Ejercicio_06 {

    public static void main(String[] args) {
        Scanner input = new Scanner(System.in);
        
        // 1. Lectura de enteros
        System.out.print("Ingrese el primer número entero: ");
        int numInt1 = Integer.parseInt(input.nextLine());
        
        System.out.print("Ingrese el segundo número entero: ");
        int numInt2 = Integer.parseInt(input.nextLine());
        
        int divEntera = numInt1 / numInt2;
        
        // 2. Lectura de doubles
        System.out.print("\nIngrese el primer número decimal (double): ");
        double numDouble1 = Double.parseDouble(input.nextLine());
        
        System.out.print("Ingrese el segundo número decimal (double): ");
        double numDouble2 = Double.parseDouble(input.nextLine());
        
        double divReal = numDouble1 / numDouble2;
        
        System.out.println("\n--- COMPARACIÓN DE RESULTADOS ---");
        System.out.println("División entera (int / int): " + divEntera);
        System.out.println("División real (double / double): " + divReal);
        
        input.close();
    }
}

```

---

### 🔹 Ejercicio 07: Corrección y Análisis de Errores

* **Consigna:** Corregir un fragmento de código que presentaba incompatibilidad de tipos al leer un `String` mediante `scanner.nextInt()`.

```java
package modulo_01;

import java.util.Scanner;

/**
 * Ejercicio 07: Corrección de error de lectura e incompatibilidad de tipos.
 * @author Mariano Popolo
 */
public class Ejercicio_07 {

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        
        System.out.print("Ingresa tu nombre: ");
        
        /*
         * CORRECCIÓN:
         * Se reemplazó scanner.nextInt() por scanner.nextLine().
         * nextInt() intentaba asignar un entero a una variable String, lo cual
         * generaba un error de compilación por tipos incompatibles e
         * InputMismatchException si el usuario ingresaba texto.
         */
        String nombre = scanner.nextLine(); 
        
        System.out.println("Hola, " + nombre);
        
        scanner.close();
    }
}

```

---

### 🔹 Ejercicio 08: Prueba de Escritorio y Análisis de División

* **Consigna:** Analizar el comportamiento del código `int resultado = 5 / 2;` y elaborar la tabla de prueba de escritorio.

```java
package modulo_01;

/**
 * Ejercicio 08: Análisis de división entera y prueba de escritorio.
 * @author Mariano Popolo
 */
public class Ejercicio_08 {

    public static void main(String[] args) {
        int a = 5;
        int b = 2;
        int resultado = a / b;
        
        System.out.println("Resultado: " + resultado);
        
        /*
         * PRUEBA DE ESCRITORIO:
         * ---------------------------------------------------------------------
         * Línea | Variable a | Variable b | Variable resultado | Explicación
         *   1   |     5      |     -      |        -           | Asignación de a
         *   2   |     5      |     2      |        -           | Asignación de b
         *   3   |     5      |     2      |        2           | División entera
         *   4   |     5      |     2      |        2           | Imprime por pantalla
         * ---------------------------------------------------------------------
         * RESPUESTA:
         * El valor final de 'resultado' es 2. En Java, la división entre enteros 
         * calcula únicamente el cociente descartando los decimales. 
         * El resto (1) se obtiene mediante el operador módulo (%): a % b.
         */
    }
}

```

