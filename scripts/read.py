############------------ IMPORTS ------------############
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from orm import Scuderias


############------------ GLOBAL VARIABLE(S) ------------############
engine = create_engine('sqlite:///scuderias.db', echo=True)

# create a session
Session = sessionmaker(bind=engine)
session = Session()


############------------ FUNCTION(S) ------------############
def read_from_db():
    global session

    for record in session.query(Scuderias).order_by(Scuderias.id):
        print(record.id, \
            record.scuderias_name, \
            record.principals_firstname, \
            record.principals_lastname, \
            record.driver1_firstname, \
            record.driver1_lastname, \
            record.driver2_firstname, \
            record.driver2_lastname
        )


############------------ DRIVER CODE ------------############
if __name__ == "__main__":
    read_from_db()