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
scuderia = Scuderias("Red Bull", "Christian", "Horner", "Max", "Verstappen", "Checo", "Perez", "2013-12-01")
session.add(scuderia)

# try:
#     scuderia = Scuderias("Mercedes", "Toto", "Wolf", "Lews", "Hamilton")
#     session.add(scuderia)
# except:
#     print("Something's not right: are you adding everything? All values are required")

# commit additions to the db
session.commit()