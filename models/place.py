#!/usr/bin/python3
"""
    Write all those classes that inherit from BaseModel
"""
from models.base_model import BaseModel


class Place(BaseModel):
    """
        Amenity
    """
    name = ""
    city_id = ""
    user_id = ""
    description = ""
    number_rooms = 0
    number_bathrooms = 0
    max_guest = 0
    price_by_night = 0
    latitude = 0.0
    longitude = 0.0
    amenity_ids = []
