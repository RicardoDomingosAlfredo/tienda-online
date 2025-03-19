import { reactive, watch } from 'vue';

export const crearInventario = () => {
  const productos = reactive([
    { nombre: 'Ordenadores', precio: 130, stock: 5, disponible: true },
    { nombre: 'Monitores', precio: 105, stock: 0, disponible: false },
    { nombre: 'Ratón', precio: 150, stock: 3, disponible: true },
    { nombre: 'Portatil', precio: 990, stock: 5, disponible: true},
      { nombre: 'Cable USB', precio: 10, stock: 2, disponible: false},
      { nombre: 'Cable de vídeo', precio: 18, stock: 11, disponible: true},
  ]);

  productos.forEach((producto, index) => {
    watch(
      () => producto.stock,
      (nuevoStock) => {
        producto.disponible = nuevoStock > 0;
      }
    );
  });

  return productos;
};