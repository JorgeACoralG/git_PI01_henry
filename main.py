from fastapi import FastAPI
import pydantic
from pydantic import BaseModel

app = FastAPI()

## http://127.0.0.1:8000

@app.get("/")
def index ():
    return {"message" : "Hola, Pythonianos"}

@app.get("/libros/{id}")
def mostrar_libro(id):
    return {"data": id} #Lo toma como String

@app.get("/librosInt/{id}")
def mostrar_libro(id: int):
    return {"data": id} #Lo toma como Interger

## Api lista y funcionando

class Libro(BaseModel): ## Asegurar tipo de adto definido en las anotaciones
    titulo: str
    autor: str
    paginas: int
    editorial: str

## PAra ver la documentacion, seria http://127.0.0.1:8000/docs