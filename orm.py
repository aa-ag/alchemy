############------------ IMPORTS ------------############
from sqlalchemy import create_engine, ForeignKey, Column
from sqlalchemy import Date, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, backref


############------------ GLOBAL VARIABLE(S) ------------############
engine = create_engine('sqlite:///student.db', echo=True)

Base = declarative_base()

############------------ CLASSES ------------############
class Student(Base):
    __tablename__ = "student"

    id = Column(Integer, primary_key=True)
    username = Column(String)
    firstname = Column(String)
    lastname = Column(String)
    school = Column(String)

    def __init__(self, username, firstname, lastname, school):
        self.username = username
        self.firstname = firstname
        self.lastname = lastname
        self.school = school

Base.metadata.create_all(engine)