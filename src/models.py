import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship, declarative_base
from sqlalchemy import create_engine
from eralchemy2 import render_er

Base = declarative_base()

class User(Base):
    __tablename__ = 'user'
    id = Column(Integer, primary_key=True)
    name = Column(String(90), unique=True, nullable=False)
    last_name = Column(String(90), unique=True, nullable=False)
    email = Column(String(90), unique=True, nullable=False)
    password = Column(String(20), unique=True, nullable=False)
    favorites = relationship('Favorite', back_populates='user')

class Planet(Base):
    __tablename__ = 'planet'
    id = Column(Integer, primary_key=True)
    name = Column(String(90), unique=True, nullable=False)
    climate = Column(String(90), unique=True, nullable=False)
    terrain = Column(String(90), unique=True, nullable=False)
    favorites = relationship('Favorite', back_populates='planet')
    
class Character(Base):
    __tablename__ = 'character'
    id = Column(Integer, primary_key=True)
    name = Column(String(90), unique=True, nullable=False)
    species = Column(String(90), unique=True, nullable=False)
    gender = Column(String(90), unique=True, nullable=False)
    favorites = relationship('Favorite', back_populates='character')

class Favorites(Base):
    __tablename__ = 'favorites'
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('user.id'))
    planet_id = Column(Integer, ForeignKey('planet.id'))
    character_id = Column(Integer, ForeignKey('character.id'))
    user = relationship(User, back_populates='favorites')
    planet = relationship(Planet, back_populates='favorites')
    character = relationship(Character, back_populates='favorites')


    def to_dict(self):
        return {}


render_er(Base, 'diagram.png')
