#!/usr/bin/env python
"""
Script pour initialiser les données de formations
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

def create_formations():
    """Créer les formations par défaut"""
    
    formations_data = [
        {
            'nom': 'Habilitations électriques',
            'type_formation': 'habilitation',
            'description_courte': 'Formation aux habilitations électriques selon la norme NF C18-510 pour travailler en sécurité sur les installations électriques.',
            'description_longue': '''
Cette formation prépare les participants à obtenir leur habilitation électrique selon la norme NF C18-510.

**Programme de formation :**

• Notions de base en électricité
• Les dangers de l'électricité et leurs effets sur le corps humain
• Les mesures de prévention à mettre en œuvre
• Les équipements de protection individuelle et collective
• La conduite à tenir en cas d'accident ou d'incendie d'origine électrique
• Les travaux hors tension et sous tension
• La consignation électrique
• Les procédures d'intervention

**Public concerné :**
Personnel électricien ou non électricien devant effectuer des opérations sur ou au voisinage des installations électriques.

**Prérequis :**
Avoir des notions de base en électricité pour les électriciens, aucun prérequis pour les non-électriciens.

**Validation :**
Remise d'un avis d'habilitation après évaluation théorique et pratique.
            ''',
            'duree': '1 à 3 jours selon le niveau',
            'prix': 'À partir de 280€ HT'
        },
        {
            'nom': 'Formation à la NF C15-100',
            'type_formation': 'nfc15100',
            'description_courte': 'Maîtrisez la norme française NF C15-100 pour la conception et la réalisation d\'installations électriques conformes.',
            'description_longue': '''
Cette formation vous permet de maîtriser la norme NF C15-100 qui régit les installations électriques basse tension en France.

**Programme de formation :**

• Présentation générale de la norme NF C15-100
• Les locaux d'habitation : exigences particulières
• Les circuits et appareillages
• La protection contre les surintensités
• La protection contre les contacts directs et indirects
• La mise à la terre et les liaisons équipotentielles
• Les installations dans les salles de bains
• Les locaux contenant une baignoire ou une douche
• Les évolutions récentes de la norme

**Public concerné :**
Électriciens, installateurs, bureau d'études, contrôleurs techniques.

**Prérequis :**
Connaissances de base en électricité.

**Validation :**
Attestation de formation délivrée en fin de stage.
            ''',
            'duree': '2 jours',
            'prix': '680€ HT'
        },
        {
            'nom': 'Formation de formateur en habilitation électrique',
            'type_formation': 'formateur',
            'description_courte': 'Devenez formateur certifié pour dispenser les formations d\'habilitation électrique dans votre entreprise.',
            'description_longue': '''
Cette formation vous prépare à devenir formateur en habilitation électrique selon la norme NF C18-510.

**Programme de formation :**

• Rappels sur la réglementation et la norme NF C18-510
• Les principes de la pédagogie pour adultes
• La construction d'un programme de formation
• Les techniques d'animation et de communication
• L'évaluation des acquis
• La gestion des situations difficiles
• Les outils pédagogiques
• Mise en situation pratique d'animation

**Public concerné :**
Futurs formateurs internes, responsables HSE, préventeurs.

**Prérequis :**
Être habilité électriquement et avoir une expérience significative dans le domaine électrique.

**Validation :**
Certificat de formateur en habilitation électrique délivré après évaluation.
            ''',
            'duree': '3 jours',
            'prix': '1200€ HT'
        },
        {
            'nom': 'Formation des élus du CSE',
            'type_formation': 'cse',
            'description_courte': 'Formation obligatoire des membres du Comité Social et Économique en matière de santé, sécurité et conditions de travail.',
            'description_longue': '''
Cette formation répond à l'obligation légale de formation des élus du CSE en matière de santé, sécurité et conditions de travail.

**Programme de formation :**

• Le cadre juridique du CSE
• Les missions et les moyens du CSE
• L'analyse des risques professionnels
• L'enquête en cas d'accident du travail
• Le droit d'alerte et de retrait
• L'inspection des lieux de travail
• Les relations avec les organismes de prévention
• La participation aux réunions du CSE

**Public concerné :**
Élus du CSE, représentants du personnel.

**Prérequis :**
Être élu au CSE.

**Validation :**
Attestation de formation réglementaire.
            ''',
            'duree': '5 jours',
            'prix': '1500€ HT'
        }
    ]
    
    for formation_data in formations_data:
        formation, created = Formation.objects.get_or_create(
            type_formation=formation_data['type_formation'],
            defaults=formation_data
        )
        if created:
            print(f"Formation créée : {formation.nom}")
        else:
            print(f"Formation existante : {formation.nom}")

if __name__ == '__main__':
    print("Initialisation des formations...")
    create_formations()
    print("Initialisation terminée !")
