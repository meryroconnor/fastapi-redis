from fastapi import APIRouter
from env.schemas.product import Product
from redis_cli import *


routes_product = APIRouter()
db = [{"id": "5493d7ff-8cf5-4fcd-8881-d91c134cfad0",
  "name": "Guantes",
  "price": 3000,
  "date": "2023-06-04 17:46:53.456065"}]
@routes_product.post("/create", response_model=Product)

def create(product: Product):
    try:
        # OPERACION DB
        db.append(product.dict())
        # OPERACION CACHE
        save_hash(key=product)
        return product
    except Exception as e:
        return e

@routes_product.get("/product/{id}")
def get(id: str):
    try:
        return list(filter(lambda field: field["id"] == id, db))[0]
    except Exception as e:
        return e

@routes_product.delete("/delete/{id}")
def get(id: str):
    try:
        product = list(filter(lambda field: field["id"] != id, db))
        if len(product) != 0:
            db.remove(product)
        return {
            "message": "success "
        }
    except Exception as e:
        return e