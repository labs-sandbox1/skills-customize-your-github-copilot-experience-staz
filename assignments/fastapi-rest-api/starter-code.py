# Starter code for FastAPI REST API assignment

from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

# Example resource model
class Item(BaseModel):
    id: int
    name: str
    description: str = None

# In-memory storage for demonstration
items = {}

@app.get("/")
def read_root():
    return {"message": "Welcome to your FastAPI REST API!"}

# Add more endpoints for CRUD operations below...
