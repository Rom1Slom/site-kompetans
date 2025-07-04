from django.contrib import admin
from .models import Formation, ContactFormation

@admin.register(Formation)
class FormationAdmin(admin.ModelAdmin):
    list_display = ('nom', 'type_formation', 'duree', 'prix')
    list_filter = ('type_formation',)
    search_fields = ('nom', 'description_courte')
    fieldsets = (
        ('Informations générales', {
            'fields': ('nom', 'type_formation')
        }),
        ('Descriptions', {
            'fields': ('description_courte', 'description_longue')
        }),
        ('Détails', {
            'fields': ('duree', 'prix')
        }),
    )

@admin.register(ContactFormation)
class ContactFormationAdmin(admin.ModelAdmin):
    list_display = ('nom', 'prenom', 'email', 'formation', 'date_creation', 'traite')
    list_filter = ('formation', 'traite', 'date_creation')
    search_fields = ('nom', 'prenom', 'email', 'entreprise')
    readonly_fields = ('date_creation',)
    list_editable = ('traite',)
    date_hierarchy = 'date_creation'
    
    fieldsets = (
        ('Contact', {
            'fields': ('nom', 'prenom', 'entreprise', 'email', 'telephone')
        }),
        ('Formation', {
            'fields': ('formation',)
        }),
        ('Message', {
            'fields': ('message',)
        }),
        ('Suivi', {
            'fields': ('traite', 'date_creation')
        }),
    )
    
    def get_queryset(self, request):
        return super().get_queryset(request).select_related('formation')
