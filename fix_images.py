#!/usr/bin/env python
import os
import sys

# Aller dans le bon répertoire
os.chdir('c:\\Users\\admin\\Documents\\Programmation\\Kompetans2')

# Configurer Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'kompetans2.settings')

import django
django.setup()

from main.models import Formation

print("=== Diagnostic des formations ===")

formations = Formation.objects.all()
print(f"Nombre de formations: {formations.count()}")

for formation in formations:
    print(f"\nFormation: {formation.nom}")
    print(f"Type: {formation.type_formation}")
    print(f"Image actuelle: {formation.image}")
    
    # Associer l'image selon le type
    if formation.type_formation == 'habilitation':
        formation.image = 'formations/habilitation.jpg'
    elif formation.type_formation == 'nfc15100':
        formation.image = 'formations/nfc15100.jpg'
    elif formation.type_formation == 'formateur':
        formation.image = 'formations/formateur.jpg'
    elif formation.type_formation == 'cse':
        formation.image = 'formations/cse.jpg'
    
    formation.save()
    print(f"Image mise à jour: {formation.image}")

print("\n=== Mise à jour terminée ===")
