from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('creeruncompte/', views.create, name="createcompte"),
    path('connexion/', views.connexion, name="connexion"),
    path('homespace/', views.dashboard, name="espace")
]