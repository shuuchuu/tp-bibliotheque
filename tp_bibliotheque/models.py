"""Classes SQLAlchemy des différentes tables utilisées par l'application."""

from datetime import date

from sqlalchemy import ForeignKey, String
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, relationship

from .session import engine


class _Base(DeclarativeBase):
    pass


class Livre(_Base):
    """Classe de la table livres."""

    __tablename__ = "livres"
    id: Mapped[int] = mapped_column(primary_key=True)
    nom: Mapped[str] = mapped_column(String(100))
    emprunt: Mapped["Emprunt"] = relationship(back_populates="livre")


class Membre(_Base):
    """Classe de la table membres."""

    __tablename__ = "membres"
    id: Mapped[int] = mapped_column(primary_key=True)
    nom: Mapped[str] = mapped_column(String(100))
    emprunts: Mapped[list["Emprunt"]] = relationship(back_populates="membre")


class Emprunt(_Base):
    """Classe de la table emprunts."""

    __tablename__ = "emprunts"
    id: Mapped[int] = mapped_column(primary_key=True)
    id_livre = mapped_column(ForeignKey("livres.id"))
    livre: Mapped[Livre] = relationship(back_populates="emprunt")
    id_membre = mapped_column(ForeignKey("membres.id"))
    membre: Mapped[Membre] = relationship(back_populates="emprunts")
    date: Mapped[date]


_Base.metadata.drop_all(engine)
_Base.metadata.create_all(engine)
