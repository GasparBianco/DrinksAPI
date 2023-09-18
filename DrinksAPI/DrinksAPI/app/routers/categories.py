from fastapi import APIRouter, HTTPException
from .models import Category
from .schemas import CategoryList, CategoryBase
from .db_config import *
from sqlalchemy.orm import Session
from fastapi import Depends


router = APIRouter()

@router.get("/category/{id}", response_model=CategoryBase)
def getCategoryByID(id:int, db: Session = Depends(get_db)):
    category = db.query(Category).filter(Category.id == id).first()
    if category is None:
        raise HTTPException(status_code=404, detail="Category not found")
    
    return category

@router.get("/categories/", response_model=CategoryList)
def getAllCategories(db: Session = Depends(get_db)):
    category = db.query(Category).all()
    
    return {'categories': category}