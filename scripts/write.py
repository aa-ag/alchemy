############------------ IMPORTS ------------############
import datetime
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from orm import *


############------------ GLOBAL VARIABLE(S) ------------############
engine = create_engine('sqlite:///scuderias.db', echo=True)

# create a session
Session = sessionmaker(bind=engine)
session = Session()

# create objects
scuderia = Scuderias("Red Bull", "Christian", "Horner", "Max", "Verstappen", "Checo", "Perez", "2013")
session.add(scuderia)

# commit additions to the db
session.commit()