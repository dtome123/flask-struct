
from sqlalchemy import Column, String, Integer, Float, ForeignKey
from sqlalchemy.orm import sessionmaker
from app import db

class User(db.Model):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(100), nullable=False)
    avatar = Column(String(100))
    username = Column(String(50), nullable=False)
    password = Column(String(256), nullable=False)
    user_role = Column(String(20), default='USER')

# CREATE A SESSION OBJECT TO INITIATE QUERY IN DATABASE
Session = sessionmaker(bind=db.get_engine())
session = Session()