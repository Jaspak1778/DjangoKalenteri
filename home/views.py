#Path: E:\Koodi\DJANGO\Calendar\home\home\views.py

from django.shortcuts import render, redirect 
from databasemgnt.models import Events      #Tässä viittauksilla 'kansio.tiedosto' määrityksillä saadaan niiden tuottamat toiminnot
from databasemgnt.forms import AddForm      #- tänne.

def home(request):                          # home/alku sivun codebehind
    tapahtuma = Events.objects.all()
    context = {'tapahtumia':tapahtuma}
    return render (request, 'home.html',context)

