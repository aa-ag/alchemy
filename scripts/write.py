############------------ IMPORTS ------------############
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from orm import *
import re


############------------ GLOBAL VARIABLE(S) ------------############
engine = create_engine('sqlite:///scuderias.db', echo=True)

# create a session
Session = sessionmaker(bind=engine)
session = Session()

# create objects
try:
    scuderias_name = "Red Bull"
    principals_firstname = "To to"
    principals_lastname = "Wolf"
    driver1_firstname = "Lews"
    driver1_lastname = "Hamilton"
    driver2_firstname = "Valteri"
    driver2_lastname = "Bottas"
    lastchampionship = "2021-12-01"

    if principals_firstname.isalpha():

        scuderia = Scuderias(scuderias_name, principals_firstname, \
                        principals_lastname, driver1_firstname, driver1_lastname, \
                        driver2_firstname, driver2_lastname, lastchampionship )

        session.add(scuderia)
    print("Principal's name must only have letters from the alphabet")

except:
    print("Something's not right: are you adding everything? All values are required")

# try:
#     scuderia = Scuderias("Mercedes", "Toto", "Wolf", "Lews", "Hamilton", "Valteri", "Bottas", "2021-12-01")
#     session.add(scuderia)
# except:
#     print("Something's not right: are you adding everything? All values are required")

# commit additions to the db
session.commit()