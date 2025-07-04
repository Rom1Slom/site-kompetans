from django import forms
from .models import ContactFormation

class ContactFormationForm(forms.ModelForm):
    """Formulaire de contact pour une formation"""
    
    class Meta:
        model = ContactFormation
        fields = ['nom', 'prenom', 'entreprise', 'email', 'telephone', 'message']
        widgets = {
            'nom': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Votre nom'
            }),
            'prenom': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Votre prénom'
            }),
            'entreprise': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Nom de votre entreprise (optionnel)'
            }),
            'email': forms.EmailInput(attrs={
                'class': 'form-control',
                'placeholder': 'votre.email@exemple.com'
            }),
            'telephone': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Votre numéro de téléphone (optionnel)'
            }),
            'message': forms.Textarea(attrs={
                'class': 'form-control',
                'rows': 5,
                'placeholder': 'Votre message : précisez vos besoins, dates souhaitées, nombre de participants...'
            })
        }
        labels = {
            'nom': 'Nom *',
            'prenom': 'Prénom *',
            'entreprise': 'Entreprise',
            'email': 'Email *',
            'telephone': 'Téléphone',
            'message': 'Message *'
        }
