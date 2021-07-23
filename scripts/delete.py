############------------ IMPORTS ------------############
import datetime
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from orm import Scuderias, key
from sqlalchemy import delete


############------------ GLOBAL VARIABLE(S) ------------############
engine = create_engine('sqlite:///scuderias.db', echo=True)

# create a session
Session = sessionmaker(bind=engine)
session = Session()

############------------ FUNCTION(S) ------------############
def delete_from_db():
    global session

    for record in session.query(Scuderias).order_by(Scuderias.id):
        session.delete(record)

    session.commit()



############------------ DRIVER CODE ------------############
if __name__ == "__main__":
    delete_from_db()