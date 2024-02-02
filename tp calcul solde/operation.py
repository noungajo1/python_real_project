import json
from datetime import datetime, timedelta

#Read python object from a json file

def load_data_base():
    with open("data.json","r") as json_file:
        data = json.load(json_file)
    return data

data_base = load_data_base()
salaire = 22.18
"""
je te fourni une date tu me donnes:
- le nombre de jour valide durant cette semaine, 
- les plage horaire present de chaque jour
- le nombre d'heure totale pointe
- Quel salaire pour cette semaine
format : aaaa/mm/jj
"""
def get_hour_from_plages(plages):
    time_in_seconde = 0
    for plage in plages:
        h1 = datetime.strptime(plage.split(" ")[0],'%H:%M')
        h2 = datetime.strptime(plage.split(" ")[1],'%H:%M')
        difference = (h2 - h1)
        time_in_seconde = difference.seconds + time_in_seconde
    return time_in_seconde/3600

 # Fonction pour convertir une plage de temps en secondes
def plage_to_seconds(plage):
    h1, h2 = map(lambda x: datetime.strptime(x, '%H:%M'), plage.split(" "))
    difference = h2 - h1
    return difference.seconds
def get_hour_from_plage(plages):
    # Utilisation de la fonction map pour appliquer la conversion à chaque plage
    time_in_seconds_list = map(plage_to_seconds, plages)
    # Utilisation de la fonction sum pour calculer la somme totale des différences de temps
    total_time_in_seconds = sum(time_in_seconds_list)
    # Conversion du temps total en heures
    total_hours = total_time_in_seconds / 3600
    return total_hours

def get_plage_horaire(jours, salaire):
    heure_total_pointe = 0

    for jour in jours:
        libelle_jour = jour['libelle_jour']
        list_plage = jour['plages']
        
        # Affichage du jour et des plages horaires si nécessaire
        print(f"{libelle_jour}: {list_plage}")

        # Calcul des heures pointe pour le jour actuel
        heure_total_pointe += get_hour_from_plage(list_plage)

    # Calcul du salaire total
    salaire_final = salaire * heure_total_pointe

    # Affichage des résultats
    print(f'Le nombre d\'heures valide est : {heure_total_pointe:.2f}')
    print(f'Le salaire de cette semaine est : {salaire_final:.2f} $')

    return 0

"""
a partir d'une date fourni le premier jour 
de la semaine auquel ce jour appartient
"""
def premier_jour_semaine(date_formatee):
    # Conversion de la date en objet datetime
    date_obj = datetime.strptime(date_formatee, "%Y-%m-%d")

    # Calcul du jour de la semaine (0 = lundi, 6 = dimanche)
    jour_semaine = date_obj.weekday()

    # Calcul du décalage pour obtenir le premier jour de la semaine
    decalage = timedelta(days=jour_semaine)

    # Calcul du premier jour de la semaine
    premier_jour = date_obj - decalage

    # Formater la date du premier jour de la semaine
    premier_jour_formate = premier_jour.strftime("%Y-%m-%d")
    return premier_jour_formate

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
    
    
date_formatee = datetime.now().strftime("%Y-%m-%d")

load_week_history_from_date(date_formatee,salaire)

