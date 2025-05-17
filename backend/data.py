productos = [
    {'id': 1, 'nombre': 'Monitor', 'precio': 130.0, 'stock': 5, 'disponible': True},
    {'id': 2, 'nombre': 'Ratón', 'precio': 105.0, 'stock': 0, 'disponible': False},
    {'id': 3, 'nombre': 'Cargador PC', 'precio': 150.0, 'stock': 3, 'disponible': True},
    {'id': 4, 'nombre': 'Portátil', 'precio': 990.0, 'stock': 5, 'disponible': True},
    {'id': 5, 'nombre': 'Cable USB', 'precio': 10.0, 'stock': 2, 'disponible': True},
    {'id': 6, 'nombre': 'Cable de vídeo', 'precio': 18.0, 'stock': 11, 'disponible': True},
]

def actualizar_disponibilidad(producto):
    producto["disponible"] = producto["stock"] > 0
