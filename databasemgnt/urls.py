#path: E:\Koodi\DJANGO\Calendar\home\databasemgnt\urls.py
"""
from django.urls import path
from .views import add_event, poistaevent

urlpatterns = [
    path('',add_event),
    path('poistaevent/<int:id>/', poistaevent, name="poistaevent"),
]"""