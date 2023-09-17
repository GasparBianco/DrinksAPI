from pydantic import BaseModel
from typing import List, Optional
    

class Glass(BaseModel):
    id: int
    glass: str

    class Config:
        orm_mode = True    


class Category(BaseModel):
    id: int
    category: str

    class Config:
        orm_mode = True

class Ingredient(BaseModel):
    id: int
    ingredient: str

    class Config:
        orm_mode = True 

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