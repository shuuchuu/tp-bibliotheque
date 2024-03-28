"""Fonctions d'import depuis un fichier yml vers la base de données."""

from datetime import date
from pathlib import Path

from yaml import safe_load

from .models import Emprunt, Livre, Membre
from .session import Session


def import_data(path: Path) -> None:
    """Importe les données d'un fichier yml en base."""
    with path.open(encoding="utf8") as fh:
        content = safe_load(fh)
    with Session() as session, session.begin():
        livres = {}
        membres = {}
        if "livres" in content:
            for nom_livre in content["livres"]:
                livre = Livre(nom=nom_livre)
                livres[nom_livre] = livre
                session.add(livre)
        if "membres" in content:
            for nom_membre in content["membres"]:
                membre = Membre(nom=nom_membre)
                membres[nom_membre] = membre
                session.add(membre)
        if "emprunts" in content:
            for donnees_emprunt in content["emprunts"]:
                session.add(
                    Emprunt(
                        membre=membres[donnees_emprunt["membre"]],
                        livre=livres[donnees_emprunt["livre"]],
                        date=date.fromisoformat(donnees_emprunt["date"]),
                    )
                )
