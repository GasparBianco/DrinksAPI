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