from sqlalchemy import Column, Integer, String, create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# URL de connexion à la base de données MySQL
DATABASE_URL = "mysql://admin2:admin@localhost/campus"
DATABASE_URL = "mysql://admin2:admin@localhost/campus"

# Définir la base de données et la session
Base = declarative_base()
engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Définir le modèle de données pour les produits
class Product(Base):
    __tablename__ = "products"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(255), index=True)
    description = Column(String(255), index=True)
    price = Column(Integer)