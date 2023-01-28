"""
this module defines pydantic (provides Py3 dataclasses validation out of box ) modules used for validation and (de) serialisation in API requests/responses
"""
from typing import List, Optional
from decimal import Decimal
from models.basemodel import Base


class Planet_(Base):
    """
    Pydantic model class meant to validate the data for "planet" object from single resource endpoint from starwars API
    """
    # attribute fields

    climate:str
    diameter:str
    gravity: str
    name: str
    orbital_period: str
    population: str
    rotation_period: str
    surface_water: str
    terrain: str

    # Relationship attribute fields
    films: Optional[List[str]]
    residents: Optional[List[str]]
