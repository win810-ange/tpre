from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import authenticate, login
from .models import User
from django.contrib import sessions



# Create your views here.
def home(request):
    return render(request, 'index.html')

def connexion(request):
    if request.method == 'POST':
        nom = request.POST.get('name')
        password = request.POST.get('password')
        user_test = User.objects.filter(username=nom)
        if user_test is not None:
            user = User.objects.filter(username=nom).first()
            if user is not None:
                login(request, user)
                return redirect('espace')
            else :
                return HttpResponse("<h1>quelque chose s'est mal passé</h1>")
        else :
            return HttpResponse('<h1>Errreur ce nom existe deja</h1>')
    return render(request, 'connexion.html')
    

def create(request):
    if request.method == 'POST':
        nom = request.POST.get('name')
        number = request.POST.get('number')
        password = request.POST.get('password')
        
        if User.objects.filter(username=nom).exists():
            user1 = User.objects.create_user(
            username = nom,
            numero = number,
            password = password
            )
            user1.save()
        else :
            return HttpResponse("<h1>l utilisateur exist déjà</h1>")
    
    return render(request, 'compte.html')
    
 
def dashboard(request):
    context = {
        'user':request.user
    }
    return render(request, 'dash.html', context)
