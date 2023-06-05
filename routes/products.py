from fastapi import APIRouter
from env.schemas.product import Product
from .redis_cli.crud import *


routes_product = APIRouter()
db = []
@routes_product.post("/create", response_model=Product)

def create(product: Product):
    try:
        # OPERACION DB
        db.append(product.dict())

        # OPERACION CACHE
        save_hash(key=product.dict()["id"], data=product.dict())
        return product
    except Exception as e:
        return e

@routes_product.get("/product/{id}")
def get(id: str):
    try:
        #return list(filter(lambda field: field["id"] == id, db))[0]
        return get_hash(id)
    except Exception as e:
        return e

@routes_product.delete("/delete/{id}")
def delete(id: str):
    # OPERACION DB
    product = list(filter(lambda field: field["id"] != id, db))
    if len(product) != 0:
        db.remove(product)
    # OPERACION CACHE
    delete_hash(key=id, keys=["id","name","price","date"])
    return {
        "message": "success removed"
    }