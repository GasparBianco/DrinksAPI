from pydantic import BaseModel
from typing import List, Optional
    

class GlassBase(BaseModel):
    id: int
    glass: str

    class Config:
        orm_mode = True   

class GlassList(BaseModel):
    glasses: List[GlassBase] = []


class CategoryBase(BaseModel):
    id: int
    category: str

    class Config:
        orm_mode = True

class CategoryList(BaseModel):
    categories: List[CategoryBase] = []

class IngredientBase(BaseModel):
    id: int
    ingredient: str

    class Config:
        orm_mode = True 

class IngredientList(BaseModel):
    ingredients: List[IngredientBase] = []

class AssociationBase(BaseModel):
    measure: Optional[str]
    ingredient: IngredientBase
    
class CocktailBase(BaseModel):
    id: int
    cocktail: str
    instruction: Optional[str]
    glass: GlassBase
    category: CategoryBase
    ingredients: List[AssociationBase] = []

    class Config:
        orm_mode = True

class CocktailDB(BaseModel):
    cocktail: str
    instruction: Optional[str]
    glass: int
    category: int
    ingredients: List[int] = []


class CocktailList(BaseModel):
    cocktails: List[CocktailBase] = []

