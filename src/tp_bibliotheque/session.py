"""Outils de création de session SQLAlchemy."""

from os import getenv

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

db_uri = getenv("DB_BIBLIOTHEQUE", "sqlite:///bibliotheque.db")
engine = create_engine(db_uri, echo=True)

Session = sessionmaker(engine)
