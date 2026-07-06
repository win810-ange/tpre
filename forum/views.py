from django.shortcuts import render
from .models import Discussion, Reponse

# Create your views here.
def create(request):
    if request.method == "POST":
       sujet = request.POST.get('sujet')
       Discussion.objects.create(sujet=sujet).save()
    
    context = {
        'Discussion':Discussion.objects.all()
    }
    return render(request, 'forum.html', context)





def Lirecommentaire(request, pk):
    discu1 = Discussion.objects.get(id=pk)
    context = {
        'reponse':Reponse.objects.filter(Sujet=discu1).all(),
        'Discussion':Discussion.objects.get(id=pk)
    }
    if request.method == 'POST':
        commentaire = request.POST.get('commentaire')
        Reponse.objects.create(Sujet=discu1, commentaire=commentaire).save()

    return render(request, 'reponse.html', context)


def DeleteReponse(request, id):
    Reponse.objects.get(id=id).delete
    return render(request, 'reponse.html')


