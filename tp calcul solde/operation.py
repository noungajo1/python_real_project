import json
from datetime import datetime

#Read python object from a json file

def load_data_base():
    with open("data.json","r") as json_file:
        data = json.load(json_file)
    return data

data_base = load_data_base()
"""
je te fourni une date tu me donnes:
- le nombre de jour valide durant cette semaine, 
- les plage horaire present de chaque jour
- le nombre d'heure totale pointe
format : aaaa/mm/jj
"""
def get_hour_from_plage(plages):
    time_in_seconde = 0
    for plage in plages:
        h1 = datetime.strptime(plage.split(" ")[0],'%H:%M')
        h2 = datetime.strptime(plage.split(" ")[1],'%H:%M')
        difference = (h2 - h1)
        time_in_seconde = difference.seconds + time_in_seconde
    return time_in_seconde/3600



def get_plage_horaire(jours):
    heure_total_pointe = 0
    for jour in jours:
        print(f"{jour['libelle_jour']} : ")
        list_plage = jour["plages"]
        print(list_plage)
        heure_total_pointe = get_hour_from_plage(list_plage) + heure_total_pointe  
    print(f'Le nombre d\heures valide est : {heure_total_pointe:.2f}') 
    return 0


def load_week_history_from_date(week_date):
    weeks = data_base.values()
    jour_valide = 0
    for week in weeks:
        if(week['date_debut']==week_date):
            if(week['present']==1):
                jour_valide = len(week['jours'])
                get_plage_horaire(week['jours'])
                print(f'Jour valide : {jour_valide}')
            else:
                print("Je n'ai pas travailler cette semaine")
            return 0
    print('Date non prise en charge')
    return 0

    
    

load_week_history_from_date('2024/01/22')

