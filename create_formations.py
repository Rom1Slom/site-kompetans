import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'kompetans2.settings')
django.setup()

from main.models import Formation
from django.db import transaction

# Transaction pour garantir la cohérence
with transaction.atomic():

    # Supprimer toutes les formations existantes
    Formation.objects.all().delete()

     # Forcer la réinitialisation de la séquence
    from django.db import connection
    if connection.vendor == 'sqlite':
        with connection.cursor() as cursor:
            cursor.execute("DELETE FROM sqlite_sequence WHERE name='main_formation';")
    elif connection.vendor == 'postgresql':
        with connection.cursor() as cursor:
            cursor.execute("ALTER SEQUENCE main_formation_id_seq RESTART WITH 1;")
    elif connection.vendor == 'mysql':
        with connection.cursor() as cursor:
            cursor.execute("ALTER TABLE main_formation AUTO_INCREMENT = 1;")

print("✅ Base de données nettoyée et séquence réinitialisée")

# Créer les 4 formations
formations_data = [
    {
        'nom': 'Habilitations électriques',
        'type_formation': 'habilitation',
        'description_courte': 'Formation aux habilitations électriques B0, B1, B2, BR, BC selon la norme NF C18-510.',
        'description_longue': 'Formation complète aux habilitations électriques pour travailler en sécurité sur ou à proximité d\'installations électriques.',
        'duree': '1, 2 ou 3 jours selon le niveau',
        'prix': 'À partir de 150€ HT/personne ; devis sur demande'
    },
    {
        'nom': 'Formation à la NF C15-100',
        'type_formation': 'nfc15100',
        'description_courte': 'Maîtrisez la norme NF C15-100 pour concevoir et réaliser des installations électriques conformes.',
        'description_longue': 'Formation complète sur la norme NF C15-100, référence en matière d\'installations électriques basse tension.',
        'duree': '3 jours',
        'prix': 'Devis personnalisé sur demande'
    },
    {
        'nom': 'Formation de formateur en habilitation électrique',
        'type_formation': 'formateur',
        'description_courte': 'Devenez formateur certifié en habilitation électrique et transmettez vos compétences.',
        'description_longue': 'Formation pour devenir formateur en habilitation électrique selon la norme NF C18-510.',
        'duree': '5 jours',
        'prix': 'Devis personnalisé sur demande'
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