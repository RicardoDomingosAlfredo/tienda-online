##Inventario de Productos – Vue + Flask + GraphQL##

🎯 Objetivo

El objetivo de este proyecto es comprender cómo funciona la reactividad en Vue 3 al manejar listas de objetos, y cómo integrarla con un backend desarrollado en Flask + GraphQL. La aplicación gestiona un inventario de productos donde se reflejan dinámicamente los cambios de stock y disponibilidad, tanto en frontend como en backend.
🛠️ Tecnologías Utilizadas

##Frontend##
-Vue 3 con Composition API
-Vite como entorno de desarrollo
-CSS personalizados

##Backend##
 -Python 3
 -Flask
 -Graphene para la API GraphQL
 
 ##Funcionalidades##

##Frontend (Vue)##
Muestra una lista de productos con imagen, nombre, precio y stock.
El botón "Reducir stock" decrementa el valor del stock, y "Aumentar stock" lo incrementa.
Si el stock llega a 0, disponible cambia automáticamente a false y se desactiva el botón.
Si el stock sube desde 0, disponible vuelve a true.

##Backend (Flask + GraphQL)##
Base de datos en memoria (lista de productos con: id, nombre, precio, stock, disponible).
Query: permite obtener todos los productos.
Mutations:
aumentarStock(id)
reducirStock(id)
La lógica de disponibilidad (disponible = stock > 0) se actualiza automáticamente en el backend, independientemente del frontend.
