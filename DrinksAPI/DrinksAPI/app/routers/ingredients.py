from fastapi import APIRouter, HTTPException, Depends
from .models import Ingredient
from .schemas import IngredientBase, IngredientList
from .db_config import *
from sqlalchemy.orm import Session


router = APIRouter()

@router.get("/ingredient/{id}", response_model=IngredientBase)
async def getIngredientByID(id:int, db: Session = Depends(get_db)):
    ingredient = db.query(Ingredient).filter(Ingredient.id == id).first()
    if ingredient is None:
        raise HTTPException(status_code=404, detail="Ingredient not found")
    
    return ingredient

@router.get("/ingredient/page/{page}", response_model=IngredientList)
async def getIngredientPage(page:int, db: Session = Depends(get_db)):
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

@router.post("/ingredient/", response_model=IngredientBase, status_code=201)
async def createIngredient(ingredient: str, db: Session = Depends(get_db)):
    if db.query(Ingredient).filter(Ingredient.ingredient == ingredient).first():
        raise HTTPException(status_code=404, detail="Ingredient already exist")
    
    new_ingredient = Ingredient(category=ingredient)
    db.add(new_ingredient)
    db.commit()
    db.refresh(new_ingredient)
    return new_ingredient

def deleteIngredientById(id: int, db: Session):
    ingredient = db.query(Ingredient).filter(Ingredient.id == id).first()
    if ingredient is None:
        raise HTTPException(status_code=404, detail="Ingredient not found")
    
    db.delete(ingredient)
    db.commit()
    return {"detail": "Ingredient deleted successfully"}

@router.delete("/ingredient/{ingredient}")
async def deleteIngredientByName(ingredient: str, db: Session = Depends(get_db)):
    try:
        id = int(ingredient)
        return deleteIngredientById(id, db)
    except:
        Exception


    ingredient = db.query(Ingredient).filter(Ingredient.ingredient == ingredient).first()
    if ingredient is None:
        raise HTTPException(status_code=404, detail="Ingrdient not found")
    
    db.delete(ingredient)
    db.commit()
    return {"detail": "Ingredient deleted successfully"}