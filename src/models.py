import os
import sys
import enum
from sqlalchemy import Column, ForeignKey, Integer, String, Table
from sqlalchemy.orm import relationship, declarative_base
from sqlalchemy import create_engine
from eralchemy2 import render_er

Base = declarative_base()

class MediaType(enum.Enum):
    audio = 1
    video = 2
    image =3

class Person(Base):
    __tablename__ = 'person'
    # Here we define columns for the table person
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)

class Address(Base):
    __tablename__ = 'address'
    # Here we define columns for the table address.
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    street_name = Column(String(250))
    street_number = Column(String(250))
    post_code = Column(String(250), nullable=False)
    person_id = Column(Integer, ForeignKey('person.id'))
    person = relationship(Person)

    def to_dict(self):
        return {}
    
    class User(Base):
        __tablename__ = 'User'
        id = Column(Integer, primary_key=True)
        username = Column(String(255), nullable=False)
        firstname = Column(String(255), nullable=False)
        lastname = Column(String(255), nullable=False)
        email = Column(String(255), nullable=False)

    class Post(Base):
        __tablename__: 'Post'
        id = Column(Integer, primary_key=True)
        user_id = Column(Integer, ForeignKey('User.id'))
        user = relationship(User)
    
    class Media(Base):
        __tablename__: 'Media'
        id = Column(Integer, primary_key=True)
        type = Column(type , Enum(MediaType))
        url = Column(String(255), nullable=False)
        post_id = Column(Integer, ForeignKey('Post.id'))

    class Follower(Base):
        __tablename__: 'Follower'

        id = Column(Integer, primary_key=True)
        follower_id = Column(Integer, ForeignKey('User.id'), nullable=False)
        followee_id = Column(Integer, ForeignKey('Post.id'), nullable=False)
        
        follower = relationship('User', back_populates='followers')
        followee = relationship('Post', back_populates='followees')

    class Comment(Base):
        __tablename__: 'Comment'
        id = Column(Integer, primary_key=True)
        comment_text = Column(String(10000), nullable=False)
        author_id = Column(Integer, ForeignKey('User.id'), nullable=False)
        post_id = Column(Integer, ForeignKey('Post.id'), nullable=False)
        
        user = relationship('User', back_populates='comments')
        post = relationship('Post', back_populates='comments')





        


## Draw from SQLAlchemy base
try:
    result = render_er(Base, 'diagram.png')
    print("Success! Check the diagram.png file")
except Exception as e:
    print("There was a problem genering the diagram")
    raise e
