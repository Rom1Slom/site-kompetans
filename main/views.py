from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from django.http import JsonResponse
from django.core.mail import send_mail  # ← AJOUT NÉCESSAIRE
from django.conf import settings        # ← AJOUT NÉCESSAIRE
from .models import Formation, ContactFormation
from .forms import ContactFormationForm

def home(request):
    """Page d'accueil avec les 4 formations"""
    formations = Formation.objects.all()[:4]
    return render(request, 'main/home.html', {'formations': formations})

def formation_detail(request, formation_id):
    """Page de détail d'une formation avec formulaire de contact"""
    formation = get_object_or_404(Formation, id=formation_id)
    
    if request.method == 'POST':
        form = ContactFormationForm(request.POST)
        if form.is_valid():
            contact = form.save(commit=False)
            contact.formation = formation
            contact.save()
            
            # SECTION EMAIL AUTOMATIQUE
            try:
                subject = f'Nouvelle demande de contact - {formation.nom}'
                message = f"""
Nouvelle demande de contact pour la formation : {formation.nom}

Informations du contact :
- Nom : {contact.nom}
- Prénom : {contact.prenom}
- Email : {contact.email}
- Téléphone : {contact.telephone}
- Entreprise : {contact.entreprise}

Message :
{contact.message}

Formation demandée :
- Nom : {formation.nom}
- Type : {formation.type_formation}
- Durée : {formation.duree}
- Prix : {formation.prix}
"""
                
                send_mail(
                    subject=subject,
                    message=message,
                    from_email=settings.DEFAULT_FROM_EMAIL,  # contact@kompetans.fr
                    recipient_list=['contact@kompetans.fr'], # ← VOTRE DESTINATAIRE
                    fail_silently=False,
                )
                
                messages.success(request, 'Votre demande a été envoyée avec succès ! Nous vous recontacterons dans les plus brefs délais.')
                
            except Exception as e:
                messages.warning(request, 'Votre demande a été enregistrée, mais l\'email n\'a pas pu être envoyé.')
                print(f"Erreur envoi email: {e}")
            
            return redirect('formation_detail', formation_id=formation.id)
    else:
        form = ContactFormationForm()
    
    return render(request, 'main/formation_detail.html', {
        'formation': formation,
        'form': form
    })

def about(request):
    """Page à propos de Kompetans"""
    return render(request, 'main/about.html')