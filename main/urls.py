from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    # ✅ URL avec SLUG pour SEO (priorité)
    path('formation/<slug:slug>/', views.formation_detail_slug, name='formation_detail'),
    # ✅ URL avec ID pour compatibilité (différent chemin)
    path('formation/id/<int:formation_id>/', views.formation_detail, name='formation_detail_id'),
    path('about/', views.about, name='about'),
    path('electrical-accreditation/', views.electrical_accreditation, name='electrical_accreditation'),
]
