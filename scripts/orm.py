############------------ IMPORTS ------------############
from sqlalchemy import create_engine, Column
from sqlalchemy import Integer, String
from sqlalchemy.ext.declarative import declarative_base
import hashlib

############------------ GLOBAL VARIABLE(S) ------------############
engine = create_engine('sqlite:///scuderias.db?charset=utf8', echo=True)

Base = declarative_base()


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
        self.scuderias_name = hashlib.sha3_256(scuderias_name).hexdigest()
        self.principals_firstname = hashlib.sha3_256(principals_firstname).hexdigest()
        self.principals_lastname = hashlib.sha3_256(principals_lastname).hexdigest()
        self.driver1_firstname = hashlib.sha3_256(driver1_firstname).hexdigest()
        self.driver1_lastname = hashlib.sha3_256(driver1_lastname).hexdigest()
        self.driver2_firstname = hashlib.sha3_256(driver2_firstname).hexdigest()
        self.driver2_lastname = hashlib.sha3_256(driver2_lastname).hexdigest()
        self.lastchampionship = hashlib.sha3_256(lastchampionship).hexdigest()

try:
    Base.metadata.create_all(engine)
    print("All set.")
except:
    print("Somthing went wrong.")