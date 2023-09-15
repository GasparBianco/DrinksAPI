from pydantic import BaseModel
from typing import List

class GlassDB(BaseModel):

    id: int
    glass: str

    class Config:
        orm_mode=True

class CategoryDB(BaseModel):

    id: int
    category: str
    class Config:
        orm_mode=True

class IngredientDB(BaseModel):

    id: int
    ingredient: str
    class Config:
        orm_mode=True

class CocktailDB(BaseModel):

    id: int
    cocktail: str
    instruction: str
    id_glass: int
    id_category: int
    class Config:
        orm_mode=True

class RelationCocktailIngredientDB(BaseModel):

    idCocktail: int
    idIngredient: int
    measure: str
    class Config:
        orm_mode=True

class Cocktail(BaseModel):

    id: int
    cocktail: str
    instruction: str
    glass: GlassDB
    category: CategoryDB
    ingredient: List[IngredientDB]