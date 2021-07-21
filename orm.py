############------------ IMPORTS ------------############
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

############------------ GLOBAL VARIABLE(S) ------------############


############------------ FUNCTION(S) ------------############
def create_postgresql_engine():
    engine = create_engine('postgresql://usr:pass@localhost:5432/sqlalchemy')

    Session = sessionmaker(bind=engine)

    Base = declarative_base()


############------------ DRIVER CODE ------------############
if __name__ == "__main__":
    create_postgresql_engine()