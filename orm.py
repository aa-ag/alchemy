############------------ IMPORTS ------------############
from sqlalchemy import create_engine, ForeignKey, Column, 
from sqlalchemy import Date, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, backref


############------------ GLOBAL VARIABLE(S) ------------############
engine = create_engine('sqlite:///student.db', echo=True)

Base = declarative_base()

############------------ CLASSES ------------############