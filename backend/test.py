import pytest # type: ignore
from app import app, productos

@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

def ejecutar_query(client, query):
    res = client.post('/graphql', json={'query': query})
    return res.get_json()

def test_query_productos(client):
    query = """
    query {
        productos {
            id
            nombre
            precio
            stock
            disponible
        }
    }
    """
    data = ejecutar_query(client, query)
    assert "productos" in data
    assert isinstance(data["productos"], list)
    assert len(data["productos"]) > 0
    p = data["productos"][0]
    assert "id" in p and "nombre" in p and "precio" in p and "stock" in p and "disponible" in p

def test_reducir_stock(client):
    id_producto = 1
    producto = next(p for p in productos if p["id"] == id_producto)
    stock_inicial = producto["stock"]

    mutation = f"""
    mutation {{
        reducirStock(id: {id_producto}) {{
            producto {{
                id
                stock
                disponible
            }}
        }}
    }}
    """
    data = ejecutar_query(client, mutation)
    nuevo_stock = data["reducirStock"]["producto"]["stock"]

    assert nuevo_stock == max(0, stock_inicial - 1)

def test_aumentar_stock(client):
    id_producto = 2 
    producto = next(p for p in productos if p["id"] == id_producto)
    stock_inicial = producto["stock"]

    mutation = f"""
    mutation {{
        aumentarStock(id: {id_producto}) {{
            producto {{
                id
                stock
                disponible
            }}
        }}
    }}
    """
    data = ejecutar_query(client, mutation)
    nuevo_stock = data["aumentarStock"]["producto"]["stock"]
    disponible = data["aumentarStock"]["producto"]["disponible"]

    assert nuevo_stock == stock_inicial + 1
    if stock_inicial == 0:
        assert disponible == True

def test_stock_no_negativo(client):
    id_producto = 2
    mutation = f"""
    mutation {{
        reducirStock(id: {id_producto}) {{
            producto {{
                stock
            }}
        }}
    }}
    """

    for _ in range(5):
        data = ejecutar_query(client, mutation)

    stock_final = data["reducirStock"]["producto"]["stock"]
    assert stock_final == 0
