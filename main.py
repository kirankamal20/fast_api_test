from fastapi import FastAPI
from pymongo import MongoClient
from pydantic import BaseModel

app = FastAPI()
client = MongoClient("mongodb+srv://Kiran123:Kiran123@cluster0.tqocdec.mongodb.net/?retryWrites=true&w=majority")
db = client["test"]


class Task(BaseModel) :
    title: str
    description: str


@app.post("/items/")
def create_item(item: Task) :
    result = db["kiran"].insert_one(dict(item))
    return {"item_id" : str(result.inserted_id)}
