from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from controller.Controller import Controller

import json

app = FastAPI()

origins = [
    "http://localhost",
    "http://localhost:5173",
]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")  
async def hello():
    return {"message" : "Seja bem vindo"}

@app.get("/person/{person}")
async def get_person(person: str):
    person_information = Controller.get_person(person)
    return person_information

    ## source env/bin/activate
    # uvicorn main:app --reload    