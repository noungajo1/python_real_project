from function import load_data_base, premier_jour_semaine, get_plage_horaire

data_base = load_data_base()
"""
je te fourni une date tu me donnes:
- le nombre de jour valide durant cette semaine, 
- les plage horaire present de chaque jour
- le nombre d'heure totale pointe
- Quel salaire pour cette semaine
format : aaaa/mm/jj
"""

def load_week_history_from_date(week_date, salaire):
    week_date = premier_jour_semaine(week_date)
    for week in data_base.values():
        if week['date_debut'] == week_date:
            if week['present'] == 1:
                jour_valide = len(week['jours'])
                get_plage_horaire(week['jours'], salaire)
                print(f'Jour valide : {jour_valide}')
            else:
                print("Je n'ai pas travaillé cette semaine")
            return 0

    # Si aucune correspondance n'est trouvée dans la boucle
    print('Date non prise en charge')
    return 0

"""
La phase deux du TP consiste a donner le salaire 
courant a recevoir lorsque la date courante est saisie.
si le salaire se fait chaque deux semaines, il faudra que l'appli
donne l'historique de la plage salariale, si c'est 1 mois donne l'historique sur un mois
si c'est deux semaines donnee l'historique du travail sur deux semaines
"""
