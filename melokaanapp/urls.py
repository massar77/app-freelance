from . import views
from django.urls import path, include

urlpatterns = [
    path('', views.home, name='home'),
    path('<slug:slug_text>/', views.post, name='post'),
    path('categorie/<slug:slug_text>/', views.categorie, name='categorie'),
    path('sous-categorie/<slug:slug_text>/', views.sous_categorie, name='sous_categorie'),
]