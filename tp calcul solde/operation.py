import json


#Read python object from a json file

def load_data_base():
    with open("data.json","r") as json_file:
        data = json.load(json_file)
    return data

data_base = load_data_base()
print(type(data_base))
"""
je te fourni une date tu me donnes:
- le nombre de jour valide durant cette semaine, 
- les plage horaire present de chaque jour
- le nombre d'heure totale pointe
format : aaaa/mm/jj
"""
def get_plage_horaire(jours):
    print('Les jours')
    for jour in jours:
        list_plage = jour["plage"]
        for plage in  list_plage:
            print()


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

    
    

load_week_history_from_date('2024/01/29')

