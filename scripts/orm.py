############------------ IMPORTS ------------############
from sqlalchemy import create_engine, Column
from sqlalchemy import Integer, String
from sqlalchemy.ext.declarative import declarative_base
from cryptography.fernet import Fernet

############------------ GLOBAL VARIABLE(S) ------------############
engine = create_engine('sqlite:///scuderias.db?charset=utf8', echo=True)

Base = declarative_base()

key = Fernet.generate_key()

f = Fernet(key)

############------------ CLASSES ------------############
class Scuderias(Base):
    __tablename__ = "scuderias"

    id = Column(Integer, primary_key=True, nullable=False)
    scuderias_name = Column(String, max_lenght=80, nullable=False)
    principals_firstname = Column(String, max_lenght=20, nullable=False)
    principals_lastname = Column(String, max_lenght=20, nullable=False)
    driver1_firstname = Column(String, max_lenght=20, nullable=False)
    driver1_lastname = Column(String, max_lenght=20, nullable=False)
    driver2_firstname = Column(String, max_lenght=20, nullable=False)
    driver2_lastname = Column(String, max_lenght=20, nullable=False)
    lastchampionship = Column(String, nullable=False)

    def __init__(self, scuderias_name, \
        principals_firstname, principals_lastname, \
        driver1_firstname, driver1_lastname, \
            driver2_firstname, driver2_lastname, \
                lastchampionship):
        self.scuderias_name = f.encrypt(scuderias_name)
        self.principals_firstname = f.encrypt(principals_firstname)
        self.principals_lastname = f.encrypt(principals_lastname)
        self.driver1_firstname = f.encrypt(driver1_firstname)
        self.driver1_lastname = f.encrypt(driver1_lastname)
        self.driver2_firstname = f.encrypt(driver2_firstname)
        self.driver2_lastname = f.encrypt(driver2_lastname)
        self.lastchampionship = f.encrypt(lastchampionship)

try:
    Base.metadata.create_all(engine)
    print("All set.")
except:
    print("Somthing went wrong.")