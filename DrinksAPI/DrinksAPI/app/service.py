from pydantic import BaseModel
from typing import List

class GlassBase(BaseModel):
    glass: str

class GlassCreate(GlassBase):
    pass

class Glass(GlassBase):
    id: int

    class Config:
        orm_mode = True

class CategoryBase(BaseModel):
    category: str

class CategoryCreate(CategoryBase):
    pass

class Category(CategoryBase):
    id: int

    class Config:
        orm_mode = True

class IngredientBase(BaseModel):
    ingredient: str

class IngredientCreate(IngredientBase):
    pass

class Ingredient(IngredientBase):
    id: int

    class Config:
        orm_mode = True

class CocktailBase(BaseModel):
    cocktail: str
    instruction: str
    id_glass: int
    id_category: int
    ingredients: List[int]  # Lista de IDs de ingredientes en lugar de objetos completos

class CocktailCreate(CocktailBase):
    pass

class Cocktail(CocktailBase):
    id: int
    glass: Glass
    category: Category
    ingredients: List[Ingredient] = []  # Puedes dejarlo vacío si no necesitas cargar ingredientes completos

    class Config:
        orm_mode = True
