from django.db import models
from django.utils import timezone
from django.utils.text import slugify


class Formation(models.Model):
    """Modèle pour les formations proposées"""
    FORMATION_CHOICES = [
        ('habilitation', 'Habilitations électriques'),
        ('nfc15100', 'Formation à la NF C15-100'),
        ('formateur', 'Formation de formateur en habilitation électrique'),
        ('cse', 'Formation des élus du Comité social et économique (CSE)'),
    ]
    
    nom = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200, unique=True, blank=True)
    type_formation = models.CharField(max_length=50, choices=FORMATION_CHOICES)
    description_courte = models.TextField()
    description_longue = models.TextField()
    duree = models.CharField(max_length=100, blank=True)
    prix = models.CharField(max_length=100, blank=True)
    prix_numerique = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)  # ← AJOUTEZ
    
    def save(self, *args, **kwargs):
        # Génère automatiquement le slug si vide
        if not self.slug:
            self.slug = slugify(self.nom)
            
            # Évite les doublons
            original_slug = self.slug
            counter = 1
            while Formation.objects.filter(slug=self.slug).exists():
                self.slug = f"{original_slug}-{counter}"
                counter += 1
                
        super().save(*args, **kwargs)
    
    def get_absolute_url(self):  # ← AJOUTEZ CETTE MÉTHODE
        return f'/formation/{self.slug}/'

    def get_image_url(self):
        """Retourne l'URL de l'image statique correspondant au type de formation"""
        image_mapping = {
            'habilitation': 'images/formations/habilitation.svg',
            'nfc15100': 'images/formations/nfc15100.svg',
            'formateur': 'images/formations/formateur.svg',
            'cse': 'images/formations/cse.svg',
        }
        return image_mapping.get(self.type_formation, 'images/formations/default.svg')
    
    def __str__(self):
        return self.nom
    
    class Meta:
        verbose_name = "Formation"
        verbose_name_plural = "Formations"


class ContactFormation(models.Model):
    """Modèle pour les demandes de contact concernant une formation"""
    formation = models.ForeignKey(Formation, on_delete=models.CASCADE)
    nom = models.CharField(max_length=100)
    prenom = models.CharField(max_length=100)
    entreprise = models.CharField(max_length=200, blank=True)
    email = models.EmailField()
    telephone = models.CharField(max_length=20, blank=True)
    message = models.TextField()
    date_creation = models.DateTimeField(default=timezone.now)
    traite = models.BooleanField(default=False)
    
    def __str__(self):
        return f"{self.nom} {self.prenom} - {self.formation.nom}"
    
    class Meta:
        verbose_name = "Demande de contact"
        verbose_name_plural = "Demandes de contact"
        ordering = ['-date_creation']
