from fastapi import FastAPI
from pydantic import BaseModel
app = FastAPI()

@app.get("/")

def root():
    return {"Hello":"World!!"}

@app.post("/mobiles")

def root():
    return {"Mob_model":"Moto 60 g",
            "Price":15000,
            "Code":112233}





