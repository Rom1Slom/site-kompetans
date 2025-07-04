# Kompetans - Site Web de Formation en Électricité

## Description

Kompetans est un site web Django pour un organisme de conseil et de formation spécialisé en électricité. Le site présente 4 types de formations principales :

1. **Habilitations électriques** - Formation selon la norme NF C18-510
2. **Formation à la NF C15-100** - Maîtrise de la norme française pour les installations électriques
3. **Formation de formateur en habilitation électrique** - Certification pour devenir formateur
4. **Formation des élus du CSE** - Formation obligatoire pour les membres du Comité Social et Économique

## Fonctionnalités

- **Page d'accueil** : Présentation de l'entreprise avec 4 boutons/images pour chaque formation
- **Pages de formation** : Landing pages détaillées avec formulaire de contact
- **Formulaires de contact** : Collecte d'informations client avec validation
- **Administration Django** : Gestion des formations et des demandes de contact
- **Design responsive** : Interface moderne compatible mobile et desktop
- **Interface français** : Entièrement en langue française

## Technologies utilisées

- **Backend** : Django 5.2.4
- **Frontend** : Bootstrap 5.3, HTML5, CSS3, JavaScript
- **Base de données** : SQLite (développement)
- **Images** : Support Pillow pour les uploads

## Installation et Configuration

### Prérequis

- Python 3.11+
- pip

### Installation

1. **Cloner ou accéder au projet** :
   ```bash
   cd c:\Users\admin\Documents\Programmation\Kompetans2
   ```

2. **Activer l'environnement virtuel** :
   ```bash
   .venv\Scripts\activate
   ```

3. **Installer les dépendances** :
   ```bash
   pip install django pillow
   ```

4. **Appliquer les migrations** :
   ```bash
   python manage.py migrate
   ```

5. **Initialiser les données** :
   ```bash
   python init_data.py
   ```

6. **Créer un superutilisateur** (optionnel) :
   ```bash
   python manage.py createsuperuser
   ```

7. **Lancer le serveur de développement** :
   ```bash
   python manage.py runserver
   ```

8. **Accéder au site** :
   - Site principal : http://127.0.0.1:8000/
   - Administration : http://127.0.0.1:8000/admin/

## Structure du Projet

```
Kompetans2/
├── kompetans2/          # Configuration Django
│   ├── settings.py      # Paramètres du projet
│   ├── urls.py         # URLs principales
│   └── wsgi.py         # Configuration WSGI
├── main/               # Application principale
│   ├── models.py       # Modèles de données
│   ├── views.py        # Vues/Contrôleurs
│   ├── forms.py        # Formulaires Django
│   ├── admin.py        # Configuration admin
│   └── urls.py         # URLs de l'application
├── templates/          # Templates HTML
│   ├── base.html       # Template de base
│   └── main/           # Templates de l'app main
├── static/             # Fichiers statiques
│   ├── css/            # Feuilles de style
│   ├── js/             # Fichiers JavaScript
│   └── images/         # Images statiques
├── media/              # Fichiers uploadés
├── manage.py           # Script de gestion Django
└── init_data.py        # Script d'initialisation
```

## Modèles de Données

### Formation
- `nom` : Nom de la formation
- `type_formation` : Type (habilitation, nfc15100, formateur, cse)
- `description_courte` : Description pour la page d'accueil
- `description_longue` : Description détaillée
- `image` : Image de la formation
- `duree` : Durée de la formation
- `prix` : Prix de la formation

### ContactFormation
- `formation` : Formation concernée (clé étrangère)
- `nom`, `prenom` : Nom et prénom du contact
- `entreprise` : Nom de l'entreprise (optionnel)
- `email` : Adresse email
- `telephone` : Numéro de téléphone (optionnel)
- `message` : Message du client
- `date_creation` : Date de création automatique
- `traite` : Statut de traitement

## Fonctionnalités Principales

### Page d'Accueil
- Hero section avec présentation de Kompetans
- 4 cartes de formation avec images et descriptions courtes
- Section "Pourquoi choisir Kompetans"
- Appel à l'action pour contacter

### Pages de Formation
- Description détaillée de chaque formation
- Objectifs pédagogiques spécifiques
- Formulaire de contact intégré
- Informations sur la durée et le prix

### Formulaires de Contact
- Validation côté client et serveur
- Messages de confirmation
- Sauvegarde en base de données
- Interface d'administration pour le suivi

### Administration
- Gestion des formations
- Suivi des demandes de contact
- Filtres et recherche
- Interface Django Admin personnalisée

## Personnalisation

### Couleurs et Style
Le fichier `static/css/style.css` contient toutes les personnalisations CSS. Les couleurs principales sont définies dans les variables CSS :

```css
:root {
    --primary-color: #0d6efd;
    --secondary-color: #6c757d;
    /* ... */
}
```

### Ajout de Formations
Pour ajouter de nouvelles formations :
1. Accéder à l'admin Django
2. Aller dans "Formations"
3. Cliquer sur "Ajouter formation"
4. Remplir les informations

### Modification du Contenu
- Textes : Modifier les templates dans `templates/`
- Styles : Modifier `static/css/style.css`
- Fonctionnalités JS : Modifier `static/js/script.js`

## Production

Pour déployer en production :

1. Modifier `DEBUG = False` dans settings.py
2. Configurer `ALLOWED_HOSTS`
3. Utiliser une base de données de production (PostgreSQL recommandé)
4. Configurer un serveur web (Nginx + Gunicorn)
5. Configurer les fichiers statiques avec `collectstatic`

## Support et Contact

Pour toute question ou assistance concernant ce projet, contactez l'équipe de développement.

---

**Kompetans** - Formation et Conseil en Électricité  
© 2025 - Tous droits réservés
