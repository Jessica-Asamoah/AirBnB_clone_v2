#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String
from os import getenv


class Amenity(BaseModel, Base):
    """Amenities available at a Place"""
    __tablename__ = 'amenities'
    name = Column(String(128), nullable=False
                  ) if getenv('HBNB_TYPE_STORAGE') == 'db' else ''
