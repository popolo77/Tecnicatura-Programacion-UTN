# 🏛️ Guía Integral y Visual: Módulo 2 – Modelo Conceptual de Datos

Este informe consolida todo el marco conceptual, gráfico y práctico de la **Unidad 2: Modelado Conceptual de Bases de Datos y Diagramas Entidad-Relación (DER)** de la Tecnicatura Universitaria en Programación (UTN)[cite: 2].

---

## 1. El Modelo Conceptual: Propósito y Rol del DBMS

El **Modelo Conceptual** es una representación abstracta de alto nivel que captura la información del mundo real ignorando detalles de implementación técnica o de sintaxis SQL[cite: 1, 2]. Su propósito fundamental es servir de plano guía y facilitar la comunicación clara entre las partes interesadas (stakeholders) y el equipo de desarrollo[cite: 2, 3].

```text
┌─────────────────────────┐
│ Requerimientos del      │
│ Negocio (Mundo Real)    │
└───────────┬─────────────┘
            ▼
┌─────────────────────────┐
│ MODELO CONCEPTUAL (MER) │ ◄── Peter Chen (1976)
└───────────┬─────────────┘
            ▼
┌─────────────────────────┐
│ MODELO LÓGICO           │ ◄── Tablas, Claves Primarias/Foráneas
└───────────┬─────────────┘
            ▼
┌─────────────────────────┐
│ MOTOR DBMS (Físico)     │ ◄── MySQL, PostgreSQL, SQLite, Oracle
└─────────────────────────┘

```

### Funciones del DBMS (Sistema de Gestión de Base de Datos)

El **DBMS** actúa como intermediario entre los usuarios/aplicaciones y los datos almacenados, garantizando:

* **Definición de estructuras:** Creación y modificación de tablas, índices y restricciones.


* **Manipulación de datos:** Inserción, consulta, actualización y borrado (`CRUD`).


* **Seguridad y Control de Acceso:** Permisos por roles de usuario.


* **Mantenimiento y Respaldo:** Copias de seguridad y recuperación ante desastres.



| DBMS | Características y Casos de Uso |
| --- | --- |
| **MySQL** | Ligero, veloz, ideal para la web y aplicaciones estándar.

 |
| **PostgreSQL** | Avanzado, robusto, de código abierto, alta extensibilidad y soporte de datos complejos.

 |
| **SQLite** | Motor embebido, sin servidor, utilizado en aplicaciones móviles y de escritorio.

 |
| **Oracle / SQL Server** | Alto rendimiento empresarial, escalabilidad masiva y entornos corporativos.

 |

---

## 2. Componentes Fundamentales del MER y Simbología DER

Propuesto por **Peter Chen en 1976**, el Modelo Entidad-Relación (MER) estandarizó el diseño de datos.

```text
  ┌──────────────────┐               ◇───────────────◇               ┌──────────────────┐
  │     ENTIDAD      ├───────────────┤   RELACIÓN    ├───────────────┤     ENTIDAD      │
  │   [Rectángulo]   │               │   [Rombo]     │               │   [Rectángulo]   │
  └─────────┬────────┘               ◇───────────────◇               └──────────────────┘
            │
            ├── ( Atributo Simple )         [Óvalo sólido]
            ├── (( Atributo Multivaluado )) [Óvalo doble]
            └── ( <u>Atributo Clave/PK</u> )   [Óvalo con texto subrayado]

```

### A. Entidades

Objetos del mundo real con existencia independiente que pueden identificarse de forma unívoca.

* **Entidades Físicas / Tangibles:** `Estudiante`, `Profesor`, `Producto`, `Vehículo`.


* **Entidades Conceptuales / Intangibles:** `Curso`, `Materia`, `Departamento`, `Inscripción`.


* **Entidades Débiles:** No pueden identificarse únicamente por sus propios atributos y tienen **dependencia de existencia** respecto a una entidad fuerte/propietaria. Se representan con **rectángulos dobles** y poseen una **clave parcial (o discriminador)**.


* *Ejemplo:* La entidad `Examen` dentro de un `Curso`.





### B. Atributos

Propiedades o cualidades que describen a una entidad:

* **Por su Estructura:**
* **Simples / Atómicos:** Indivisibles (ej. `DNI`, `Precio`, `ID_Estudiante`).


* **Compuestos:** Pueden dividirse en partes más pequeñas (ej. `Dirección` en `Calle`, `Número`, `Ciudad`, `Código_Postal`).




* **Por su Cardinalidad:**
* **Monovaluados:** Contienen un solo valor por instancia (ej. `Fecha_Nacimiento`).


* **Multivaluados:** Pueden albergar múltiples valores simultáneos para la misma entidad (ej. lista de `Teléfonos`, `Correos_Electrónicos`). Se representan con doble óvalo.




* **Atributos Derivados:** Valores que no se almacenan directamente, sino que se calculan en base a otros (ej. `Edad` calculada a partir de la `Fecha_Nacimiento`).



### C. Estilos de Notación Gráfica

* **Notación Chen:** Rectángulos, rombos y óvalos. Muy completa teóricamente.


* **Notación Pata de Gallo (Crow's Foot):** Enfocada en tablas rectangulares con terminaciones en forma de ramificación para representar cardinalidades múltiples (`N`). Es la más empleada en la industria.


* **Diagramas de Clases UML:** Representa las entidades como clases estructuradas con atributos y operaciones para diseño orientado a objetos.



---

## 3. Cardinalidades y Relaciones

Indica el número de instancias de una entidad que pueden vincularse con instancias de otra.

```text
[ 1:1 ]   (1) Persona ─────────────── posee ─────────────── (1) DNI
[ 1:N ]   (1) Departamento ────────── emplea ────────────── (N) Empleados
[ N:M ]   (N) Estudiante ──────────── inscribe ──────────── (M) Cursos

```

* **Uno a Uno (1:1):** Cada elemento de A se asocia exactamente con un elemento de B, y viceversa (ej. `Persona` tiene una sola `Identificación Nacional`).


* **Uno a Muchos (1:N):** Un registro en A se asocia con muchos en B, pero cada registro de B pertenece a uno solo de A (ej. Un `Departamento` emplea muchos `Empleados`).


* **Muchos a Muchos (N:M):** Múltiples instancias de A se asocian con múltiples de B (ej. `Estudiante` se inscribe en varios `Cursos` y un `Curso` tiene varios `Estudiantes`).


* **Regla de transformación al modelo lógico:** Toda relación N:M se descompone obligatoriamente en **dos relaciones 1:N utilizando una tabla intermedia o de intersección** (`Inscripción`).





---

## 4. Claves e Integridad Referencial

### A. Claves

* **Clave Primaria (Primary Key - PK):** Atributo único e irrepetible que no admite valores `NULL`. Debe ser mínima y preferentemente inmutable (claves numéricas autoincrementales).


* **Claves Candidatas:** Todos los atributos únicos que califican para ser clave primaria antes de la selección final.


* **Clave Foránea (Foreign Key - FK):** Campo en una tabla que referencia a la PK de otra tabla, estableciendo la conexión lógica.



```sql
CREATE TABLE prestamos (
    id INT PRIMARY KEY,
    id_libro INT,
    FOREIGN KEY (id_libro) REFERENCES libros(id)
);

```

### B. Acciones de Integridad Referencial

Evitan los registros "huérfanos" en la base de datos cuando se modifican o eliminan registros padres:

* **CASCADE:** Si se elimina/actualiza el registro principal, se replica la acción automáticamente en todos los registros hijos relacionados.


* **RESTRICT / NO ACTION:** Impide eliminar o modificar el registro padre si tiene elementos vinculados en la tabla secundaria (ej. impide borrar un curso si hay alumnos inscriptos).


* **SET NULL:** Si se borra la clave principal, los campos foráneos vinculados se establecen automáticamente en `NULL`.


* **SET DEFAULT:** Asigna un valor predeterminado al campo foráneo si se suprime la entidad principal.



---

## 5. Caso Práctico Integrador: Sistema de Biblioteca

Aplicando la metodología paso a paso desde el análisis conceptual hasta las relaciones lógicas:

```text
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


* `Préstamo`: `ID_Préstamo` (PK), `Fecha_Préstamo`, `Fecha_Vencimiento`, `Fecha_Devolución`, `Multa`.


* `Autor`: `ID_Autor` (PK), `Nombre`, `Biografía`.


* `Editorial`: `ID_Editorial` (PK), `Nombre`, `Dirección`.




* **Relaciones:**
* `Libro` — (N:M) — `Autor` (*requiere tabla intermedia `Libro_Autor*`).


* `Editorial` — (1:N) — `Libro` (una editorial publica varios libros).


* `Miembro` — (1:N) — `Préstamo` y `Libro` — (1:N) — `Préstamo`.





---

## 6. Errores Comunes de Diseño a Evitar

* **Confundir Entidad con Atributo:** Colocar `Autor` como un simple campo de texto dentro de `Libro` en lugar de crear una entidad independiente `Autor` con sus propios datos.


* **Cardinalidades Incorrectas:** Declarar relaciones como 1:N cuando en la realidad del negocio son N:M.


* **Relaciones Redundantes:** Crear conexiones directas entre tablas cuando el camino lógico ya está resuelto mediante entidades intermedias.


* **Ignorar Reglas del Negocio:** Omitir restricciones de integridad provocando inconsistencias en el ciclo de vida del dato.



---

## 📚 Bibliografía y Referencias

* **Chen, Peter P.** (1976). *The Entity-Relationship Model—Toward a Unified View of Data*.


* **Cátedra Bases de Datos I** — *Guía de Estudio Ampliada: Diseño de Bases de Datos - Modelo Conceptual* (UTN).


* **Cátedra Bases de Datos I** — *Presentación: Modelado Conceptual de Bases de Datos y Diagramas Entidad-Relación* (UTN).


* **Cátedra Bases de Datos I** — *Diseño de Bases de Datos: Modelo Conceptual* (UTN).



```

```