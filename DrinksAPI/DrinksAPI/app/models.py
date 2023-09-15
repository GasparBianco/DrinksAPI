from pydantic import BaseModel

class Glass(BaseModel):

    id: int
    glass: str

class Category(BaseModel):

    id: int
    category: str

class Cocktail(BaseModel):

    id: int
    cocktail: str
    intruction: str
    id_glass: int
    id_category: int

    