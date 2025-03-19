#  Comprendiendo la Reactividad en Vue al Manejar Listas de Objetos 

## 🎯 Objetivo
El propósito de este proyecto es comprender cómo funciona la reactividad en Vue al gestionar listas de objetos y detectar cambios en propiedades anidadas. Para ello, implementaremos un sistema de inventario de productos que refleje dinámicamente su disponibilidad según el stock.

## 🛒 Enunciado
Tienes una tienda online y necesitas manejar un inventario de productos en Vue. Cada producto tiene las siguientes propiedades:

- **Nombre** (string): Nombre del producto.
- **Precio** (número): Precio del producto.
- **Stock** (número): Cantidad disponible en inventario.
- **Disponible** (booleano): Indica si el producto está disponible (true si stock > 0, false si stock = 0).

### 🔥 Requisitos
Debes implementar un sistema en Vue donde:

1. Cuando el stock de un producto llegue a 0, la propiedad `disponible` debe cambiar automáticamente a `false`.
2. Si el stock de un producto aumenta desde 0, `disponible` debe cambiar automáticamente a `true`.
3. La interfaz debe reflejar dinámicamente qué productos están disponibles y cuáles no.
4. **No** se permite el uso de `computed`. Solo se pueden emplear `reactive()` y `watch()` para gestionar la reactividad.

## 🛠️ Tecnologías Utilizadas
Este proyecto ha sido desarrollado utilizando las siguientes tecnologías:

-  **Vue3** con Composition API
- **Vite** para el entorno de desarrollo
- **JavaScript** para la lógica del proyecto
- **HTML y CSS** para la estructura y estilos básicos

## ❓ Preguntas a Responder
En el código del proyecto se debe incluir un archivo con respuestas a las siguientes preguntas:

1. **Vue no detecta cambios dentro de objetos reactivos de la forma que esperarías. ¿Cómo podrías observar un cambio en una propiedad anidada?**
2. **`watch()` permite escuchar cambios en propiedades específicas dentro de `reactive()`. Explica cómo funciona.**
3. **¿Cómo harías que un `watch()` detecte cambios en `stock` dentro de un array de productos?**

---
💡 Este ejercicio permitirá explorar en profundidad el funcionamiento de la reactividad en Vue y cómo manejar cambios en estructuras de datos anidadas dentro de `reactive()`. ¡Manos a la obra! 🚀


