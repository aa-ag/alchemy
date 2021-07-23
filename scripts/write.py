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
scuderia = Scuderias("Red Bull".encode('utf-8'), \
    "Christian".encode('utf-8'), \
        "Horner".encode('utf-8'), \
            "Max".encode('utf-8'), \
                "Verstappen".encode('utf-8'), \
                    "Checo".encode('utf-8'), \
                        "Perez".encode('utf-8'),\
                             "2013-12-01".encode('utf-8'))

# try:
#     scuderia = Scuderias("Mercedes", "Toto", "Wolf", "Lews", "Hamilton")
#     session.add(scuderia)
# except:
#     print("Something's not right: are you adding everything? All values are required")

# commit additions to the db
session.commit()