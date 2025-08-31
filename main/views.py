from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from django.http import JsonResponse
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
            messages.success(request, 'Votre demande a été envoyée avec succès ! Nous vous recontacterons dans les plus brefs délais.')
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

            # Construire le message à partir du formulaire
            subject = f"Demande de contact - {formation.titre}"
            message = (
                f"Nouvelle demande pour la formation : {formation.titre}\n\n"
                f"Nom : {contact.nom}\n"
                f"Prénom : {contact.prenom}\n"
                f"Entreprise : {contact.entreprise}\n"
                f"Email : {contact.email}\n"
                f"Téléphone : {contact.telephone}\n\n"
                f"Message :\n{contact.message}"
            )

            try:
                result = send_mail(
                    subject,
                    message,
                    "contact@kompetans.fr",           # expéditeur (Zoho)
                    ["slomczynskiromain@yahoo.fr"],         # destinataire
                    fail_silently=False,
                )
                logger.warning('Résultat envoi email: %s', result)
                messages.success(request, 'Votre demande a été envoyée avec succès ! Nous vous recontacterons dans les plus brefs délais.')
            except Exception as e:
                logger.error('Erreur envoi email: %s', e)
                messages.error(request, "Une erreur est survenue lors de l'envoi de votre demande. Réessayez plus tard.")
            
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