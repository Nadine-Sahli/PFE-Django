from django.shortcuts import render, redirect
from . import views
from . forms import *

# Create your views here.

def compte(request, pk):
    if pk == 'composteur':
        if request.method == 'POST':
            formulaire = Form_composteur(request.POST)
            if formulaire.is_valid():
                formulaire.enregistrer()
                pseudo = formulaire.cleaned_data['pseudo']
                variable = 'composteur'
                #######PB here
                return redirect('maps/',  pseudo)
                # return redirect('map', variable, pseudo)
            return render(request, 'registre.html', {'form': formulaire})
        return render(request, 'registre.html', {'form': Form_composteur()})
    else:
        if request.method == 'POST':
            formulaire = Form_client(request.POST)
            if formulaire.is_valid():
                formulaire.enregistrer()
                pseudo = formulaire.cleaned_data['pseudo']
                variable = 'client'
                ####### redirect dashboard normally
                #return redirect('map/',variable, pseudo)
                return redirect('maps/')
            return render(request, 'registre.html', {'form': formulaire})
        return render(request, 'registre.html', {'form': Form_client()})
        
# def signup(request):
#     return render(request,'signup.html')