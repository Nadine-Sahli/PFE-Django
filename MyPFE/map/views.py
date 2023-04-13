from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from .forms import LoginForm
from .models import *
from django.contrib.gis.geos import Point
# from .models import Marker
# from .forms import MarkerForm


def logine(request):
    if request.method == 'POST':
        formulaire = LoginForm(request.POST)
        if formulaire.is_valid(request):
            pseudo = formulaire.cleaned_data['pseudo']
            mot_de_passe = formulaire.cleaned_data['mot_de_passe']
            data = authenticate(request, username=pseudo, password=mot_de_passe)
            if data is not None:
                login(request, data)
            return redirect('add_node')
               
        return render(request, 'login.html', {'form': formulaire})
        
    return render(request, 'login.html', {'form': LoginForm()})


def add_node(request):
    if request.method == 'POST':
        mylatitude = request.POST.get('Latitude') 
        mylongitude = request.POST.get('Longitude') 
        point= Point(x=float(mylongitude),y=float(mylatitude))
        instance = nodes(Position=point, Latitude=mylatitude,Longitude=mylongitude)

        instance.save()
        return redirect('add_node')

    all_nodes = nodes.objects.all()


    return render(request, 'map.html', {'all_nodes': all_nodes})    


def interface(request):
    node = nodes.objects.order_by('-id').first()
    return render(request, 'interface.html', {'node': node})
# def add_marker(request):
#     if request.method == 'POST':
#         form = MarkerForm(request.POST)
#         if form.is_valid():
#             marker = form.save()
#             return redirect('map')
#     else:
#         form = MarkerForm()

#     context = {
#         'form': form
#     }

#     return render(request, 'add_marker.html', context)