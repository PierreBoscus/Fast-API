from fastapi import FastAPI

# Création d'une instance fastAPI
app = FastAPI()

# Definition d'une route 
@app.get("/")
def road_root():
    return{"message":"Bonjour"}

# Definition d'une route get avec un: parametre 
@app.get("/items/{item_id}")
def road_item(item_id, q: str = None):
    return{"item_id": item_id, "q": q}
