#! /usr/bin/env python

import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.exe.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine

Base = declarative_base()

class Restaurant(Base):
	
	__tablename__ = 'restaurant'
	
	id = Column(Integer, primary_key = True)
	name = Column(String(250), nullabel = False)


class MenuItem(Base):

	__tablename__ = 'menu_item'
	
	name = Column(String(50), nallable = False)
	id = Column(Integer, primary_key = True)
	description = Column(String(250))
	price = Column(String(8))
	course = Column(String(250))
	restaurant_id = Column(Integer, Foreignkey('retsaurant.id'))
	restaurant = relationship(Restaurant)


engine = create_engine('sqlite:///restaurantmenu.db')
Base.metadata.create_all(engine)