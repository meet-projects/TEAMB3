from sqlalchemy import Column, Date, Float, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, sessionmaker
from sqlalchemy import create_engine

Base = declarative_base()

#PLACE YOUR TABLE SETUP INFORMATION HERE

class User (Base):
	__tablename__ = 'user'
	id = Column(Integer, primary_key=True)
	First_name = Column(String(60))
	Last_name = Column(String(60))
	Username = Column(String(60))
	Password = Column(String(60))
	Bio = Column(String(140))
	

	
