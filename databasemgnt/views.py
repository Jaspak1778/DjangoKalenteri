#Path: E:\Koodi\DJANGO\Calendar\home\databasemgnt\views.py
from django.shortcuts import render, redirect
from .forms import AddForm
from .models import Events
from home.views import home   #esimerkki


# Create your views here.
#lomake controller
def add_event(request):                  # tietokantaan tallennus 
    
    if request.method == 'POST':
        # Viedään POST ja data formille
        form = AddForm(request.POST)
        if form.is_valid():
        
            eve = form.cleaned_data['eventname']
            aloituspvm = form.cleaned_data['startdate']
            lopetuspvm = form.cleaned_data['enddate']
            aloitusaika = form.cleaned_data['starttime']
            lopetusaika = form.cleaned_data['endtime']
            muistio = form.cleaned_data['notes']

            #Tehdään olio Events ja viedään tiedot kantaan
            Events(eventname=eve, startdate=aloituspvm, enddate=lopetuspvm, starttime=aloitusaika, endtime=lopetusaika, notes=muistio).save()
            
            # Redirect after successfully handling the POST request
            return redirect(home)
    else:
        # jos onkin GET niin tyhjä formi
        form = AddForm()

    #formi ajetaan contex dict
    context = {'form': form}
    return render(request, 'eventadd.html', context)


def poistaevent(request, id):
    Events.objects.get(id = id).delete()
    return redirect(home)