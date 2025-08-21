from fastapi import FastAPI, HTTPException
from typing import List

app = FastAPI()

items = []

@app.get("/")
def read_root():
    return {"message": "Welcome to your FastAPI REST API!"}

@app.get("/items", response_model=List[str])
def get_items():
    return items

@app.post("/items")
def add_item(item: str):
    items.append(item)
    return {"message": "Item added", "item": item}

@app.delete("/items/{item_id}")
def delete_item(item_id: int):
    if 0 <= item_id < len(items):
        removed = items.pop(item_id)
        return {"message": "Item deleted", "item": removed}
    raise HTTPException(status_code=404, detail="Item not found")
