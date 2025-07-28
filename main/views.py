from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from django.http import JsonResponse
from django.core.mail import send_mail  # ← AJOUTER
from django.conf import settings  # ← AJOUTER
from .models import Formation, ContactFormation
from .forms import ContactFormationForm

def home(request):
    """Page d'accueil avec les 4 formations"""
    formations = Formation.objects.all()[:4]
    return render(request, 'main/home.html', {'formations': formations})

def formation_detail(request, type_formation):
    """Page de détail d'une formation avec formulaire de contact"""
    formation = get_object_or_404(Formation, type_formation=type_formation)
    
    if request.method == 'POST':
        form = ContactFormationForm(request.POST)
        if form.is_valid():
            contact = form.save(commit=False)
            contact.formation = formation
            contact.save()
            
            # Envoyer un email de notification ← NOUVEAU
            try:
                send_mail(
                    subject=f'Nouvelle demande - {formation.nom}',
                    message=f'''
Nouvelle demande de contact reçue sur kompetans.fr :

Formation : {formation.nom}
Nom : {contact.nom} {contact.prenom}
Entreprise : {contact.entreprise or "Non renseignée"}
Email : {contact.email}
Téléphone : {contact.telephone or "Non renseigné"}

Message :
{contact.message}

---
Email automatique depuis kompetans.fr
                    ''',
                    from_email=settings.DEFAULT_FROM_EMAIL,
                    recipient_list=['contact@kompetans.fr'],
                    fail_silently=False,
                )
                messages.success(request, 'Votre demande a été envoyée avec succès ! Nous vous recontacterons rapidement.')
            except Exception as e:
                print(f"Erreur email : {e}")  # Pour débugger
                messages.success(request, 'Votre demande a été enregistrée. Nous vous recontacterons rapidement.')
            
            return redirect('main:formation_detail', type_formation=type_formation)
    else:
        form = ContactFormationForm()
    
    return render(request, 'main/formation_detail.html', {
        'formation': formation,
        'form': form
    })

def about(request):
    """Page à propos de Kompetans"""
    return render(request, 'main/about.html')
