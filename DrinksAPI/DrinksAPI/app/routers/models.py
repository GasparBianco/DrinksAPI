from sqlalchemy import Column, Integer, String, ForeignKey, Table
from .db_config import Base
from sqlalchemy.orm import relationship


class Glass(Base):
    __tablename__ = "glasses"
    id = Column(Integer, primary_key=True, index=True)
    glass = Column(String(255))

class Category(Base):
    __tablename__ = "categories"
    id = Column(Integer, primary_key=True, index=True)
    category = Column(String(255))

class Association(Base):
    __tablename__ = "relationCocktailIngredient"
    id_cocktail = Column(Integer, ForeignKey("cocktails.id"), primary_key=True)
    id_ingredient = Column(Integer, ForeignKey("ingredients.id"), primary_key=True)
    measure = Column(String(255))
    ingredient = relationship("Ingredient")

class Ingredient(Base):
    __tablename__ = "ingredients"
    id = Column(Integer, primary_key=True)
    ingredient = Column(String(255))
    

class Cocktail(Base):
    __tablename__ = "cocktails"
    id = Column(Integer, primary_key=True)
    cocktail = Column(String(255))
    instruction = Column(String(255))
    id_glass = Column(Integer, ForeignKey('glasses.id', ondelete="SET NULL"))
    id_category = Column(Integer, ForeignKey('categories.id', ondelete="SET NULL"))
    glass = relationship('Glass')
    category = relationship('Category', backref='cocktails')
    ingredients = relationship('Association', cascade="all, delete-orphan")