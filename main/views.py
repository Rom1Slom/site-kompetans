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
            # Avant send_mail
            logger.warning(f"Envoi email à : {['contact@kompetans.fr']}")

            send_mail(
                        'Nouvelle demande de contact formation',
                        f'Nom : {contact.nom}\\nPrénom : {contact.prenom}\\nEmail : {contact.email}\\nMessage : {contact.message}',
                        None,  # Utilise DEFAULT_FROM_EMAIL
                        ['contact@kompetans.fr'],
                        fail_silently=False,
                    )
            messages.success(request, 'Votre demande a été envoyée avec succès ! Nous vous recontacterons dans les plus brefs délais.')
            # Après send_mail
            try:
                    result = send_mail(
                        'Test Render',
                        'Ceci est un test',
                        'contact@kompetans.fr',
                        ['slomczynskiromain@yahoo.fr'],
                        fail_silently=False,
                    )
                    logger.warning('Résultat envoi email: %s', result)
            except Exception as e:
                    logger.error('Erreur envoi email: %s', e)
        else:
                        form = ContactFormationForm()
    
    return render(request, 'main/formation_detail.html', {
        'formation': formation,
        'form': form
    })

def about(request):
    """Page à propos de Kompetans"""
    return render(request, 'main/about.html')