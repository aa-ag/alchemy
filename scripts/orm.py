############------------ IMPORTS ------------############
from sqlalchemy import create_engine, Column
from sqlalchemy import Integer, String
from sqlalchemy.ext.declarative import declarative_base
from Crypto.Hash import SHA256
from settings import key

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
        self.scuderias_name = SHA256.new(scuderias_name.encode('utf-8'))
        self.principals_firstname = SHA256.new(principals_firstname.encode('utf-8'))
        self.principals_lastname = SHA256.new(principals_lastname.encode('utf-8'))
        self.driver1_firstname = SHA256.new(driver1_firstname.encode('utf-8'))
        self.driver1_lastname = SHA256.new(driver1_lastname.encode('utf-8'))
        self.driver2_firstname = SHA256.new(driver2_firstname.encode('utf-8'))
        self.driver2_lastname = SHA256.new(driver2_lastname.encode('utf-8'))
        self.lastchampionship = SHA256.new(lastchampionship.encode('utf-8'))

try:
    Base.metadata.create_all(engine)
    print("All set.")
except:
    print("Somthing went wrong.")