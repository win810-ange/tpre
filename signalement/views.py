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
    
    context = {
        'erosion':Signalement.objects.filter(type="erosion").count(),
        'dechet': Signalement.objects.filter(type="dechet").count(),
        'inondation':Signalement.objects.filter(type="inondation").count(),
        'signalement':Signalement.objects.all(),
        'total':Signalement.objects.all().count()
    }
    return render(reuqest, 'statistique.html', context)


