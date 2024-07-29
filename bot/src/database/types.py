from enum import Enum
import sqlalchemy.dialects.postgresql as sadp

class Role(Enum):
    """Enum for the role of the player"""
    __name__ = 'role'
    TOP = 'TOP'
    JUNGLE = 'JUNGLE'
    MID = 'MID'
    ADC = 'ADC'
    SUPPORT = 'SUPPORT'

RoleColumn = sadp.ENUM(Role, create_type=False, name='role')