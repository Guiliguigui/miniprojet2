import csv

format_trad={'address': 'adresse_titulaire',
            'carrosserie': 'carrosserie',
            'categorie': 'categorie',
            'couleur': 'couleur',
            'cylindree': 'cylindree',
            'date_immat': 'date_immatriculation',
            'denomination': 'denomination_commerciale',
            'energy': 'energie',
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

format_souhaite = ['adresse_titulaire',
                   'nom',
                   'prenom',
                   'immatriculation',
                   'date_immatriculation',
                   'vin',
                    'marque',
                    'denomination_commerciale',
                    'couleur',
                    'carrosserie',
                    'categorie',
                    'cylindree',
                    'energie',
                    'places',
                    'poids',
                    'puissance',
                    'type',
                    'variante',
                    'version']

csvfile = open('auto.csv', 'r', newline='')
reader = csv.DictReader(csvfile, delimiter='|')

csvfile2 = open('auto2.csv', 'w', newline='')
writer = csv.DictWriter(csvfile2, fieldnames=format_souhaite, delimiter=';')
writer.writeheader()

for row in reader :
    newrow = {}
    for cle in row.keys() :
        newrow[format_trad[cle]] = row[cle]
        if cle == 'type_variante_version':
            temp = row[cle].split(', ')
            newrow['type'] = temp[0]
            newrow['variante'] = temp[1]
            newrow['version'] = temp[2]
    row={}
    for fieldname in format_souhaite:
        row[fieldname] = newrow[fieldname]
    writer.writerow(row)
