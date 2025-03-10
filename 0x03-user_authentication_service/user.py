#!/usr/bin/env python3
"""
0. User model
"""
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, INTEGER, VARCHAR

Base = declarative_base()


class User(Base):
    """
    User Model
    """
    __tablename__ = 'users'
    id = Column(INTEGER, primary_key=True)
    email = Column(VARCHAR(250), nullable=False)
    hashed_password = Column(VARCHAR(250), nullable=False)
    session_id = Column(VARCHAR(250))
    reset_token = Column(VARCHAR(250))
