from fastapi import APIRouter, HTTPException, Depends
from .models import Cocktail, Association
from .schemas import CocktailBase, CocktailList, CocktailDB
from .db_config import *
from sqlalchemy.orm import Session


router = APIRouter()


@router.get("/cocktail/{id}", response_model=CocktailBase)
async def getCocktailByID(id:int, db: Session = Depends(get_db)):
    cocktail = db.query(Cocktail).filter(Cocktail.id == id).first()
    if cocktail is None:
        raise HTTPException(status_code=404, detail="Cocktail not found")
    
    return cocktail

@router.get("/cocktail/", response_model=CocktailList)
async def getAllCategories(db: Session = Depends(get_db)):
    cocktails = db.query(Cocktail).all()
    
    return {'cocktails': cocktails}
    
    
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

@router.post("/cocktail/", response_model=CocktailBase, status_code=201)
async def createCocktail(cocktail: CocktailDB, db: Session = Depends(get_db)):
    if db.query(Cocktail).filter(Cocktail.cocktail == cocktail.cocktail).first():
        raise HTTPException(status_code=404, detail="Cocktail already exist")    
    new_cocktail = Cocktail(**cocktail.dict())
    db.add(new_cocktail)
    db.commit()
    db.refresh(new_cocktail)
    return new_cocktail

def deleteCocktailById(id: int, db: Session):
    cocktail = db.query(Cocktail).filter(Cocktail.id == id).first()
    if cocktail is None:
        raise HTTPException(status_code=404, detail="Cocktail not found")
    
    db.delete(cocktail)
    db.commit()
    return {"detail": "Cocktail deleted successfully"}

@router.delete("/cocktail/{cocktail}")
async def deleteCocktailByName(cocktail: str, db: Session = Depends(get_db)):
    try:
        id = int(cocktail)
        return deleteCocktailById(id, db)
    except:
        Exception


    category = db.query(Cocktail).filter(Cocktail.cocktail == cocktail).first()
    if cocktail is None:
        raise HTTPException(status_code=404, detail="Cocktail not found")
    
    db.delete(cocktail)
    db.commit()
    return {"detail": "Cocktail deleted successfully"}

@router.get("/prueba/", response_model=CocktailDB)
async def prueba(db: Session = Depends(get_db)):
    cocktail = db.query(Cocktail).first()
    return cocktail