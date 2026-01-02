def electrical_accreditation(request):
    """English page for electrical accreditation only"""
    return render(request, 'main/electrical_accreditation.html')
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from django.http import JsonResponse

from kompetans2 import settings
from .models import Formation, ContactFormation
from .forms import ContactFormationForm
from django.core.mail import send_mail
import logging
logger = logging.getLogger(__name__)


def home(request):
    """Page d'accueil avec les 4 formations"""
    formations = Formation.objects.all()[:4]
    return render(request, 'main/home.html', {'formations': formations})

def formation_detail_slug(request, slug):
    """Page de détail d'une formation avec SLUG (SEO-friendly)"""
    formation = get_object_or_404(Formation, slug=slug)
    
    if request.method == 'POST':
        form = ContactFormationForm(request.POST)
        if form.is_valid():
            contact = form.save(commit=False)
            contact.formation = formation
            contact.save()
            # SECTION EMAIL AUTOMATIQUE (à ajouter)
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
                    from_email=settings.DEFAULT_FROM_EMAIL,
                    recipient_list=['contact@kompetans.fr'],
                    fail_silently=False,
                    timeout=10,
                )
                messages.success(request, 'Votre demande a été envoyée avec succès ! Nous vous recontacterons dans les plus brefs délais.')
            except Exception as e:
                import traceback
                messages.warning(request, 'Votre demande a été enregistrée, mais l\'email n\'a pas pu être envoyé.')
                logger.error(f"Erreur envoi email: {e}\n{traceback.format_exc()}")
                print(f"Erreur envoi email: {e}\n{traceback.format_exc()}")
            return redirect('formation_detail', slug=formation.slug)
    else:
        form = ContactFormationForm()
    
    return render(request, 'main/formation_detail.html', {
        'formation': formation,
        'form': form
    })

def formation_detail(request, formation_id):
    """Page de détail d'une formation avec ID (compatibilité)"""
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
                    recipient_list=['contact@kompetans.fr'],  # ← VOTRE DESTINATAIRE
                    fail_silently=False,
                    timeout=10,
                )
                messages.success(request, 'Votre demande a été envoyée avec succès ! Nous vous recontacterons dans les plus brefs délais.')
            except Exception as e:
                import traceback
                messages.warning(request, 'Votre demande a été enregistrée, mais l\'email n\'a pas pu être envoyé.')
                logger.error(f"Erreur envoi email: {e}\n{traceback.format_exc()}")
                print(f"Erreur envoi email: {e}\n{traceback.format_exc()}")
            
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