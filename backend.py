from fastapi import FastAPI
from pydantic import BaseModel
from typing import List
import uvicorn

app = FastAPI()

# Database Simluation (Asli project mein MongoDB use karein)
products = []
orders = []

class Product(BaseModel):
    id: int
    name: str
    price: float
    stock: int
    category: str

@app.post("/add-product")
def add_product(item: Product):
    products.append(item)
    return {"status": "Success", "message": f"{item.name} added!"}

@app.get("/get-products")
def get_products():
    return products

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)