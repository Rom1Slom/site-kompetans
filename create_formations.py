import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'kompetans2.settings')
django.setup()

from main.models import Formation

# Supprimer toutes les formations existantes
Formation.objects.all().delete()

# Créer les 4 formations
formations_data = [
    {
        'nom': 'Habilitations électriques',
        'type_formation': 'habilitation',
        'description_courte': 'Formation aux habilitations électriques B0, B1, B2, BR, BC selon la norme NF C18-510.',
        'description_longue': 'Formation complète aux habilitations électriques pour travailler en sécurité sur ou à proximité d\'installations électriques.',
        'duree': '2 à 3 jours selon le niveau',
        'prix': 'À partir de 350€ HT/personne'
    },
    {
        'nom': 'Formation à la NF C15-100',
        'type_formation': 'nfc15100',
        'description_courte': 'Maîtrisez la norme NF C15-100 pour concevoir et réaliser des installations électriques conformes.',
        'description_longue': 'Formation complète sur la norme NF C15-100, référence en matière d\'installations électriques basse tension.',
        'duree': '3 jours',
        'prix': 'À partir de 890€ HT/personne'
    },
    {
        'nom': 'Formation de formateur en habilitation électrique',
        'type_formation': 'formateur',
        'description_courte': 'Devenez formateur certifié en habilitation électrique et transmettez vos compétences.',
        'description_longue': 'Formation pour devenir formateur en habilitation électrique selon la norme NF C18-510.',
        'duree': '5 jours',
        'prix': 'À partir de 1890€ HT/personne'
    },
    {
        'nom': 'Formation des élus du Comité Social et Économique (CSE)',
        'type_formation': 'cse',
        'description_courte': 'Formation obligatoire pour les représentants du personnel en santé, sécurité et conditions de travail.',
        'description_longue': 'Formation réglementaire destinée aux membres du CSE pour exercer leurs missions en santé-sécurité.',
        'duree': '3 à 5 jours selon effectif',
        'prix': 'À partir de 690€ HT/personne'
    }
]

for data in formations_data:
    formation = Formation.objects.create(**data)
    print(f"Formation créée : {formation.nom}")

print(f"\nTotal : {Formation.objects.count()} formations créées avec succès !")