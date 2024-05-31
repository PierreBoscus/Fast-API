from pydantic import BaseModel

# Schéma de base pour un produit
class ProductBase(BaseModel):
    name: str
    description: str
    price: int

# Schéma pour la création d'un produit
class ProductCreate(ProductBase):
    pass

# Schéma pour un produit avec ID
class Product(ProductBase):
    id: int

    class Config:
        orm_mode = True