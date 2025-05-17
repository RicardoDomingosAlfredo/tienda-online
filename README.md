#  Inventario de Productos – Vue + Flask + GraphQL

## 🎯 Objetivo

Comprender cómo funciona la **reactividad en Vue 3** al manejar listas de objetos, y cómo integrarla con un backend desarrollado en **Flask + GraphQL**.  
La aplicación gestiona un inventario de productos donde los cambios de stock y disponibilidad se reflejan **dinámicamente**, tanto en el **frontend** como en el **backend**.

---

## 🛠️ Tecnologías Utilizadas

### Frontend
-  Vue 3 con Composition API  
-  Vite como entorno de desarrollo  
-  CSS personalizado  

###  Backend
-  Python 3  
-  Flask  
-  Graphene (GraphQL para Python)  

---

## Funcionalidades

### Frontend (Vue)

-  Muestra una lista de productos con imagen, nombre, precio y stock.
-  El botón **"Reducir stock"** decrementa el stock.
-  El botón **"Aumentar stock"** incrementa el stock.
-  Si el stock llega a `0`, `disponible` cambia automáticamente a `false` y se desactiva el botón.
-  Si el stock sube desde `0`, `disponible` vuelve a `true`.

### Backend (Flask + GraphQL)

- 🗂️ Base de datos en memoria:
  ```python
  { id, nombre, precio, stock, disponible }
