from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('formation/<int:formation_id>/', views.formation_detail, name='formation_detail'),
     path('formation/<slug:slug>/', views.formation_detail_slug, name='formation_detail_slug'),  # Nouvelle URL avec slug
    path('about/', views.about, name='about'),
    path('zones-intervention/', views.zones, name='zones'),
]
