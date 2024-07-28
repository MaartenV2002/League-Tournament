from sqlalchemy import Integer, TEXT
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy.ext.declarative import declarative_base

from src.database.types import Role, RoleColumn

# Base class for all models
Base = declarative_base()

class Player(Base):
    __tablename__ = 'players'
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    summoner_name: Mapped[str] = mapped_column(TEXT, nullable=False)
    role: Mapped[Role] = mapped_column(RoleColumn, nullable=False)

    def __repr__(self) -> str:
        return f'<Player(id={self.id}, name={self.name}, role={self.role})>'