############------------ IMPORTS ------------############
from sqlalchemy import create_engine, Column
from sqlalchemy import Integer, String
from sqlalchemy.ext.declarative import declarative_base


############------------ GLOBAL VARIABLE(S) ------------############
engine = create_engine('sqlite:///scuderias.db', echo=True)

Base = declarative_base()

############------------ CLASSES ------------############
class Scuderias(Base):
    __tablename__ = "scuderias"

    id = Column(Integer, primary_key=True, nullable=False)
    scuderias_name = Column(String, nullable=False)
    principals_firstname = Column(String, nullable=False)
    principals_lastname = Column(String, nullable=False)
    driver1_firstname = Column(String, nullable=False)
    driver1_lastname = Column(String, nullable=False)
    driver2_firstname = Column(String, nullable=False)
    driver2_lastname = Column(String, nullable=False)
    lastchampionship = Column(String, nullable=False)

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