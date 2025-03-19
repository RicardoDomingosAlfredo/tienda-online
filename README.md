# Comprendiendo la Reactividad en Vue al Manejar Listas de Objetos

Objetivo

El propósito de este proyecto es comprender cómo funciona la reactividad en Vue al gestionar listas de objetos y detectar cambios en propiedades anidadas. Para ello, implementaremos un sistema de inventario de productos que refleje dinámicamente su disponibilidad según el stock.

Enunciado

Tienes una tienda online y necesitas manejar un inventario de productos en Vue. Cada producto tiene las siguientes propiedades:

nombre (string): Nombre del producto.

precio (número): Precio del producto.

stock (número): Cantidad disponible en inventario.

disponible (booleano): Indica si el producto está disponible (true si stock > 0, false si stock = 0).

Requisitos

Debes implementar un sistema en Vue donde:

Cuando el stock de un producto llegue a 0, la propiedad disponible debe cambiar automáticamente a false.

Si el stock de un producto aumenta desde 0, disponible debe cambiar automáticamente a true.

La interfaz debe reflejar dinámicamente qué productos están disponibles y cuáles no.

No se permite el uso de computed. Solo se pueden emplear reactive() y watch() para gestionar la reactividad.

