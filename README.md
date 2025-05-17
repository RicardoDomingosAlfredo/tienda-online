🧠 Comprendiendo la Reactividad en Vue al Gestionar Listas de Objetos

🎯 Objetivo

Este proyecto tiene como finalidad explorar en profundidad el sistema de reactividad de Vue 3, enfocándonos en cómo manejar listas de objetos y detectar cambios en propiedades anidadas. Para lograrlo, implementaremos un sistema de inventario de productos que actualiza su estado de disponibilidad de forma dinámica y reactiva según el stock.
🛒 Contexto

Gestionas una tienda online y necesitas una interfaz que refleje en tiempo real qué productos están disponibles en función de su stock. Cada producto tiene:
nombre (string): Nombre del producto.
precio (número): Precio en euros.
stock (número): Cantidad actual en inventario.
disponible (boolean): Estado de disponibilidad. Es true si el stock es mayor que 0, false en caso contrario.
🔧 Requisitos Técnicos

Tu implementación en Vue debe cumplir con los siguientes puntos:
Cuando el stock de un producto llegue a 0, su propiedad disponible debe cambiar automáticamente a false.
Si el stock aumenta desde 0, disponible debe volver a true.
La interfaz debe actualizarse en tiempo real mostrando qué productos están disponibles o no.
Restricción importante: No se permite el uso de computed. Solo puedes utilizar reactive() y watch() para controlar la reactividad.
🛠️ Tecnologías Utilizadas

Este proyecto está construido con las siguientes herramientas:
✅ Vue 3 con la Composition API
⚡ Vite como bundler y entorno de desarrollo
💻 JavaScript para la lógica de negocio
🎨 HTML y CSS para la estructura visual y estilos básicos
🧩 Conceptos Clave Explorados

Reactividad en objetos y listas con reactive()
Observación de propiedades específicas usando watch()
Actualización condicional de propiedades basadas en otras
Renderizado dinámico de listas con v-for y clases reactivas

