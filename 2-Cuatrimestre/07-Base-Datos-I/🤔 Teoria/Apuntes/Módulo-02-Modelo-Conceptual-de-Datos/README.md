```markdown
# 🏛️ Módulo 02: Modelo Conceptual de Datos y Diagramas Entidad-Relación (DER)

> **Materia:** Bases de Datos I  
> **Carrera:** Tecnicatura Universitaria en Programación a Distancia (UTN)  
> **Material:** Apuntes de teoría y síntesis conceptual

---

## 📌 Tabla de Contenidos
- [1. ¿Qué es el Modelo Conceptual?](#1-qué-es-el-modelo-conceptual)
- [2. El Sistema Gestor de Base de Datos (DBMS)](#2-el-sistema-gestor-de-base-de-datos-dbms)
- [3. Componentes Fundamentales del MER](#3-componentes-fundamentales-del-mer)
  - [Entidades](#a-entidades)
  - [Atributos](#b-atributos)
  - [Relaciones](#c-relaciones)
- [4. Cardinalidad](#4-cardinalidad)
- [5. Claves e Integridad Referencial](#5-claves-e-integridad-referencial)
- [6. Simbología y Notaciones del DER](#6-simbología-y-notaciones-del-der)
- [7. Caso Práctico Integrador (Sistema de Biblioteca)](#7-caso-práctico-integrador)
- [8. Errores Comunes de Diseño](#8-errores-comunes-de-diseño)

---

## 1. ¿Qué es el Modelo Conceptual?

El **modelo conceptual** representa la primera etapa formal en el diseño de una base de datos. Consiste en una representación abstracta y de alto nivel que describe la estructura lógica de los datos y sus reglas del negocio, sin depender de ningún software o lenguaje específico.

* **Propósito:** Captura los elementos esenciales de la realidad y sirve como plano de comunicación unificado entre los analistas, desarrolladores y clientes.
* **Origen:** Fue introducido formalmente por **Peter Chen en 1976** bajo el nombre de **Modelo Entidad-Relación (MER)**.


```

┌─────────────────────────────────┐
│     Mundo Real / Requisitos     │
└────────────────┬────────────────┘
▼
┌─────────────────────────────────┐
│   MODELO CONCEPTUAL (MER/DER)   │ ◄── Peter Chen (1976)
└────────────────┬────────────────┘
▼
┌─────────────────────────────────┐
│         MODELO LÓGICO           │ ◄── Tablas, Claves Primarias/Foráneas
└────────────────┬────────────────┘
▼
┌─────────────────────────────────┐
│   MODELO FÍSICO / DBMS (Motor)  │ ◄── MySQL, PostgreSQL, SQLite, etc.
└─────────────────────────────────┘

```

---

## 2. El Sistema Gestor de Base de Datos (DBMS)

Un **DBMS** (*Database Management System*) es el software intermediario entre los usuarios/aplicaciones y los datos físicos almacenados.

### Funciones Principales
* **Definición de estructuras:** Creación y ajuste de tablas, índices y esquemas.
* **Manipulación de datos:** Inserción, consulta, actualización y eliminación (`CRUD`).
* **Seguridad y Control:** Administración de permisos, roles y usuarios.
* **Integridad y Respaldo:** Transacciones seguras, copias de seguridad y recuperación ante fallos.

| DBMS | Tipo / Enfoque Principal |
| :--- | :--- |
| **MySQL** | Ligero, veloz, altamente adoptado en desarrollo web. |
| **PostgreSQL** | Robusto, de código abierto, extensible y con soporte avanzado para datos complejos. |
| **SQLite** | Motor embebido (sin servidor), ideal para apps móviles y utilidades locales. |
| **Oracle / SQL Server** | Entornos corporativos de alto volumen de transacciones y misión crítica. |

---

## 3. Componentes Fundamentales del MER

### A. Entidades
Objetos o conceptos del mundo real con existencia propia e identificación unívoca.
* **Entidades Físicas / Tangibles:** `Estudiante`, `Profesor`, `Producto`, `Vehículo`.
* **Entidades Conceptuales / Intangibles:** `Curso`, `Materia`, `Inscripción`, `Departamento`.
* **Entidades Débiles:** Entidades que no pueden identificarse por sí solas y dependen de la existencia de una entidad fuerte (propietaria). Poseen una **clave parcial** o discriminador y se representan con un **rectángulo doble**.

### B. Atributos
Propiedades o características que describen a una entidad.

* **Por Estructura:**
  * **Simples (Atómicos):** Indivisibles (ej. `DNI`, `Precio`, `Legajo`).
  * **Compuestos:** Se dividen en subcomponentes (ej. `Dirección` $\rightarrow$ `Calle`, `Número`, `Ciudad`).
* **Por Cardinalidad:**
  * **Monovaluados:** Tienen un único valor por entidad (ej. `Fecha_Nacimiento`).
  * **Multivaluados:** Pueden tener múltiples valores simultáneos (ej. `Teléfono`, `Email`). Se representan con **doble óvalo**.
* **Atributos Derivados:** Valores que no se guardan estáticamente, sino que se calculan a partir de otros (ej. `Edad` calculada desde la `Fecha_Nacimiento`).

### C. Relaciones
Asociaciones lógicas y semánticas que vinculan a dos o más entidades entre sí. Se representan gráficamente mediante un **rombo**.

---

## 4. Cardinalidad

Indica la cantidad mínima y máxima de ocurrencias de una entidad que pueden asociarse con ocurrencias de otra:


```

[ 1:1 ]   (1) Persona ─────────────── posee ─────────────── (1) Pasaporte
[ 1:N ]   (1) Departamento ────────── emplea ────────────── (N) Empleados
[ N:M ]   (N) Estudiante ──────────── cursa ─────────────── (M) Materias

```

* **Uno a Uno (1:1):** Cada elemento de A se vincula exclusivamente con uno de B, y viceversa.
* **Uno a Muchos (1:N):** Un registro en A se asocia con muchos en B, pero cada registro de B pertenece únicamente a uno de A.
* **Muchos a Muchos (N:M):** Varios registros de A se asocian con varios de B.
  > ⚠️ **Regla de pasaje al modelo lógico:** Toda relación `N:M` se transforma obligatoriamente en **dos relaciones 1:N** mediante una tabla intermedia o de intersección.

---

## 5. Claves e Integridad Referencial

* **Clave Primaria (Primary Key - PK):** Atributo único que identifica unívocamente a cada registro. No admite valores nulos (`NOT NULL`) ni repetidos.
* **Claves Candidatas:** Todos los atributos que cumplen los requisitos de unicidad para ser elegidos como clave primaria.
* **Clave Foránea (Foreign Key - FK):** Atributo que hace referencia a la clave primaria de otra tabla, estableciendo el vínculo formal entre ambas.

### Acciones ante Modificación / Eliminación

```sql
CREATE TABLE Prestamos (
    id INT PRIMARY KEY,
    id_libro INT,
    FOREIGN KEY (id_libro) REFERENCES Libros(id)
        ON DELETE RESTRICT
        ON UPDATE CASCADE
);

```

* **RESTRICT / NO ACTION:** Bloquea el borrado/modificación del registro padre si existen registros hijos dependientes.
* **CASCADE:** Aplica en cascada la eliminación o modificación sobre todas las filas hijas vinculadas.
* **SET NULL:** Asigna `NULL` a la clave foránea hija cuando se suprime la entidad principal.
* **SET DEFAULT:** Asigna un valor predeterminado al campo foráneo al eliminarse el registro padre.

---

## 6. Simbología y Notaciones del DER

```
       [ ENTIDAD ]  ─────────────◇ RELACIÓN ◇─────────────  [ ENTIDAD ]
            │
            ├── ( Atributo Simple )
            ├── (( Atributo Multivaluado ))
            └── ( <u>Atributo Clave (PK)</u> )

```

* **Notación Peter Chen:** Utiliza rectángulos (entidades), rombos (relaciones), elipses (atributos) y líneas de unión.
* **Notación Pata de Gallo (Crow's Foot):** Enfocada en tablas con ramificaciones finales que representan cardinalidades (`1`, `0..1`, `1..N`, `0..N`). Es el estándar predominante en la industria y herramientas CASE.
* **Diagramas de Clases UML:** Representa las entidades como clases estructuradas con atributos y visibilidad.

---

## 7. Caso Práctico Integrador

### Dominio: Sistema de Biblioteca

```
┌──────────────────┐               ◇──────────────────◇               ┌──────────────────┐
│     MIEMBRO      │ (1)           │     PRÉSTAMO     │           (N) │      LIBRO       │
│ PK: ID_Miembro   ├───────────────┤ PK: ID_Prestamo  ├───────────────┤ PK: ISBN         │
│ Nombre, Teléfono │               │ Fecha_Prestamo   │               │ Titulo, Año      │
└──────────────────┘               ◇──────────────────◇               └────────┬─────────┘
                                                                               │ (N)
                                                                               │
                                                                               ◇ Escrito_Por ◇
                                                                               │
                                                                               │ (M)
                                                                      ┌────────┴─────────┐
                                                                      │      AUTOR       │
                                                                      │ PK: ID_Autor     │
                                                                      │ Nombre, Bio      │
                                                                      └──────────────────┘

```

* **Entidades y Atributos:**
* `Libro`: `ISBN` (PK), `Título`, `Año_Publicación`, `Copias_Disponibles`.
* `Miembro`: `ID_Miembro` (PK), `Nombre`, `Dirección`, `Teléfono`, `Email`.
* `Préstamo`: `ID_Préstamo` (PK), `Fecha_Préstamo`, `Fecha_Vencimiento`, `Fecha_Devolución`.
* `Autor`: `ID_Autor` (PK), `Nombre`, `Biografía`.
* `Editorial`: `ID_Editorial` (PK), `Nombre`, `Dirección`.


* **Relaciones:**
* `Libro` — (N:M) — `Autor` *(requiere tabla intermedia `Libro_Autor`)*.
* `Editorial` — (1:N) — `Libro` *(una editorial publica muchos libros)*.
* `Miembro` — (1:N) — `Préstamo` y `Libro` — (1:N) — `Préstamo`.



---

## 8. Errores Comunes de Diseño

1. **Confundir entidad con atributo:** Guardar datos complejos como cadenas de texto sueltas dentro de una entidad en vez de modularizarlos en una entidad independiente.
2. **Asignación errónea de cardinalidades:** Asumir relaciones `1:N` sin contemplar escenarios del dominio que exigen `N:M`.
3. **Relaciones redundantes:** Establecer asociaciones directas innecesarias entre dos entidades cuando su vínculo ya queda resuelto transitivamente.
4. **Omitir reglas de integridad:** No prever comportamientos de cascada o restricción ante bajas de registros.

---

## 📚 Bibliografía y Referencias

* **Chen, Peter P.** (1976). *The Entity-Relationship Model—Toward a Unified View of Data*. ACM Transactions on Database Systems.
* **Cátedra Bases de Datos I** — *Guía de Estudio Ampliada: Diseño de Bases de Datos - Modelo Conceptual* (UTN).
* **Cátedra Bases de Datos I** — *Presentación: Modelado Conceptual de Bases de Datos y Diagramas Entidad-Relación* (UTN).

```

```