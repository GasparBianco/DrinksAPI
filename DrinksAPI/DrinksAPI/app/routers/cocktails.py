from fastapi import APIRouter, HTTPException, Depends
from .models import Cocktail
from .schemas import CocktailBase, CocktailList
from .db_config import *
from sqlalchemy.orm import Session


router = APIRouter()

@router.get("/cocktail/{id}", response_model=CocktailBase)
async def getCocktailByID(id:int, db: Session = Depends(get_db)):
    cocktail = db.query(Cocktail).filter(Cocktail.id == id).first()
    if cocktail is None:
        raise HTTPException(status_code=404, detail="Cocktail not found")
    
    return cocktail
    
    
@router.get("/cocktail/page/{page}", response_model=CocktailList)
async def getCocktailByID(page:int, db: Session = Depends(get_db)):
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