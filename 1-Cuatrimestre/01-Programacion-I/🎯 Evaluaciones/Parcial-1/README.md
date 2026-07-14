# 🛠️ Parcial 1: Sistema de Control de Inventario de Ferretería
> **Materia:** Programación I (1° Cuatrimestre)  
> **Alumno:** Mariano Popolo  
> **Calificación:** 97 / 100 🌟

---

## 📹 Defensa del Parcial en Video

En este video explico en detalle la estructura del programa, las validaciones aplicadas a las entradas y realizo una demostración en vivo de su funcionamiento en la terminal:

[![Ver Explicación del Parcial](https://img.shields.io/badge/YouTube-Play_Video-red?style=for-the-badge&logo=youtube)](https://www.youtube.com/watch?v=9JAIjXJir-4)

*🔗 [Enlace directo a la defensa del parcial](https://www.youtube.com/watch?v=9JAIjXJir-4)*

---

## 📝 Enunciado del Problema

Desarrollar un sistema de consola interactivo en Python para la gestión de inventario en una ferretería utilizando estructuras de datos fundamentales (listas paralelas). El sistema debe operar continuamente mediante un menú de opciones hasta que el usuario decida finalizar la ejecución.

### Requisitos Técnicos:
1. **Listas Paralelas:** Uso estricto de listas sincronizadas por índice para gestionar nombres y cantidades de herramientas.
2. **Validaciones de Entrada:** Controlar que no se ingresen datos vacíos, nombres de herramientas repetidos o valores de stock negativos.
3. **Manejo de Flujo:** Estructuras cíclicas y de decisión para controlar el menú principal de 8 opciones de manera limpia y sin caídas de ejecución.

---

## ⚙️ Explicación del Código e Implementación

El programa (`parcial.py`) funciona bajo la lógica de **sincronía por índice** entre dos listas principales:
* `herramientas = []` (para almacenar los nombres de los productos).
* `existencias = []` (para almacenar las unidades físicas disponibles).

A continuación se detalla cómo se resuelven los puntos principales del menú en base al código:

### 🔹 Menú de Control Principal
Se utiliza un bucle `while` controlado por la opción elegida por el usuario. El programa sigue ejecutándose de forma iterativa hasta que se digita la opción `8`, finalizando de forma limpia.

### 🔹 Carga Inicial de Herramientas (Opción 1)
* Se solicita al usuario la cantidad de herramientas a ingresar.
* Mediante un ciclo `for` en base a ese rango, se piden los nombres correspondientes.
* **Validación Crucial:** Se implementa un control para verificar que el nombre no esté vacío y no se encuentre ya registrado en la lista de herramientas. Si el dato es inválido, el sistema lo rechaza y vuelve a solicitarlo.

### 🔹 Carga de Existencias (Opción 2)
* Se recorre la lista de herramientas ya cargadas.
* El sistema solicita la cantidad física para cada una.
* **Validación Crucial:** Se verifica que el stock ingresado no sea menor a cero.

### 🔹 Visualización del Inventario (Opción 3)
* Muestra de forma tabulada el contenido sincronizado.
* Se recorre la longitud de la lista mediante `range(len(herramientas))` imprimiendo en simultáneo el elemento `herramientas[i]` y su stock `existencias[i]`.
* Incluye validaciones previas para alertar al usuario si intenta listar el inventario antes de haber realizado las cargas de datos.

### 🔹 Consulta de Stock individual (Opción 4)
* El usuario ingresa la herramienta que desea consultar.
* El programa busca la coincidencia de nombre y extrae su índice utilizando el método `.index()`.
* Utilizando esa posición obtenida, accede directamente a la lista de `existencias` para verificar e informar la cantidad exacta disponible o si se encuentra temporalmente agotado.

### 🔹 Reporte de Productos Agotados (Opción 5)
* El sistema barre toda la lista de stock y filtra únicamente aquellas herramientas cuyo valor en `existencias` sea igual a `0`, listándolas en pantalla como alerta de reposición.

### 🔹 Alta de un Nuevo Producto individual (Opción 6)
* Permite expandir el catálogo en tiempo de ejecución. Pide el nombre de la nueva herramienta, aplica las mismas validaciones de duplicados/vacíos y, tras ser aprobada, la agrega al final de las listas mediante el método `.append()`.