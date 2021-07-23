############------------ IMPORTS ------------############
import datetime
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from orm import *


############------------ GLOBAL VARIABLE(S) ------------############
engine = create_engine('sqlite:///student.db', echo=True)

# create a session
Session = sessionmaker(bind=engine)
session = Session()

############------------ FUNCTION(S) ------------############
def read_from_db():
    global session

    for i in session.query(Scuderias).order_by(Scuderias.id):
        print(i.id)


############------------ DRIVER CODE ------------############
if __name__ == "__main__":
    read_from_db()
    '''
    Afirstname Alastname
    Bfirstname Alastname
    Cfirstname Clastname
    '''