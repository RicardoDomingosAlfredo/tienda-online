#  Inventario de Productos – Vue + Flask + GraphQL

## 🎯 Objetivo

Este proyecto tiene como finalidad **comprender la reactividad en Vue 3** al manejar listas de objetos, e integrarla con un backend construido en **Flask + GraphQL**.  
Simula el inventario de una tienda online, donde los cambios en el stock afectan directamente la disponibilidad de los productos, tanto en el **frontend** como en el **backend**.

---

##  Tecnologías Utilizadas

###  Frontend
- Vue 3 + Composition API
-  Vite
- CSS personalizado
- 🌐 Axios (para conectar con GraphQL)

###  Backend
-  Python 3
-  Flask
-  Graphene (GraphQL para Python)

---

## Funcionalidades

### Frontend (Vue)
-  Muestra productos con imagen, nombre, precio y stock.
-  Botón para **reducir stock** (si llega a 0, el producto se desactiva).
-  Botón para **aumentar stock** (si sube desde 0, vuelve a estar disponible).
-  Reactividad completa usando `reactive()` y `watch()` (sin `computed`).

### Backend (Flask + GraphQL)
-  Base de datos en memoria con productos:  
  `id`, `nombre`, `precio`, `stock`, `disponible`
-  Query para obtener todos los productos.
-  Mutations para:
  - `aumentarStock(id)`
  - `reducirStock(id)`
- 🧠 La lógica de `disponible` depende del `stock` y se actualiza automáticamente (incluso sin frontend).

---

## ⚙ Instalación y Ejecución

### 📌 Requisitos previos
- Node.js (v16+)
- Python 3.10+
- pip (gestor de paquetes de Python)

---

### 🖥️ 1. Backend – Flask + GraphQL

```bash
# Entra a la carpeta del backend
cd backend

# Instala las dependencias
pip install -r requirements.txt

# Ejecuta la API
python app.py
