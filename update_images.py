#!/usr/bin/env python
"""
Script pour associer les images aux formations
"""
import os
import sys
import django

# Ajouter le répertoire du projet au path
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

# Configurer Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'kompetans2.settings')
django.setup()

from main.models import Formation

def update_formation_images():
    """Associer les images aux formations"""
    
    # Mapping des types de formation vers les noms d'images
    image_mapping = {
        'habilitation': 'formations/habilitation.jpg',
        'nfc15100': 'formations/nfc15100.jpg',
        'formateur': 'formations/formateur.jpg',
        'cse': 'formations/cse.jpg',
    }
    
    formations = Formation.objects.all()
    
    for formation in formations:
        if formation.type_formation in image_mapping:
            image_path = image_mapping[formation.type_formation]
            formation.image = image_path
            formation.save()
            print(f"Image associée à {formation.nom}: {image_path}")
        else:
            print(f"Pas d'image trouvée pour {formation.nom}")

if __name__ == '__main__':
    print("Association des images aux formations...")
    update_formation_images()
    print("Terminé !")
