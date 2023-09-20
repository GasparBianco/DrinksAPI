from fastapi import APIRouter, HTTPException, Depends
from .models import Category
from .schemas import CategoryList, CategoryBase, CategoryCreate
from .db_config import *
from sqlalchemy.orm import Session



router = APIRouter()

@router.get("/category/{id}", response_model=CategoryBase)
async def getCategoryByID(id:int, db: Session = Depends(get_db)):
    category = db.query(Category).filter(Category.id == id).first()
    if category is None:
        raise HTTPException(status_code=404, detail="Category not found")
    
    return category

@router.get("/category/", response_model=CategoryList)
async def getAllCategories(db: Session = Depends(get_db)):
    category = db.query(Category).all()
    
    return {'categories': category}

@router.post("/category/", response_model=CategoryBase, status_code=201)
async def create_category_endpoint(category: CategoryCreate, db: Session = Depends(get_db)):
    if db.query(Category).filter(Category.category == category.category).first():
        raise HTTPException(status_code=404, detail="Category already exist")
    
    new_category = Category(category=category.category)
    db.add(new_category)
    db.commit()
    db.refresh(new_category)
    return new_category

def deleteCategoryById(id: int, db: Session):
    category = db.query(Category).filter(Category.id == id).first()
    if category is None:
        raise HTTPException(status_code=404, detail="Category not found")
    
    db.delete(category)
    db.commit()
    return {"detail": "Category deleted successfully"}

@router.delete("/category/{category}")
async def deleteCategoryByName(category: str, db: Session = Depends(get_db)):
    try:
        id = int(category)
        return deleteCategoryById(id, db)
    except:
        Exception


    category = db.query(Category).filter(Category.category == category).first()
    if category is None:
        raise HTTPException(status_code=404, detail="Category not found")
    
    db.delete(category)
    db.commit()
    return {"detail": "Category deleted successfully"}



