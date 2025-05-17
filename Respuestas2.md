# Respuestas – Práctica Flask + GraphQL + Vue

---

## 1. ¿Qué ventajas ofrece GraphQL sobre REST en este contexto?

GraphQL permite consultar exactamente los datos necesarios, lo cual es útil en una app de inventario donde el frontend puede requerir solo ciertas propiedades de los productos (por ejemplo, `nombre`, `stock` y `disponible`) sin recibir toda la información como en REST.

Además, permite agrupar múltiples operaciones en una sola petición (por ejemplo, obtener productos y luego modificar el stock), lo que reduce la sobrecarga de red y hace la app más eficiente y dinámica.

---

## 2. ¿Cómo se definen los tipos y resolvers en una API con GraphQL?

En Graphene (usado con Flask), los tipos se definen creando clases que heredan de `graphene.ObjectType`. Cada campo del tipo se define como una propiedad de clase (por ejemplo, `nombre = graphene.String()`).

Los resolvers se definen como métodos con el nombre `resolve_<campo>()`, o en el caso de las mutaciones, se implementan como clases que heredan de `graphene.Mutation`, donde se define:
- Los argumentos de entrada (`Arguments`)
- Los campos de salida
- El método `mutate(self, info, args...)` donde se implementa la lógica

---

## 3. ¿Por qué es importante que el backend también actualice `disponible` y no depender solo del frontend?

Porque el backend es la fuente de la verdad. Si el backend no actualiza `disponible`, otros clientes (por ejemplo, otra interfaz o una API externa) podrían obtener datos inconsistentes.

Además, la lógica de disponibilidad depende del stock, por lo tanto debe estar **centralizada** en el backend para garantizar integridad y coherencia, sin importar desde dónde se acceda al sistema.

---

## 4. ¿Cómo garantizas que la lógica de actualización de stock y disponibilidad sea coherente?

En las funciones de mutación (`aumentarStock` y `reducirStock`), se actualiza el stock y se evalúa inmediatamente si el stock es mayor que 0 o no. Según ese valor, se actualiza el campo `disponible`.

Este control está encapsulado dentro del backend, lo que evita depender de la lógica del cliente (frontend) y asegura que el estado siempre sea correcto.

---
