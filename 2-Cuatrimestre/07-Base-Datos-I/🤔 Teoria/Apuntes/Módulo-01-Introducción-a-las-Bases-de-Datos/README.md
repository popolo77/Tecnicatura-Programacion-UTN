# 📚 Módulo 1: Introducción a las Bases de Datos

Este módulo abarca las definiciones fundamentales sobre datos e información, la evolución histórica de los sistemas de almacenamiento, el surgimiento y las características del modelo relacional, la comparación con archivos planos y estructuras de datos, y los entornos de desarrollo locales esenciales para gestionar bases de datos.

---

## 1. ⚙️ Conceptos Fundamentales de la Información

En los sistemas de información existen conceptos jerárquicos clave que diferencian los datos primitivos de las estructuras complejas de toma de decisiones.

## Definiciones Básicas

* **Dato:** Unidad mínima e indivisible de representación simbólica (numérica, alfabética o gráfica). Por sí solo carece de significado o contexto (ejemplo: `35`, `"Juan"`).


* **Información:** Conjunto de datos procesados, estructurados y contextualizados que aportan significado útil para la toma de decisiones (ejemplo: `"Juan tiene 35 años y aprobó la materia"`).


* **Sistema de Información (SI):** Conjunto articulado de recursos (personas, datos, procesos y tecnologías) que recolectan, procesan, almacenan y distribuyen información en una organización. Sus fases principales son *Entrada*, *Procesamiento*, *Salida* y *Retroalimentación*.


* **Base de Datos (BD):** Colección organizada de datos estructurados, guardados electrónicamente de forma persistente. Garantiza el acceso, actualización y manipulación eficiente minimizando la redundancia y asegurando la integridad.


* **Sistema de Gestión de Bases de Datos (SGBD / DBMS):** Software que actúa como interfaz entre la base de datos, las aplicaciones y los usuarios. Administra el almacenamiento físico, la seguridad, la concurrencia, la integridad y la ejecución de consultas.

---

## 2. 📜 Historia y Evolución de los Sistemas de Datos

La forma en que almacenamos y recuperamos datos ha evolucionado a lo largo de las décadas para resolver problemas de rigidez, redundancia y escalabilidad.

## Línea de Tiempo Histórica

1. **Década de 1950 - 1960 (Archivos Planos):** Almacenamiento en ficheros de texto simples. Presentaban alta redundancia, inconsistencia de datos y fuerte dependencia entre el programa y el archivo.


2. **Década de 1960 (Modelos Jerárquico y de Red):**
* **Jerárquico:** Estructura en forma de árbol (padre-hijo).


* **En Red:** Estructura más flexible basada en grafos y punteros.


* *Limitación:* Alta rigidez y complejidad en la navegación y actualización.




3. **Año 1970 (Modelo Relacional):** Edgar Frank Codd (IBM) publica la teoría que revoluciona el área al incorporar el uso de tablas (relaciones) e independizar la lógica del almacenamiento físico.


4. **Décadas de 1980 - 1990:** Consolidación de SGBD relacionales comerciales (Oracle, DB2, SQL Server, MySQL) y estándar SQL.


5. **Años 2000 en adelante (NoSQL y Era Cloud):** Surgimiento de soluciones NoSQL (documentales como MongoDB, clave-valor, grafos) para escalabilidad masiva y esquemas flexibles en la nube.


6. **Enfoque Actual (Arquitectura Políglota):** Combinación pragmática de bases SQL y NoSQL dentro de un mismo ecosistema según la necesidad específica de cada componente.



---

## 3. 🧩 El Modelo Relacional y su Estructura

Fundamentado en la teoría de conjuntos y el álgebra relacional, el modelo relacional es la base de la mayoría de los sistemas actuales.

## Características Principales

* **Estructura Tabular:** Datos organizados formalmente en tablas con filas y columnas.


* **Independencia de Datos:** Separación entre la estructura lógica y la implementación física en disco.


* **Normalización:** Proceso que minimiza la redundancia y evita anomalias de actualización.


* **Integridad Referencial:** Reglas y restricciones que garantizan consistencia entre tablas relacionadas.



## Equivalencias Teórico-Prácticas

* **Relación:** Equivalente a una **Tabla**.


* **Tupla:** Equivalente a una **Fila** o **Registro**.


* **Atributo:** Equivalente a una **Columna** o **Campo**.



---

## 4. 🔑 Elementos Clave: Tuplas, Claves e Índices

Para garantizar la unívocidad de la información y la rapidez de acceso, el modelo relacional emplea estructuras especializadas.

## Claves e Identificadores

* **Clave (Key):** Atributo o conjunto de atributos que identifica de forma única a cada tupla en una tabla.


* **Garantías de las Claves:** Aseguran la unicidad de los registros, permiten la relación formal entre tablas distintas, preservan la integridad de datos y facilitan la búsqueda directa.


* **Claves Artificiales:** Identificadores autogestionados (ejemplo: un `ID` numérico autonumérico) creados cuando no existe un atributo natural único en la realidad.



## Índices de Base de Datos

Un **Índice** es una estructura de datos secundaria que funciona como el índice alfabético de un libro. Permite localizar registros rápidamente sin necesidad de realizar un recorrido secuencial completo (*Full Table Scan*).

## Ejemplo Comparativo de Búsqueda

* **Sin Índice (Búsqueda Secuencial):** Revisa tupla por tupla hasta encontrar el resultado (tiempo de búsqueda elevado).


* **Con Índice (Búsqueda Directa):** Accede al puntero directo del registro en una fracción de segundo mediante árboles de búsqueda (B-Trees).



---

## 5. ⚖️ Comparativa de Estructuras y Almacenamiento

Comprender la diferencia entre archivos, bases de datos y estructuras de memoria es vital para el desarrollo de software.

## Archivos vs. Bases de Datos Relacionales

* **Estructura:** Los archivos poseen estructura simple/plana; las bases de datos son complejas y organizadas.


* **Acceso:** En archivos es secuencial o aleatorio simple; en BD es acceso directo indexado.


* **Redundancia:** Alta en archivos; baja en bases de datos gracias a la normalización.


* **Integridad y Seguridad:** En archivos depende del sistema operativo; en BD es gestionada, robusta e integrada al SGBD.



## Estructuras de Datos de Programación en BD

* **Vectores (Arrays):** Tamaño fijo, acceso directo por índice pero ineficientes para inserciones o eliminaciones dinámicas.


* **Listas:** Estructura dinámica que facilita la inserción/eliminación, pero requiere recorrido secuencial para búsquedas.


* **Árboles Binarios (B-Trees):** Estructura jerárquica con excelente rendimiento para búsqueda, inserción y eliminación. *Es la base técnica utilizada internamente por los SGBD para la creación de índices*.



---

## 6. 🛠️ Entorno de Trabajo Local

Para interactuar con motores relacionales tipo MySQL/MariaDB durante la cursada, utilizaremos entornos gráficos estándar de la industria:

## Herramientas Principales

* **XAMPP + phpMyAdmin:**
* **XAMPP:** Servidor local independiente que integra Apache, MariaDB/MySQL y PHP.


* **phpMyAdmin:** Cliente web accesible desde `localhost/phpmyadmin` para administrar bases de datos, crear tablas y ejecutar SQL de forma visual e intuitiva.




* **MySQL Workbench:** Aplicación cliente de escritorio oficial para modelado diagramático (DER), administración avanzada y desarrollo de scripts SQL.