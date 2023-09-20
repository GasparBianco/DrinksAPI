from fastapi import APIRouter, HTTPException, Depends
from .models import Glass
from .schemas import GlassBase, GlassList, GlassCreate
from .db_config import *
from sqlalchemy.orm import Session


router = APIRouter()

@router.get("/glass/{id}", response_model=GlassBase)
async def getGlassByID(id:int, db: Session = Depends(get_db)):
    glass = db.query(Glass).filter(Glass.id == id).first()
    if glass is None:
        raise HTTPException(status_code=404, detail="Glass not found")
    
    return glass

@router.get("/glass/", response_model=GlassList)
async def getAllGlasses(db: Session = Depends(get_db)):
    glasses = db.query(Glass).all()
    
    return {'glasses': glasses}

@router.post("/glass/", response_model=GlassBase, status_code=201)
async def createGlass(glass: GlassCreate, db: Session = Depends(get_db)):
    if db.query(Glass).filter(Glass.glass == glass.glass).first():
        raise HTTPException(status_code=404, detail="Glass already exist")
    
    new_glass = Glass(glass=glass.glass)
    db.add(new_glass)
    db.commit()
    db.refresh(new_glass)
    return new_glass

def deleteGlassById(id: int, db: Session):
    glass = db.query(Glass).filter(Glass.id == id).first()
    if glass is None:
        raise HTTPException(status_code=404, detail="Glass not found")
    
    db.delete(glass)
    db.commit()
    return {"detail": "Glass deleted successfully"}

@router.delete("/glass/{glass}")
async def deleteGlassByName(glass: str, db: Session = Depends(get_db)):
    try:
        id = int(glass)
        return deleteGlassById(id, db)
    except:
        ValueError


    glass = db.query(Glass).filter(Glass.glass == glass).first()
    if glass is None:
        raise HTTPException(status_code=404, detail="Glass not found")
    
    db.delete(glass)
    db.commit()
    return {"detail": "Glass deleted successfully"}