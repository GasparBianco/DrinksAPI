from pydantic import BaseModel
from typing import List, Optional
    

class GlassBase(BaseModel):
    id: int
    

    class Config:
        orm_mode = True

class GlassFull(GlassBase):
    glass: str

class GlassList(BaseModel):
    glasses: List[GlassFull] = []


class CategoryBase(BaseModel):
    id: int

    class Config:
        orm_mode = True

class CategoryFull(CategoryBase):
    category:str

class CategoryList(BaseModel):
    categories: List[CategoryBase] = []

class IngredientBase(BaseModel):
    id: int


    class Config:
        orm_mode = True 

class IngredientFull(IngredientBase):
    ingredient: str

class IngredientList(BaseModel):
    ingredients: List[IngredientFull] = []

class AssociationBase(BaseModel):
    measure: Optional[str]
    ingredient: IngredientBase
    
    class Config:
        orm_mode = True

class AssciationFull(AssociationBase):
    ingredient: IngredientFull

class CocktailBase(BaseModel):
    id: int
    cocktail: str
    instruction: Optional[str]
    glass: GlassFull
    category: CategoryFull
    ingredients: List[AssociationBase] = []

    class Config:
        orm_mode = True

class IngredientCocktail(BaseModel):
    id_ingredient: IngredientBase
    measure: Optional[str]

class CocktailDB(BaseModel):
    cocktail: str
    instruction: Optional[str]
    glass: GlassBase
    category: CategoryBase
    ingredients: List[AssociationBase] = []


class CocktailList(BaseModel):
    cocktails: List[CocktailBase] = []

