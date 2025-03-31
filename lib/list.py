import pandas as pd
import random
import os

class Dataprep:
    full_data = [
        {
            "id": 1,
            "email": "george.bluth@reqres.in",
            "first_name": "George",
            "last_name": "Bluth",
            "avatar": "https://reqres.in/img/faces/1-image.jpg"
        },
        {
            "id": 2,
            "email": "janet.weaver@reqres.in",
            "first_name": "Janet",
            "last_name": "Weaver",
            "avatar": "https://reqres.in/img/faces/2-image.jpg"
        },
        {
            "id": 3,
            "email": "emma.wong@reqres.in",
            "first_name": "Emma",
            "last_name": "Wong",
            "avatar": "https://reqres.in/img/faces/3-image.jpg"
        },
        {
            "id": 4,
            "email": "eve.holt@reqres.in",
            "first_name": "Eve",
            "last_name": "Holt",
            "avatar": "https://reqres.in/img/faces/4-image.jpg"
        },
        {
            "id": 5,
            "email": "charles.morris@reqres.in",
            "first_name": "Charles",
            "last_name": "Morris",
            "avatar": "https://reqres.in/img/faces/5-image.jpg"
        },
        {
            "id": 6,
            "email": "tracey.ramos@reqres.in",
            "first_name": "Tracey",
            "last_name": "Ramos",
            "avatar": "https://reqres.in/img/faces/6-image.jpg"
        }
    ]

    def __init__(self, path):
        self.path = path
    
    def CreatData(self, frac=0.5):
        # Si le fichier existe déjà, on peut choisir d'ignorer l'écriture ou de l'écraser
        if os.path.exists(self.path):
            print(f"Le fichier {self.path} existe déjà. Il va être écrasé.")
        else:
            print(f"Création du fichier {self.path}.")

        data = pd.DataFrame(Dataprep.full_data).sample(frac=frac, random_state=random.randint(1, 100))
        

        data.to_csv(self.path, index=False) 
        
        print(f"Les données ont été sauvegardées dans {self.path}")

if __name__ == "__main__":
    data_prep = Dataprep("data/data.csv")  
    data_prep.CreatData(frac=1)  
