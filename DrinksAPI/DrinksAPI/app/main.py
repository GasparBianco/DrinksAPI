from fastapi import FastAPI, HTTPException
from starlette.responses import RedirectResponse
from sqlalchemy.orm import Session
from db_config import SessionLocal
from models import *
from fastapi import Depends
import schemas



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
    
    

@app.get("/category/{id}", response_model=schemas.Category)
def getCategoryByID(id:int, db: Session = Depends(get_db)):
    category = db.query(Category).filter(Category.id == id).first()
    if category is None:
        raise HTTPException(status_code=404, detail="Category not found")
    
    return category

@app.get("/categories/", response_model=schemas.CategoryList)
def getAllCategories(db: Session = Depends(get_db)):
    category = db.query(Category).all()
    
    return {'categories': category}

@app.get("/glass/{id}", response_model=schemas.Glass)
def getGlassByID(id:int, db: Session = Depends(get_db)):
    glass = db.query(Glass).filter(Glass.id == id).first()
    if glass is None:
        raise HTTPException(status_code=404, detail="Glass not found")
    
    return glass

@app.get("/glasses/", response_model=schemas.GlassList)
def getAllGlasses(db: Session = Depends(get_db)):
    glasses = db.query(Glass).all()
    
    return {'glasses': glasses}

@app.get("/ingredient/{id}", response_model=schemas.Ingredient)
def getIngredientByID(id:int, db: Session = Depends(get_db)):
    ingredient = db.query(Ingredient).filter(Ingredient.id == id).first()
    if ingredient is None:
        raise HTTPException(status_code=404, detail="Ingredient not found")
    
    return ingredient

@app.get("/ingredient/page/{page}", response_model=schemas.IngredientList)
def getIngredientPage(page:int, db: Session = Depends(get_db)):
    if page <0:
        raise HTTPException(status_code=404, detail="Page cant be less than 0")

    ingredients = []
    for i in range(0,10):
        id = 10 * page + i + 1
        ingredient = db.query(Ingredient).filter(Ingredient.id == id).first()
        if ingredient is not None:
            ingredients.append(ingredient)    

    if ingredients:
        return {'ingredients': ingredients}
    raise HTTPException(status_code=404, detail="Page was to big")