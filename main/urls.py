from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('formation/<int:formation_id>/', views.formation_detail, name='formation_detail'),
    path('about/', views.about, name='about'),
]
