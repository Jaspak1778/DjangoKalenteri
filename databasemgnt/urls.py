from django.urls import path
from .views import add_event, poistaevent

urlpatterns = [
    path('',add_event),
    path('poista_tapahtuma/<int:id>/', poistaevent, name="poistaeve"),
]