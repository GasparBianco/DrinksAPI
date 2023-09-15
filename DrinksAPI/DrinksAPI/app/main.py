from fastapi import FastAPI, HTTPException
from repository import *
from starlette.responses import RedirectResponse
from sqlalchemy.orm import Session
from db_config import SessionLocal
from models import Category, Cocktail, Ingredient
from fastapi import Depends
import schemas
import service


app = FastAPI()

@app.get("/")
def main():
    return RedirectResponse(url="/docs/")





def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.get("/cocktail/", response_model=service.Cocktail)
def getCocktailByID(db: Session = Depends(get_db)):
    cocktail = db.query(Cocktail).filter(Cocktail.id == 2).first()
    return cocktail


async def CocktailByID(id):
    return getCocktailByID(id)


