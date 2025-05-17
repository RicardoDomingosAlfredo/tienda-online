from flask import Flask, request, jsonify
from flask_cors import CORS
from graphene import ObjectType, String, Schema, Field, Int, Float, Boolean, List, Mutation
productos = [
    {"id": 1, "nombre": "Monitor", "precio": 130.0, "stock": 5, "disponible": True},
    {"id": 2, "nombre": "Ratón", "precio": 105.0, "stock": 0, "disponible": False},
    {"id": 3, "nombre": "Cargador", "precio": 150.0, "stock": 3, "disponible": True},
]
class ProductoType(ObjectType):
    id = Int()
    nombre = String()
    precio = Float()
    stock = Int()
    disponible = Boolean()
class Query(ObjectType):
    productos = List(ProductoType)

    def resolve_productos(self, info):
        return productos
class ReducirStock(Mutation):
    class Arguments:
        id = Int(required=True)

    producto = Field(lambda: ProductoType)

    def mutate(self, info, id):
        for p in productos:
            if p["id"] == id:
                if p["stock"] > 0:
                    p["stock"] -= 1
                p["disponible"] = p["stock"] > 0
                return ReducirStock(producto=p)
        return ReducirStock(producto=None)
class AumentarStock(Mutation):
    class Arguments:
        id = Int(required=True)

    producto = Field(lambda: ProductoType)

    def mutate(self, info, id):
        for p in productos:
            if p["id"] == id:
                p["stock"] += 1
                p["disponible"] = p["stock"] > 0
                return AumentarStock(producto=p)
        return AumentarStock(producto=None)

class Mutation(ObjectType):
    reducir_stock = ReducirStock.Field()
    aumentar_stock = AumentarStock.Field()
app = Flask(__name__)
CORS(app)
schema = Schema(query=Query, mutation=Mutation)

@app.route("/graphql", methods=["POST"])
def graphql_api():
    data = request.get_json()
    success, result = schema.execute_sync(
        data.get("query"),
        variable_values=data.get("variables")
    )
    return jsonify(result.data)

if __name__ == "__main__":
    app.run(debug=True)
