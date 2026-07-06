from django.urls import path
from . import views



urlpatterns = [
    path('', views.create, name="creersujet"),
    path('participer/<int:pk>/', views.Lirecommentaire, name="repondre"),
    path('delete/<int:id>/', views.DeleteReponse, name="delete")
]