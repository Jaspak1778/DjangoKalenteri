#form class tapahtumien lisäykselle
#Path: E:\Koodi\DJANGO\Calendar\home\databasemgnt\forms.py
from django import forms        #Djangon moduulit
from .models import Events      #Event tulee importata models kansiosta

class AddForm(forms.Form):
    eventname = forms.CharField(label="Tapahtuman nimi", max_length=100) 
    startdate = forms.DateField(label="Aloituspvm", widget=forms.DateInput)       
    starttime = forms.TimeField(label="Aloitusaika", widget=forms.TimeInput)    
    enddate = forms.DateField(label="Lopetuspvm", widget=forms.DateInput)
    endtime = forms.TimeField(label="Loppuaika", widget=forms.TimeInput)
    notes = forms.CharField(label="Memo", max_length=100)

#huomaa että muuttujien nimet tulee olla samat kuin models.py tiedostossa


"""
class AddForm(forms.ModelForm):
    class Meta:
        model = Events  # Tässä voidaan määritellä että lomake perustuu tietokanta malliin, Events
        fields = ['eventname', 'starttime', 'startdate', 'endtime', 'enddate', 'notes']  # Luodaan lomake näistä kentistä

#Tässä on suoraviivaisempi tapa viitata tietokannan kenttiin"""