from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String




Base = declarative_base()




class actor(Base):
    __tablename__ = 'actor'

    # pola i ich typy
    actor_id = Column(Integer, primary_key=True)
    first_name = Column(String)
    last_name = Column(String)

    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name

    def __repr__(self):
        return "<User('%s','%s')>" % (self.first_name, self.last_name)
