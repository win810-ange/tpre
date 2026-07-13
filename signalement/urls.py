from django.urls import path
from . import views

urlpatterns = [
    path('', views.create, name="creersignal"),
    path('/signalement/statistique', views.countSignal_type, name="afficherstat" )
]