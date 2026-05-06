from fastapi import FastAPI
from pydantic import BaseModel

app=FastAPI()

class Item(BaseModel):
    name: str
    price: float

items={}

# @app.get("/")
# def first_example():
#     return {"message": "Hello, FastAPI!"}

@app.post("/items")
async def create_item(item: Item):
    item_id=len(items)+1
    items[item_id]=item
    return{"id": item_id, "item":item}