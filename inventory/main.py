from math import prod
from fastapi import FastAPI, HTTPException, Response
from fastapi.middleware.cors import CORSMiddleware
from inventory.db.models import Product
from redis_om.model.model import NotFoundError

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],
    allow_methods=["*"],
    allow_headers=["*"],
)


def format(primary_key: str):
    product = Product.get(primary_key)
    return {
        "id": product.pk,
        "name": product.name,
        "price": product.price,
        "quantity": product.quantity,
    }


@app.get("/products", response_model=list[Product])
async def get_all_products():
    return [format(primary_key) for primary_key in Product.all_pks()]


@app.post("/products", response_model=Product)
async def create_product(product: Product):
    return product.save()


@app.get("/products/{primary_key}", response_model=Product)
async def get_product_by_id(primary_key: str):
    try:
        return Product.get(primary_key)
    except NotFoundError:
        raise HTTPException(status_code=404)


@app.delete("/products/{primary_key}")
async def delete_product_by_id(primary_key: str):
    response = Product.delete(primary_key)
    match response:
        case 0:
            return Response(status_code=404)
        case 1:
            return Response(status_code=200)
