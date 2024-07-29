from sqlalchemy import Integer, TEXT, BigInteger
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy.ext.declarative import declarative_base

from src.database.types import Role, RoleColumn

# Base class for all models
Base = declarative_base()

class Player(Base):
    __tablename__ = 'players'
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    discord_id: Mapped[int] = mapped_column(BigInteger, nullable=False)
    discord_name: Mapped[str] = mapped_column(TEXT, nullable=False)
    summoner_name: Mapped[str] = mapped_column(TEXT)
    role: Mapped[Role] = mapped_column(RoleColumn, nullable=True)
    riot_puuid: Mapped[str] = mapped_column(TEXT)
    

    def __repr__(self) -> str:
        return f'<Player(id={self.id}, name={self.name}, role={self.role})>'