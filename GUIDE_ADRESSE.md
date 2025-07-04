# Guide : Comment changer l'adresse de l'entreprise et la carte Google Maps

## 📍 Modifier l'adresse de l'entreprise

Pour personnaliser les informations de contact et la localisation de Kompetans :

### 1. Fichier à modifier :
```
c:\Users\admin\Documents\Programmation\Kompetans2\kompetans2\settings.py
```

### 2. Section à modifier :
Trouvez la section `COMPANY_INFO` et modifiez les valeurs :

```python
COMPANY_INFO = {
    'name': 'Kompetans',
    'address': 'VOTRE_ADRESSE_ICI',  # ← Modifiez ici
    'phone': 'VOTRE_TELEPHONE',      # ← Modifiez ici
    'email': 'VOTRE_EMAIL',          # ← Modifiez ici
    'description': 'Organisme de conseil et de formation spécialisé en électricité',
    'hours': 'Lun-Ven 9h-18h',      # ← Modifiez ici
    'maps_embed_url': 'URL_GOOGLE_MAPS'  # ← Voir ci-dessous
}
```

## 🗺️ Générer une nouvelle URL Google Maps

### Étapes pour obtenir l'URL d'intégration :

1. **Allez sur Google Maps** : https://maps.google.com
2. **Recherchez votre adresse**
3. **Cliquez sur "Partager"**
4. **Sélectionnez "Intégrer une carte"**
5. **Choisissez la taille** (recommandé : Grande)
6. **Copiez le code HTML** qui commence par `<iframe src="..."`
7. **Extrayez uniquement l'URL** entre les guillemets après `src="`

### Exemple :
Si Google vous donne :
```html
<iframe src="https://www.google.com/maps/embed?pb=!1m18..." width="600" height="450"...></iframe>
```

Copiez seulement : `https://www.google.com/maps/embed?pb=!1m18...`

### 3. Remplacez dans settings.py :
```python
'maps_embed_url': 'https://www.google.com/maps/embed?pb=!1m18...'
```

## ✅ Appliquer les changements

1. **Sauvegardez** le fichier `settings.py`
2. **Redémarrez** le serveur Django :
   ```bash
   python manage.py runserver
   ```
3. **Rafraîchissez** votre navigateur

## 📧 Les changements s'appliqueront automatiquement sur :

- ✅ Page d'accueil (section carte)
- ✅ Page "À propos" (section contact et carte)
- ✅ Footer (informations de contact)
- ✅ Toutes les pages du site

## 🎯 Exemple complet :

```python
COMPANY_INFO = {
    'name': 'Kompetans',
    'address': '123 Rue de l\'Électricité, 75001 Paris',
    'phone': '01 42 33 44 55',
    'email': 'info@kompetans.fr',
    'description': 'Organisme de conseil et de formation spécialisé en électricité',
    'hours': 'Lun-Ven 8h30-17h30',
    'maps_embed_url': 'https://www.google.com/maps/embed?pb=!1m18!1m12...'
}
```

---

**Note :** La carte Google Maps actuelle pointe vers la Tour Eiffel comme exemple. N'oubliez pas de la remplacer par votre vraie adresse !
