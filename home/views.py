#Path: E:\Koodi\DJANGO\Calendar\home\home\views.py

from django.shortcuts import render 
from databasemgnt.models import Events      #Tässä viittauksilla 'kansio.tiedosto' määrityksillä saadaan niiden tuottamat toiminnot
                                             #- tänne.

def home(request):                          # home/alku sivun codebehind
    tapahtuma = Events.objects.all()
    context = {'tapahtumia':tapahtuma}
    return render (request, 'home.html',context)
