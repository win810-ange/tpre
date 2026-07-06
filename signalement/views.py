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

def LireSignal(reuqest):
    context = {
        'signalements':Signalement.objects.all()
    }
    return render(reuqest, 'statistique.html', context)


def EnvoyerStatistique(request):
    context = {
        'total':Signalement.objects.count(),
        
    }