from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from django.http import JsonResponse
from .models import Formation, ContactFormation
from .forms import ContactFormationForm
from django.core.mail import send_mail

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
            send_mail(
                        'Nouvelle demande de contact formation',
                        f'Nom : {contact.nom}\\nPrénom : {contact.prenom}\\nEmail : {contact.email}\\nMessage : {contact.message}',
                        None,  # Utilise DEFAULT_FROM_EMAIL
                        ['contact@kompetans.fr', 'veromain@yahoo.fr'],
                        fail_silently=False,
                    )
            messages.success(request, 'Votre demande a été envoyée avec succès ! Nous vous recontacterons dans les plus brefs délais.')
            return redirect('formation_detail_id', formation_id=formation.id)
    else:
        form = ContactFormationForm()
    
    return render(request, 'main/formation_detail.html', {
        'formation': formation,
        'form': form
    })

def about(request):
    """Page à propos de Kompetans"""
    return render(request, 'main/about.html')