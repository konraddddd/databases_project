from sqlalchemy import create_engine

from sqlalchemy.orm import sessionmaker

from config import config
from tables import *

# config from .ini
db = config()

# engine
values = list(db.values())
path = 'postgresql://' + values[2] + ':' + values[3] + '@' + values[0] + ':5432/' + values[1]
engine = create_engine(path, echo=True)

# session
Session = sessionmaker(bind=engine)
session = Session()

# tables refreshing
Base.metadata.create_all(engine)

