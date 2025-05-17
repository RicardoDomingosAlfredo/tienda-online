## 1. ¿Qué ventajas ofrece GraphQL sobre REST en este contexto?

R: En este contexto graphQL ofrece varias ventajas frente a REST, especialmente en aplicaciones donde se requiere un control preciso de los datos que se solicitan y actualizan. En este contexto, las principales ventajas son:
- **Consulta personalizada de datos**: El cliente puede solicitar exactamente los campos que necesita, reduciendo la sobrecarga de datos innecesarios.
- **Menor número de llamadas a la API**: Se pueden obtener múltiples recursos relacionados en una sola petición, evitando múltiples llamadas como en REST.
- **Mejor rendimiento en redes lentas o móviles**: Al permitir peticiones más precisas, se reduce la cantidad de datos transferidos.
- **Mayor flexibilidad para evolucionar el esquema**: Es posible modificar o extender el esquema de la API sin romper los clientes existentes.

## 2. ¿Cómo se definen los tipos y resolvers en una API con GraphQL?
R: En graphQL, se definen dos componentes clave:

- **Tipos (Types)**: Se definen en el esquema (schema) y representan la estructura de los datos que se pueden consultar o mutar.

- **Resolvers**: Son funciones que indican cómo obtener o modificar los datos definidos en el esquema. 

## 3. ¿Por qué es importante que el backend también actualice `disponible` y no depender solo del frontend?

R: Porque la lógica de negocio debe estar centralizada y asegurada en el backend para evitar inconsistencias, fraudes o errores derivados de:

- **Manipulación del frontend**: Un usuario malintencionado puede alterar el código del cliente.
- **Errores de sincronización**: El frontend puede no tener la lógica completa o actualizada para determinar correctamente la disponibilidad.
- **Fuente única de verdad**: El backend debe ser la única fuente fiable del estado de un producto o servicio.

Centralizar la lógica de actualización garantiza integridad, seguridad y coherencia de los datos.

## 4. ¿Cómo garantizas que la lógica de actualización de stock y disponibilidad sea coherente?

R:Para garantizar coherencia, se deben aplicar varias buenas prácticas:

- **Encapsular la lógica de negocio en el backend**: Toda modificación de stock o disponibilidad debe hacerse desde el backend, en un solo punto del código.
- **Transacciones o bloqueos en operaciones concurrentes**: Si múltiples usuarios pueden modificar stock simultáneamente, usar mecanismos como transacciones o bloqueos para evitar condiciones de carrera.
- **Validaciones antes de actualizar**: Verificar que la operación sea válida (por ejemplo, que no se reste más stock del disponible).
- **Test automatizados de integridad**: Asegurar que las reglas se cumplen mediante pruebas automáticas.
- **Actualización atómica**: Siempre que se modifique el stock, se debe actualizar también el campo `disponible` en la misma operación, para evitar discrepancias.
