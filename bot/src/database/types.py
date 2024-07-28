from enum import Enum
import sqlalchemy.dialects.postgresql as sadp

class Role(Enum):
    """Enum for the role of the player"""
    __name__ = 'role'
    TOP = 'top'
    JUNGLE = 'jungle'
    MID = 'mid'
    ADC = 'adc'
    SUPPORT = 'support'

RoleColumn = sadp.ENUM(Role, create_type=False, name='role')