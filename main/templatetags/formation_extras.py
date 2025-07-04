from django import template
from django.templatetags.static import static

register = template.Library()

@register.simple_tag
def formation_image(formation_type):
    """Retourne l'URL statique de l'image pour un type de formation"""
    image_mapping = {
        'habilitation': 'images/formations/habilitation.jpg',
        'nfc15100': 'images/formations/nfc15100.jpg',
        'formateur': 'images/formations/formateur.jpg',
        'cse': 'images/formations/cse.jpg',
    }
    
    image_path = image_mapping.get(formation_type, 'images/formations/default.jpg')
    return static(image_path)
