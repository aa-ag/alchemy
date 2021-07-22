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

############------------ CLASSES ------------############