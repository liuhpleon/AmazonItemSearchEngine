from sqlalchemy import Column, ForeignKey, Integer,String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine

base = declarative_base()

class User(base):
    __tablename__ = 'user'
    name = Column(String(20),nullable = False,primary_key=True)
    password = Column(String(20),nullable = False)
    email = Column(String(30),nullable = False)
    phone = Column(String(30),nullable = False)
    item = Column(String(1000))

engine = create_engine('sqlite:///user.db')
base.metadata.create_all(engine)
