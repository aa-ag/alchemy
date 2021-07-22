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

# create objects
user = Student("usernameX", "Afirstname", "Alastname", "SchoolX")
session.add(user)

user = Student("usernameY", "Bfirstname", "Alastname", "SchoolY")
session.add(user)

user = Student("usernameZ", "Cfirstname", "Clastname", "SchoolZ")
session.add(user)

# commit additions to the db
session.commit()