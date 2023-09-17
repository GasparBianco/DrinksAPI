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

@app.get("/cocktail/{id}", response_model=schemas.Cocktail)
def getCocktailByID(id:int, db: Session = Depends(get_db)):
    cocktail = db.query(Cocktail).filter(Cocktail.id == id).first()
    if cocktail is None:
        raise HTTPException(status_code=404, detail="Cocktail not found")
    
    return cocktail
    
    
@app.get("/cocktail/page/{page}", response_model=schemas.CocktailList)
def getCocktailByID(page:int, db: Session = Depends(get_db)):
    if page <0:
        raise HTTPException(status_code=404, detail="Page cant be less than 0")

    cocktails = []
    for i in range(0,10):
        id = 10 * page + i + 1
        cocktail = db.query(Cocktail).filter(Cocktail.id == id).first()
        if cocktail is not None:
            cocktails.append(cocktail)    

    if cocktails:
        return {'cocktails': cocktails}
    raise HTTPException(status_code=404, detail="Page was to big")
    
    

