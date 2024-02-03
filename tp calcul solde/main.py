import argparse
from datetime import datetime

def votre_fonction(salaire, date_formatee='je suis le meilleur'):
    # Votre logique ici
    print(f"Salaire: {salaire}")
    print(f"Date Formatee: {date_formatee}")
    # Ajoutez le reste de votre logique ici

def main():
    # Configuration d'argparse pour les arguments en ligne de commande
    parser = argparse.ArgumentParser(description='Script description.')
    parser.add_argument('salaire', type=float, help='La valeur du salaire')
    parser.add_argument('--date_formatee', type=str, help='La date formatee')

    # Récupération des arguments
    args = parser.parse_args()
    if args.date_formatee is None:
        date_formatee = datetime.now().strftime("%Y-%m-%d")
    # Appel de votre fonction avec les arguments
    #load_week_history_from_date(date_formatee,args.salaire)

if __name__ == "__main__":
    main()