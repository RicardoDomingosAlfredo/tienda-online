const API_URL = 'http://localhost:5000/graphql';

export const obtenerProductos = async () => {
  const res = await fetch(API_URL, {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify({
      query: `
        query {
          productos {
            id
            nombre
            precio
            stock
            disponible
          }
        }
      `
    })
  });
  const data = await res.json();
  return data.data.productos;
};

export const reducirStock = async (id) => {
  await fetch(API_URL, {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify({
      query: `
        mutation {
          reducirStock(id: ${id}) {
            producto {
              id
              stock
              disponible
            }
          }
        }
      `
    })
  });
};

export const aumentarStock = async (id) => {
  await fetch(API_URL, {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify({
      query: `
        mutation {
          aumentarStock(id: ${id}) {
            producto {
              id
              stock
              disponible
            }
          }
        }
      `
    })
  });
};
