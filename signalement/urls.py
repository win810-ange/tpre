from django.urls import path
from . import views

urlpatterns = [
    path('', views.create, name="creersignal"),
    path('/signalement/statistique', views.LireSignal, name="afficherstat" )
]