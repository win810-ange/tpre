from django.shortcuts import render
from .models import Signalement



# Create your views here.

def create(request):
    if request.method == 'POST':
        type = request.POST.get('signal')
        image = request.POST.get('image')
        localisation = request.POST.get('lieu')
        
        signa= Signalement.objects.create(
            type=type,
            image=image,
            localisation=localisation
        )
        signa.save()
        
    return render(request, 'dash.html')

def countSignal_type(reuqest):
    signals = Signalement.objects.all()
    #un petit programme pour les types de signale
    lst_type = []
    for signal in signals:
        if not(signal.type in lst_type):
            lst_type.append(signal.type)

    type_cpt_dict = {}

    for type in lst_type:
        nbr_rp = Signalement.objects.filter(type=type).count()
        type_cpt_dict[type] = nbr_rp



    #ce petit programme lit toute les localisations de façon unique et renvoie une liste des communes
    
    lst_lclstion = [] #list qui va contenir les localisation
    for signal in signals:
        if not(signal.localisation in lst_lclstion):
            lst_lclstion.append(signal.localisation)



    #dictionnaire localisation : nombre de fois declarée
    lclstion_cpt_dict = {}

    #ce programme renvoie un dictionnaire commune nombre de signalement par commune
    for localisaion in lst_lclstion:
        nbr_rpt = Signalement.objects.filter(localisation=localisaion).count() #on obtient donc les nombre de fois qu'un signal et fait dans une localisation
        lclstion_cpt_dict[localisaion]=nbr_rpt



    context = {
        'types':type_cpt_dict,
        'communes':lclstion_cpt_dict,
        'total':Signalement.objects.all().count()
    }

    return render(reuqest, 'statistique.html', context)


def detail(request):
    context = {
        'signalements':Signalement.objects.all()
    }

    return render(request, "detail.html", context)