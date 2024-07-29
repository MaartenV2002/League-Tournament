from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, Session

from src.database.models import Player

# Database URL
DATABASE_URL = 'postgresql://dev:dev@postgres_container:5432/TournamentDB'

# Create async engine and session
engine = create_engine(DATABASE_URL, echo=False)
session = sessionmaker(bind=engine)

def create_db_session() -> Session:
    """Return a new db session"""
    return session()

def get_player_from_discord_id(session: Session, discord_id: int) -> Player | None:
    """Return a player object from the given discord id"""
    player = session.query(Player).filter(Player.discord_id == discord_id).first()
    if player:
        return player
    return None