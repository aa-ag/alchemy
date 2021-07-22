############------------ IMPORTS ------------############
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy import Column, String, Integer, Date, Boolean, Numeric


############------------ GLOBAL VARIABLE(S) ------------############
engine = create_engine('postgresql://usr:pass@localhost:5432/sqlalchemy')

Session = sessionmaker(bind=engine)

Base = declarative_base()

class Product(Base):
    __tablename__ = 'products'
    id=Column(Integer, primary_key=True)
    title=Column('title', String(32))
    in_stock=Column('in_stock', Boolean)
    quantity=Column('quantity', Integer)
    price=Column('price', Numeric)