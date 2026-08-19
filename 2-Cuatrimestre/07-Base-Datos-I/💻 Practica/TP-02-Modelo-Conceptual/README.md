# 📚 Trabajo Práctico N° 2: Modelado Conceptual de Bases de Datos

| Institución | Carrera | Materia | Comisión | Alumno |
| :--- | :--- | :--- | :--- | :--- |
| **UTN FRSN** | Tecnicatura Universitaria en Programación (TUP)[cite: 3] | Bases de Datos I[cite: 1, 3] | M26 C2-01 | Mariano Popolo |

---

## 🎯 Escenario Planteado
Diseño del modelo conceptual para un **Sistema de Gestión de Biblioteca Universitaria** encargado de registrar y controlar el préstamo de recursos bibliográficos a estudiantes y docentes de la facultad[cite: 1, 3].

---

## 📝 Desarrollo de Consignas

### Ejercicio 1: Identificación y Justificación de Entidades
* **Estudiante (Física / Tangible):** Representa a los alumnos de la institución que solicitan material bibliográfico; posee existencia independiente en el sistema académico[cite: 1, 2, 3].
* **Profesor (Física / Tangible):** Modela a los docentes de la facultad que retiran libros para cátedra e investigación[cite: 1, 2, 3].
* **Libro (Física / Tangible):** Modela el recurso bibliográfico tangible disponible en la biblioteca[cite: 1, 2, 3].
* **Préstamo (Conceptual / Transaccional):** Representa el evento temporal en el que un usuario retira un libro; indispensable para registrar atributos dinámicos (fechas de retiro y devolución) que no pertenecen de forma estática ni al usuario ni al ejemplar[cite: 1, 2, 3].

### Ejercicio 2: Descripción y Clasificación de Atributos
* **Estudiante:** `Legajo` (Simple/Monovaluado), `Nombre_Completo` (Compuesto/Monovaluado), `Dirección` (Compuesto/Monovaluado), `Email` (Simple/Monovaluado), `Teléfonos` (Simple/Multivaluado)[cite: 1, 2, 3].
* **Profesor:** `ID_Profesor` (Simple/Monovaluado), `Nombre_Completo` (Compuesto/Monovaluado), `Departamento` (Simple/Monovaluado), `Email` (Simple/Monovaluado)[cite: 1, 2, 3].
* **Libro:** `Código_Libro` (Simple/Monovaluado), `Título` (Simple/Monovaluado), `Autor(es)` (Simple/Multivaluado), `Editorial` (Simple/Monovaluado), `Ejemplares_Disponibles` (Simple/Monovaluado)[cite: 1, 2, 3].
* **Préstamo:** `ID_Préstamo` (Simple/Monovaluado), `Fecha_Préstamo` (Simple/Monovaluado), `Fecha_Devolución` (Simple/Monovaluado)[cite: 1, 2, 3].

### Ejercicio 3: Identificación y Clasificación de Relaciones
* **Estudiante — Préstamo (1:N):** Un estudiante realiza muchos préstamos; cada préstamo pertenece a un único estudiante[cite: 1, 2, 3].
* **Profesor — Préstamo (1:N):** Un profesor realiza muchos préstamos; cada préstamo pertenece a un único profesor[cite: 1, 2, 3].
* **Libro — Préstamo (1:N):** Un libro puede ser prestado muchas veces a lo largo del tiempo; cada registro de préstamo refiere a un libro puntual[cite: 1, 2, 3].

### Ejercicio 4: Propuesta y Justificación de Claves Primarias y Candidatas
* **Estudiante:** PK: `Legajo` (identificador numérico simple e inalterable)[cite: 2, 3] | Candidatas: `DNI`, `Email`[cite: 1, 2, 3].
* **Profesor:** PK: `ID_Profesor` (código institucional unívoco)[cite: 1, 3] | Candidatas: `DNI`, `Email`[cite: 1, 2, 3].
* **Libro:** PK: `Código_Libro` (o `ISBN`) (estándar internacional unívoco)[cite: 1, 2, 3] | Candidatas: No aplican[cite: 1, 3].
* **Préstamo:** PK: `ID_Préstamo` (clave subrogada numérica)[cite: 1, 2, 3] | Candidata: Clave compuesta `Usuario + Código_Libro + Fecha_Préstamo`[cite: 1, 2, 3].

### Ejercicio 5: Claves Foráneas (FK) e Integridad Referencial
* **Claves Foráneas en Préstamo:** `Legajo` $\rightarrow$ `Estudiante(Legajo)`, `ID_Profesor` $\rightarrow$ `Profesor(ID_Profesor)`, `Código_Libro` $\rightarrow$ `Libro(Código_Libro)`[cite: 1, 2, 3].
* **Garantías de la Integridad Referencial:**
  1. **Prevención de registros huérfanos:** No permite registrar un préstamo con un usuario o libro inexistente en el sistema[cite: 1, 2, 3].
  2. **Control de bajas y modificaciones:** Mediante restricciones como `RESTRICT`, impide borrar un libro o un estudiante si poseen préstamos activos vinculados[cite: 1, 2, 3].
  3. **Eficiencia relacional:** Facilita operaciones `JOIN` rápidas y normalizadas mediante claves numéricas simples[cite: 2, 3].

---

## 📐 Diagrama Entidad-Relación (DER Conceptual)

```text
  ┌──────────────┐                                       ┌──────────────┐
  │  ESTUDIANTE  │(1)                                 (1)│    LIBRO     │
  └──────┬───────┘                                       └──────┬───────┘
         │                                                      │
         │ solicita                                             │ incluye
         │                                                      │
        [N]                                                    [N]
  ┌──────┴──────────────────────────────────────────────────────┴───────┐
  │                              PRÉSTAMO                               │
  │ PK: ID_Préstamo                                                     │
  │ FK: Legajo / ID_Profesor                                            │
  │ FK: Código_Libro                                                    │
  │ Atributos: Fecha_Préstamo, Fecha_Devolución                         │
  └──────┬──────────────────────────────────────────────────────────────┘
        [N]
         │
         │ solicita
         │
  ┌──────┴───────┐(1)
  │   PROFESOR   │
  └──────────────┘

```

---

## 🗄️ Esquema del Modelo Relacional (Tablas con Datos de Ejemplo)

A continuación se muestra cómo se implementa el modelo conceptual en el modelo lógico relacional, convirtiendo cada entidad en una tabla independiente con sus filas, columnas, Claves Primarias (`PK`) y Claves Foráneas (`FK`):

### 1. Tabla: `Estudiantes`

* **Clave Primaria (PK):** `Legajo`


| Legajo (PK) | Nombre_Completo | Direccion | Email | Telefono |
| --- | --- | --- | --- | --- |
| `1001` | Mariano Popolo | Mitre 345, San Nicolás | mariano.popolo@alumnos.frsn.utn.edu.ar | 336-4112233 |
| `1002` | Juan Manuel Pérez | Pellegrini 890, San Nicolás | juan.perez@alumnos.frsn.utn.edu.ar | 336-4556677 |
| `1003` | Sofía Bianchi | Belgrano 120, Villa Constitución | sofia.bianchi@alumnos.frsn.utn.edu.ar | 3400-488990 |

### 2. Tabla: `Profesores`

* **Clave Primaria (PK):** `ID_Profesor`


| ID_Profesor (PK) | Nombre_Completo | Departamento | Email |
| --- | --- | --- | --- |
| `201` | Ing. Carlos Gómez | Sistemas y Computación | cgomez@frsn.utn.edu.ar |
| `202` | Lic. Laura Fernández | Ciencias Básicas | lfernandez@frsn.utn.edu.ar |
| `203` | Dr. Martín Rossi | Electrónica y Redes | mrossi@frsn.utn.edu.ar |

### 3. Tabla: `Libros`

* **Clave Primaria (PK):** `Codigo_Libro`


| Codigo_Libro (PK) | Titulo | Autor | Editorial | Ejemplares_Disponibles |
| --- | --- | --- | --- | --- |
| `LIB-101` | Sistemas de Bases de Datos | Peter Chen | Rama | 4 |
| `LIB-102` | Introducción a los Algoritmos | Thomas Cormen | MIT Press | 2 |
| `LIB-103` | Redes de Computadoras | Andrew Tanenbaum | Pearson | 5 |
| `LIB-104` | Clean Code | Robert C. Martin | Prentice Hall | 3 |

### 4. Tabla: `Prestamos` (Entidad Transaccional / Hija)

* **Clave Primaria (PK):** `ID_Prestamo`

* **Claves Foráneas (FK):** `Legajo_Estudiante`, `ID_Profesor`, `Codigo_Libro`


| ID_Prestamo (PK) | Legajo_Estudiante (FK) | ID_Profesor (FK) | Codigo_Libro (FK) | Fecha_Prestamo | Fecha_Devolucion |
| --- | --- | --- | --- | --- | --- |
| `1` | `1001` | *NULL* | `LIB-101` | 2026-08-10 | 2026-08-17 |
| `2` | *NULL* | `201` | `LIB-103` | 2026-08-12 | 2026-08-26 |
| `3` | `1002` | *NULL* | `LIB-104` | 2026-08-14 | 2026-08-21 |
| `4` | `1001` | *NULL* | `LIB-102` | 2026-08-18 | 2026-08-25 |

---

### 💡 Justificación Técnica del Esquema Relacional

* **Integridad Referencial:** No es posible cargar un préstamo con el código `LIB-999` si dicho libro no existe previamente en la tabla `Libros`.


* **Eliminación de redundancia:** La tabla `Prestamos` almacena únicamente claves numéricas (`1001`, `LIB-101`) en lugar de duplicar nombres, correos o títulos en cada retiro.


* **Flexibilidad de usuario:** Los campos foráneos `Legajo_Estudiante` e `ID_Profesor` admiten valores nulos (`NULL`) según si el préstamo fue solicitado por un alumno o por un docente.



---

## 📖 Bibliografía de Cátedra

* `Modelo conceptual DB DERelacion.pdf` — Cátedra Bases de Datos I (UTN).


* `Diseño de Bases de Datos - Modelo Conceptual.pdf` — Cátedra Bases de Datos I (UTN).


* `Modelo Conceptual - Material Complementario.pdf` — Cátedra Bases de Datos I (UTN).


