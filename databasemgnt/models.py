#Path: E:\Koodi\DJANGO\Calendar\home\databasemgnt\models.py

from django.db import models

#tietokanta malli ja objekti Events

class Events(models.Model):
    
    eventname = models.CharField(max_length=50, default="event")   
    startdate = models.DateField()                              # Käyttäjä syöttää päivämäärän käsin
    enddate = models.DateField()                                
    starttime = models.TimeField()                              
    endtime = models.TimeField()                                
    notes = models.CharField(max_length=50, default="memo")

    def __str__(self):
        return self.eventname                                   #   Palautetaan eventname näkymässä

#huomaa että muuttujien nimet tulee olla samat kuin forms.py tiedostossa


    
