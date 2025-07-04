from django.conf import settings

def company_info(request):
    """Context processor pour les informations de l'entreprise"""
    return {
        'company': settings.COMPANY_INFO
    }
