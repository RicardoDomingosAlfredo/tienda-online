from schema import Mutation
from data import productos

def test_modificar_stock():
    mutacion = Mutation()
    result = mutacion.modificar_stock(None, id=2, cantidad=2)
    assert result.producto.stock == 2
    assert result.producto.disponible is True

    result2 = mutacion.modificar_stock(None, id=2, cantidad=-2)
    assert result2.producto.stock == 0
    assert result2.producto.disponible is False

    print("Tests pasados correctamente")

if __name__ == "__main__":
    test_modificar_stock()
