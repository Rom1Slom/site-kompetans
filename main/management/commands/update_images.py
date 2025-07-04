from django.core.management.base import BaseCommand
from main.models import Formation

class Command(BaseCommand):
    help = 'Associe les images aux formations'

    def handle(self, *args, **options):
        self.stdout.write('Début de l\'association des images...')
        
        # Mapping des types de formation vers les noms d'images
        image_mapping = {
            'habilitation': 'formations/habilitation.jpg',
            'nfc15100': 'formations/nfc15100.jpg',
            'formateur': 'formations/formateur.jpg',
            'cse': 'formations/cse.jpg',
        }
        
        formations = Formation.objects.all()
        self.stdout.write(f'Nombre de formations trouvées: {formations.count()}')
        
        for formation in formations:
            if formation.type_formation in image_mapping:
                image_path = image_mapping[formation.type_formation]
                formation.image = image_path
                formation.save()
                self.stdout.write(
                    self.style.SUCCESS(f'Image associée à {formation.nom}: {image_path}')
                )
            else:
                self.stdout.write(
                    self.style.WARNING(f'Pas d\'image trouvée pour {formation.nom}')
                )
        
        self.stdout.write(self.style.SUCCESS('Association terminée!'))
