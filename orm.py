############------------ IMPORTS ------------############
from sqlalchemy import create_engine

############------------ GLOBAL VARIABLE(S) ------------############


############------------ FUNCTION(S) ------------############
def create_postgresql_engine():
    engine = create_engine('postgresql://usr:pass@localhost:5432/sqlalchemy')
    

############------------ DRIVER CODE ------------############
if __name__ == "__main__":
    create_postgresql_engine()