from sqlalchemy.orm import Session
from db_config import SessionLocal
from models import Category, Cocktail, Ingredient
from fastapi import Depends



def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

def getCocktailByID(cocktail_id: int, db: Session = Depends(get_db)):
    cocktail = db.query(Cocktail).filter(Cocktail.id == cocktail_id).first()
    return cocktail
