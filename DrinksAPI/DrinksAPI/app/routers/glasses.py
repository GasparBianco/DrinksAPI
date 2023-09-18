from fastapi import APIRouter, HTTPException
from .models import Glass
from .schemas import GlassBase, GlassList
from .db_config import *
from sqlalchemy.orm import Session
from fastapi import Depends

router = APIRouter()

@router.get("/glass/{id}", response_model=GlassBase)
def getGlassByID(id:int, db: Session = Depends(get_db)):
    glass = db.query(Glass).filter(Glass.id == id).first()
    if glass is None:
        raise HTTPException(status_code=404, detail="Glass not found")
    
    return glass

@router.get("/glasses/", response_model=GlassList)
def getAllGlasses(db: Session = Depends(get_db)):
    glasses = db.query(Glass).all()
    
    return {'glasses': glasses}