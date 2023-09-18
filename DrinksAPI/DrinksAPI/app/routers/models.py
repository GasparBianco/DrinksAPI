from sqlalchemy import Column, Integer, String, ForeignKey, Table
from .db_config import Base
from sqlalchemy.orm import relationship

relationCocktailIngredient = Table(
    'relationCocktailIngredient',
    Base.metadata,
    Column('id_cocktail', Integer, ForeignKey('cocktails.id')),
    Column('id_ingredient', Integer, ForeignKey('ingredients.id')),
    Column('measure', String(255))
)

class Glass(Base):
    __tablename__ = "glasses"
    id = Column(Integer, primary_key=True, index=True)
    glass = Column(String(255))

class Category(Base):
    __tablename__ = "categories"
    id = Column(Integer, primary_key=True, index=True)
    category = Column(String(255))

class Ingredient(Base):
    __tablename__ = "ingredients"
    id = Column(Integer, primary_key=True, index=True)
    ingredient = Column(String(255))
    cocktails = relationship('Cocktail', secondary=relationCocktailIngredient, back_populates='ingredients', 
                            primaryjoin="Ingredient.id == relationCocktailIngredient.c.id_ingredient",
                            secondaryjoin="Cocktail.id == relationCocktailIngredient.c.id_cocktail")

class Cocktail(Base):
    __tablename__ = "cocktails"
    id = Column(Integer, primary_key=True, index=True)
    cocktail = Column(String(255))
    instruction = Column(String(255))
    id_glass = Column(Integer, ForeignKey('glasses.id'))
    id_category = Column(Integer, ForeignKey('categories.id'))
    ingredients = relationship('Ingredient', secondary=relationCocktailIngredient, back_populates='cocktails')
    glass = relationship('Glass', backref='cocktails')
    category = relationship('Category', backref='cocktails')
