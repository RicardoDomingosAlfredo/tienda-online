import graphene
from graphene import ObjectType, Int, String, Float, Boolean
from data import productos, actualizar_disponibilidad

class ProductoType(ObjectType):
    id = Int()
    nombre = String()
    precio = Float()
    stock = Int()
    disponible = Boolean()

class Query(ObjectType):
    productos = graphene.List(ProductoType)

    def resolve_productos(root, info):
        return productos

class ModificarStock(graphene.Mutation):
    class Arguments:
        id = Int(required=True)
        cantidad = Int(required=True) 

    producto = graphene.Field(ProductoType)

    def mutate(root, info, id, cantidad):
        for p in productos:
            if p["id"] == id:
                p["stock"] += cantidad
                if p["stock"] < 0:
                    p["stock"] = 0  
                actualizar_disponibilidad(p)
                return ModificarStock(producto=p)
        raise Exception("Producto no encontrado")

class Mutation(ObjectType):
    modificar_stock = ModificarStock.Field()
