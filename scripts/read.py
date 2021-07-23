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

############------------ FUNCTION(S) ------------############
def read_from_db():
    global session

    for record in session.query(Scuderias).order_by(Scuderias.id):
        print(record.id, record.scuderias_name)


############------------ DRIVER CODE ------------############
if __name__ == "__main__":
    read_from_db()