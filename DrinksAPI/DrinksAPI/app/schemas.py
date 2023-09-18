from pydantic import BaseModel
from typing import List, Optional
    

class Glass(BaseModel):
    id: int
    glass: str

    class Config:
        orm_mode = True   

class GlassList(BaseModel):
    glasses: List[Glass] = []


class Category(BaseModel):
    id: int
    category: str

    class Config:
        orm_mode = True

class CategoryList(BaseModel):
    categories: List[Category] = []

class Ingredient(BaseModel):
    id: int
    ingredient: str

    class Config:
        orm_mode = True 

class IngredientList(BaseModel):
    ingredients: List[Ingredient] = []

class Cocktail(BaseModel):
    id: int
    cocktail: str
    instruction: Optional[str]
    glass: Glass
    category: Category
    ingredients: List[Ingredient] = []

    class Config:
        orm_mode = True

class CocktailList(BaseModel):
    cocktails: List[Cocktail] = []