############------------ IMPORTS ------------############
from sqlalchemy import create_engine, ForeignKey, Column
from sqlalchemy import Date, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, backref


############------------ GLOBAL VARIABLE(S) ------------############
engine = create_engine('sqlite:///scuderias.db', echo=True)

Base = declarative_base()

############------------ CLASSES ------------############
class Scuderias(Base):
    __tablename__ = "scuderias"

    id = Column(Integer, primary_key=True)
    scuderias_name = Column(String, max_lenght=80)
    principals_firstname = Column(String, max_lenght=20)
    principals_lastname = Column(String, max_lenght=20)
    driver1_firstname = Column(String, max_lenght=20)
    driver1_lastname = Column(String, max_lenght=20)
    driver2_firstname = Column(String, max_lenght=20)
    driver2_lastname = Column(String, max_lenght=20)
    lastchampionship = Column(Date)

    def __init__(self, scuderias_name, \
        principals_firstname, principals_lastname, \
        driver1_firstname, driver1_lastname, \
            driver2_firstname, driver2_lastname, \
                lastchampionship):
        self.scuderias_name = scuderias_name
        self.principals_firstname = principals_firstname
        self.principals_lastname = principals_lastname
        self.driver1_firstname = driver1_firstname
        self.driver1_lastname = driver1_lastname
        self.driver2_firstname = driver2_firstname
        self.driver2_lastname = driver2_lastname
        self.lastchampionship = lastchampionship

try:
    Base.metadata.create_all(engine)
    print("All set.")
except:
    print("Somthing went wrong.")