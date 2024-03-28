"""Interface en ligne de commandes."""

from argparse import ArgumentParser
from pathlib import Path

from .importer import import_data


def main() -> None:
    """Point d'entrée du programme."""
    parser = ArgumentParser(
        description="bibli - CLI pour gérer des emprunts de livres."
    )

    parser.add_argument("donnees", help="Fichier de données à importer.")
    args = parser.parse_args()
    import_data(Path(args.donnees))
