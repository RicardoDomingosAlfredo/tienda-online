<template>
  <div class="container">
    <h1 class="title">Inventario de Productos</h1>
    <div class="product-list">
      <div class="product-card" v-for="(producto, index) in productos" :key="index">
        <img :src="producto.imagen" alt="Imagen del producto" class="product-image" />
        <h2 class="product-name">{{ producto.nombre }}</h2>
        <p class="product-price">€{{ convertirADolares(producto.precio, tipoCambio).toFixed(2) }}</p>
        <p class="product-stock">Stock: {{ producto.stock }}</p>
        <p class="product-availability" :class="{ available: producto.disponible, unavailable: !producto.disponible }">
          {{ producto.disponible ? 'Disponible' : 'No Disponible' }}
        </p>
        <div class="product-actions">
          <button @click="reducirStock(index)" class="btn reduce" :disabled="!producto.disponible">Reducir Stock</button>
          <button @click="aumentarStock(index)" class="btn increase">Aumentar Stock</button>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import { reactive, watch } from 'vue';

export default {
  setup() {
    const tipoCambio = 0.85; // Tipo de cambio de dólares a euros

    const productos = reactive([
      { nombre: 'Monitor', precio: 130, stock: 5, disponible: true, imagen: 'https://external-content.duckduckgo.com/iu/?u=https%3A%2F%2Ftse1.mm.bing.net%2Fth%3Fid%3DOIP.mx-LO9JyjvzbTL3yttGDWwHaHJ%26pid%3DApi&f=1&ipt=529a55a3056ea72cb90f4b903205fa25deaad6170f9401c19c14201be96520a7&ipo=images' },
      { nombre: 'Ratón', precio: 105, stock: 0, disponible: false, imagen: 'https://external-content.duckduckgo.com/iu/?u=https%3A%2F%2Fi5.walmartimages.com%2Fasr%2F2359c3f8-611d-40c4-88ab-49d4695dfd5f.5b26b18ccda9066176d9e3346f969843.jpeg%3FodnWidth%3D1000%26odnHeight%3D1000%26odnBg%3Dffffff&f=1&nofb=1&ipt=3d271b8348953fb1cb19ea72f54fd2b25fd7f00c8a58c430a4f8433876991b09&ipo=images' },
      { nombre: 'Cargardor pc', precio: 150, stock: 3, disponible: true, imagen: 'https://external-content.duckduckgo.com/iu/?u=https%3A%2F%2Fntcomputacion.com%2Fwp-content%2Fuploads%2F2020%2F02%2Fcargador-original-hp-hstnn-45w-195v-231a-pin-azul-D_NQ_NP_753314-MLA29607371630_032019-F.jpg&f=1&nofb=1&ipt=3e16c5141564940a8e865897858283a57d01f04dfdee42244cf978cc6c966626&ipo=images' },
      { nombre: 'Portatil', precio: 990, stock: 5, disponible: true, imagen: 'https://www.apple.com/newsroom/images/2024/03/apple-unveils-the-new-13-and-15-inch-macbook-air-with-the-powerful-m3-chip/tile/Apple-MacBook-Air-2-up-hero-240304-lp.jpg.og.jpg?202503102112' },
      { nombre: 'Cable USB', precio: 10, stock: 2, disponible: false, imagen: 'https://store.storeimages.cdn-apple.com/4668/as-images.apple.com/is/HRHL2?wid=2994&hei=2994&fmt=jpeg&qlt=95&.v=1717524835340' },
      { nombre: 'Cable de vídeo', precio: 18, stock: 11, disponible: true, imagen: 'https://energitperu.com/wp-content/uploads/2020/06/EPHD0428.jpg' },
    ]);

    productos.forEach((producto) => {
      watch(
        () => producto.stock,
        (nuevoStock) => {
          producto.disponible = nuevoStock > 0;
        }
      );
    });

    const reducirStock = (index) => {
      if (productos[index].stock > 0) {
        productos[index].stock--;
      }
    };

    const aumentarStock = (index) => {
      productos[index].stock++;
    };

    const convertirADolares = (dolares, tipoCambio) => {
      return dolares * tipoCambio;
    };

    return {
      productos,
      reducirStock,
      aumentarStock,
      convertirADolares,
      tipoCambio,
    };
  },
};
</script>
