import csv
import pandas

format_trad={'address': 'adresse_titulaire',
            'carrosserie': 'carrosserie',
            'categorie': 'categorie',
            'couleur': 'couleur',
            'cylindree': 'cylindree',
            'date_immat': 'date_immatriculation',
            'denomination': 'denomination commerciale',
            'energy': 'puissance',
            'firstname': 'prenom',
            'immat': 'immatriculation',
            'marque': 'marque',
            'name': 'nom',
            'places': 'places',
            'poids': 'poids',
            'puissance': 'puissance',
            'type_variante_version': 'type',
            'vin': 'vin',
}

with open('auto.csv', 'r') as csvfile:
    reader = pandas.read_csv(csvfile, delimiter='|')
    
reader = reader.rename(format_trad, inplace=True)
    
print(reader)


  