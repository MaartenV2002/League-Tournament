from sqlalchemy import create_engine, text
from sqlalchemy.orm import sessionmaker
import os

# Database URL
DATABASE_URL = 'postgresql://dev:dev@postgres_container:5432/TournamentDB'

# Create async engine and session
engine = create_engine(DATABASE_URL, echo=True)
session = sessionmaker(bind=engine)

def create_db_session():
    """Return a new db session"""
    return session()
