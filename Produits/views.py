from django.shortcuts import render
from .models import *
from django.views.generic import ListView

# Create your views here.

# def home(request):

    #recuperation des donnees

    # donnees = Produits.objects.all()

    # context ={
    #     'donnee':donnees
    # }
    # return render(request , 'home.html' , context)



class affichage(ListView):

    #affichage du template
    template_name = 'home.html'
    
    #recuperation de toutes les donnes presentes en BD
    queryset = Produits.objects.all()
