import unittest
from  CSVTRAD import lecture
from  CSVTRAD import nommage_colonnes
from  CSVTRAD import reorganisation_valeurs

class TestCSVTRADFunctions(unittest.TestCase):

    def setUp(self):
        format_actuel = ["address",
                         "carrosserie",
                         "categorie",
                         "couleur",
                         "cylindree",
                         "date_immat",
                         "denomination",
                         "energy",
                         "firstname",
                         "immat",
                         "marque",
                         "name",
                         "places",
                         "poids",
                         "puissance",
                         "type_variante_version",
                         "vin"]
        
        format_souhaite = ["adresse_titulaire",
                           "nom",
                           "prenom",
                           "immatriculation",
                           "date_immatriculation",
                           "vin",
                           "marque",
                           "denomination commerciale",
                           "couleur",
                           "carrosserie",
                           "categorie",
                           "cylindree",
                           "energie",
                           "places",
                           "poids",
                           "puissance",
                           "type",
                           "variante",
                           "version"]


    def test_lecture(self):
        self.assertEqual(lecture("abc;123"), ["abc","123"])

    def test_nommage_colonnes(self):
        self.assertEqual(nommage_colonnes(format_actuel),format_souhaite)

    def test_reorganisation_valeurs(self):
        raise NotImplementedError
        



 