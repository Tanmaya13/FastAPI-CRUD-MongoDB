"""Execution starts fom this file"""

from fastapi import FastAPI
import db                       # db.py file is imported here
import models

app = FastAPI()

@app.get("/")
def root():
    return {"message":"welcome to API"}


@app.get("/all")
def get_all():
    data = db.all()             # db.all() represents, in db.py file there is an all() function that is executed and the response in stored in data
    return {"data":data}


@app.get("/get")
def get_one(name:str):
    data = db.get_one(name)
    return {"data":data}


@app.post("/create")
def create(data : models.DemoDB):
    data = models.DemoDB(name = data.name, description = data.description)
    id = db.create(data)
    return {"created":True, "inserted_id" : id}


@app.delete("/delete")
def delete(name : str):
    data = db.delete(name)
    return {"deleted":True, "deleted_count":data}


@app.put("/update")
def update(data : models.DemoDB):
    data = db.update(data)
    return {"updated":True , "updated_count":data}
    
