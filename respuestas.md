# Respuestas

### 1. ¿Cómo podrías observar un cambio en una propiedad anidada?
Vue no detecta cambios en propiedades anidadas de objetos reactivos automáticamente. Para observar cambios en una propiedad específica dentro de un objeto reactivo, se puede usar `watch()` con `{ deep: true }`.

Ejemplo:
```js
watch(() => objeto.propiedad, (nuevoValor, viejoValor) => {
  console.log('Cambio detectado:', nuevoValor);
}, { deep: true });
```

### 2. ¿Cómo funciona watch() en propiedades específicas dentro de reactive()?
`watch()` permite observar cambios en propiedades dentro de `reactive()`. Para ello, se puede pasar una función que devuelva la propiedad específica a observar.

Ejemplo:
```js
watch(() => objeto.propiedad, (nuevoValor, viejoValor) => {
  console.log('Cambio detectado');
});
```

### 3. ¿Cómo harías que un watch() detecte cambios en stock dentro de un array de productos?
Se puede observar los cambios en el stock de los productos dentro de un array usando `watch()` con `map()`, asegurando que detecte cambios en cada objeto dentro del array.

Ejemplo:
```js
watch(
  () => productos.map(p => p.stock),
  (newStock) => {
    productos.forEach((producto, index) => {
      producto.disponible = newStock[index] > 0;
    });
  },
  { deep: true }
);
```
