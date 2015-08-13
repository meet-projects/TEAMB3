from sqlalchemy import Column, Date, Float, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, sessionmaker
from sqlalchemy import create_engine

Base = declarative_base()

#PLACE YOUR TABLE SETUP INFORMATION HERE

class User (Base):
	__tablename__ = 'user'
	id = Column(Integer, primary_key=True)
	first_name = Column(String(60))
	last_name = Column(String(60))
	username = Column(String(60))
	password = Column(String(60))
	bio = Column(String(140))
	background = Column(String(500))
	
class Interests (Base):
	__tablename__ = 'interests'
	id = Column(Integer, primary_key=True) #the id matches the user id
	fav_book = Column(String(60))
	fav_movie = Column(String(60))
	fav_hobby = Column(String(60))
	fav_song = Column(String(60)) 
	other = Column(String(60))

	
