MÓDULO 02: MODELO CONCEPTUAL DE DATOS Y DIAGRAMAS ENTIDAD-RELACIÓN (DER)

Materia: Bases de Datos I
Carrera: Tecnicatura Universitaria en Programación a Distancia (UTN)
Material: Apuntes de teoría y síntesis conceptual

==================================================

1. ¿QUÉ ES EL MODELO CONCEPTUAL?
==================================================

El modelo conceptual representa el primer paso formal en el diseño de una base de datos. Es una representación abstracta de alto nivel que describe qué información necesita guardar un sistema y cómo interactúa, sin importar la tecnología ni el gestor de bases de datos que se use después.

* Propósito: Captura los elementos esenciales de la realidad, valida reglas de negocio y sirve de comunicación unificada entre analistas, desarrolladores y clientes.


* Origen histórico: Propuesto por Peter Chen en 1976 con el Modelo Entidad-Relación (MER).



Flujo de Diseño:
Requerimientos del Negocio -> Modelo Conceptual (MER/DER) -> Modelo Lógico (Tablas, PK/FK) -> Modelo Físico / DBMS (MySQL, PostgreSQL, etc.)

# ==================================================
2. EL SISTEMA GESTOR DE BASE DE DATOS (DBMS)

Un DBMS (Database Management System) es el software intermediario entre los usuarios o aplicaciones y los datos físicos almacenados.

Funciones Principales:

* Definición de estructuras (creación y modificación de tablas, índices y restricciones).


* Manipulación de datos (inserción, consulta, actualización y borrado).


* Seguridad y control de acceso (permisos por roles de usuario).


* Integridad, transacciones, copias de seguridad y recuperación ante desastres.



Principales DBMS:

* MySQL: Ligero, rápido y muy utilizado en aplicaciones web.


* PostgreSQL: Robusto, avanzado, de código abierto y extensible.


* SQLite: Embebido, sin servidor, ideal para dispositivos móviles y aplicaciones de escritorio.


* Oracle / SQL Server: Alto rendimiento corporativo y manejo masivo de transacciones.



# ==================================================
3. COMPONENTES FUNDAMENTALES DEL MER

A. Entidades:
Objetos o conceptos del mundo real con existencia independiente e identificación unívoca.

* Físicas o Tangibles: Estudiante, Profesor, Producto, Vehículo.


* Conceptuales o Intangibles: Curso, Materia, Inscripción, Departamento.


* Entidades Débiles: No pueden identificarse únicamente por sus propios atributos y tienen dependencia de existencia respecto a una entidad fuerte propietaria. Poseen una clave parcial o discriminador y se representan con un rectángulo doble. (Ejemplo: Examen dentro de Curso).



B. Atributos:
Características que describen a una entidad.

* Por estructura:
* Simples (atómicos): Indivisibles (ej. DNI, Precio).


* Compuestos: Se descomponen en partes (ej. Dirección en Calle, Número, Ciudad).




* Por cardinalidad:
* Monovaluados: Un solo valor por registro (ej. Fecha de nacimiento).


* Multivaluados: Múltiples valores simultáneos (ej. lista de Teléfonos, Correos).




* Atributos Derivados: Se calculan a partir de otros datos (ej. Edad a partir de la fecha de nacimiento).



C. Relaciones:
Asociaciones e interacciones lógicas entre dos o más entidades.

# ==================================================
4. CARDINALIDAD

Indica el número de ocurrencias de una entidad que pueden vincularse con las ocurrencias de otra:

* Uno a Uno (1:1): Cada registro de A se asocia con un único registro de B, y viceversa (ej. Persona - Pasaporte).


* Uno a Muchos (1:N): Un registro de A se asocia con muchos de B, pero cada registro de B pertenece a uno solo de A (ej. Departamento - Empleados).


* Muchos a Muchos (N:M): Múltiples registros de A se asocian con múltiples de B (ej. Estudiante - Materias).



* Regla de pasaje al modelo lógico: Toda relación N:M se transforma obligatoriamente en dos relaciones 1:N mediante una tabla intermedia o de intersección.



# ==================================================
5. CLAVES E INTEGRIDAD REFERENCIAL

* Clave Primaria (PK): Identificador único e irrepetible de cada fila; no admite nulos (NOT NULL).


* Claves Candidatas: Todos los atributos únicos que califican para ser clave primaria.


* Clave Foránea (FK): Campo que apunta a la clave primaria de otra tabla para formalizar la relación.



Acciones ante Modificación o Eliminación:

* RESTRICT / NO ACTION: Impide borrar o modificar el registro principal si tiene hijos vinculados.


* CASCADE: Replica en cascada la eliminación o actualización sobre los registros relacionados.


* SET NULL: Pone en NULL el campo foráneo de los registros hijos si se elimina el principal.


* SET DEFAULT: Asigna un valor predeterminado al campo foráneo al eliminarse la entidad padre.



# ==================================================
6. SIMBOLOGÍA Y NOTACIONES DEL DER

Simbología Chen:

* Rectángulos: Entidades


* Rombos: Relaciones


* Elipses / Óvalos: Atributos


* Doble elipse: Atributo multivaluado
* Doble rectángulo: Entidad débil


* Texto subrayado: Atributo clave primaria (PK)

Otras notaciones:

* Notación Pata de Gallo (Crow's Foot): Utiliza símbolos en forma de ramificaciones para indicar cardinalidad múltiple, muy empleada en la industria.


* Diagramas de Clases UML: Representa entidades como clases con propiedades y métodos.



# ==================================================
7. CASO PRÁCTICO: SISTEMA DE BIBLIOTECA

Entidades y Atributos:

* Libro: ISBN (PK), Título, Año_Publicación, Copias_Disponibles.


* Miembro: ID_Miembro (PK), Nombre, Dirección, Teléfono, Email.


* Préstamo: ID_Préstamo (PK), Fecha_Préstamo, Fecha_Vencimiento, Fecha_Devolución.


* Autor: ID_Autor (PK), Nombre, Biografía.


* Editorial: ID_Editorial (PK), Nombre, Dirección.



Relaciones:

* Libro - Autor: N:M (requiere tabla intermedia Libro_Autor).


* Editorial - Libro: 1:N (una editorial publica varios libros).


* Miembro - Préstamo: 1:N.


* Libro - Préstamo: 1:N.



# ==================================================
8. ERRORES COMUNES DE DISEÑO

1. Confundir entidad con atributo (ej. poner el autor como un simple texto dentro de libro en lugar de crear una entidad Autor).


2. Asignar cardinalidades incorrectas por no analizar todos los casos de uso.


3. Crear relaciones redundantes que ya están resueltas por caminos transitivos.


4. Omitir reglas de integridad referencial.



# ==================================================
FUENTES Y REFERENCIAS

* Chen, Peter P. (1976). The Entity-Relationship Model—Toward a Unified View of Data.


* Cátedra Bases de Datos I — Guía de Estudio Ampliada: Diseño de Bases de Datos - Modelo Conceptual (UTN).


* Cátedra Bases de Datos I — Presentación: Modelado Conceptual de Bases de Datos y Diagramas Entidad-Relación (UTN).


* Cátedra Bases de Datos I — Diseño de Bases de Datos: Modelo Conceptual (UTN).